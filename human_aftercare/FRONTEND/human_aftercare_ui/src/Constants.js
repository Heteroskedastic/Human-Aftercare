export const UI_VERSION_HEADER_NAME = "x-ui-version";

export const GENDER_OPTIONS = [
  { value: "m", title: "Male" },
  { value: "f", title: "Female" },
  { value: "o", title: "Other" },
];
export const GENDER_MAP = {};
GENDER_OPTIONS.forEach(function(v) {
  GENDER_MAP[v.value] = v;
});

export const EYE_COLOR_OPTIONS = [
  { value: "BLK", title: "Black" },
  { value: "BLU", title: "Blue" },
  { value: "BRO", title: "Brown" },
  { value: "GRY", title: "Gray" },
  { value: "GRN", title: "Green" },
  { value: "HAZ", title: "Hazel" },
  { value: "MAR", title: "Maroon" },
  { value: "MUL", title: "Multi-Colored" },
  { value: "PNK", title: "Pink" },
  { value: "XXX", title: "Unknown" }
];
export const EYE_COLOR_MAP = {};
EYE_COLOR_OPTIONS.forEach(function(v) {
  EYE_COLOR_MAP[v.value] = v;
});

export const HAIR_COLOR_OPTIONS = [
  { value: "BLK", title: "Black" },
  { value: "BAL", title: "Bald" },
  { value: "BLN", title: "Blonde or strawberry" },
  { value: "BRO", title: "Brown" },
  { value: "GRY", title: "Gray or partially gray" },
  { value: "GRN", title: "Green" },
  { value: "ONG", title: "Orange" },
  { value: "PLE", title: "Purple" },
  { value: "PNK", title: "Pink" },
  { value: "RED", title: "Red or auburn" },
  { value: "SDY", title: "Sandy" },
  { value: "WHI", title: "White" },
  { value: "XXX", title: "Unknown" }
];
export const HAIR_COLOR_MAP = {};
HAIR_COLOR_OPTIONS.forEach(function(v) {
  HAIR_COLOR_MAP[v.value] = v;
});
