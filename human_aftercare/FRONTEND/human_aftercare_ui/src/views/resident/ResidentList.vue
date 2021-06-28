<style>
  .resident-list-table td {
    vertical-align: middle !important;
  }
  .resident-list-table th {
    color: #B5B5C3;
    font-size: 0.9rem;
    text-transform: uppercase;
    font-weight: 600;
    letter-spacing: 0.1rem;
  }
  .resident-list-table th.id-col {
    width: 50px;
  }
  .resident-list-table th.actions-col {
    width: 40px;
  }
  .resident-list-table td.actions-col {
    vertical-align: middle;
    padding: 0 !important;
  }

</style>

<template>
  <div class="resident-list-page">
    <page-bar></page-bar>
    <div class="d-flex flex-column-fluid">
      <div class="container">
        <div class="card card-custom">
          <div class="card-header flex-wrap border-0 pt-6 pb-0">
            <div class="card-title">
              <h3 class="card-label">Resident List
                <span class="d-block text-muted pt-2 font-size-sm">resident list and management</span></h3>
            </div>
            <div class="card-toolbar">
              <a is="router-link" :to="{name: $rns.RESIDENT_ADD}"
                 class="btn btn-light-success font-weight-bolder" :class="{disabled: $cannot('add', 'resident')}">
                <span class="fas fa-plus"></span> New Resident
              </a>
            </div>
          </div>
          <div class="card-body">
            <b-table :items="residents" :fields="bTableFields" :sort-by.sync="bTableSortBy" no-local-sorting responsive
                     show-empty
                     class="resident-list-table" :sort-desc.sync="bTableSortDesc">
              <template #empty="scope">
                <h6 class="text-muted text-center pt-10">{{ scope.emptyText }}</h6>
              </template>
              <template #cell(name)="data">
                <div class="d-flex align-items-center">
                  <div class="symbol symbol-40 symbol-light-primary flex-shrink-0">
                    <img v-if="data.item.photo_thumb" class="fit-cover" :src="data.item.photo_thumb" alt="photo">
                    <span v-else class="symbol-label font-size-h4 font-weight-bold">{{data.item.first_name[0]}}</span>
                  </div>
                  <div class="ml-4">
                    <a is="router-link"  :to="{name: $rns.RESIDENT_DETAIL, params: {record_id: data.item.id}}">
                      <div class="text-primary font-weight-bolder font-size-lg mb-0">{{data.item.first_name}} {{data.item.last_name}}</div>
                    </a>
                    <span class="text-muted font-weight-bold">{{data.item.middle_name || '-'}}</span></div>
                </div>
              </template>
              <template #cell(gender)="data">
                <span class="font-weight-bold text-dark-50">{{ ($const.GENDER_MAP[data.item.gender] || {}).title }}</span>
              </template>
              <template #cell(email)="data">
                <a :class="data.item.email? 'text-dark-65': 'text-muted'" target="_blank"
                   :href="data.item.email? `mailto:${data.item.email}`: null">{{ data.item.email || '[NO E-MAIL]' }}
                </a>
              </template>
              <template #cell(phone_number)="data">
                <a :class="data.item.phone_number? 'text-dark-65': 'text-muted'" target="_blank"
                   :href="data.item.phone_number? `tel:${data.item.phone_number}`: null">{{ data.item.phone_number || '[NO PHONE]' }}
                </a>
              </template>
              <template #cell(birth_date)="data">
                <span class="font-weight-bold text-dark-50">{{formatDate(data.item.birth_date, 'MMM D, YYYY')}}</span>
              </template>
              <template #cell(actions)="data">
                <a is="router-link" :to="{name: $rns.RESIDENT_EDIT, params: {record_id: data.item.id}}"
                   class="btn btn-sm btn-default btn-text-warning btn-hover-warning btn-icon mr-2"
                   :class="{disabled: $cannot('change', 'resident')}"
                   title="Edit Resident">
                  <i class="far fa-edit"></i>
                </a>
                <a href="javascript:" class="btn btn-sm btn-default btn-text-danger btn-hover-danger btn-icon mr-2"
                   :class="{disabled: $cannot('delete', 'resident')}"
                   title="Delete Resident" @click="showConfirmDeleteModal(data.item)">
                  <i class="far fa-trash-alt"></i>
                </a>
              </template>
            </b-table>
          </div>
          <div class="card-footer">
            <b-table-pagination
                @page-change="p => bTableCurrentPage=p"
                @per-page-change="p => {bTableCurrentPage=1; bTablePerPage=p}"
                :init-per-page="bTablePerPage"
                :per-page-options="bTablePageSizeOptions"
                :table-pagination="bTablePagination"></b-table-pagination>
          </div>
        </div>
      </div>
    </div>
    <b-modal ref="confirmDeleteModalRef" id="confirmDeleteModal" :hide-header="true">
      <p class="text-danger h6">Are you sure to delete this record?</p>
      <div slot="modal-footer" class="w-100">

        <button
          type="button"
          class="btn btn-light-primary font-weight-bold float-left"
          @click="$refs.confirmDeleteModalRef.hide()"
        >
          Cancel
        </button>
        <button
          type="button"
          class="btn btn-light-danger font-weight-bold float-right"
          :disabled="deletingRecord"
          @click="deleteRecord()"
        >
          <i :class="deletingRecord? 'fa fa-spin fa-spinner':'fa fa-trash'"></i>
          <span v-show="!deletingRecord">Delete</span>
          <span v-show="deletingRecord">Deleting</span>
        </button>
      </div>
    </b-modal>

  </div>

