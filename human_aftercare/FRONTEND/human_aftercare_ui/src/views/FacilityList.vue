<style scoped>

</style>

<template>
  <div>
    <div class="card">
      <div class="card-header">
        <h3>Facility List</h3>
      </div>
      <div class="card-body">
        <div class="d-flex align-items-center mb-10" v-for="f in (facilities || [])">
          <!--begin::Symbol-->
          <div class="symbol symbol-40 symbol-light-primary mr-5">
            <span class="symbol-label">
              <span class="fas fa-hospital-user">
              </span>
            </span>
          </div>
          <!--end::Symbol-->
          <!--begin::Text-->
          <div class="d-flex flex-column font-weight-bold">
            <a is="router-link" :to="{name: $rns.ROOT, params: {facility_domain: f.domain}}" class="text-dark text-hover-primary mb-1 font-size-lg">{{f.name}}</a>
            <span class="text-muted">{{f.description}}</span>
          </div>
          <!--end::Text-->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import LoadingOverlayableMixin from "@/components/mixins/LoadingOverlayableMixin";

export default {
  mixins: [LoadingOverlayableMixin],
  data: function () {
    return  {
      facilities: null
    }
  },
  mounted: function () {
    this.loadingOverlay = true;
    this.$http.get('facility', {params: {page_size: 0}}).then(
      (response) => {
        this.loadingOverlay = false;
        this.facilities = response.data.results;
      },
      (error) => {
        this.loadingOverlay = false;
        this.showDefaultServerError(error);
      }
    );
  }
}
</script>
