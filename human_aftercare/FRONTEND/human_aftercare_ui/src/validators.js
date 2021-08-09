/****************************************
 * Register Vee-Validate and include    *
 * Extra vee-validate validators        *
 ****************************************/

import Vue from "vue";
import VeeValidate from "vee-validate";
import { Validator } from "vee-validate";
import { parse } from "libphonenumber-js";

Vue.use(VeeValidate, {
  fieldsBagName: "formFields",
  delay: 10,
  events: "input|blur"
});

const moment = window.moment;

Validator.extend("age", {
  getMessage: function(field, args, data) {
    return data.message;
  },
  validate: function(value, args) {
    var min = args[0],
      max = args[1];
    if (!max && !min) {
      throw '"age": at-least 1 arguments required!';
    }
    var now = moment(),
      message = null;
    if (min && max) {
      message = `age should be between "${min} and "${max}" years`;
    }
    if (min && now.diff(value, "years") < parseInt(min)) {
      return {
        valid: false,
        data: { message: message || `age should be more than "${min}" years` }
      };
    }
    if (max && now.diff(value, "years") > parseInt(max)) {
      return {
        valid: false,
        data: { message: message || `age should be less than "${max}" years` }
      };
    }
    return true;
  }
});

Validator.extend("phone", {
  getMessage: function(field, args, data) {
    return data.message;
  },
  validate: function(value, args) {
    if (!value) {
      return true;
    }
    var parsed = parse(value);
    if (parsed.country) {
      return true;
    }
    return { valid: false, data: { message: `Invalid phone: "${value}"` } };
  }
});
