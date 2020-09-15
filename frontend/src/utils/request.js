import axios from "axios";
import {
  contentType,
  invalidCode,
  messageDuration,
  noPermissionCode,
  requestTimeout,
  okCode,
  errorCode,
  tokenType,
  debounce,
} from "@/config/settings";
import { Loading, Message } from "element-ui";
import store from "@/store";
import qs from "qs";
import router from "@/router";
import _ from "lodash";
import {
  getAccessToken,
  getRefreshToken,
  setAccessToken,
} from "@/utils/accessToken";

const service = axios.create({
  baseURL: process.env.VUE_APP_BASE_API,
  timeout: requestTimeout,
  headers: {
    "Content-Type": contentType,
  },
});

let loadingInstance;
service.interceptors.request.use(
  (config) => {
    // if (store.getters["user/accessToken"]) {
    if (getAccessToken()) {
      config.headers["Authorization"] =
        // tokenType + store.getters["user/accessToken"];
        tokenType + getAccessToken();
    }
    if (config.data) {
      config.data = _.pickBy(config.data, _.identity);
    }
    const url = config.url;
    if (url.replace(/[\/]/g, "") === "refreshtoken") {
      config.headers["Authorization"] =
        // tokenType + store.getters["user/refreshToken"];
        tokenType + getRefreshToken();
    }
    if (process.env.NODE_ENV !== "test") {
      if (contentType === "application/x-www-form-urlencoded;charset=UTF-8") {
        if (config.data && !config.data.param) {
          config.data = qs.stringify(config.data);
        }
      }
    }
    const needLoading = () => {
      let status = false;
      debounce.forEach((item) => {
        if (_.includes(config.url, item)) {
          status = true;
        }
      });
      return status;
    };
    if (needLoading()) {
      loadingInstance = Loading.service();
    }

    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

const errorMsg = (message) => {
  return Message({
    message: message,
    type: "error",
    duration: messageDuration,
  });
};

function refreshToken() {
  // instance是当前request.js中已创建的axios实例
  return service.put("/refresh/token").then((res) => res);
}

// 给实例添加一个setToken方法，用于登录后将最新token动态添加到header，同时将token保存在localStorage中
service.setToken = (token) => {
  service.defaults.headers["Authorization"] = tokenType + token;
  setAccessToken(token);
};

// 是否正在刷新的标记
let isRefreshing = false;
// 重试队列，每一项将是一个待执行的函数形式
let requests = [];

service.interceptors.response.use(
  (response) => {
    if (loadingInstance) {
      loadingInstance.close();
    }
    const { status, data, config } = response;
    const { code, msg } = data;
    if (code !== okCode && code !== errorCode) {
      switch (code) {
        case invalidCode:
          errorMsg(msg || `后端接口${code}异常`);
          store.dispatch("user/resetAccessToken");
          store.dispatch("user/resetRefreshToken");
          break;
        case noPermissionCode:
          const config = response.config;
          if (!isRefreshing) {
            isRefreshing = true;
            return refreshToken()
              .then((res) => {
                const { code } = res;
                if (code === okCode) {
                  const { access_token } = res.data;
                  service.setToken(access_token);
                  config.headers["Authorization"] = tokenType + access_token;
                  config.baseURL = process.env.VUE_APP_BASE_API;
                  // 已经刷新了token，将所有队列中的请求进行重试
                  requests.forEach((cb) => cb(access_token));
                  requests = [];
                  return service(config);
                } else {
                  router.push({
                    path: "/401",
                  });
                }
              })
              .catch((res) => {
                Message({
                  message: `Token过期，请重新登陆！`,
                  type: "error",
                  duration: 10000,
                });
                store.dispatch("user/resetAccessToken");
                store.dispatch("user/resetRefreshToken");
                console.error("refreshtoken error =>", res);
                // setTimeout(function () {
                //   window.location.href = "/";
                // }, 3000);
              })
              .finally(() => {
                isRefreshing = false;
              });
          } else {
            // 正在刷新token，将返回一个未执行resolve的promise
            return new Promise((resolve) => {
              // 将resolve放进队列，用一个函数形式来保存，等token刷新后直接执行
              requests.push((token) => {
                config.baseURL = process.env.VUE_APP_BASE_API;
                config.headers["Authorization"] = tokenType + token;
                resolve(service(config));
              });
            });
          }
          break;
        default:
          errorMsg(msg || `后端接口${code}异常`);
          break;
      }
      return Promise.reject(
        "vue-flask-mysql-demo请求异常拦截:" +
          JSON.stringify({ url: config.url, code, msg }) || "Error"
      );
    } else {
      return data;
    }
  },
  (error) => {
    if (loadingInstance) {
      loadingInstance.close();
    }
    /*网络连接过程异常处理*/
    let { message } = error;
    switch (message) {
      case "Network Error":
        message = "后端接口连接异常";
        break;
      case "timeout":
        message = "后端接口请求超时";
        break;
      case "Request failed with status code":
        message = "后端接口" + message.substr(message.length - 3) + "异常";
        break;
    }
    errorMsg(message || "后端接口未知异常");
    return Promise.reject(error);
  }
);

export default service;
