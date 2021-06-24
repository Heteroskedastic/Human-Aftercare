import { subject as abilitySubject } from "@casl/ability";

export default function(Vue, ability) {
  const bus = new Vue();
  const update = ability.update;
  const can = ability.can;
  const cannot = ability.cannot;

  ability.update = function updateAndNotify(...args) {
    const result = update.apply(this, args);
    bus.$emit("ability:update");
    return result;
  };

  Vue.mixin({
    methods: {
      $can: function(action, subject, object) {
        if (this.$store.getters.isSuperUser) {
          // true to all actions for superuser
          return true;
        }
        if (typeof object === "object") {
          subject = abilitySubject(subject, object);
        }
        return can.apply(ability, [action, subject]);
      },
      $cannot: function(action, subject, object) {
        if (this.$store.getters.isSuperUser) {
          // false to all actions for superuser
          return false;
        }
        if (typeof object === "object") {
          subject = abilitySubject(subject, object);
        }
        return cannot.apply(ability, [action, subject]);
      }
    },
    beforeCreate() {
      this.$forceUpdate = this.$forceUpdate.bind(this);
      bus.$on("ability:update", this.$forceUpdate);
    },
    beforeDestroy() {
      bus.$off("ability:update", this.$forceUpdate);
    }
  });
}
