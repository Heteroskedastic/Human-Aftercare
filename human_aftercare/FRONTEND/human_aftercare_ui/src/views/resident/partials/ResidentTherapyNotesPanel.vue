<style>
  .resident-therapy-notes-table th.id-col {
    width: 50px;
  }
  .resident-therapy-notes-table th.actions-col {
    width: 40px;
  }
  .resident-therapy-notes-table td.actions-col {
    padding: 0 !important;
    text-align: right;
  }
  .resident-therapy-notes-table td.created-col,
  .resident-therapy-notes-table td.updated-col {
    padding-top: 1px !important;
    padding-bottom: 1px !important;
  }
  .resident-therapy-notes-table td.actions-col {
    padding: 0 !important;
  }

</style>

<template>
  <div class="card card-custom gutter-b resident-records-panel">
    <div class="card-header">
      <div class="card-title">
        <span class="card-icon">
          <i class="fas fa-book-medical text-primary"></i>
        </span>
        <h3 class="card-label">
          <a v-b-toggle.resident-therapy-note-table-container href="javascript:">
            <span class="text-dark-65 pr-1">Therapy Notes</span>
            <span class="label label-pill font-weight-bold mr-1"
                   :class="bTablePagination.total? 'label-info': 'label-muted'">
              {{ bTablePagination.total || 0 }}
            </span>
            <i class="la la-angle-down when-closed text-dark-50"></i>
            <i class="la la-angle-up when-opened text-dark-50"></i>

          </a>
        </h3>
      </div>
      <div class="card-toolbar">
        <a href="javascript:" @click="$refs.therapyNoteModalRef.show()"
           :class="{disabled: $cannot('add', 'therapynote')}"
           class="btn btn-sm btn-light-success font-weight-bold" title="Add New Therapy Note">
          <i class="flaticon2-add-1"></i> Add
        </a>
      </div>
    </div>
    <b-collapse id="resident-therapy-note-table-container" @show="!records && loadRecords()">
      <div class="card-body" v-if="records">
        <b-table :items="records" :fields="bTableFields" :sort-by.sync="bTableSortBy" no-local-sorting responsive
                 show-empty
                 class="resident-therapy-notes-table custom-table" :sort-desc.sync="bTableSortDesc">
          <template #empty="scope">
            <h6 class="text-muted text-center pt-10">{{ scope.emptyText }}</h6>
          </template>
          <template #cell(datetime)="data">
            <span class="font-weight-bold text-dark-65">{{formatDate(data.item.datetime, 'MMM D, YYYY hh:mm A')}}</span>
          </template>
          <template #cell(create_datetime)="data">
            <div :title="formatDate(data.item.create_datetime, 'MMM D, YYYY hh:mm A')">
              <span class="text-dark-65 font-weight-bold d-block">{{data.item._create_by.username}}</span>
              <span class="text-muted small">{{formatDate(data.item.create_datetime, 'MMM D, YYYY')}}</span>
            </div>
          </template>
          <template #cell(update_datetime)="data">
            <div :title="formatDate(data.item.update_datetime, 'MMM D, YYYY hh:mm A')">
              <span class="text-dark-65 font-weight-bold d-block">{{data.item._update_by.username}}</span>
              <span class="text-muted small">{{formatDate(data.item.update_datetime, 'MMM D, YYYY')}}</span>
            </div>
          </template>
          <template #cell(duration_minutes)="data">
            <span class="font-weight-bold text-dark-65">{{data.item.duration_minutes}}</span><small> min</small>
          </template>
          <template #cell(actions)="data">
            <a href="javascript:" @click="$refs.therapyNoteModalRef.show(data.item)"
               class="btn btn-sm btn-default btn-text-warning btn-hover-warning btn-icon mr-2"
               :class="{disabled: $cannot('change', 'resident')}"
               title="Edit Record">
              <i class="far fa-edit"></i>
            </a>
          </template>
        </b-table>
        <b-table-pagination
            @page-change="p => bTableCurrentPage=p"
            @per-page-change="p => {bTableCurrentPage=1; bTablePerPage=p}"
            :init-per-page="bTablePerPage"
            :per-page-options="bTablePageSizeOptions"
            :table-pagination="bTablePagination">
        </b-table-pagination>

      </div>
    </b-collapse>
    <resident-therapy-note-modal
        ref="therapyNoteModalRef"
        :resident="resident"
        @saved-success="bTableLoadData"
        @deleted-success="bTableLoadData"
        @reload-plans="bTableLoadData"
    ></resident-therapy-note-modal>
  </div>
</template>

<script>
import LoadingOverlayableMixin from "@/components/mixins/LoadingOverlayableMixin";
import UtilMixin from "@/components/mixins/UtilMixin";
import BTableMixin from "@/components/mixins/BTableMixin";
import BTablePagination from "@/components/BTablePagination";
import ResidentTherapyNoteModal from "@/views/resident/partials/ResidentTherapyNoteModal";

export default {
  mixins: [UtilMixin, LoadingOverlayableMixin, BTableMixin],
  components: {ResidentTherapyNoteModal, BTablePagination},
  props: {
    resident: {
      type: Object
    }
  },
  data: function() {
    return {
      bTablePerPage: 5,
      bTableFields: [
        {key: "id", label: "#", class: "id-col", sortable: true},
        {key: "datetime", sortable: true},
        {key: "duration_minutes", label: "Duration", sortable: true},
        {key: "create_datetime", label: "Created", class: "created-col", sortable: true},
        {key: "update_datetime", label: "Updated", class: "updated-col", sortable: true},
        {key: "actions", class: "actions-col"},
      ],
      records: null
    }
  },
  created: function() {
    this.loadRecords(true);
  },
  methods: {
    bTableLoadData: function() {
      this.loadRecords();
    },
    loadRecords: function(pageOnly) {
      this.loadingOverlay = true;
      var params = Object.assign({}, this.bTableHttpParams, {
          resident: this.resident.id,
          xfields: "_resident",
          page_size: pageOnly ? 1 : this.bTableHttpParams.page_size,
      });
      this.$http.get("therapy_note", { params: params }).then((response) => {
        if (!pageOnly) {
          this.records = response.data.results;
        }
        this.bTablePagination = response.data.pagination;
        this.loadingOverlay = false;
      }, (error) => {
        this.showDefaultServerError(error);
        this.loadingOverlay = false;
      });
    }
  }
}
</script>
