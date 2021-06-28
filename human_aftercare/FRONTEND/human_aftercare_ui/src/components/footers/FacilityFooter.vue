<style scoped>
</style>

<template>
  <div class="footer bg-white py-4 d-flex flex-lg-column" id="kt_footer">
    <div class="container-fluid d-flex flex-column flex-md-row align-items-center justify-content-between">
      <div class="text-dark order-2 order-md-1">
        <span class="text-muted font-weight-bold mr-2">2021©</span>
        <a href="javascript:" target="_blank" class="text-dark-50 text-hover-primary mr-2">Human-Aftercare</a>
        <span class="badge badge-pill badge-success" title="UI Version">Version: {{$appVersion}}</span>
      </div>
      <div class="nav nav-dark">
        <a href="javascript:" target="_blank" class="nav-link pl-0 pr-5">About</a>
        <a href="javascript:" target="_blank" class="nav-link pl-0 pr-5">Team</a>
        <a href="javascript:" target="_blank" class="nav-link pl-0 pr-0">Contact</a>
      </div>
      <!--end::Nav-->
    </div>
    <!--end::Container-->
  </div>

</template>

<script>
import UtilMixin from "@/components/mixins/UtilMixin";

export default {
  mixins: [UtilMixin],
  components: {},
  data: function () {
    return {
    };
  },
  methods: {},
  created: function () {
  }
};
</script>
