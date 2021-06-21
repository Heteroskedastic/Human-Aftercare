const PUBLIC_PATH = "/static/vue/";
const BACKEND_URL = process.env.VUE_APP_API_BASE_URL || "http://localhost:8000";

module.exports = {
  publicPath: PUBLIC_PATH,
  productionSourceMap: false,
  runtimeCompiler: true,
  chainWebpack: config => {
    config.externals({
      jquery: "jQuery",
      moment: "moment",
    });
  },
  devServer: {
    setup: function(app) {
      app.get("/", function(req, res) {
        res.redirect(PUBLIC_PATH);
      });
    },
    watchOptions: {
      poll: true
    },
    proxy: {
      "/api": {
        target: BACKEND_URL,
        changeOrigin: true
      },
      "/login": {
        target: BACKEND_URL,
        changeOrigin: true
      },
      "/signup": {
        target: BACKEND_URL,
        changeOrigin: true
      },
      "/password/": {
        target: BACKEND_URL,
        changeOrigin: true
      },
      "/static/dj": {
        target: BACKEND_URL,
        changeOrigin: true
      },
      "/media/": {
        target: BACKEND_URL,
        changeOrigin: true
      }
    }
  }
};
