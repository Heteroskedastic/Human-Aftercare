<style scoped>
.app-version-tag {
  right: 0;
  left: unset;
  border-radius: 0;
  background-color: #b37b11;
  z-index: 9999999999;
}
</style>

<template>
  <div class="d-flex flex-column flex-column-fluid">
    <router-view></router-view>
    <version-alert v-if="mismatchVersion" :new-version="newAppVersion"></version-alert>
  </div>

</template>

<script>
import VersionAlert from "@/components/VersionAlert";
import UtilMixin from "@/components/mixins/UtilMixin"

document.onreadystatechange = function () {
  if (document.readyState === "complete") {
    var initialLoader = document.getElementById("initialLoader");
    if (initialLoader) {
      initialLoader.style.display = "none";
    }
  }
};

export default {
  name: "App",
  components: {VersionAlert},
  mixins: [UtilMixin],
  computed: {
  },
  data() {
    return {
      mismatchVersion: false,
      newAppVersion: null
    };
  },
  methods: {
    onSessionRefresh: function () {
      this.$http.get("session").then(
        (response) => {
          this.$store.state.currentUser = response.data;
        },
        (error) => {
          this.showDefaultServerError(error);
        }
      );
    },
    onSessionExpired: function() {
      this.$store.state.currentUser = {facility: {}};
      // this.$router.replace({ name: this.$rns.LOGIN }).catch(err => {});
    },
    onMismatchVersion: function(newVersion) {
      this.mismatchVersion = true;
      this.newAppVersion = newVersion;
    }
  },
  mounted: function() {
    this.$eventsBus.$on("user:session-expired", this.onSessionExpired);
    this.$eventsBus.$on("user:session-refresh", this.onSessionRefresh);
    this.$eventsBus.$on("ui:mismatch-version", this.onMismatchVersion);
  },
  destroyed: function() {
    this.$eventsBus.$off("user:session-expired", this.onSessionExpired);
    this.$eventsBus.$off("user:session-refresh", this.onSessionRefresh);
    this.$eventsBus.$off("ui:mismatch-version", this.onMismatchVersion);
  }
};
</script>
