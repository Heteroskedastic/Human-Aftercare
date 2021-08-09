import { Config } from "@/Config";
import $ from "jquery";
import moment from "moment"
import { parsePhoneNumberFromString } from "libphonenumber-js";

const countryCodes = {
  "247": "AC",
  "376": "AD",
  "971": "AE",
  "93": "AF",
  "1268": "AG",
  "1264": "AI",
  "355": "AL",
  "374": "AM",
  "244": "AO",
  "54": "AR",
  "1684": "AS",
  "43": "AT",
  "61": "AU",
  "297": "AW",
  "994": "AZ",
  "387": "BA",
  "1246": "BB",
  "880": "BD",
  "32": "BE",
  "226": "BF",
  "359": "BG",
  "973": "BH",
  "257": "BI",
  "229": "BJ",
  "1441": "BM",
  "673": "BN",
  "591": "BO",
  "55": "BR",
  "1242": "BS",
  "975": "BT",
  "267": "BW",
  "375": "BY",
  "501": "BZ",
  "243": "CD",
  "236": "CF",
  "242": "CG",
  "41": "CH",
  "225": "CI",
  "682": "CK",
  "56": "CL",
  "237": "CM",
  "86": "CN",
  "57": "CO",
  "506": "CR",
  "53": "CU",
  "238": "CV",
  "599": "CW",
  "537": "CY",
  "357": "CY",
  "420": "CZ",
  "49": "DE",
  "253": "DJ",
  "45": "DK",
  "1767": "DM",
  "1849": "DO",
  "213": "DZ",
  "593": "EC",
  "372": "EE",
  "20": "EG",
  "291": "ER",
  "34": "ES",
  "251": "ET",
  "358": "FI",
  "679": "FJ",
  "500": "FK",
  "691": "FM",
  "298": "FO",
  "33": "FR",
  "241": "GA",
  "44": "GB",
  "1473": "GD",
  "995": "GE",
  "594": "GF",
  "233": "GH",
  "350": "GI",
  "299": "GL",
  "220": "GM",
  "224": "GN",
  "240": "GQ",
  "30": "GR",
  "502": "GT",
  "1671": "GU",
  "245": "GW",
  "592": "GY",
  "852": "HK",
  "504": "HN",
  "385": "HR",
  "509": "HT",
  "36": "HU",
  "62": "ID",
  "353": "IE",
  "972": "IL",
  "91": "IN",
  "246": "IO",
  "964": "IQ",
  "98": "IR",
  "354": "IS",
  "39": "IT",
  "1876": "JM",
  "962": "JO",
  "81": "JP",
  "254": "KE",
  "996": "KG",
  "855": "KH",
  "686": "KI",
  "269": "KM",
  "1869": "KN",
  "850": "KP",
  "82": "KR",
  "965": "KW",
  "345": "KY",
  "77": "KZ",
  "856": "LA",
  "961": "LB",
  "1758": "LC",
  "423": "LI",
  "94": "LK",
  "231": "LR",
  "266": "LS",
  "370": "LT",
  "352": "LU",
  "371": "LV",
  "218": "LY",
  "212": "MA",
  "377": "MC",
  "373": "MD",
  "382": "ME",
  "590": "MF",
  "261": "MG",
  "692": "MH",
  "389": "MK",
  "223": "ML",
  "95": "MM",
  "976": "MN",
  "853": "MO",
  "1670": "MP",
  "596": "MQ",
  "222": "MR",
  "1664": "MS",
  "356": "MT",
  "230": "MU",
  "960": "MV",
  "265": "MW",
  "52": "MX",
  "60": "MY",
  "258": "MZ",
  "264": "NA",
  "687": "NC",
  "227": "NE",
  "672": "NF",
  "234": "NG",
  "505": "NI",
  "31": "NL",
  "47": "NO",
  "977": "NP",
  "674": "NR",
  "683": "NU",
  "64": "NZ",
  "968": "OM",
  "507": "PA",
  "51": "PE",
  "689": "PF",
  "675": "PG",
  "63": "PH",
  "92": "PK",
  "48": "PL",
  "508": "PM",
  "872": "PN",
  "1939": "PR",
  "970": "PS",
  "351": "PT",
  "680": "PW",
  "595": "PY",
  "974": "QA",
  "262": "RE",
  "40": "RO",
  "381": "RS",
  "7": "RU",
  "250": "RW",
  "966": "SA",
  "677": "SB",
  "248": "SC",
  "249": "SD",
  "46": "SE",
  "65": "SG",
  "290": "SH",
  "386": "SI",
  "421": "SK",
  "232": "SL",
  "378": "SM",
  "221": "SN",
  "252": "SO",
  "597": "SR",
  "211": "SS",
  "239": "ST",
  "503": "SV",
  "963": "SY",
  "268": "SZ",
  "1649": "TC",
  "235": "TD",
  "228": "TG",
  "66": "TH",
  "992": "TJ",
  "690": "TK",
  "670": "TL",
  "993": "TM",
  "216": "TN",
  "676": "TO",
  "90": "TR",
  "1868": "TT",
  "688": "TV",
  "886": "TW",
  "255": "TZ",
  "380": "UA",
  "256": "UG",
  "1": "US",
  "598": "UY",
  "998": "UZ",
  "379": "VA",
  "1784": "VC",
  "58": "VE",
  "1284": "VG",
  "1340": "VI",
  "84": "VN",
  "678": "VU",
  "681": "WF",
  "685": "WS",
  "967": "YE",
  "27": "ZA",
  "260": "ZM",
  "263": "ZW"
};

