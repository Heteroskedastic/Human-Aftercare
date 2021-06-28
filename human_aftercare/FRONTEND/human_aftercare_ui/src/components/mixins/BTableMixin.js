export default {
  watch: {
    bTableFiltering: {
      handler: function() {
        this.bTableLoadData();
      },
      deep: true,
    },
    bTableCurrentPage: function() {
      this.bTableLoadData();
    },
    bTablePerPage: function() {
      this.bTableLoadData();
    },
    bTableSortBy: function() {
      this.bTableLoadData();
    },
    bTableSortDesc: function() {
      this.bTableLoadData();
    }
  },
  data: function() {
    return {
      bTablePerPage: 10,
      bTableCurrentPage: 1,
      bTableFiltering: {},
      bTablePageSizeOptions: [5, 10, 15, 25, 50, 100, 200, 0],
      bTableSortBy: "id",
      bTableSortDesc: false,
      bTableFields: null,
      bTablePagination: {},
      bTableSortKeyMap: {},
    };
  },
  computed: {
    bTableSortParam: function() {
      var sortBy = this.bTableSortKeyMap[this.bTableSortBy] || this.bTableSortBy;
      return `${this.bTableSortDesc? '-': ''}${sortBy}`
    },
    bTableHttpParams: function() {
      return Object.assign({
        page_size: this.bTablePerPage,
        page: this.bTableCurrentPage,
        order_by: this.bTableSortParam,
      }, this.bTableFiltering);
    }
  },
  methods: {
    bTableLoadData: function() {
      throw "Not Implemented!";
    }
  },
};
