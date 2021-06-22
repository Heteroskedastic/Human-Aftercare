/****************************************
 ***************** Router ***************
 ****************************************/
import Vue from "vue";
import VueRouter from "vue-router";
import axiosInstance from "@/axios";
import store from "@/store";
import {Config} from "@/Config";
import Dashboard from "@/views/Dashboard";
import FacilityList from "@/views/FacilityList";
import FacilityLayout from "@/components/layouts/FacilityLayout";
import SiteLayout from "@/components/layouts/SiteLayout";
import ResidentList from "@/views/ResidentList";
import UserProfile from "@/views/UserProfile";

Vue.use(VueRouter);

export const routeNames = {
  SITE_ROOT: "site_root",
  SITE_FACILITY_LIST: "site_facility_list",
  ROOT: "root",
  LOGIN: "login",
  USER_PROFILE: "user_profile",
  DASHBOARD: "dashboard",
  RESIDENT_LIST: "resident_list",
};

Vue.prototype.$rns = routeNames;

const router = new VueRouter({
  scrollBehavior: function (to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    } else {
      return {x: 0, y: 0};
    }
  },
  routes: [
    {
      path: '/site/',
      component: SiteLayout,
      meta: {
      },
      beforeEnter: (to, from, next) => {
        store.state.routeDomain = null;
        next();
      },
      children: [
        {
          path: "",
          name: routeNames.SITE_ROOT,
          redirect: {name: routeNames.SITE_FACILITY_LIST},
        }, {
          path: 'facility-list',
          name: routeNames.SITE_FACILITY_LIST,
          component: FacilityList,
          meta: {
            pageInfo: {
              title: "Facility List"
            }
          },

        },
        {
          path: "*",
          redirect: {name: routeNames.SITE_ROOT}
        }
      ]
    },
    {
      path: "/fc/:facility_domain/",
      component: FacilityLayout,
      meta: {
        rootRoute: routeNames.ROOT
      },
      beforeEnter: (to, from, next) => {
        store.state.routeDomain = to.params.facility_domain;
        //{baseURL: Config.FACILITY_API_BASE_URL(to.params.facility_domain)}
        axiosInstance.get("session").then(
          function(response) {
            store.state.currentUser = response.data;
            next();
          },
          function(error) {
            if (error.response.status === 404) {
              store.state.routeDomain = null;
              alert("Invalid facility page!");
              next({name: routeNames.SITE_ROOT, replace: true})
            } else if (error.response.status === 401) {
              next();
            }
          }
        );
      },
      children: [
        {
          path: "",
          name: routeNames.ROOT,
          redirect: {name: routeNames.DASHBOARD},
        },
        {
          path: "user-profile",
          name: routeNames.USER_PROFILE,
          meta: {
            pageInfo: {
              title: "User Profile"
            }
          },
          component: UserProfile
        },
        {
          path: "dashboard",
          name: routeNames.DASHBOARD,
          meta: {
            pageInfo: {
              title: "Dashboard"
            }
          },
          component: Dashboard
        },
        {
          path: "resident-list",
          name: routeNames.RESIDENT_LIST,
          meta: {
            pageInfo: {
              title: "Resident List"
            }
          },
          component: ResidentList
        },
        {
          path: "*",
          redirect: {name: routeNames.ROOT}
        }
      ]
    },
    {
      path: "*",
      redirect: {name: routeNames.SITE_ROOT}
    }
  ]
});

router.afterEach(function (toRoute) {
  let title = "Human-Aftercare :: ",
      pageInfo = toRoute.meta.pageInfo || {};
  if (pageInfo.title) {
    title = title + pageInfo.title + " :: ";
  }
  if (pageInfo.titleDesc) {
    title = title + pageInfo.titleDesc;
  }
  window.document.title = title;
});

export default router;
