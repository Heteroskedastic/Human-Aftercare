import { AbilityBuilder, Ability } from '@casl/ability'

export const permAbility = new Ability([]);

export function definePermAbilitiesFor(user) {
  user = user || {};
  var builder = new AbilityBuilder(Ability),
    perms = (user.groups || []).map(g => g.permissions);
  perms.push(user.user_permissions);
  perms.forEach(function(permsSet) {
    (permsSet || []).forEach(function(perm) {
      var splittedPerm = perm.codename.split("_"),
        action = splittedPerm[0],
        resource = splittedPerm.slice(1).join("_");
      builder.can([action], resource);
    });
  });
  permAbility.update(builder.rules || []);
  return permAbility;
}
