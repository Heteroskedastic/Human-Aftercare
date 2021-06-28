import $ from "jquery";
import {blockUI} from "blockui";

export default {
  data: function() {
    return {
      loadingOverlay: false,
      loadingOverlayEl: null,
      blockUIOptions: {
      }
    };
  },
  watch: {
    loadingOverlay: function(value) {
      var $el = $(this.$el);
      if (this.loadingOverlayEl) {
        $el = $(this.loadingOverlayEl, $el);
      }
      if (value) {
        window.KTApp.block($el, Object.assign({
          overlayColor: "#000000",
          opacity: 0.2,
          state: 'primary'
        }, this.blockUIOptions || {}));
      } else {
        window.KTApp.unblock($el);
      }
    }
  }
};
