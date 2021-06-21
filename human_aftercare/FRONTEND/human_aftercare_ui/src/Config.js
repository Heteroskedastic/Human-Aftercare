export const Config = {
  API_BASE_URL: "/api/v1", // to use that locally change that to 'http://BACKEND_SERVER/api/v1'
  FACILITY_API_BASE_URL: domain => `/fc/${domain}/api/v1`,
  DEFAULT_PHONE_COUNTRY_CODE: "+1",
  DEFAULT_AXIOS_TIMEOUT: undefined,  // in ms. undefined means no timeout set
};
