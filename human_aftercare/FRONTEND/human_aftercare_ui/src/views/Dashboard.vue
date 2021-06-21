<style scoped>

</style>

<template>
  <div>
    <page-bar></page-bar>
    <div class="d-flex flex-column-fluid">
      <div class="container">
        <div class="card">
          <div class="card-body">
            <h3>Dashboard</h3>
            <h6 class="text-info">Dashboard widgets should be here!</h6>
            <h1 class="text-danger">Not Implemented Yet!</h1>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import PageBar from "@/components/PageBar";
import UtilMixin from "@/components/mixins/UtilMixin";
export default {
  mixins: [UtilMixin],
  components: {PageBar}
}
</script>
