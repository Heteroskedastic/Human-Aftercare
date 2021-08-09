<style scoped>
</style>

<template>
  <div>
    <page-bar>
      <template slot="breadcrumb-title-text">
        <span class="text-muted">
          Resident Detail: <span class="text-warning">{{ resident.first_name }} {{ resident.last_name }}</span>
        </span>
      </template>
    </page-bar>
    <div class="d-flex flex-column-fluid" v-if="resident.id">
      <div class="container">
        <div class="card card-custom gutter-b">
          <div class="card-body">
            <!--begin::Details-->
            <div class="d-flex mb-9">
              <!--begin: Pic-->
              <div class="flex-shrink-0 mr-7 mt-lg-0 mt-3">
                <div class="symbol symbol-50 symbol-lg-120" v-if="resident.photo">
                  <img :src="resident.photo" alt="image" class="fit-cover" />
                </div>
                <div class="symbol symbol-50 symbol-lg-120 symbol-primary" v-else>
                  <span class="font-size-h1 symbol-label font-weight-boldest">
                    {{ resident.first_name[0] }} {{ resident.last_name[0] }}
                  </span>
                </div>
              </div>
              <!--end::Pic-->
              <!--begin::Info-->
              <div class="flex-grow-1">
                <!--begin::Title-->
                <div class="d-flex justify-content-between flex-wrap mt-1">
                  <div class="d-flex mr-3">
                    <a href="#" class="text-dark-75 text-hover-primary font-size-h5 font-weight-bold mr-3">
                      {{ resident.first_name }} {{ resident.last_name }}
                    </a>
                    <a href="javascript:">
                      <i class="flaticon2-correct text-success font-size-h5"></i>
                    </a>
                  </div>
                  <div class="my-lg-0 my-3">
                    <a is="router-link"
                       :to="{name: $rns.RESIDENT_LIST}"
                       class="btn btn-sm btn-light-info font-weight-bolder text-uppercase mr-3">
                      <i class="flaticon2-left-arrow-1"></i>Back
                    </a>
                    <a is="router-link"
                       :to="{name: $rns.RESIDENT_EDIT, params: {record_id: $route.params.record_id, backRef: $route.name}}"
                       class="btn btn-sm btn-light-warning font-weight-bolder text-uppercase mr-3"
                       :class="{disabled: $cannot('change', 'resident')}">
                      <i class="fas fa-edit"></i>Edit
                    </a>
                  </div>
                </div>
                <!--end::Title-->
                <!--begin::Content-->
                <div class="d-flex flex-wrap justify-content-between mt-1">
                  <div class="d-flex flex-column flex-grow-1 pr-8">
                    <div class="d-flex flex-wrap mb-4">
                      <a href="#" class="text-dark-50 text-hover-primary font-weight-bold mr-lg-8 mr-5 mb-lg-0 mb-2">
                        <i class="flaticon2-new-email mr-2 font-size-lg"></i>{{resident.email || '[No E-mail]'}}
                      </a>
                      <a href="#" class="text-dark-50 text-hover-primary font-weight-bold mr-lg-8 mr-5 mb-lg-0 mb-2">
                        <i class="flaticon2-phone mr-2 font-size-lg"></i>{{formatPhone(resident.phone_number, {_default: '[NO PHONE]'})}}
                      </a>
                      <a href="#" class="text-dark-50 text-hover-primary font-weight-bold">
                        <i class="mr-2 font-size-lg" :class="resident.gender=='f'? 'fa fa-female': 'fa fa-male'">
                        </i>{{ageFormat(resident.birth_date)}}
                      </a>
                    </div>
                    <span class="font-weight-bold text-dark-50">Some info about resident can be here!</span>
                    <span class="font-weight-bold text-dark-50">Some info about resident can be here!</span>
                  </div>
                  <div class="d-flex align-items-center w-25 flex-fill float-right mt-lg-12 mt-8">
                    <span class="font-weight-bold text-dark-75">Progress</span>
                    <div class="progress progress-xs mx-3 w-100">
                      <div class="progress-bar bg-success" role="progressbar" style="width: 63%;" aria-valuenow="50"
                           aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                    <span class="font-weight-bolder text-dark">78%</span>
                  </div>
                </div>
                <!--end::Content-->
              </div>
              <!--end::Info-->
            </div>
            <!--end::Details-->
            <div class="separator separator-solid"></div>
            <!--begin::Items-->
            <div class="d-flex align-items-center flex-wrap mt-8">
              <div class="d-flex align-items-center flex-lg-fill mr-5 mb-2">
                <span class="mr-4">
                  <i class="fas fa-book-medical fa-2x text-muted"></i>
                </span>
                <div class="d-flex flex-column flex-lg-fill">
                  <span class="text-dark-75 font-weight-bolder font-size-sm">35 Therapy Notes</span>
                  <a href="javascript:" class="text-primary font-weight-bolder">View</a>
                </div>
              </div>
              <div class="d-flex align-items-center flex-lg-fill mr-5 mb-2">
                <span class="mr-4">
                  <i class="fas fa-notes-medical fa-2x text-muted"></i>
                </span>
                <div class="d-flex flex-column flex-lg-fill">
                  <span class="text-dark-75 font-weight-bolder font-size-sm">25 Medical Notes</span>
                  <a href="javascript:" class="text-primary font-weight-bolder">View</a>
                </div>
              </div>
              <div class="d-flex align-items-center flex-lg-fill mr-5 mb-2">
                <span class="mr-4">
                  <i class="flaticon2-writing display-4 text-muted font-weight-bold"></i>
                </span>
                <div class="d-flex flex-column flex-lg-fill">
                  <span class="text-dark-75 font-weight-bolder font-size-sm">10 General Notes</span>
                  <a href="javascript:" class="text-primary font-weight-bolder">View</a>
                </div>
              </div>
              <div class="d-flex align-items-center flex-lg-fill mr-5 mb-2">
                <span class="mr-4">
                  <i class="flaticon2-calendar-5 display-4 text-muted font-weight-bold"></i>
                </span>
                <div class="d-flex flex-column flex-lg-fill">
                  <span class="text-dark-75 font-weight-bolder font-size-sm">73 Tasks</span>
                  <a href="javascript:" class="text-primary font-weight-bolder">View</a>
                </div>
              </div>
              <div class="d-flex align-items-center flex-lg-fill mr-5 mb-2">
                <span class="mr-4">
                  <i class="flaticon2-chat display-4 text-muted font-weight-bold"></i>
                </span>
                <div class="d-flex flex-column">
                  <span class="text-dark-75 font-weight-bolder font-size-sm">648 Comments</span>
                  <a href="javascript:" class="text-primary font-weight-bolder">View</a>
                </div>
              </div>
              <!--end::Item-->
            </div>
            <!--begin::Items-->
          </div>
        </div>
        <resident-therapy-notes-panel :resident="resident"></resident-therapy-notes-panel>
      </div>
    </div>

  </div>
</template>

<script>
import PageBar from "@/components/PageBar";
import LoadingOverlayableMixin from "@/components/mixins/LoadingOverlayableMixin";
import UtilMixin from "@/components/mixins/UtilMixin";
import ResidentTherapyNotesPanel from "@/views/resident/partials/ResidentTherapyNotesPanel";

export default {
  components: {ResidentTherapyNotesPanel, PageBar},
  mixins: [LoadingOverlayableMixin, UtilMixin],
  data: function () {
    return {
      resident: {}
    };
  },
  created: function () {
    this.loadResident();
  },
  methods: {
    loadResident: function () {
      var residentId = this.$route.params.record_id;
      this.loadingOverlay = true;
      this.$http.get(`resident/${residentId}/`).then(
          (response) => {
            this.loadingOverlay = false;
            this.resident = response.data;
          },
          (error) => {
            this.loadingOverlay = false;
            this.showDefaultServerError(error);
          }
      );
    }
  }
};
</script>
