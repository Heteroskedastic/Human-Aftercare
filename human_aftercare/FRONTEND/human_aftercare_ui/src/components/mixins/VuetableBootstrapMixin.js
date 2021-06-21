import LoadingOverlayableMixin from "./LoadingOverlayableMixin";

export default {
  mixins: [LoadingOverlayableMixin],
  data: function() {
    return {
      tablePerPage: 10,
      tableFiltering: {},
      pageSizeOptions: [5, 10, 15, 25, 50, 100, 200, 0],
      tableHTTPOptions: {},
      css: {
        table: {
          tableClass: "table",
          loadingClass: "loading",
          ascendingIcon: "la la-arrow-up",
          descendingIcon: "la la-arrow-down",
          handleIcon: "glyphicon glyphicon-menu-hamburger",
          detailRowClass: "table-row-details",
          ascendingClass: "sorted-asc", // since v1.7
          descendingClass: "sorted-desc", // since v1.7
        },
      },
    };
  },
  watch: {
    tablePerPage: function() {
      this.$nextTick(function() {
        this.$refs.vuetable.refresh();
      });
    },
    tableFiltering: {
      handler: function() {
        this.onTableFilteringChanged();
      },
      deep: true,
    },
  },
  methods: {
    onTableFilteringChanged: function() {
      if (this.$refs.vuetable) {
        this.$refs.vuetable.selectedTo = [];
        this.$refs.vuetable.visibleDetailRows = [];
        this.$nextTick(function() {
          this.$refs.vuetable.refresh();
        });
      }
    },
    vuetableHttpFetch: function(apiUrl, httpOptions) {
      return this.$http.get(apiUrl, httpOptions);
    },
    getSortParam: function(sortOrder) {
      if (!sortOrder || sortOrder.field === "") {
        return "";
      }
      return sortOrder
        .map(function(sort) {
          return (
            (sort.direction === "desc" ? "" : "-") +
            (sort.sortField || sort.field)
          );
        })
        .join(",");
    },
    onPaginationData: function(paginationData) {
      paginationData.from =
        (paginationData.current_page - 1) * paginationData.page_size + 1;
      paginationData.to = Math.min(
        paginationData.current_page * paginationData.page_size,
        paginationData.total
      );
      this.$refs.pagination.setPaginationData(paginationData);
      this.$refs.paginationInfo.setPaginationData(paginationData);
    },
    onChangePage: function(page) {
      this.$refs.vuetable.changePage(page);
    },
    OnLoadErrorData: function(response) {
      this.showDefaultServerError(response);
    },
    OnLoadedData: function(page) {
      this.loadingOverlay = false;
      this.suppressOverlay = false;
      this.onFinishedLoadData && this.onFinishedLoadData(page);
    },
    OnLoadingData: function(page) {
      if (!this.suppressOverlay) {
        this.loadingOverlay = true;
      }
    },
  },
};
