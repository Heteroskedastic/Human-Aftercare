import $ from "jquery";
import {blockUI} from "blockui";

export default {
  data: function() {
    return {
      multiLoadingOverlayVars: {},
      multiLoadingOverlayEls: {},
      blockUIOptions: {
      }
    };
  },
  watch: {
    multiLoadingOverlayVars: {
      deep: true,
      handler: function handler(newValue, oldValue) {
        for (var p in newValue) {
          if (!Object.prototype.hasOwnProperty.call(newValue, p)) {
            continue;
          }
          this.makeLoadingOverlay(newValue[p], this.multiLoadingOverlayEls[p]);
        }
      }
    },
  },
  methods: {
    makeLoadingOverlay: function(value, el) {
      if (!el) {
        return;
      }
      var $el = $(el, $(this.$el));
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
          ignoreIfBlocked: true,
          message: "<span class='fas fa-3x fa-spin fa-spinner'></span>"
        }, this.blockUIOptions || {}));
      } else {
        $el.unblock();
      }
    }
  }
};
