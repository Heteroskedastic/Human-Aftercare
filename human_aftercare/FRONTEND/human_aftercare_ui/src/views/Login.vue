<style scoped>
.content {
  padding-top: 0 !important;
  padding-bottom: 0!important;
}
.login.login-1 .login-aside .title {
  color: #986923;
}
.login.login-1 .login-aside {
  background-color: rgb(242, 201, 138);
}
.login.login-1 .login-aside .aside-img {
  min-height: 450px;
}
.login.login-1 .login-signin,
.login.login-1 .login-signup,
.login.login-1 .login-forgot {
  display: none;
}
.login.login-1.login-signin-on .login-signup {
  display: none;
}
.login.login-1.login-signin-on .login-signin {
  display: block;
}
.login.login-1.login-signin-on .login-forgot {
  display: none;
}
.login.login-1.login-signup-on .login-signup {
  display: block;
}
.login.login-1.login-signup-on .login-signin {
  display: none;
}
.login.login-1.login-signup-on .login-forgot {
  display: none;
}
.login.login-1.login-forgot-on .login-signup {
  display: none;
}
.login.login-1.login-forgot-on .login-signin {
  display: none;
}
.login.login-1.login-forgot-on .login-forgot {
  display: block;
}

@media (min-width: 992px) {
  .login.login-1 .login-aside {
    width: 100%;
    max-width: 700px;
  }
  .login.login-1 .login-content {
    width: 100%;
    max-width: 500px;
  }
  .login.login-1 .login-content .login-form {
    width: 100%;
    max-width: 450px;
  }
}
@media (min-width: 992px) and (max-width: 1399.98px) {
  .login.login-1 .login-aside {
    width: 100%;
    max-width: 450px;
  }
}
@media (max-width: 991.98px) {
  .login.login-1 .login-content .login-form {
    width: 100%;
    max-width: 400px;
  }
}
@media (max-width: 575.98px) {
  .login.login-1 .aside-img {
    min-height: 300px !important;
    background-size: 400px;
  }
  .login.login-1 .login-content .login-form {
    width: 100%;
    max-width: 100%;
  }
}

</style>

