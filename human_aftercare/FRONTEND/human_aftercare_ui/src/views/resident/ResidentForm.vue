<style scoped>
  .image-input [data-action=cancel] {
    display: flex;
  }
  .image-input-wrapper {
    background-position: 50%;
    background-color: #f1f8ff;
  }
  .image-input-wrapper.blank-photo i {
    color: #b6c9dc;
    font-size: 6rem;
  }
  .image-input-wrapper.blank-photo {
    display: flex;
    align-items: center;
    justify-content: center;
  }
</style>

<template>
  <div>
    <page-bar v-if="$route.params.record_id">
      <template slot="breadcrumb-title-text">
        <span class="text-muted">
          Edit Resident: <span class="text-warning">{{record.first_name}} {{record.last_name}}</span>
        </span>
      </template>
    </page-bar>
    <page-bar v-else></page-bar>
    <div class="d-flex flex-column-fluid">
      <div class="container">
        <div class="card card-custom">
          <div class="card-header card-header-tabs-line">
            <div class="card-title">
              <h3 class="card-label">
                <template v-if="$route.params.record_id">
                  Edit Resident: <span class="text-primary">{{record.first_name}} {{record.last_name}}</span>
                </template>
                <template v-else>
                  Add New Resident
                </template>
              </h3>
            </div>
          </div>
          <div class="card-body">
            <form @submit.prevent="saveRecord">
              <div class="form-group row">
                <label class="col-xl-3 col-lg-3 col-form-label">Photo</label>
                <div class="col-lg-9 col-xl-6">
                  <div class="image-input image-input-outline" id="kt_profile_avatar">
                    <div v-if="!photoChosenFileData && !record.photo" class="image-input-wrapper blank-photo">
                      <i class="far fa-user"></i>
                    </div>
                    <div v-else class="image-input-wrapper"
                         :style="`background-image: url(${photoChosenFileData || record.photo})`"></div>

                    <label class="btn btn-xs btn-icon btn-circle btn-white btn-hover-text-primary btn-shadow"
                           data-action="change" data-toggle="tooltip" title="" data-original-title="Change photo">
                      <i class="fa fa-pen icon-sm text-muted"></i>
                      <input type="file" name="photo_image" id="photo_image" ref="photoRef" @change="onChangePhotoFile" accept=".png, .jpg, .jpeg"/>
                    </label>
                    <span v-show="!!photoChosenFileData" class="btn btn-xs btn-icon btn-circle btn-white btn-hover-text-primary btn-shadow"
                          data-action="cancel" data-toggle="tooltip" title="Cancel photo" @click="clearChosenPhoto()">
                        <i class="ki ki-bold-close icon-xs text-muted"></i>
                    </span>
                    <span v-show="!photoChosenFileData && record.photo" class="btn btn-xs btn-icon btn-circle btn-danger btn-hover-text-danger btn-shadow"
                          data-action="remove" data-toggle="tooltip" title="Remove photo" @click="record.photo=null">
                      <i class="far fa-trash-alt text-light"></i>
                    </span>
                  </div>
                  <span class="form-text text-muted">Allowed file types: png, jpg, jpeg.</span>
                </div>
              </div>
              <div class="form-group row">
                <label class="col-xl-3 col-lg-3 col-form-label">First Name</label>
                <div class="col-lg-9 col-xl-6">
                  <input v-model="record.first_name" class="form-control form-control-lg form-control-solid" type="text" required/>
                </div>
              </div>
              <div class="form-group row">
                <label class="col-xl-3 col-lg-3 col-form-label">Last Name</label>
                <div class="col-lg-9 col-xl-6">
                  <input v-model="record.last_name" class="form-control form-control-lg form-control-solid" type="text" required/>
                </div>
              </div>
              <div class="form-group row">
                <label class="col-xl-3 col-lg-3 col-form-label">Middle Name</label>
                <div class="col-lg-9 col-xl-6">
                  <input v-model="record.middle_name" class="form-control form-control-lg form-control-solid" type="text"/>
                </div>
              </div>
              <div class="form-group row">
                <label class="col-xl-3 col-lg-3 col-form-label">Birth Date</label>
                <div class="col-lg-9 col-xl-6">
                  <div class="input-group input-group-lg input-group-solid">
                    <div class="input-group-prepend birthdate-picker cursor-pointer">
                      <span class="input-group-text">
                        <i class="la la-calendar"></i>
                      </span>
                    </div>
                    <vue-datetimepicker v-model="record.birth_date"
                                        :dateonly="true"
                                        placeholder=""
                                        name="birth_date"
                                        :wrap="true"
                                        iconRef=".birthdate-picker"
                                        class="form-control form-control-lg form-control-solid"
                                        :config="{format: 'YYYY-MM-DD', mask: true, timepicker: false, scrollInput: false}"></vue-datetimepicker>
                  </div>
                </div>
              </div>
              <div class="form-group row">
                <label class="col-xl-3 col-lg-3 col-form-label">Gender</label>
                <div class="col-lg-9 col-xl-6">
                  <div class="radio-inline">
                      <label v-for="g in $const.GENDER_OPTIONS" :key="g.value" class="radio">
                        <input type="radio" name="genderRadio" v-model="record.gender" :value="g.value" required/>
                        <span></span>{{g.title}}
                      </label>
                  </div>
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
                    <input v-model="record.email" type="email" class="form-control form-control-lg form-control-solid"/>
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
                    <input v-model="record.phone_number" type="text" class="form-control form-control-lg form-control-solid"/>
                  </div>
                </div>
              </div>
              <div class="form-group row">
                <label class="col-xl-3 col-lg-3 col-form-label">Eye Color</label>
                <div class="col-lg-9 col-xl-6">
                  <select class="form-control form-control-lg form-control-solid" v-model="record.eye_color">
                    <option :value="null">-</option>
                    <option v-for="c in $const.EYE_COLOR_OPTIONS" :value="c.value">{{ c.title }}</option>
                  </select>
                </div>
              </div>
              <div class="form-group row">
                <label class="col-xl-3 col-lg-3 col-form-label">Hair Color</label>
                <div class="col-lg-9 col-xl-6">
                  <select class="form-control form-control-lg form-control-solid" v-model="record.hair_color">
                    <option :value="null">-</option>
                    <option v-for="c in $const.HAIR_COLOR_OPTIONS" :value="c.value">{{ c.title }}</option>
                  </select>
                </div>
              </div>
              <div class="card-footer">
                <div class="row">
                  <div class="col text-left">
                    <button type="submit" class="btn btn-primary mr-2" :disabled="saving">
                      <template v-if="$route.params.record_id">
                        <i :class="saving? 'fa fa-spin fa-spinner': 'fa fa-save'"></i>
                        <span v-show="!saving">Save</span>
                        <span v-show="saving">Saving</span>
                      </template>
                      <template v-else>
                        <i :class="saving? 'fa fa-spin fa-spinner': 'fa fa-plus'"></i>
                        <span v-show="!saving">Add</span>
                        <span v-show="saving">Adding</span>
                      </template>
                    </button>
                    <a is="router-link" :to="{name: backRoute}" class="btn btn-secondary">Cancel</a>
                  </div>
                  <div class="col text-right">
                    <span
                      ref="deleteConfirm"
                      v-if="$route.params.record_id"
                      @confirmed="deleteRecord"
                      is="inline-confirm"
                      btn-class="btn btn-danger"
                      sure-class="text-danger"
                      yes-class="btn-danger"
                      no-class="btn-secondary"
                      confirming-icon-class="fa fa-spin fa-spinner"
                      class="inline"
                      :confirming="deleting"
                      :disabled="$cannot('delete', 'academicgoal')"
                    >
                      <i class="far fa-trash-alt"></i> Delete
                    </span>
                  </div>

                </div>
              </div>
            </form>
          </div>
        </div>

      </div>
    </div>

  </div>
