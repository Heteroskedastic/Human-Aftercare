<style scoped>
  .bt-pagination a.active {
    color: #FFFFFF !important;
    background-color: #3699FF !important;
    border-color: #3699FF !important;
  }
  .bt-pagination a.page-item {
    margin-right: 5px;
  }
  .bt-pagination a.page-item.number:not(.active):hover {
    color: #7e8299!important;
    background-color: #f3f6f9!important;
    border-color: #f3f6f9!important;
  }
</style>

<template>
  <div class="d-flex justify-content-between align-items-center flex-wrap">
    <div class="d-flex flex-wrap mr-3 bt-pagination" v-if="showPagination && tablePagination.current_page">
      <a href="javascript:" @click="goToPage(1)" :class="{'disabled': isOnFirstPage}"
         class="btn btn-icon btn-sm btn-light-primary page-item">
        <i class="ki ki-bold-double-arrow-back icon-xs"></i>
      </a>
      <a href="javascript:" @click="goToPage(currentPage - 1)" :class="{'disabled': isOnFirstPage}"
         class="btn btn-icon btn-sm btn-light-primary page-item">
        <i class="ki ki-bold-arrow-back icon-xs"></i>
      </a>
      <template v-if="notEnoughPages">
        <a v-for="n in totalPage" href="javascript:" @click="goToPage(n)"
           :class="{'active': isCurrentPage(n)}"
           class="btn btn-icon btn-sm border-0 number page-item">
          {{n}}
        </a>
      </template>
      <template v-else>
        <template v-if="windowStart!=1">
          <a href="javascript:" @click="goToPage(1)" class="btn btn-icon btn-sm border-0 number page-item">1</a>
          <a v-if="windowStart>2" href="javascript:" class="btn btn-icon btn-sm border-0 page-item">...</a>
        </template>

        <a v-for="n in windowSize" href="javascript:" @click="goToPage(windowStart+n-1)"
           :class="{'active': isCurrentPage(windowStart+n-1)}"
           class="btn btn-icon btn-sm border-0 number page-item">
          {{windowStart+n-1}}
        </a>

        <template v-if="windowSize+windowStart<totalPage+1">
          <a v-if="windowSize+windowStart<=totalPage" href="javascript:" class="btn btn-icon btn-sm border-0 page-item">...</a>
          <a href="javascript:" @click="goToPage(totalPage)" class="btn btn-icon btn-sm border-0 number page-item">{{totalPage}}</a>
        </template>

      </template>

      <a href="javascript:" @click="goToPage(currentPage + 1)" :class="{'disabled': isOnLastPage}"
         class="btn btn-icon btn-sm btn-light-primary page-item">
        <i class="ki ki-bold-arrow-next icon-xs"></i>
      </a>
      <a href="javascript:" @click="goToPage(totalPage)" :class="{'disabled': isOnLastPage}"
         class="btn btn-icon btn-sm btn-light-primary page-item">
        <i class="ki ki-bold-double-arrow-next icon-xs"></i>
      </a>
    </div>
    <div class="d-flex align-items-center bt-pagination-info" v-if="showPaginationInfo && tablePagination.current_page">
      <select v-model="perPage" class="form-control form-control-sm text-primary font-weight-bold mr-4 border-0 bg-light-primary"
              style="width: 75px;">
        <option :value="p" v-for="p in perPageOptions">{{p || "Max"}}</option>
      </select>
      <span class="text-muted">
        Displaying <span class="font-weight-bolder">{{fromRecord}}</span> - <span  class="font-weight-bolder">{{toRecord}}</span> of <span class="font-weight-bolder">{{tablePagination.total}}</span> records</span>
    </div>

  </div>
</template>

<script>
export default {
  watch: {
    perPage: function (value) {
      this.$emit("per-page-change", value);
    }
  },
  props: {
    showPaginationInfo: {
      type: Boolean,
      default: true
    },
    showPagination: {
      type: Boolean,
      default: true
    },
    initPerPage: {
      type: Number,
      default: 10
    },
    tablePagination: {
      type: Object,
      default: () => {
        return {
          current_page: null,
          next_page: null,
          previous_page: null,
          first_page: null,
          last_page: null,
          page_size: null,
          total: null,
        }
      }
    },
    perPageOptions: {
      type: Array,
      default: () => {
        return [5, 10, 15, 25, 50, 100, 200, 0]
      }
    },
    onEachSide: {
      type: Number,
      default () {
        return 2
      }
    },
  },
  computed: {
    fromRecord: function() {
      var pg = (this.tablePagination || {});
      if (!pg.total) {
        return 0;
      }
      return Math.max(0, (pg.current_page  - 1) * pg.page_size + 1)
    },
    toRecord: function() {
      var pg = (this.tablePagination || {});
      return Math.min(pg.total, pg.current_page * pg.page_size);
    },
    currentPage: function() {
      return (this.tablePagination || {}).current_page || 1
    },
    totalPage () {
      return this.tablePagination === null
        ? 0
        : this.tablePagination.last_page
    },
    isOnFirstPage () {
      return this.tablePagination === null
        ? false
        : this.tablePagination.current_page === 1
    },
    isOnLastPage () {
      return this.tablePagination === null
        ? false
        : this.tablePagination.current_page === this.tablePagination.last_page
    },
    notEnoughPages () {
      return this.totalPage < (this.onEachSide * 2) + 4
    },
    windowSize () {
      return this.onEachSide * 2 +1;
    },
    windowStart () {
      if (!this.tablePagination || this.tablePagination.current_page <= this.onEachSide) {
        return 1
      } else if (this.tablePagination.current_page >= (this.totalPage - this.onEachSide)) {
        return this.totalPage - this.onEachSide*2
      }

      return this.tablePagination.current_page - this.onEachSide
    },
  },
  data: function () {
    return {
      perPage: this.initPerPage
    }
  },
  methods: {
    isCurrentPage (page) {
      return page === this.tablePagination.current_page
    },
    goToPage: function(p) {
      if (p >= 1 && p <= this.totalPage) {
        this.$emit("page-change", p);
      }
    }
  }

}
</script>
