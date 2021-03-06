import Vue from "vue";
import BootstrapVue from "bootstrap-vue";
import MaskedInput from "vue-text-mask";
import Toasted from 'vue-toasted';

import router from "./router";
import store from "./store";
import axiosInstance from "./axios";
import App from "./App";
import UtilMixin from "./components/mixins/UtilMixin";
import "./validators";
import EventBus from "./EventBus";
import * as Constants from "./Constants";

import { version as AppVersion } from "../package.json";
import {permAbility, definePermAbilitiesFor} from "./ability";
import abilityPluginPerm from "./abilityPluginPerm";

import "bootstrap-vue/dist/bootstrap-vue.css"
import "../public/metronic/assets/plugins/global/plugins.bundle.css";
import "../public/metronic/assets/css/style.bundle.css";
import "../public/metronic/assets/css/themes/layout/header/base/light.css";
import "../public/metronic/assets/css/themes/layout/header/menu/light.css";
import "../public/metronic/assets/css/themes/layout/brand/dark.css";
import "../public/metronic/assets/css/themes/layout/aside/dark.css";
import "../public/resources/css/custom.css";

Vue.use(abilityPluginPerm, permAbility);

Vue.use(BootstrapVue);
Vue.component("masked-input", MaskedInput);
Vue.use(Toasted, {
  iconPack: "custom-class",
  theme: "bubble",
  position: "top-center"
});

Vue.prototype.$eventsBus = EventBus;

/****************************************
 ****************** App *****************
 ****************************************/

Vue.prototype.$http = axiosInstance;
Vue.prototype.$publicPath = process.env.BASE_URL;
Vue.prototype.$appVersion = AppVersion;
Vue.prototype.$const = Constants;

new Vue({
  el: "#app",
  template: "<App/>",
  components: { App },
  store: store,
  router: router,
  data: {},
  mixins: [UtilMixin],
  methods: {
  },
  created: function() {
    this.$store.watch(
      (state) => {
        return state.currentUser;
      },
      (newUser) => {
        definePermAbilitiesFor(newUser);
      }
    );

  },
  mounted: function() {}
});

