import {
  storage,
  tokenTableName,
  refreshTokenTableName,
} from "@/config/settings";
import cookie from "js-cookie";

/**
 * @description 获取accessToken
 * @returns {string|ActiveX.IXMLDOMNode|Promise<any>|any|IDBRequest<any>|MediaKeyStatus|FormDataEntryValue|Function|Promise<Credential | null>}
 */
export function getAccessToken() {
  if (storage) {
    if ("localStorage" === storage) {
      return localStorage.getItem(tokenTableName);
    } else if ("sessionStorage" === storage) {
      return sessionStorage.getItem(tokenTableName);
    } else if ("cookie" === storage) {
      return cookie.get(tokenTableName);
    } else {
      return localStorage.getItem(tokenTableName);
    }
  } else {
    return localStorage.getItem(tokenTableName);
  }
}
/**
 * @description 获取refreshToken
 * @returns {string|ActiveX.IXMLDOMNode|Promise<any>|any|IDBRequest<any>|MediaKeyStatus|FormDataEntryValue|Function|Promise<Credential | null>}
 */
export function getRefreshToken() {
  if (storage) {
    if ("localStorage" === storage) {
      return localStorage.getItem(refreshTokenTableName);
    } else if ("sessionStorage" === storage) {
      return sessionStorage.getItem(refreshTokenTableName);
    } else if ("cookie" === storage) {
      return cookie.get(refreshTokenTableName);
    } else {
      return localStorage.getItem(refreshTokenTableName);
    }
  } else {
    return localStorage.getItem(refreshTokenTableName);
  }
}
/**
 * @description 存储accessToken
 * @param accessToken
 * @returns {void|*}
 */
export function setAccessToken(accessToken) {
  if (storage) {
    if ("localStorage" === storage) {
      return localStorage.setItem(tokenTableName, accessToken);
    } else if ("sessionStorage" === storage) {
      return sessionStorage.setItem(tokenTableName, accessToken);
    } else if ("cookie" === storage) {
      return cookie.set(tokenTableName, accessToken);
    } else {
      return localStorage.setItem(tokenTableName, accessToken);
    }
  } else {
    return localStorage.setItem(tokenTableName, accessToken);
  }
}
/**
 * @description 存储refreshToken
 * @param refreshToken
 * @returns {void|*}
 */
export function setRefreshToken(refreshToken) {
  if (storage) {
    if ("localStorage" === storage) {
      return localStorage.setItem(refreshTokenTableName, refreshToken);
    } else if ("sessionStorage" === storage) {
      return sessionStorage.setItem(refreshTokenTableName, refreshToken);
    } else if ("cookie" === storage) {
      return cookie.set(refreshTokenTableName, refreshToken);
    } else {
      return localStorage.setItem(refreshTokenTableName, refreshToken);
    }
  } else {
    return localStorage.setItem(refreshTokenTableName, refreshToken);
  }
}
/**
 * @description 移除accessToken
 * @returns {void|Promise<void>}
 */
export function removeAccessToken() {
  if (storage) {
    if ("localStorage" === storage) {
      return localStorage.removeItem(tokenTableName);
    } else if ("sessionStorage" === storage) {
      return sessionStorage.clear();
    } else if ("cookie" === storage) {
      return cookie.remove(tokenTableName);
    } else {
      return localStorage.removeItem(tokenTableName);
    }
  } else {
    return localStorage.removeItem(tokenTableName);
  }
}

/**
 * @description 移除refreshToken
 * @returns {void|Promise<void>}
 */
export function removeRefreshToken() {
  if (storage) {
    if ("localStorage" === storage) {
      return localStorage.removeItem(refreshTokenTableName);
    } else if ("sessionStorage" === storage) {
      return sessionStorage.clear();
    } else if ("cookie" === storage) {
      return cookie.remove(refreshTokenTableName);
    } else {
      return localStorage.removeItem(refreshTokenTableName);
    }
  } else {
    return localStorage.removeItem(refreshTokenTableName);
  }
}