moment.updateLocale("en", {
  relativeTime: {
    s: "Just now",
    ss: "Just now",
    m: "1 min",
    mm: "%d mins",
    h: "1 hr",
    hh: "%d hrs"
  }
});

export default {
  mixins: [Config],
  data: function () {
    return {
      libs: {
        moment, $
      }
    }
  },
  methods: {
    getTimeLabel: function(hour, minute, baseHour) {
      var mer = "AM";
      hour = (hour + (baseHour === undefined ? 21 : baseHour)) % 24;
      if (hour === 0) {
        hour = 12;
      }
      if (hour > 12) {
        mer = "PM";
        hour = hour % 12;
      }
      hour = `${hour}`.padStart(2, "0");
      if (minute === undefined) {
        return `${hour} ${mer}`;
      }
      minute = `${minute}`.padStart(2, "0");
      return `${hour}:${minute} ${mer}`;
    },
    todayDate: function(options) {
      options = options || {};
      if (options.asDate) {
        return moment().toDate();
      }
      return moment().format(options.format || "YYYY-MM-DD");
    },
    formatDate: function(value, fmt, _default) {
      _default = _default === undefined ? "" : _default;
      if (!value) {
        return _default;
      }
      fmt = fmt === undefined ? "MMM D, YYYY HH:mm" : fmt;
      return moment(value).format(fmt);
    },
    formatTime: function(value, fmt, _default) {
      _default = _default === undefined ? "" : _default;
      if (!value) {
        return _default;
      }
      fmt = fmt === undefined ? "hh:mm A" : fmt;
      return moment.utc(`2000-01-01T${value}Z`).format(fmt);
    },
    formatDefault: function(value, _default) {
      return value === null || value === undefined || value === ""
        ? _default
        : value;
    },
    formatBoolean: function(value) {
      return `<span class="fa fa-${
        value ? "check text-success" : "times text-danger"
      }"></span>`;
    },
    formatFileUrl: function(fileUrl) {
      return fileUrl
        .split("?")[0]
        .split("/")
        .pop();
    },
    formatDuration: function(d, includeSeconds, _default) {
      d = d || 0;
      if (!d && _default !== undefined) {
        return _default;
      }
      var hours = Math.floor(d / 3600),
        minutes = Math.floor((d % 3600) / 60);
      var s = `${hours}<sub>h</sub> : ${minutes}<sub>m</sub>`;
      if (includeSeconds) {
        var seconds = Math.floor((d % 3600) % 60);
        s = `${s}: ${seconds}<sub>s</sub>`;
      }
      return s;
    },
    formatDuration2: function(d, includeSeconds, _default) {
      d = d || 0;
      if (!d && _default !== undefined) {
        return _default;
      }
      var hours = Math.floor(d / 3600),
        minutes = Math.floor((d % 3600) / 60);
      var s = `${hours}:${minutes}`;
      if (includeSeconds) {
        var seconds = Math.floor((d % 3600) % 60);
        s = `${s}: ${seconds}`;
      }
      return s;
    },
    formatFileType: function(fileUrl, showText, showIcon) {
      if (!fileUrl) {
        return "";
      }
      showText = showText === undefined ? true : showText;
      showIcon = showIcon === undefined ? true : showIcon;
      var ext = fileUrl
          .split(".")
          .slice(-1)[0]
          .toLowerCase(),
        extTypes = {
          jpg: "image",
          jpeg: "image",
          png: "image",
          gif: "image",
          pdf: "pdf",
          doc: "word",
          docx: "word",
          xls: "excel",
          xlsx: "excel",
          csv: "excel",
          zip: "zip",
          tar: "zip",
          "7z": "zip",
          bz2: "zip",
          gz: "zip",
          tgz: "zip"
        },
        icons = {
          image: "fa-file-image-o",
          pdf: "fa-file-pdf-o",
          word: "fa-file-word-o",
          excel: "fa-file-excel-o",
          zip: "fa-file-zip-o",
          unknown: "fa-file-o"
        },
        extType = extTypes[ext] || "unknown",
        icon = icons[extType];
      var s = "";
      if (showIcon) {
        s += `<span class="fa ${icon}"></span> `;
      }
      if (showText) {
        s += extType;
      }
      return s;
    },
    ifEmptyFormat: function(value, _default) {
      return value || (_default || "-");
    },
    formatFileSize: function(value, _default) {
      _default = _default === undefined ? "" : _default;
      const UNITS = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"];
      if (value === null || value === undefined) {
        return _default;
      }
      if (!Number.isFinite(value)) {
        throw new TypeError("Expected a finite number");
      }
      const neg = value < 0;
      if (neg) {
        value = -value;
      }
      if (value < 1) {
        return (neg ? "-" : "") + value + " B";
      }
      const exponent = Math.min(
        Math.floor(Math.log10(value) / 3),
        UNITS.length - 1
      );
      const valueStr = Number(
        (value / Math.pow(1000, exponent)).toPrecision(3)
      );
      const unit = UNITS[exponent];
      return (neg ? "-" : "") + valueStr + " " + unit;
    },
    formatPhone: function(phone, options) {
      options = options || {};
      if (!phone) {
        return options._default || '-';
      }
      var phoneNumber = parsePhoneNumberFromString(phone);
      if (options.format === "international") {
        phone = phoneNumber.formatInternational();
      } else if (options.format === "national") {
        phone = phoneNumber.formatNational();
      } else if (options.format === "uri") {
        phone = phoneNumber.getURI();
      } else {
        return phone.startsWith(Config.DEFAULT_PHONE_COUNTRY_CODE) ?
          phoneNumber.formatNational() : phoneNumber.formatInternational();
      }
      return phone;
    },
    capitalize: function(value) {
      if (!value) return "";
      value = value.toString();
      return value.charAt(0).toUpperCase() + value.slice(1);
    },
    ageFormat: function(birth_date, showLabel, decimalCount) {
      showLabel = showLabel === undefined ? true : showLabel;
      var age = moment().diff(birth_date, "years", !!decimalCount);
      age = decimalCount? this.removeTrailingZero(age, decimalCount): Math.floor(age);
      return `${age}${
        showLabel ? " years" : ""
      }`;
    },
    internationalPhoneMask: function(rawValue) {
      var number = (rawValue || "").replace(/\D/g, ""),
        codesDigit = ["+", /\d/];
      if (!rawValue.startsWith("+")) {
        codesDigit = (Config.DEFAULT_PHONE_COUNTRY_CODE || "+1").split("");
      } else if (number) {
        var countryCode,
          i = 1;
        while (i <= number.length && i <= 5) {
          countryCode = countryCodes[number.slice(0, i)];
          if (countryCode) {
            break;
          }
          codesDigit.push(/\d/);
          i++;
        }
        if (!countryCode) {
          codesDigit = ["+", /\d/];
        }
      }
      return codesDigit.concat([
        " ",
        "(",
        /[1-9]/,
        /\d/,
        /\d/,
        ")",
        " ",
        /\d/,
        /\d/,
        /\d/,
        "-",
        /\d/,
        /\d/,
        /\d/,
        /\d/
      ]);
    },
    internationalPhoneFormat: function(number, options) {
      options = options || {};
      if (!number.startsWith("+")) {
        number = Config.DEFAULT_PHONE_COUNTRY_CODE + number;
      }
      if (!options.isRaw) {
        number = "+" + number.replace(/\D/g, "");
      }
      return number + (options.ext ? `,${options.ext}` : "");
    },
    linkPhoneFormat: function(number, options) {
      if (!number) {
        return "";
      }
      options = options || {};
      return "tel:" + number + (options.ext ? `,${options.ext}` : "");
    },
    removeTrailingZero: function(n, decimalPoint) {
      if (n === null || n === undefined) {
        return n;
      }
      if (typeof n === "number" && decimalPoint !== undefined) {
        n = n.toFixed(decimalPoint);
      }
      if (typeof n !== "string") {
        n = n + "";
      }
      return n.replace(/(\.[0-9]*[1-9])0+$|\.0*$/, "$1");
    },
    findIndexBy: function(array, property, value) {
      for (var i = 0; i < array.length; i++) {
        if (array[i][property] === value) {
          return i;
        }
      }
      return -1;
    },
    findValueBy: function(array, property, value) {
      for (var i = 0; i < array.length; i++) {
        if (array[i][property] === value) {
          return array[i];
        }
      }
    },
    getCookie: function(cName) {
      if (document.cookie.length > 0) {
        var cStart = document.cookie.indexOf(cName + "=");
        if (cStart !== -1) {
          cStart = cStart + cName.length + 1;
          var cEnd = document.cookie.indexOf(";", cStart);
          if (cEnd === -1) {
            cEnd = document.cookie.length;
          }
          return encodeURI(document.cookie.substring(cStart, cEnd));
        }
      }
      return "";
    },
    getWeekRange: function(weeksAgo, date, weekday) {
      date = date ? moment(date) : moment();
      weeksAgo = weeksAgo || 0;
      var startOfWeek = date
          .clone()
          .subtract({ days: weeksAgo * 7 + (date.days() % 7) + (weekday? weekday : 0) }),
        endOfWeek = startOfWeek.clone().add({ days: 6 });
      return [startOfWeek, endOfWeek];
    },
    closeAllNotify: function() {
      this.$toasted.toasts.forEach(t => t.goAway(0));
    },
    showMessage: function(msg, opts) {
      opts = Object.assign(
        {
          icon: "fas fa-info-circle mr-1 text-light",
          type: "info",
          duration : 5000,
          action: {
            text: "x",
            class: "text-light",
            onClick: (e, toastObject) => {
              toastObject.goAway(0);
            }
          }
        },
        opts || {}
      );
      this.$toasted.show(msg, opts);
    },
    showSuccess: function(msg, duration) {
      this.showMessage(msg, {
        icon: "fas fa-check-circle mr-1 text-light",
        type: "success",
        duration: duration !== undefined ? duration : 5000
      });
    },
    showError: function(msg, duration) {
      this.showMessage(msg, {
        icon: "fas fa-exclamation-circle mr-1 text-light",
        type: "error",
        duration: duration !== undefined ? duration : 5000
      });
    },
    showWarn: function(msg, duration) {
      this.showMessage(msg, {
        icon: "fas fa-exclamation-triangle mr-1 text-light",
        type: "warning",
        duration: duration !== undefined ? duration : 5000
      });
    },
    showInfo: function(msg, duration) {
      this.showMessage(msg, {
        className: "bg-info",
        duration: duration !== undefined ? duration : 5000
      });
    },
    showDefaultServerSuccess: function(response, duration) {
      duration = duration !== undefined ? duration : 5000;
      var defaultMsg = "Operation done successfully";
      this.showSuccess(response.statusText || defaultMsg, duration);
    },
    showDefaultServerError: function(error, showDetail, duration, extra_message) {
      var response = error.response || error.request;
      if (response.status === 401) {
        return;
      }
      var msg;
      duration = duration !== undefined ? duration : 50000;
      showDetail = showDetail !== undefined ? showDetail : true;
      if (!response || response.status <= 0) {
        msg = "<strong>Server Connection Error</strong>";
      } else {
        msg =
          "<strong>" +
          response.status +
          ": " +
          response.statusText +
          " | </strong>";
        var jData = this.safeFromJson(response.data);
        if (showDetail && jData) {
          msg += "<p>" + this.prettifyError(response.data) + "</p>";
        }
        if (extra_message) {
          msg += "<p>" + extra_message + "</p>";
        }
      }
      this.showError(msg, duration);
    },
    prettifyError: function(data) {
      return JSON.stringify(data)
        .replace(/\[|\]|\}|\{/g, "")
        .replace(/\\"/g, '"')
        .replace('"non_field_errors":', "");
    },
    safeFromJson: function(s, nullIfFail) {
      if (typeof s === "object") {
        return s;
      }
      nullIfFail = nullIfFail === undefined;
      try {
        return JSON.parse(s);
      } catch (e) {
        return nullIfFail ? null : s;
      }
    },
    randomId: function(n) {
      n = n || 10;
      return Math.floor(Math.random() * Math.pow(10, n) + 1);
    },
    addQSParm: function(url, name, value, override) {
      override = override === undefined ? true : override;
      var self = this;
      if (value instanceof Array) {
        $.each(value, function(k, v) {
          url = self.addQSParm(url, name, v, false);
        });
        return url;
      }
      var re = new RegExp("([?&]" + name + "=)[^&]+", "");

      function add(sep) {
        url += sep + name + "=" + encodeURIComponent(value);
      }

      function change() {
        url = url.replace(re, "$1" + encodeURIComponent(value));
      }

      if (url.indexOf("?") === -1) {
        add("?");
      } else {
        if (override && re.test(url)) {
          change();
        } else {
          add("&");
        }
      }
      return url;
    },
    noCacheUrl: function(url) {
      var r = this.randomId();
      return this.addQSParm(url, "nc", r);
    },
    combineURLs: function(baseURL, relativeURL) {
      return (
        baseURL.replace(/\/+$/, "") + "/" + relativeURL.replace(/^\/+/, "")
      );
    },
    download: function downloadURL(url, params) {
      var self = this;
      $.each(params, function(k, v) {
        url = self.addQSParm(url, k, v);
      });
      var hiddenIFrameID = "hiddenDownloader",
        iframe = document.getElementById(hiddenIFrameID);
      if (iframe === null) {
        iframe = document.createElement("iframe");
        iframe.id = hiddenIFrameID;
        iframe.style.display = "none";
        document.body.appendChild(iframe);
      }
      iframe.src = url;
    },
    download2: function downloadURL(url, params) {
      var self = this;
      $.each(params, function(k, v) {
        url = self.addQSParm(url, k, v);
      });
      var hiddenLinkID = "hiddenLink",
        link = document.getElementById(hiddenLinkID);
      if (link === null) {
        link = document.createElement("a");
        link.target = "_blank";
        link.id = hiddenLinkID;
        link.style.display = "none";
        document.body.appendChild(link);
      }
      link.href = url;
      link.click();
    },
    convertModelToFormData: function(model, form, namespace, filter) {
      var formData = form || new FormData();
      var formKey;
      filter = filter === undefined ? k => k.startsWith("_") : filter;

      for (var propertyName in model) {
        if (
          !Object.prototype.hasOwnProperty.call(model, propertyName) ||
          model[propertyName] === undefined ||
          (filter && filter(propertyName))
        ) {
          continue;
        }
        formKey = namespace || propertyName;
        if (model[propertyName] === null) {
          formData.append(formKey, "");
        } else if (model[propertyName] instanceof Date) {
          formData.append(formKey, model[propertyName].toISOString());
        } else if (model[propertyName] instanceof File) {
          formData.append(formKey, model[propertyName]);
        } else if (typeof model[propertyName] === "object") {
          this.convertModelToFormData(
            model[propertyName],
            formData,
            formKey,
            filter
          );
        } else {
          formData.append(formKey, model[propertyName].toString());
        }
      }
      return formData;
    },
    stripTags: function(value) {
      return $(`<span>${value}</span>`).text();
    },
    displayUser: function(user, _default) {
      if (!user) {
        return _default || "-"
      }
      if (!user.first_name && !user.last_name) {
        return "[NO NAME]";
      }
      return `${user.first_name || ""} ${user.last_name || ""}`.trim();
    },
    displayHotelLocation: function(hotel, _default) {
      if (!hotel) {
        return _default || "-"
      }
      var arr = [];
      if (hotel.city) {
        arr.push(hotel.city);
      }
      if (hotel.state) {
        arr.push(hotel.state);
      }
      if (hotel.country) {
        arr.push(hotel.country);
      }
      return arr.join(', ')  || _default || "-";
    }
  }
};
