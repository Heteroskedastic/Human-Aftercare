<style scoped>
</style>
<template>
  <div class="d-flex flex-column flex-root">
    <div class="d-flex flex-row flex-column-fluid page">
      <facility-side-menu></facility-side-menu>
      <div class="d-flex flex-column flex-row-fluid wrapper" id="kt_wrapper">
        <facility-header></facility-header>
        <!--begin::Content-->
        <keep-alive include="NOPAGE">
          <router-view class="content d-flex flex-column flex-column-fluid"></router-view>
        </keep-alive>
        <facility-footer></facility-footer>
      </div>
    </div>
    <div id="kt_scrolltop" class="scrolltop">
      <span class="fas fa-arrow-up text-white">
      </span>
    </div>

  </div>

</template>

<script>
import FacilitySideMenu from "../sideMenus/FacilitySideMenu";
import FacilityFooter from "../footers/FacilityFooter";
import FacilityHeader from "../headers/FacilityHeader";

export default {
  components: {
    FacilityHeader,
    FacilityFooter,
    FacilitySideMenu
  },
  methods: {
    ktInits: function () {
      // Init Desktop & Mobile Headers
      if (typeof window.KTLayoutHeader !== 'undefined') {
        window.KTLayoutHeader.init('kt_header', 'kt_header_mobile');
      }

      // Init Header Menu
      if (typeof window.KTLayoutHeaderMenu !== 'undefined') {
        window.KTLayoutHeaderMenu.init('kt_header_menu', 'kt_header_menu_wrapper');
      }

      // Init Header Topbar For Mobile Mode
      if (typeof window.KTLayoutHeaderTopbar !== 'undefined') {
        window.KTLayoutHeaderTopbar.init('kt_header_mobile_topbar_toggle');
      }

      // Init Brand Panel For Logo
      if (typeof window.KTLayoutBrand !== 'undefined') {
        window.KTLayoutBrand.init('kt_brand');
      }

      // Init Aside
      if (typeof window.KTLayoutAside !== 'undefined') {
        window.KTLayoutAside.init('kt_aside');
      }

      // Init Aside Menu Toggle
      if (typeof window.KTLayoutAsideToggle !== 'undefined') {
        window.KTLayoutAsideToggle.init('kt_aside_toggle');
      }

      // Init Aside Menu
      if (typeof window.KTLayoutAsideMenu !== 'undefined') {
        window.KTLayoutAsideMenu.init('kt_aside_menu');
      }

      // Init Subheader
      if (typeof window.KTLayoutSubheader !== 'undefined') {
        window.KTLayoutSubheader.init('kt_subheader');
      }

      // Init Content
      if (typeof window.KTLayoutContent !== 'undefined') {
        window.KTLayoutContent.init('kt_content');
      }

      // Init Footer
      if (typeof window.KTLayoutFooter !== 'undefined') {
        window.KTLayoutFooter.init('kt_footer');
      }
      // Init Scrolltop
      if (typeof window.KTLayoutScrolltop !== 'undefined') {
        window.KTLayoutScrolltop.init('kt_scrolltop');
      }

    }
  },
  mounted: function () {
    this.ktInits()
  }
};
</script>
