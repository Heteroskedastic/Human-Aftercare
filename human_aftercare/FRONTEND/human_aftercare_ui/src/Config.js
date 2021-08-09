export const Config = {
  API_BASE_URL: process.env.VUE_APP_API_PREFIX || "/api/v1",
  FACILITY_API_BASE_URL: domain => `/fc/${domain}/api/v1`,
  DEFAULT_PHONE_COUNTRY_CODE: process.env.VUE_APP_DEFAULT_PHONE_COUNTRY_CODE || "+1",
  DEFAULT_AXIOS_TIMEOUT: undefined,  // in ms. undefined means no timeout set
};