<template>
  <div class="d-flex flex-column flex-root">
    <!--begin::Login-->
    <div class="login login-1 d-flex flex-column flex-lg-row flex-column-fluid bg-white" :class="`login-${pageState}-on`" id="kt_login">
      <!--begin::Aside-->
      <div class="login-aside d-flex flex-column flex-row-auto">
        <!--begin::Aside Top-->
        <div class="d-flex flex-column-auto flex-column pt-lg-40 pt-15">
          <!--begin::Aside header-->
          <a is="router-link" :to="{name: $rns.SITE_FACILITY_LIST}" class="text-center mb-10">
            <img :src="`${$publicPath}resources/images/logo-letter-1.png`" class="max-h-70px" alt=""/>
          </a>
          <!--end::Aside header-->
          <!--begin::Aside title-->
          <h3 class="font-weight-bolder text-center font-size-h4 font-size-h1-lg title">Human Aftercare
            <br/>Facility Admin Dashboard</h3>
          <!--end::Aside title-->
        </div>
        <!--end::Aside Top-->
        <!--begin::Aside Bottom-->
        <div class="aside-img d-flex flex-row-fluid bgi-no-repeat bgi-position-y-bottom bgi-position-x-center"
             :style="`background-image: url(${$publicPath}resources/images/login-visual-1.svg)`"></div>
        <!--end::Aside Bottom-->
      </div>
      <!--begin::Aside-->
      <!--begin::Content-->
      <div
          class="login-content flex-row-fluid d-flex flex-column justify-content-center position-relative overflow-hidden p-7 mx-auto">
        <!--begin::Content body-->
        <div class="d-flex flex-column-fluid flex-center">
          <!--begin::Signin-->
          <div class="login-form login-signin">
            <!--begin::Form-->
            <form class="form" id="kt_login_signin_form" @submit.prevent="signIn">
              <!--begin::Title-->
              <div class="pb-13 pt-lg-0 pt-5">
                <h3 class="font-weight-bolder text-dark font-size-h4 font-size-h1-lg">Welcome to Human Aftercare</h3>
                <span class="text-muted font-weight-bold font-size-h4">New Here?
									<a href="javascript:" id="kt_login_signup" @click="pageState='signup'"
                     class="text-primary font-weight-bolder">Create an Account</a></span>
              </div>
              <!--begin::Title-->
              <!--begin::Form group-->
              <div class="form-group">
                <label class="font-size-h6 font-weight-bolder text-dark">Username</label>
                <input v-model="signinForm.username" class="form-control form-control-solid h-auto py-6 px-6 rounded-lg" type="text" name="username"
                       autocomplete="off" required />
              </div>
              <!--end::Form group-->
              <!--begin::Form group-->
              <div class="form-group">
                <div class="d-flex justify-content-between mt-n5">
                  <label class="font-size-h6 font-weight-bolder text-dark pt-5">Password</label>
                  <a href="javascript:" class="text-primary font-size-h6 font-weight-bolder text-hover-primary pt-5"
                     id="kt_login_forgot" @click="pageState='forgot'" tabindex="-1">Forgot Password ?</a>
                </div>
                <input v-model="signinForm.password"  class="form-control form-control-solid h-auto py-6 px-6 rounded-lg" type="password"
                       name="password" autocomplete="off" required />
              </div>
              <!--end::Form group-->
              <!--begin::Action-->
              <div class="pb-lg-0 pb-5">
                <button type="submit" id="kt_login_signin_submit"
                        class="btn btn-primary font-weight-bolder font-size-h6 px-8 py-4 my-3 mr-3" :disabled="signingIn">
                  <span :class="signingIn? 'fa fa-spin fa-spinner':'fa fa-sign-in'"></span>
                  <span v-show="!signingIn"> Sign In</span>
                  <span v-show="signingIn"> Signing In</span>
                </button>
                <button type="button" class="btn btn-light-primary font-weight-bolder px-8 py-4 my-3 font-size-lg" disabled>
									<span class="svg-icon svg-icon-md">
										<!--begin::Svg Icon | path:assets/media/svg/social-icons/google.svg-->
										<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20" fill="none">
											<path
                          d="M19.9895 10.1871C19.9895 9.36767 19.9214 8.76973 19.7742 8.14966H10.1992V11.848H15.8195C15.7062 12.7671 15.0943 14.1512 13.7346 15.0813L13.7155 15.2051L16.7429 17.4969L16.9527 17.5174C18.879 15.7789 19.9895 13.221 19.9895 10.1871Z"
                          fill="#4285F4"/>
											<path
                          d="M10.1993 19.9313C12.9527 19.9313 15.2643 19.0454 16.9527 17.5174L13.7346 15.0813C12.8734 15.6682 11.7176 16.0779 10.1993 16.0779C7.50243 16.0779 5.21352 14.3395 4.39759 11.9366L4.27799 11.9466L1.13003 14.3273L1.08887 14.4391C2.76588 17.6945 6.21061 19.9313 10.1993 19.9313Z"
                          fill="#34A853"/>
											<path
                          d="M4.39748 11.9366C4.18219 11.3166 4.05759 10.6521 4.05759 9.96565C4.05759 9.27909 4.18219 8.61473 4.38615 7.99466L4.38045 7.8626L1.19304 5.44366L1.08875 5.49214C0.397576 6.84305 0.000976562 8.36008 0.000976562 9.96565C0.000976562 11.5712 0.397576 13.0882 1.08875 14.4391L4.39748 11.9366Z"
                          fill="#FBBC05"/>
											<path
                          d="M10.1993 3.85336C12.1142 3.85336 13.406 4.66168 14.1425 5.33717L17.0207 2.59107C15.253 0.985496 12.9527 0 10.1993 0C6.2106 0 2.76588 2.23672 1.08887 5.49214L4.38626 7.99466C5.21352 5.59183 7.50242 3.85336 10.1993 3.85336Z"
                          fill="#EB4335"/>
										</svg>
                    <!--end::Svg Icon-->
									</span>Sign in with Google
                </button>
              </div>
              <!--end::Action-->
            </form>
            <!--end::Form-->
          </div>
          <!--end::Signin-->
          <!--begin::Signup-->
          <div class="login-form login-signup">
            <!--begin::Form-->
            <form class="form" novalidate="novalidate" id="kt_login_signup_form">
              <!--begin::Title-->
              <div class="pb-13 pt-lg-0 pt-5">
                <h3 class="font-weight-bolder text-dark font-size-h4 font-size-h1-lg">Sign Up</h3>
                <p class="text-muted font-weight-bold font-size-h4">Enter your details to create your account</p>
              </div>
              <!--end::Title-->
              <!--begin::Form group-->
              <div class="form-group">
                <input class="form-control form-control-solid h-auto py-6 px-6 rounded-lg font-size-h6" type="text"
                       placeholder="Fullname" name="fullname" autocomplete="off"/>
              </div>
              <!--end::Form group-->
              <!--begin::Form group-->
              <div class="form-group">
                <input class="form-control form-control-solid h-auto py-6 px-6 rounded-lg font-size-h6" type="email"
                       placeholder="Email" name="email" autocomplete="off"/>
              </div>
              <!--end::Form group-->
              <!--begin::Form group-->
              <div class="form-group">
                <input class="form-control form-control-solid h-auto py-6 px-6 rounded-lg font-size-h6" type="password"
                       placeholder="Password" name="password" autocomplete="off"/>
              </div>
              <!--end::Form group-->
              <!--begin::Form group-->
              <div class="form-group">
                <input class="form-control form-control-solid h-auto py-6 px-6 rounded-lg font-size-h6" type="password"
                       placeholder="Confirm password" name="cpassword" autocomplete="off"/>
              </div>
              <!--end::Form group-->
              <!--begin::Form group-->
              <div class="form-group">
                <label class="checkbox mb-0">
                  <input type="checkbox" name="agree"/>
                  <span></span>
                  <div class="ml-2">I Agree the
                    <a href="javascript:">terms and conditions</a>.
                  </div>
                </label>
              </div>
              <!--end::Form group-->
              <!--begin::Form group-->
              <div class="form-group d-flex flex-wrap pb-lg-0 pb-3">
                <button type="button" id="kt_login_signup_submit"
                        class="btn btn-primary font-weight-bolder font-size-h6 px-8 py-4 my-3 mr-4" disabled>Submit
                </button>
                <button type="button" id="kt_login_signup_cancel" @click="pageState='signin'"
                        class="btn btn-light-primary font-weight-bolder font-size-h6 px-8 py-4 my-3">Cancel
                </button>
              </div>
              <!--end::Form group-->
            </form>
            <!--end::Form-->
          </div>
          <!--end::Signup-->
          <!--begin::Forgot-->
          <div class="login-form login-forgot">
            <!--begin::Form-->
            <form class="form" novalidate="novalidate" id="kt_login_forgot_form">
              <!--begin::Title-->
              <div class="pb-13 pt-lg-0 pt-5">
                <h3 class="font-weight-bolder text-dark font-size-h4 font-size-h1-lg">Forgotten Password ?</h3>
                <p class="text-muted font-weight-bold font-size-h4">Enter your email to reset your password</p>
              </div>
              <!--end::Title-->
              <!--begin::Form group-->
              <div class="form-group">
                <input class="form-control form-control-solid h-auto py-6 px-6 rounded-lg font-size-h6" type="email"
                       placeholder="Email" name="email" autocomplete="off"/>
              </div>
              <!--end::Form group-->
              <!--begin::Form group-->
              <div class="form-group d-flex flex-wrap pb-lg-0">
                <button type="button" id="kt_login_forgot_submit"
                        class="btn btn-primary font-weight-bolder font-size-h6 px-8 py-4 my-3 mr-4" disabled>Submit
                </button>
                <button type="button" id="kt_login_forgot_cancel" @click="pageState='signin'"
                        class="btn btn-light-primary font-weight-bolder font-size-h6 px-8 py-4 my-3">Cancel
                </button>
              </div>
              <!--end::Form group-->
            </form>
            <!--end::Form-->
          </div>
          <!--end::Forgot-->
        </div>
        <!--end::Content body-->
        <!--begin::Content footer-->
        <div class="d-flex justify-content-lg-start justify-content-center align-items-end py-7 py-lg-0">
          <div class="text-dark-50 font-size-lg font-weight-bolder mr-10">
            <span class="mr-1">2021©</span>
            <a href="javascript:" target="_blank"
               class="text-dark-75 text-hover-primary">Human-Aftercare</a>
          </div>
          <a href="#" class="text-primary font-weight-bolder font-size-lg">Terms</a>
          <a href="#" class="text-primary ml-5 font-weight-bolder font-size-lg">Plans</a>
          <a href="#" class="text-primary ml-5 font-weight-bolder font-size-lg">Contact Us</a>
        </div>
        <!--end::Content footer-->
      </div>
      <!--end::Content-->
    </div>
    <!--end::Login-->
  </div>

</template>

<script>


import UtilMixin from "@/components/mixins/UtilMixin";

export default {
  data: function() {
    return {
      signinForm: {},
      signingIn: false,
      pageState: "signin"
    };
  },
  mixins: [UtilMixin],
  methods: {
    signIn: function() {
      var self = this;
      this.signingIn = true;
      this.$http.post("session", this.signinForm).then(
        function(response) {
          self.signinForm = {};
          self.$store.state.currentUser = response.data;
          self.signingIn = false;
          self.showSuccess("Welcome to Human-Aftercare!", 5000);
        },
        function(response) {
          self.signingIn = false;
          self.showDefaultServerError(response, true);
        }
      );
    }
  },
  computed: {
    inSigninState: function() {
      return this.pageState === "signin";
    },
    inSignupState: function() {
      return this.pageState === "signup";
    },
    inForgetPasswordState: function() {
      return this.pageState === "forgot_password";
    }
  },
  mounted: function() {
    this.closeAllNotify();
  }
};
</script>
