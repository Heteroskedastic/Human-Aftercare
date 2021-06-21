<style scoped>
</style>

<template>
  <div
    v-show="tablePagination && tablePagination.last_page > 1"
    :class="css.wrapperClass"
  >
    <ul class="pagination b-pagination pagination-lg justify-content-center">
      <li class="page-item" :class="isOnFirstPage ? css.disabledClass : ''" @click="loadPage(1)">
        <a href="javascript:"
          :class="[
            'page-link',
            css.linkClass
          ]"
        >
          <i class="fa fa-angle-double-left"></i>
        </a>
      </li>

      <li class="page-item" :class="isOnFirstPage ? css.disabledClass : ''" @click="loadPage('prev')">
        <a href="javascript:"
          :class="[
            'page-link',
            css.linkClass
          ]"
        >
          <i class="fa fa-angle-left"></i>
        </a>
      </li>
      <template v-if="notEnoughPages">
        <template v-for="n in totalPage">
          <li class="page-item" :class="isCurrentPage(n) ? css.activeClass : ''" @click="loadPage(n)">
            <a href="javascript:"
              :class="['page-link', css.pageClass]"
              v-html="n"
            >
            </a>
          </li>
        </template>
      </template>
      <template v-else>
        <template v-for="n in windowSize">
          <li
            class="page-item"
            @click="loadPage(windowStart + n - 1)"
            :class="isCurrentPage(windowStart + n - 1) ? 'active' : ''"
          >
            <a href="javascript:" :class="['page-link', css.pageClass]" v-html="windowStart + n - 1"> </a>
          </li>
        </template>
      </template>
      <li class="page-item" :class="isOnLastPage ? css.disabledClass : ''" @click="loadPage('next')">
        <a href="javascript:"
          :class="[
            'page-link',
            css.linkClass
          ]"
        >
          <i class="fa fa-angle-right"></i>
        </a>
      </li>
      <li class="page-item" :class="isOnLastPage ? css.disabledClass : ''" @click="loadPage(totalPage)">
        <a href="javascript:"
          :class="[
            'page-link',
            css.linkClass
          ]"
        >
          <i class="fa fa-angle-double-right"></i>
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
import PaginationMixin from "vuetable-2/src/components/VuetablePaginationMixin";
export default {
  mixins: [PaginationMixin],
};
</script>
