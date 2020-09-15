import request from "@/utils/request";

export function getList(data) {
  return request({
    url: "/userManagement/getList",
    method: "get",
    params: data,
  });
}
export function doAdd(data) {
  return request({
    url: "/userManagement/doAdd",
    method: "post",
    data,
  });
}

export function doEdit(data) {
  return request({
    url: "/userManagement/doEdit",
    method: "put",
    data,
  });
}

export function doDelete(data) {
  return request({
    url: "/userManagement/doDelete",
    method: "delete",
    data,
  });
}
