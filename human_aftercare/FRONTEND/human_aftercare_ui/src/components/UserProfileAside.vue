<style scoped>

</style>

<template>
  <div id="kt_quick_user" class="offcanvas offcanvas-right p-10">
    <!--begin::Header-->
    <div class="offcanvas-header d-flex align-items-center justify-content-between pb-5">
      <h3 class="font-weight-bold m-0">User Profile
        <small class="text-muted font-size-sm ml-2">0 message(s)</small></h3>
      <a href="#" class="btn btn-xs btn-icon btn-light btn-hover-primary" id="kt_quick_user_close">
        <i class="ki ki-close icon-xs text-muted"></i>
      </a>
    </div>
    <!--end::Header-->
    <!--begin::Content-->
    <div class="offcanvas-content pr-5 mr-n5">
      <!--begin::Header-->
      <div class="d-flex align-items-center mt-5">
        <div class="symbol symbol-100 mr-5">
          <div v-if="$store.state.currentUser.profile.avatar" class="symbol-label" :style="`background-image: url(${$store.state.currentUser.profile.avatar})`"></div>
          <div v-else class="symbol-label" :style="`background-image: url(${$publicPath}resources/images/blank-avatar.png)`"></div>
          <i class="symbol-badge bg-success"></i>
        </div>
        <div class="d-flex flex-column">
          <a is="router-link" :to="{name: $rns.USER_PROFILE}" @click.native="closeOffcanvas" class="font-weight-bold font-size-h5 text-dark-75 text-hover-primary">{{capitalize($store.getters.userFullName)}}</a>
          <div class="text-muted mt-1">Administrator Staff</div>
          <div class="navi mt-2">
            <a :href="`${$store.state.currentUser.email? ('mailto:'+$store.state.currentUser.email):'javascript:'}`" class="navi-item">
              <span class="navi-link p-0 pb-2">
                <span class="navi-icon">
                  <span class="fas fa-envelope text-primary">
                  </span>
                </span>
                <span class="navi-text text-muted text-hover-primary">{{ $store.state.currentUser.email || '[NO E-MAIL]'}}</span>
              </span>
            </a>
            <a href="javascript:" class="btn btn-sm btn-light-danger font-weight-bolder py-2 px-5" :class="{disabled: signingOut}" @click="logout()">
              <i class="fas" :class="signingOut? 'fa-spin fa-spinner': 'fa-power-off'"></i>
              Sign Out
            </a>
          </div>
        </div>
      </div>
      <!--end::Header-->
      <!--begin::Separator-->
      <div class="separator separator-dashed mt-8 mb-5"></div>
      <!--end::Separator-->
      <!--begin::Nav-->
      <div class="navi navi-spacer-x-0 p-0">
        <!--begin::Item-->
        <a is="router-link" :to="{name: $rns.USER_PROFILE}" class="navi-item" @click.native="closeOffcanvas">
          <div class="navi-link">
            <div class="symbol symbol-40 bg-light mr-3">
              <div class="symbol-label">
                <span class="fas fa-user-cog text-success">
                </span>
              </div>
            </div>
            <div class="navi-text">
              <div class="font-weight-bold">My Profile</div>
              <div class="text-muted">Account settings and more</div>
            </div>
          </div>
        </a>
        <!--end:Item-->
        <!--begin::Item-->
        <a class="navi-item">
          <div class="navi-link disabled">
            <div class="symbol symbol-40 bg-light mr-3">
              <div class="symbol-label">
                <span class="fas fa-envelope-open-text text-primary">
                </span>
              </div>
            </div>
            <div class="navi-text">
              <div class="font-weight-bold">My Messages</div>
              <div class="text-muted">Inbox and tasks</div>
            </div>
          </div>
        </a>
        <!--end:Item-->
        <!--begin::Item-->
        <a class="navi-item">
          <div class="navi-link disabled">
            <div class="symbol symbol-40 bg-light mr-3">
              <div class="symbol-label">
                <span class="fas fa-cogs text-info">
                </span>
              </div>
            </div>
            <div class="navi-text">
              <div class="font-weight-bold">Settings</div>
              <div class="text-muted">Settings and system configurations</div>
            </div>
          </div>
        </a>
        <!--end:Item-->
      </div>
      <!--end::Nav-->
      <!--begin::Separator-->
      <div class="separator separator-dashed my-7"></div>
      <!--end::Separator-->
      <!--begin::Notifications-->
      <div>
        <!--begin:Heading-->
        <h5 class="mb-5">Recent Notifications:</h5>
        <div>
          <span class="text-muted">[No Notification]</span>
        </div>
        <!--end::Item-->
      </div>
      <!--end::Notifications-->
    </div>
    <!--end::Content-->
  </div>

</template>

<script>
import UtilMixin from "@/components/mixins/UtilMixin";

export default {
  mixins: [UtilMixin],
  data: function() {
    return {
      signingOut: false
    }
  },
  methods: {
    logout: function () {
      this.signingOut = true;
      this.$http.delete("session").then(() => {
        this.signingOut = false;
        this.$eventsBus.$emit("user:session-expired", this.$store.state.currentUser);
      },
      (error) => {
        this.signingOut = false;
        this.showDefaultServerError(error);
      });
    },
    closeOffcanvas() {
      new window.KTOffcanvas(window.KTLayoutQuickUser.getElement()).hide();
    }

  },
  mounted: function () {
    window.KTLayoutQuickUser.init('kt_quick_user');
  }
}
</script>
