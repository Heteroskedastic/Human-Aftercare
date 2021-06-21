<style scoped>
  img.user-avatar {
    object-fit: cover;
  }
</style>
<template>
  <div id="kt_header" class="header header-fixed">
    <!--begin::Header Mobile-->
    <div id="kt_header_mobile" class="header-mobile align-items-center header-mobile-fixed">
      <!--begin::Logo-->
      <a href="javascript:">
        <img alt="Logo" :src="`${$publicPath}resources/images/logo-light.png`" />
      </a>
      <!--end::Logo-->
      <!--begin::Toolbar-->
      <div class="d-flex align-items-center">
        <!--begin::Aside Mobile Toggle-->
        <button class="btn p-0 burger-icon burger-icon-left" id="kt_aside_mobile_toggle">
          <span></span>
        </button>
        <!--end::Aside Mobile Toggle-->
        <!--begin::Header Menu Mobile Toggle-->
        <button class="btn p-0 burger-icon ml-4" id="kt_header_mobile_toggle" style="display: none">
          <span></span>
        </button>
        <!--end::Header Menu Mobile Toggle-->
        <!--begin::Topbar Mobile Toggle-->
        <button class="btn btn-hover-text-primary p-0 ml-2" id="kt_header_mobile_topbar_toggle">
          <span class="svg-icon svg-icon-xl">
            <!--begin::Svg Icon | path:assets/media/svg/icons/General/User.svg-->
            <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="24px" height="24px" viewBox="0 0 24 24" version="1.1">
              <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                <polygon points="0 0 24 0 24 24 0 24" />
                <path d="M12,11 C9.790861,11 8,9.209139 8,7 C8,4.790861 9.790861,3 12,3 C14.209139,3 16,4.790861 16,7 C16,9.209139 14.209139,11 12,11 Z" fill="#000000" fill-rule="nonzero" opacity="0.3" />
                <path d="M3.00065168,20.1992055 C3.38825852,15.4265159 7.26191235,13 11.9833413,13 C16.7712164,13 20.7048837,15.2931929 20.9979143,20.2 C21.0095879,20.3954741 20.9979143,21 20.2466999,21 C16.541124,21 11.0347247,21 3.72750223,21 C3.47671215,21 2.97953825,20.45918 3.00065168,20.1992055 Z" fill="#000000" fill-rule="nonzero" />
              </g>
            </svg>
            <!--end::Svg Icon-->
          </span>
        </button>
        <!--end::Topbar Mobile Toggle-->
      </div>
      <!--end::Toolbar-->
    </div>
    <!--end::Header Mobile-->

    <!--begin::Container-->
    <div class="container-fluid d-flex align-items-stretch justify-content-between">
      <!--begin::Header Menu Wrapper-->
      <div class="header-menu-wrapper header-menu-wrapper-left" id="kt_header_menu_wrapper">
        <!--begin::Header Menu-->
        <div id="kt_header_menu" class="header-menu header-menu-mobile header-menu-layout-default">
          <!--begin::Header Nav-->
          <ul class="menu-nav">
          </ul>
          <!--end::Header Nav-->
        </div>
        <!--end::Header Menu-->
      </div>
      <!--end::Header Menu Wrapper-->
      <!--begin::Topbar-->
      <div class="topbar">
        <!--begin::Search-->
        <div class="dropdown" id="kt_quick_search_toggle">
          <!--begin::Toggle-->
          <div class="topbar-item" data-toggle="dropdown" data-offset="10px,0px">
            <div class="btn btn-icon btn-clean btn-lg btn-dropdown mr-1">
              <span class="svg-icon svg-icon-xl svg-icon-primary">
                <!--begin::Svg Icon | path:assets/media/svg/icons/General/Search.svg-->
                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="24px" height="24px" viewBox="0 0 24 24" version="1.1">
                  <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                    <rect x="0" y="0" width="24" height="24" />
                    <path d="M14.2928932,16.7071068 C13.9023689,16.3165825 13.9023689,15.6834175 14.2928932,15.2928932 C14.6834175,14.9023689 15.3165825,14.9023689 15.7071068,15.2928932 L19.7071068,19.2928932 C20.0976311,19.6834175 20.0976311,20.3165825 19.7071068,20.7071068 C19.3165825,21.0976311 18.6834175,21.0976311 18.2928932,20.7071068 L14.2928932,16.7071068 Z" fill="#000000" fill-rule="nonzero" opacity="0.3" />
                    <path d="M11,16 C13.7614237,16 16,13.7614237 16,11 C16,8.23857625 13.7614237,6 11,6 C8.23857625,6 6,8.23857625 6,11 C6,13.7614237 8.23857625,16 11,16 Z M11,18 C7.13400675,18 4,14.8659932 4,11 C4,7.13400675 7.13400675,4 11,4 C14.8659932,4 18,7.13400675 18,11 C18,14.8659932 14.8659932,18 11,18 Z" fill="#000000" fill-rule="nonzero" />
                  </g>
                </svg>
                <!--end::Svg Icon-->
              </span>
            </div>
          </div>
          <!--end::Toggle-->
          <!--begin::Dropdown-->
          <div class="dropdown-menu p-0 m-0 dropdown-menu-right dropdown-menu-anim-up dropdown-menu-lg">
            <div class="quick-search quick-search-dropdown" id="kt_quick_search_dropdown">
              <!--begin:Form-->
              <form method="get" class="quick-search-form">
                <div class="input-group">
                  <div class="input-group-prepend">
                    <span class="input-group-text">
                      <span class="svg-icon svg-icon-lg">
                        <!--begin::Svg Icon | path:assets/media/svg/icons/General/Search.svg-->
                        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="24px" height="24px" viewBox="0 0 24 24" version="1.1">
                          <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <rect x="0" y="0" width="24" height="24" />
                            <path d="M14.2928932,16.7071068 C13.9023689,16.3165825 13.9023689,15.6834175 14.2928932,15.2928932 C14.6834175,14.9023689 15.3165825,14.9023689 15.7071068,15.2928932 L19.7071068,19.2928932 C20.0976311,19.6834175 20.0976311,20.3165825 19.7071068,20.7071068 C19.3165825,21.0976311 18.6834175,21.0976311 18.2928932,20.7071068 L14.2928932,16.7071068 Z" fill="#000000" fill-rule="nonzero" opacity="0.3" />
                            <path d="M11,16 C13.7614237,16 16,13.7614237 16,11 C16,8.23857625 13.7614237,6 11,6 C8.23857625,6 6,8.23857625 6,11 C6,13.7614237 8.23857625,16 11,16 Z M11,18 C7.13400675,18 4,14.8659932 4,11 C4,7.13400675 7.13400675,4 11,4 C14.8659932,4 18,7.13400675 18,11 C18,14.8659932 14.8659932,18 11,18 Z" fill="#000000" fill-rule="nonzero" />
                          </g>
                        </svg>
                        <!--end::Svg Icon-->
                      </span>
                    </span>
                  </div>
                  <input type="text" class="form-control" placeholder="Search..." />
                  <div class="input-group-append">
                    <span class="input-group-text">
                      <i class="quick-search-close ki ki-close icon-sm text-muted"></i>
                    </span>
                  </div>
                </div>
              </form>
              <!--end::Form-->
              <!--begin::Scroll-->
              <div class="quick-search-wrapper scroll" data-scroll="true" data-height="325" data-mobile-height="200"></div>
              <!--end::Scroll-->
            </div>
          </div>
          <!--end::Dropdown-->
        </div>
        <!--end::Search-->
        <!--begin::User-->
        <div class="topbar-item">
          <div class="btn btn-icon btn-icon-mobile w-auto btn-clean d-flex align-items-center btn-lg px-2" id="kt_quick_user_toggle">
            <span class="text-muted font-weight-bold font-size-base d-none d-md-inline mr-1">Hi,</span>
            <span class="text-dark-50 font-weight-bolder font-size-base d-none d-md-inline mr-3">{{$store.getters.userDisplayName}}</span>
            <span class="symbol symbol-lg-35 symbol-25 symbol-light-success">
              <span v-if="!$store.state.currentUser.profile.avatar" class="symbol-label font-size-h5 font-weight-bold">{{$store.getters.userDisplayName[0]}}</span>
              <img v-else :src="$store.state.currentUser.profile.avatar" class="user-avatar">
            </span>
          </div>
        </div>
        <!--end::User-->
      </div>
      <!--end::Topbar-->
    </div>
    <!--end::Container-->
    <user-profile-aside></user-profile-aside>

  </div>
</template>

<script>
import UtilMixin from "@/components/mixins/UtilMixin";
import $ from "jquery";
import UserProfileAside from "@/components/UserProfileAside";

export default {
  mixins: [UtilMixin],
  components: {UserProfileAside},
  data: function() {
    return {

    };
  },
  methods: {
    logout: function() {
      var self = this;
      this.$http.delete("session").then(
        function() {
          self.$eventsBus.$emit(
            "user:session-expired",
            self.$store.state.currentUser
          );
        },
        function(error) {
          self.showDefaultServerError(error);
        }
      );
    }
  },
  mounted: function() {

  }
};
</script>
