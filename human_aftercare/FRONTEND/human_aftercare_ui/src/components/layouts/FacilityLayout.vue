<template>
  <facility-layout-cmp v-if="$store.getters.isAuthenticated"></facility-layout-cmp>
  <login v-else></login>

</template>

<script>
import Login from "@/views/Login";
import FacilityLayoutCmp from "@/components/layouts/FacilityLayoutCmp";

export default {
  components: {
    FacilityLayoutCmp,
    Login,
  },
  methods: {
  },
  mounted: function () {

  }
};
</script>
