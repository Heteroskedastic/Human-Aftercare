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
        $el.block(Object.assign({
          centerY: true,
          centerX: true,
          css: {
            top: "0",
            left: "50%",
            border: "1",
            padding: "20px",
            cursor: "wait",
            width: "auto"
          },
          overlayCSS: {
            opacity: 0.2,
            cursor: "wait"
          },
          overlayColor: "#000000",
          message: "<span class='fas fa-3x fa-spin fa-spinner'></span>"
        }, this.blockUIOptions || {}));
      } else {
        $el.unblock();
      }
    }
  }
};
