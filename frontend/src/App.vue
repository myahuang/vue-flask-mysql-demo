<template>
  <div id="vue-flask-mysql-demo">
    <router-view />
  </div>
</template>

<script>
if (process.env.NODE_ENV === "production") {
  console.log("生产环境");
} else if (process.env.NODE_ENV === "test") {
  console.log("测试环境");
} else if (process.env.NODE_ENV === "staging") {
  console.log("预发布环境");
} else if (process.env.NODE_ENV === "development") {
  console.log("开发环境");
}
export default {
  name: "App",
  mounted() {},
};
</script>
