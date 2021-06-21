import Vue from "vue";
import Vuex from "vuex";
import axiosInstance from "./axios";
import {Config} from "./Config";

Vue.use(Vuex);

/****************************************
 **************** Store *****************
 ****************************************/
const store = new Vuex.Store({
  state: {
    routeDomain: null,
    currentUser: {
      facility: {}
    },
  },
  mutations: {
    currentUser: function (state, payload) {
      state.currentUser = payload.currentUser;
    }
  },
  actions: {
  },
  getters: {
    isStaffUser: function (state) {
      return true === state.currentUser.is_staff;
    },
    isSuperUser: function (state) {
      return true === state.currentUser.is_superuser;
    },
    isStaffOrSuperUser: function (state) {
      return (
        true === (state.currentUser.is_staff || state.currentUser.is_superuser)
      );
    },
    isAuthenticated: function (state) {
      return !!state.currentUser.id;
    },
    userFullName: function (state) {
      var name = "";
      if (state.currentUser.id) {
        if (state.currentUser.first_name) {
          name = state.currentUser.first_name;
        }
        if (state.currentUser.last_name) {
          name += " " + state.currentUser.last_name;
        }
        name = name.trim();
        if (!name) {
          name = state.currentUser.username;
        }
      }
      return name;
    },
    userDisplayName: function (state) {
      if (state.currentUser.id) {
        var name = (state.currentUser.firstname || state.currentUser.username);
        return name.charAt(0).toUpperCase() + name.slice(1);
      }
      return "";
    },
    currentUserId: function (state) {
      return state.currentUser.id;
    },
    currentFacility: function (state) {
      return state.currentUser && state.currentUser.facility;
    },
    currentFacilityId: function (state, getters) {
      return getters.currentFacility && getters.currentFacility.id;
    },
    currentFacilityDomain: function (state, getters) {
      return getters.currentFacility && getters.currentFacility.domain;
    },
    currentFacilityBaseUrl: function (state, getters) {
      return Config.HOTEL_API_BASE_URL(getters.currentFacilityDomain)
    }
  }
});

export default store;