</template>

<script>
import moment from "moment";

import PageBar from "@/components/PageBar";
import LoadingOverlayableMixin from "@/components/mixins/LoadingOverlayableMixin";
import UtilMixin from "@/components/mixins/UtilMixin";
import VueDatetimepicker from "@/components/libs/VueDatetimepicker";
import InlineConfirm from "@/components/libs/InlineConfirm";

export default {
  components: {InlineConfirm, PageBar, VueDatetimepicker },
  mixins: [LoadingOverlayableMixin, UtilMixin],
  data: function() {
    return {
      saving: false,
      deleting: false,
      photoChosenFile: null,
      photoChosenFileData: null,
      backRoute: this.$route.params.backRef || this.$rns.RESIDENT_LIST,
      record: {
        eye_color: null,
        hair_color: null,
        gender: "m"
      }
    };
  },
  methods: {
    clearChosenPhoto: function () {
      this.photoChosenFile = null;
      this.photoChosenFileData = null;
      this.$refs.photoRef.value = null;
    },
    onChangePhotoFile: function(event) {
      if (event.target.files.length > 0) {
        this.photoChosenFile = event.target.files[0];
        var f = this.photoChosenFile,
          self = this,
          r = new FileReader();
        r.onloadend = function(e) {
          self.photoChosenFileData = e.target.result;
        };
        r.readAsDataURL(f);
      }
    },
    deleteRecord: function() {
      this.deleting = true;
      this.$http.delete(`resident/${this.record.id}`).then(
        (response) => {
          this.showSuccess("Resident deleted successfully", 5000);
          this.deleting = false;
          this.$eventsBus.$emit("residents:table-updated");
          this.$router.push({ name: this.$rns.RESIDENT_LIST, replace: true });
        },
        (error) => {
          this.deleting = false;
          this.showDefaultServerError(error);
        }
      );
    },
    saveRecord: function() {
      this.saving = true;
      var url = "resident",
          httpFunc = this.$http.post,
          successMessage = "Resident added successfully";
      if (this.record.id) {
        url = `resident/${this.record.id}/`;
        httpFunc = this.$http.patch;
        successMessage = "Resident updated successfully";
      }
      var postData = Object.assign({}, this.record);
      if (postData.birth_date) {
        postData.birth_date = moment(postData.birth_date).format("YYYY-MM-DD")
      }
      if (this.photoChosenFileData) {
        postData.photo = this.photoChosenFileData;
      } else if (postData.photo !== null) {
        delete postData.photo;
      }

      httpFunc(url, postData).then(
        (response) => {
          this.saving = false;
          this.showSuccess(successMessage, 5000);
          this.$eventsBus.$emit("residents:table-updated");
          this.$router.push({ name: this.backRoute });
        },
        (error) => {
          this.saving = false;
          this.showDefaultServerError(error);
        }
      );
    }
  }
};
</script>
