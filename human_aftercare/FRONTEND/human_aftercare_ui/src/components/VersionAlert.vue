<style scoped>
.app-version-alert {
  border-radius: 0;
  font-size: 15px;
  z-index: 99999;
  margin-bottom: 0;
  background-color: #ac4bf5;
  color: white;
}
.refresh-btn {
  margin-left: 5px;
  margin-right: 5px;
  margin-top: -5px;
}
</style>

<template>
  <div class="fixed-bottom alert app-version-alert">
    <i class="fas fa-exclamation-triangle fa-2x mr-1 text-light"></i> <span class="font-weight-bolder"> Current ui version is old!</span>
    A newer version of ui <span class="badge badge-success">{{ newVersion }}</span> is available.
    <a href="javascript:" onclick="location.reload()" class="btn btn-sm btn-light text-dark refresh-btn">
      <i class="fas fa-sync-alt"></i> Click here
    </a> or refresh page to load new version.
  </div>
</template>

<script>
import UtilMixin from "@/components/mixins/UtilMixin";

export default {
  props: {
    newVersion: {
      type: String,
      default: null
    }
  },
  mixins: [UtilMixin],
  mounted: function() {}
};
</script>
