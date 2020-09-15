<template>
  <div class="test-container">
    <el-divider content-position="left">你可以在这里写demo</el-divider>
    <iframe
      id="iframeContain"
      name="iframeContain"
      seamless
      scrolling="yes"
      :src="iframeURL"
    >
    </iframe>
  </div>
</template>
<script>
export default {
  name: "Test",
  data() {
    return { show: true, iframeURL: "wwww.baidu.com" };
  },
  created() {},
  mounted() {},
  methods: {},
};
</script>
<style lang="scss" scoped>
/** iframe样式 */
#iframeContain {
  width: 100%;
  height: 800px;
}
</style>
