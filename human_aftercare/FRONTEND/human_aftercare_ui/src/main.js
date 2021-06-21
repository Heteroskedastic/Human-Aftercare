import Vue from "vue";
import BootstrapVue from "bootstrap-vue";
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

require("../public/metronic/assets/plugins/global/plugins.bundle.css");
require("../public/metronic/assets/css/style.bundle.css");
require("../public/metronic/assets/css/themes/layout/header/base/light.css");
require("../public/metronic/assets/css/themes/layout/header/menu/light.css");
require("../public/metronic/assets/css/themes/layout/brand/dark.css");
require("../public/metronic/assets/css/themes/layout/aside/dark.css");
require("../public/resources/css/custom.css");

Vue.use(BootstrapVue);
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
  },
  mounted: function() {}
});

