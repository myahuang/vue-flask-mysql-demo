/**
 * @description 路由守卫
 */
import router from "../router";
import store from "../store";
import NProgress from "nprogress";
import "nprogress/nprogress.css";
import getPageTitle from "@/utils/pageTitle";
import {
  authentication,
  loginInterception,
  routesWhiteList,
} from "@/config/settings";

NProgress.configure({ showSpinner: false });
router.beforeResolve(async (to, from, next) => {
  NProgress.start();
  document.title = getPageTitle(to.meta.title);
  let hasToken = store.getters["user/accessToken"];
  if (!loginInterception) hasToken = true;
  if (hasToken) {
    if (to.path === "/login") {
      next({ path: "/" });
      NProgress.done();
    } else {
      const hasPermissions =
        store.getters["user/permissions"] &&
        store.getters["user/permissions"].length > 0;
      if (hasPermissions) {
        next();
      } else {
        try {
          const permissions = await store.dispatch("user/getInfo");
          let accessRoutes = [];
          if (authentication === "intelligence") {
            accessRoutes = await store.dispatch(
              "permission/setRoutes",
              permissions
            );
          } else if (authentication === "all") {
            accessRoutes = await store.dispatch("permission/setAllRoutes");
          }
          router.addRoutes(accessRoutes);
          /*console.logs(to);
          let obj1 = { ...to };
          let obj2 = { replace: true };
          console.logs(Object.assign(obj1, obj2));
          console.logs({ ...to, replace: true });*/
          next({ ...to, replace: true });
        } catch (error) {
          await store.dispatch("user/resetAccessToken");
          next(`/login?redirect=${to.path}`);
          NProgress.done();
        }
      }
    }
  } else {
    if (routesWhiteList.indexOf(to.path) !== -1) {
      next();
    } else {
      next(`/login?redirect=${to.path}`);
      NProgress.done();
    }
  }
});
router.afterEach(() => {
  NProgress.done();
});
