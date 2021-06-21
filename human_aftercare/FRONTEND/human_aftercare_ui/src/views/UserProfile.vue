<style scoped>
  .image-input [data-action=cancel] {
    display: flex;
  }
  .image-input-wrapper {
    background-position: 50%;
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
              <h3 class="card-label">User Profile Setting</h3>
            </div>
            <div class="card-toolbar">
              <ul class="nav nav-tabs nav-bold nav-tabs-line">
                <li class="nav-item">
                  <a class="nav-link active" data-toggle="tab" href="#personalInfoTabPane">
                    <span class="nav-icon">
                      <i class="flaticon2-user-1"></i>
                    </span>
                    <span class="nav-text">Personal Info</span>
                  </a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" data-toggle="tab" href="#changePasswordTabPane">
                    <span class="nav-icon">
                      <i class="fas fa-user-lock"></i>
                    </span>
                    <span class="nav-text">Change Password</span>
                  </a>
                </li>
              </ul>
            </div>
          </div>
          <div class="card-body">
            <div class="tab-content">
              <div class="tab-pane fade show active" id="personalInfoTabPane" role="tabpanel"
                   aria-labelledby="personalInfoTabPane">
                <form @submit.prevent="saveProfileInfo">
                  <div class="form-group row">
                    <label class="col-xl-3 col-lg-3 col-form-label">Avatar</label>
                    <div class="col-lg-9 col-xl-6">
                      <div class="image-input image-input-outline" id="kt_profile_avatar"
                           :style="`background-image: url(${$publicPath}resources/images/blank-avatar.png)`">
                        <div class="image-input-wrapper"
                             :style="`background-image: url(${avatarChosenFileData || userProfile.profile.avatar || ($publicPath + 'resources/images/blank-avatar.png')})`"></div>
                        <label class="btn btn-xs btn-icon btn-circle btn-white btn-hover-text-primary btn-shadow"
                               data-action="change" data-toggle="tooltip" title="" data-original-title="Change avatar">
                          <i class="fa fa-pen icon-sm text-muted"></i>
                          <input type="file" name="avatar_image" id="avatar_image" ref="avatarImageRef" @change="onChangeAvatarFile" accept=".png, .jpg, .jpeg"/>
                        </label>
                        <span v-show="!!avatarChosenFileData" class="btn btn-xs btn-icon btn-circle btn-white btn-hover-text-primary btn-shadow"
                              data-action="cancel" data-toggle="tooltip" title="Cancel avatar" @click="clearChosenAvatar()">
                            <i class="ki ki-bold-close icon-xs text-muted"></i>
                        </span>
                        <span v-show="!avatarChosenFileData && userProfile.profile.avatar" class="btn btn-xs btn-icon btn-circle btn-danger btn-hover-text-danger btn-shadow"
                              data-action="remove" data-toggle="tooltip" title="Remove avatar" @click="userProfile.profile.avatar=null">
                          <i class="far fa-trash-alt text-light"></i>
                        </span>
                      </div>
                      <span class="form-text text-muted">Allowed file types: png, jpg, jpeg.</span>
                    </div>
                  </div>
                  <div class="form-group row">
                    <label class="col-xl-3 col-lg-3 col-form-label">Username</label>
                    <div class="col-lg-9 col-xl-6">
                      <input v-model="userProfile.username" class="form-control form-control-lg form-control-solid" type="text" readonly/>
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
                        <input v-model="userProfile.email" type="email" class="form-control form-control-lg form-control-solid"/>
                      </div>
                    </div>
                  </div>
                  <div class="form-group row">
                    <label class="col-xl-3 col-lg-3 col-form-label">First Name</label>
                    <div class="col-lg-9 col-xl-6">
                      <input v-model="userProfile.first_name" class="form-control form-control-lg form-control-solid" type="text"/>
                    </div>
                  </div>
                  <div class="form-group row">
                    <label class="col-xl-3 col-lg-3 col-form-label">Last Name</label>
                    <div class="col-lg-9 col-xl-6">
                      <input v-model="userProfile.last_name" class="form-control form-control-lg form-control-solid" type="text" value="Bold"/>
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
                        <vue-datetimepicker v-model="userProfile.profile.birth_date"
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
                            <input type="radio" name="genderRadio" v-model="userProfile.profile.gender" :value="g.value" />
                            <span></span>{{g.title}}
                          </label>
                      </div>
                    </div>
                  </div>
                  <div class="card-footer">
                    <button type="submit" class="btn btn-primary mr-2" :disabled="savingPersonalInfo">
                      <i v-if="savingPersonalInfo" class="fa fa-spin fa-spinner"></i>
                      Save Changes
                    </button>
                    <button type="reset" class="btn btn-secondary" @click="getProfile" :disabled="loadingOverlay">Cancel</button>
                  </div>
                </form>
              </div>
              <div class="tab-pane fade" id="changePasswordTabPane" role="tabpanel" aria-labelledby="changePasswordTabPane">
                <form @submit.prevent="changePassword">
                  <div class="form-group row">
                    <label class="col-xl-3 col-lg-3 col-form-label text-alert">Current Password</label>
                    <div class="col-lg-9 col-xl-6">
                      <input v-model="userPassword.current_password" type="password"
                             class="form-control form-control-lg form-control-solid mb-2"
                             placeholder="Current password" required/>
                    </div>
                  </div>
                  <div class="form-group row">
                    <label class="col-xl-3 col-lg-3 col-form-label text-alert">New Password</label>
                    <div class="col-lg-9 col-xl-6">
                      <input v-model="userPassword.new_password" type="password"
                             class="form-control form-control-lg form-control-solid mb-2"
                             placeholder="New password" required/>
                    </div>
                  </div>
                  <div class="form-group row">
                    <label class="col-xl-3 col-lg-3 col-form-label text-alert">Verify Password</label>
                    <div class="col-lg-9 col-xl-6">
                      <input v-model="userPassword.re_new_password" type="password"
                             class="form-control form-control-lg form-control-solid mb-2"
                             placeholder="Verify password" required/>
                    </div>
                  </div>
                  <div class="card-footer">
                    <button type="submit" class="btn btn-primary mr-2"
                            :disabled="!userPassword.new_password || !passwordMatched || changingPassword">
                      <i v-if="changingPassword" class="fa fa-spin fa-spinner"></i>
                      Change Password
                    </button>
                    <button type="reset" class="btn btn-secondary" @click="resetPasswordFields()">Cancel</button>
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
import $ from "jquery";
import moment from "moment";
import UtilMixin from "@/components/mixins/UtilMixin";
import LoadingOverlayableMixin from "@/components/mixins/LoadingOverlayableMixin";
import PageBar from "@/components/PageBar";
import InlineConfirm from "@/components/libs/InlineConfirm";
import VueDatetimepicker from "@/components/libs/VueDatetimepicker";


export default {
  mixins: [UtilMixin, LoadingOverlayableMixin],
  components: {PageBar, VueDatetimepicker},
  data: function () {
    return {
      nextRoute: this.$route.params.nextRoute ||
          this.$route.meta.pageInfo.home ||
          this.$rns.ROOT,
      avatarChosenFile: null,
      avatarChosenFileData: null,
      uploadingAvatar: false,
      deletingAvatar: false,
      savingPersonalInfo: false,
      changingPassword: false,
      userPassword: {
        current_password: "",
        new_password: "",
        re_new_password: ""
      },
      userProfile: {
        email: null,
        first_name: null,
        last_name: null,
        profile: {
          gender: null,
          birth_date: null,
          avatar: null,
        }
      }
    };
  },
  created: function () {
    this.getProfile()
  },
  computed: {
    passwordMatched: function () {
      return this.userPassword.new_password === this.userPassword.re_new_password;
    }
  },
  methods: {
    resetPasswordFields: function() {
      this.userPassword = {
        current_password: "",
        new_password: "",
        re_new_password: ""
      };
    },
    getProfile: function() {
      this.loadingOverlay = true;
      this.$http.get("me").then((response) => {
        var user = Object.assign({}, response.data);
        user.profile = Object.assign({}, user.profile);
        this.loadingOverlay = false;
        this.userProfile = response.data;
      }, (error) => {
        this.loadingOverlay = false;
        this.showDefaultServerError(error);
      });
    },
    clearChosenAvatar: function () {
      this.avatarChosenFile = null;
      this.avatarChosenFileData = null;
      this.$refs.avatarImageRef.value = null;
    },
    onChangeAvatarFile: function(event) {
      if (event.target.files.length > 0) {
        this.avatarChosenFile = event.target.files[0];
        var f = this.avatarChosenFile,
          self = this,
          r = new FileReader();
        r.onloadend = function(e) {
          self.avatarChosenFileData = e.target.result;
        };
        r.readAsDataURL(f);
      }
    },
    saveProfileInfo: function () {
      var postData = Object.assign({}, this.userProfile);
      postData.profile = Object.assign({}, this.userProfile.profile);
      if (postData.profile.birth_date) {
        postData.profile.birth_date = moment(postData.profile.birth_date).format("YYYY-MM-DD")
      }
      if (this.avatarChosenFileData) {
        postData.profile.avatar = this.avatarChosenFileData;
      } else if (postData.profile.avatar !== null) {
        delete postData.profile.avatar;
      }
      this.savingPersonalInfo = true;
      this.$http.put("me", postData).then(response => {
        var user = Object.assign({}, response.data);
        user.profile = Object.assign({}, user.profile);
        this.$store.state.currentUser = user;
        this.savingPersonalInfo = false;
        this.clearChosenAvatar();
        this.userProfile = response.data;
        this.showSuccess("Profile updated successfully", 5000);
      }, error => {
        this.savingPersonalInfo = false;
        this.showDefaultServerError(error);
      });
    },
    changePassword: function () {
      this.changingPassword = true;
      this.$http.put("me/password", this.userPassword).then(response => {
        this.userPassword = {};
        this.changingPassword = false;
        this.showSuccess("Password changed successfully", 5000);
      }, response => {
        this.changingPassword = false;
        this.showDefaultServerError(response, true);
      });
    }
  }
};
</script>
