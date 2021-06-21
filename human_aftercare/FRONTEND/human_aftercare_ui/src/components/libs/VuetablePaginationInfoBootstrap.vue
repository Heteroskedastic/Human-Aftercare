<template>
  <span :class="['vuetable-pagination-info']" v-html="paginationInfo"> </span>
</template>

<script>
import VuetablePaginationInfoMixin from "vuetable-2/src/components/VuetablePaginationInfoMixin";

export default {
  mixins: [VuetablePaginationInfoMixin],
};
</script>
