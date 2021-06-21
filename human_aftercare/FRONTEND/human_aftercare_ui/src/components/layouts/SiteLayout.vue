<template>
  <div>
    <div class="d-flex flex-column flex-root">
      <div class="d-flex flex-row flex-column-fluid page">
        <div class="d-flex flex-column flex-row-fluid container">
          <!--begin::Content-->
          <keep-alive include="NOPAGE">
            <router-view class="content d-flex flex-column flex-column-fluid"></router-view>
          </keep-alive>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  components: {
  },
  mounted: function () {
  }
};
</script>
