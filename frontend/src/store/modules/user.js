import Vue from "vue";
import { getInfo, login, logout } from "@/api/user";
import {
  getAccessToken,
  removeAccessToken,
  setAccessToken,
  getRefreshToken,
  removeRefreshToken,
  setRefreshToken,
} from "@/utils/accessToken";
import { resetRouter } from "@/router";
import {
  tokenName,
  refreshTokenName,
  title,
  // tokenExpiresTime,
} from "@/config/settings";

const state = {
  accessToken: getAccessToken(),
  refreshToken: getRefreshToken(),
  // expiresTime: "",
  userName: "",
  avatar: "",
  permissions: [],
};
const getters = {
  accessToken: (state) => state.accessToken,
  userName: (state) => state.userName,
  avatar: (state) => state.avatar,
  permissions: (state) => state.permissions,
  refreshToken: (state) => state.refreshToken,
  expiresTime: (state) => state.expiresTime,
};
const mutations = {
  setAccessToken(state, accessToken) {
    state.accessToken = accessToken;
  },
  setUserName(state, userName) {
    state.userName = userName;
  },
  setRefreshToken(state, refreshToken) {
    // 保存延续token
    state.refreshToken = refreshToken;
  },
  // SetExpiresTime(state, expiresTime) {
  //   // 保存token过期时间
  //   let NOW_DATE = parseInt(new Date().getTime() / 1000); // 保存当前登陆时间
  //   state.expiresTime = expiresTime + NOW_DATE;
  // },
  setAvatar(state, avatar) {
    state.avatar = avatar;
  },
  setPermissions(state, permissions) {
    state.permissions = permissions;
  },
};
const actions = {
  async login({ commit }, userInfo) {
    const { data, msg } = await login(userInfo);
    const accessToken = data[tokenName];
    const refreshToken = data[refreshTokenName];
    if (accessToken) {
      commit("setAccessToken", accessToken);
      commit("setRefreshToken", refreshToken); // 保存延续token
      // commit("SetExpiresTime", tokenExpiresTime); // 保存token过期时间
      setAccessToken(accessToken);
      setRefreshToken(refreshToken);
      const hour = new Date().getHours();
      const thisTime =
        hour < 8
          ? "早上好"
          : hour <= 11
          ? "上午好"
          : hour <= 13
          ? "中午好"
          : hour < 18
          ? "下午好"
          : "晚上好";
      Vue.prototype.$baseNotify(`欢迎登录${title}`, `${thisTime}！`);
    } else {
      Vue.prototype.$baseMessage(
        // `登录接口异常，未正确返回${tokenName}...`,
        msg,
        "error"
      );
    }
  },
  async getInfo({ commit, state }) {
    // const { data } = await getInfo(state.accessToken);
    const { data } = await getInfo();
    if (!data) {
      Vue.prototype.$baseMessage("验证失败，请重新登录...", "error");
      return false;
    }
    let { permission, username, avatar } = data;
    if (permission && username && avatar) {
      commit("setPermissions", [permission]);
      commit("setUserName", username);
      commit("setAvatar", avatar);
      return [permission];
    } else {
      Vue.prototype.$baseMessage("获取用户信息接口异常", "error");
      return false;
    }
  },
  async logout({ commit, dispatch }) {
    await logout();
    await dispatch("tagsBar/delAllRoutes", null, { root: true });
    commit("setAccessToken", "");
    commit("setRefreshToken", "");
    commit("setPermissions", []);
    removeAccessToken();
    removeRefreshToken();
    resetRouter();
  },
  resetAccessToken({ commit }) {
    commit("setAccessToken", "");
    removeAccessToken();
  },
  resetRefreshToken({ commit }) {
    commit("setRefreshToken", "");
    removeRefreshToken();
  },
  updateAccessToken({ accessToken }) {
    setAccessToken(accessToken);
  },
};
export default { state, getters, mutations, actions };
