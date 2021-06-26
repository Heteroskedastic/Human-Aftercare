<style scoped>
  .image-input [data-action=cancel] {
    display: flex;
  }
  .image-input-wrapper {
    background-position: 50%;
    background-color: #f1f8ff;
  }
  .image-input-wrapper.blank-logo i {
    color: #b6c9dc;
    font-size: 6rem;
  }
  .image-input-wrapper.blank-logo {
    display: flex;
    align-items: center;
    justify-content: center;
  }
</style>

<template>

  <div>
    <page-bar></page-bar>
    <div class="d-flex flex-column-fluid">
      <div class="container">
        <div class="card card-custom">
          <div class="card-header card-header-tabs-line">
            <div class="card-title">
              <h3 class="card-label">Facility Setting</h3>
            </div>
            <div class="card-toolbar">
              <ul class="nav nav-tabs nav-bold nav-tabs-line">
                <li class="nav-item">
                  <a class="nav-link active" data-toggle="tab" href="#basicInfoTabPane">
                    <span class="nav-icon">
                      <i class="fas fa-hospital-alt"></i>
                    </span>
                    <span class="nav-text">Basic Info</span>
                  </a>
                </li>
              </ul>
            </div>
          </div>
          <div class="card-body">
            <div class="tab-content">
              <div class="tab-pane fade show active" id="basicInfoTabPane" role="tabpanel"
                   aria-labelledby="basicInfoTabPane">
                <form @submit.prevent="saveBasicInfo">
                  <div class="form-group row">
                    <label class="col-xl-3 col-lg-3 col-form-label">Logo</label>
                    <div class="col-lg-9 col-xl-6">
                      <div class="image-input image-input-outline" id="kt_profile_avatar">
                        <div v-if="!logoChosenFileData && !facility.logo" class="image-input-wrapper blank-logo">
                          <i class="far fa-image"></i>
                        </div>
                        <div v-else class="image-input-wrapper"
                             :style="`background-image: url(${logoChosenFileData || facility.logo})`"></div>
                        <label class="btn btn-xs btn-icon btn-circle btn-white btn-hover-text-primary btn-shadow"
                               data-action="change" data-toggle="tooltip" title="" data-original-title="Change logo">
                          <i class="fa fa-pen icon-sm text-muted"></i>
                          <input type="file" name="logo_image" id="logo_image" ref="logoImageRef" @change="onChangeLogoFile" accept=".png, .jpg, .jpeg"/>
                        </label>
                        <span v-show="!!logoChosenFileData" class="btn btn-xs btn-icon btn-circle btn-white btn-hover-text-primary btn-shadow"
                              data-action="cancel" data-toggle="tooltip" title="Cancel logo" @click="clearChosenLogo()">
                            <i class="ki ki-bold-close icon-xs text-muted"></i>
                        </span>
                        <span v-show="!logoChosenFileData && facility.logo" class="btn btn-xs btn-icon btn-circle btn-danger btn-hover-text-danger btn-shadow"
                              data-action="remove" data-toggle="tooltip" title="Remove logo" @click="facility.logo=null">
                          <i class="far fa-trash-alt text-light"></i>
                        </span>
                      </div>
                      <span class="form-text text-muted">Allowed file types: png, jpg, jpeg.</span>
                    </div>
                  </div>
                  <div class="form-group row">
                    <label class="col-xl-3 col-lg-3 col-form-label">Domain (URL)</label>
                    <div class="col-lg-9 col-xl-6">
                      <span class="form-control form-control-lg form-control-solid text-muted">{{facility.domain}} ( <a :href="facility.url">{{ facility.url }}</a> )</span>
                    </div>
                  </div>
                  <div class="form-group row">
                    <label class="col-xl-3 col-lg-3 col-form-label">Name (*)</label>
                    <div class="col-lg-9 col-xl-6">
                      <input v-model="facility.name" class="form-control form-control-lg form-control-solid" type="text"/>
                    </div>
                  </div>
                  <div class="form-group row">
                    <label class="col-xl-3 col-lg-3 col-form-label">Description</label>
                    <div class="col-lg-9 col-xl-6">
                      <textarea v-model="facility.description" class="form-control form-control-lg form-control-solid" rows="2"></textarea>
                    </div>
                  </div>
                  <div class="form-group row">
                    <label class="col-xl-3 col-lg-3 col-form-label">Address</label>
                    <div class="col-lg-9 col-xl-6">
                      <textarea v-model="facility.address" class="form-control form-control-lg form-control-solid" rows="2"></textarea>
                    </div>
                  </div>
                  <div class="form-group row">
                    <label class="col-xl-3 col-lg-3 col-form-label">Email Address</label>
                    <div class="col-lg-9 col-xl-6">
                      <div class="input-group input-group-lg input-group-solid">
                        <div class="input-group-prepend">
                          <span class="input-group-text">
                            <i class="la la-at"></i>
                          </span>
                        </div>
                        <input v-model="facility.email" type="email" class="form-control form-control-lg form-control-solid"/>
                      </div>
                    </div>
                  </div>
                  <div class="form-group row">
                    <label class="col-xl-3 col-lg-3 col-form-label">Phone Number</label>
                    <div class="col-lg-9 col-xl-6">
                      <div class="input-group input-group-lg input-group-solid">
                        <div class="input-group-prepend">
                          <span class="input-group-text">
                            <i class="la la-phone"></i>
                          </span>
                        </div>
                        <input v-model="facility.phone_number" type="text" class="form-control form-control-lg form-control-solid"/>
                      </div>
                    </div>
                  </div>
                  <div class="form-group row">
                    <label class="col-xl-3 col-lg-3 col-form-label">Primary Contact Name</label>
                    <div class="col-lg-9 col-xl-6">
                      <input v-model="facility.primary_contact_name" class="form-control form-control-lg form-control-solid" type="text" value="Bold"/>
                    </div>
                  </div>
                  <div class="form-group row">
                    <label class="col-xl-3 col-lg-3 col-form-label">Primary Contact Email</label>
                    <div class="col-lg-9 col-xl-6">
                      <div class="input-group input-group-lg input-group-solid">
                        <div class="input-group-prepend">
                          <span class="input-group-text">
                            <i class="la la-at"></i>
                          </span>
                        </div>
                        <input v-model="facility.primary_contact_email" type="email" class="form-control form-control-lg form-control-solid"/>
                      </div>
                    </div>
                  </div>
                  <div class="form-group row">
                    <label class="col-xl-3 col-lg-3 col-form-label">Primary Contact Phone</label>
                    <div class="col-lg-9 col-xl-6">
                      <div class="input-group input-group-lg input-group-solid">
                        <div class="input-group-prepend">
                          <span class="input-group-text">
                            <i class="la la-phone"></i>
                          </span>
                        </div>
                        <input v-model="facility.primary_contact_phone" type="text" class="form-control form-control-lg form-control-solid"/>
                      </div>
                    </div>
                  </div>
                  <div class="card-footer">
                    <template v-if="$can('change', 'facility')">
                      <button type="submit" class="btn btn-primary mr-2" :disabled="savingBasicInfo">
                        <i v-if="savingBasicInfo" class="fa fa-spin fa-spinner"></i>
                        Save Changes
                      </button>
                      <button type="reset" class="btn btn-secondary" @click="getFacility" :disabled="loadingOverlay">Cancel</button>
                    </template>
                    <div v-else class="alert alert-custom alert-light-warning fade show mb-5" role="alert">
                      <div class="alert-icon"><i class="flaticon-warning"></i></div>
                      <div class="alert-text">You have no permission to change facility info!</div>
                    </div>

                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>

  </div>

