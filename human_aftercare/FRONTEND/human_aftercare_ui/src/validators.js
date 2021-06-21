/****************************************
 * Register Vee-Validate and include    *
 * Extra vee-validate validators        *
 ****************************************/

import Vue from "vue";
import { ValidationProvider, extend } from "vee-validate";

Vue.component('ValidationProvider', ValidationProvider);
