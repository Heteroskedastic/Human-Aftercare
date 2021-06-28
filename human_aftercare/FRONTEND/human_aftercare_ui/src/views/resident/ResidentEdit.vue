<script>
import ResidentForm from "./ResidentForm";

export default {
  mixins: [ResidentForm],
  created: function() {
    this.loadRecord();
  },
  methods: {
    loadRecord: function() {
      var recordId = this.$route.params.record_id;
      this.loadingOverlay = true;
      this.$http.get(`resident/${recordId}/`).then(
        (response) => {
          this.loadingOverlay = false;
          this.record = response.data;
        },
        (error) => {
          this.loadingOverlay = false;
          this.showDefaultServerError(error);
        }
      );
    }
  }
};
</script>