</template>

<script>
import PageBar from "@/components/PageBar";
import UtilMixin from "@/components/mixins/UtilMixin";
import BTableMixin from "@/components/mixins/BTableMixin";
import BTablePagination from "@/components/BTablePagination";
import LoadingOverlayableMixin from "@/components/mixins/LoadingOverlayableMixin";

export default {
  mixins: [LoadingOverlayableMixin, UtilMixin, BTableMixin],
  components: {BTablePagination, PageBar},
  data: function () {
    return {
      bTableSortKeyMap: {
        name: "first_name,last_name"
      },
      bTableFields: [
        {key: "id", label: "#", class: "id-col", sortable: true},
        {key: "name", sortable: true},
        {key: "gender", sortable: true},
        {key: "birth_date", sortable: true},
        {key: "email", sortable: true},
        {key: "phone_number", sortable: true},
        {key: "actions", class: "actions-col"},
      ],
      residents: [],
      deletingRecord: false,
      selectedRecordForDelete: null
    }
  },
  methods: {
    bTableLoadData: function() {
      this.loadResidents();
    },
    loadResidents: function() {
      this.loadingOverlay = true;
      this.$http.get("resident", {params: this.bTableHttpParams}).then(res => {
        this.loadingOverlay = false;
        this.residents = res.data.results;
        this.bTablePagination = res.data.pagination;
      }, (error) => {
        this.loadingOverlay = false;
        this.showDefaultServerError(error);
      });
    },
    showConfirmDeleteModal: function(record) {
      this.selectedRecordForDelete = record;
      this.$refs.confirmDeleteModalRef.show();
    },
    deleteRecord: function() {
      this.deletingRecord = true;
      this.$http.delete(`resident/${this.selectedRecordForDelete.id}`).then(
        (response) => {
          this.showSuccess("Resident deleted successfully", 5000);
          this.bTableLoadData();
          this.deletingRecord = false;
          this.$refs.confirmDeleteModalRef.hide();
        },
        (error) => {
          this.deletingRecord = false;
          this.showDefaultServerError(error);
        }
      );
    }
  },
  mounted: function() {
    this.loadResidents();
  }
}
</script>