</template>

<script>
import UtilMixin from "@/components/mixins/UtilMixin";
import LoadingOverlayableMixin from "@/components/mixins/LoadingOverlayableMixin";
import PageBar from "@/components/PageBar";

export default {
  mixins: [UtilMixin, LoadingOverlayableMixin],
  components: {PageBar},
  data: function () {
    return {
      nextRoute: this.$route.params.nextRoute ||
          this.$route.meta.pageInfo.home ||
          this.$rns.ROOT,
      logoChosenFile: null,
      logoChosenFileData: null,
      savingBasicInfo: false,
      facility: {}
    };
  },
  created: function () {
    this.getFacility()
  },
  computed: {
  },
  methods: {
    getFacility: function() {
      this.loadingOverlay = true;
      this.$http.get("facility").then((response) => {
        this.loadingOverlay = false;
        this.facility = response.data;
      }, (error) => {
        this.loadingOverlay = false;
        this.showDefaultServerError(error);
      });
    },
    clearChosenLogo: function () {
      this.logoChosenFile = null;
      this.logoChosenFileData = null;
      this.$refs.logoImageRef.value = null;
    },
    onChangeLogoFile: function(event) {
      if (event.target.files.length > 0) {
        this.logoChosenFile = event.target.files[0];
        var f = this.logoChosenFile,
          self = this,
          r = new FileReader();
        r.onloadend = function(e) {
          self.logoChosenFileData = e.target.result;
        };
        r.readAsDataURL(f);
      }
    },
    saveBasicInfo: function () {
      var postData = Object.assign({}, this.facility);
      if (this.logoChosenFileData) {
        postData.logo = this.logoChosenFileData;
      } else if (postData.logo !== null) {
        delete postData.logo;
      }
      this.savingBasicInfo = true;
      this.$http.put("facility", postData).then(response => {
        this.savingBasicInfo = false;
        this.$store.state.currentUser.facility = Object.assign({}, response.data);
        this.facility = response.data;
        this.clearChosenLogo();
        this.showSuccess("Profile updated successfully", 5000);
      }, error => {
        this.savingBasicInfo = false;
        this.showDefaultServerError(error);
      });
    }
  }
};
</script>
