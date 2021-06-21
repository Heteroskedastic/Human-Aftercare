module.exports = {
  root: true,
  env: {
    node: true
  },
  extends: ["plugin:vue/essential", "eslint:recommended"],
  rules: {
    "no-mixed-spaces-and-tabs": 0,
    "no-console": process.env.NODE_ENV === "production" ? "error" : "off",
    "no-debugger": process.env.NODE_ENV === "production" ? "error" : "off",
    "no-unused-vars": "off",
    "vue/no-unused-vars": "off",
    "vue/require-v-for-key": "off",
    "max-len": [0, 120, 2]
  },
  parserOptions: {
    parser: "babel-eslint"
  }
};
