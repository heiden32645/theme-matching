# Observed theme cases

Observed on 2026-10-05, desktop 1440×1000 and mobile 390×844. These cases teach mapping and failure patterns; the served styles are not all approved visual goldens. Theme settings can change these values.

| Theme | Observation | Reusable lesson |
| --- | --- | --- |
| Sunrise 13.01.02 / 57 | Select, custom dropdown, text/phone/dimension wrappers 40px; inner fields 38px. Focus changed the text wrapper border. | Measure outer and inner boxes separately; keep the two border pixels in the correct owner. |
| Grid 7.2.0 / 718 | Painted native `.select-wrapper` and GPO dropdown/wrappers 36.75px. Native `<select>` has opacity 0. GPO dropdown value font 13px, painted native wrapper 14px. | Inspect the painted wrapper/value instead of copying the invisible native select's own typography. Preserve the theme's `calc()` height formula. |
| Emerge 10.3.0 / 833 | Native purchase button 45px; GPO input/select/dropdown outer box 47px, inner field 45px. Single GPO quantity 45px. The supplied socks page has no native variant select. | A shared button-height plus wrapper borders can create a 2px difference. A button-derived field mapping is a fallback until a native field is inspected. |
| Bijou 1.2.5 / 3422 | GPO select outer box 57px, custom dropdown 56px, text/phone/dimension wrappers 40px, default visible single quantity input 22px. Text wrapper border stayed unchanged on pointer focus and its outline became none/0px. The supplied socks page has no native variant select. | Use separate select/input/quantity roles. Check the visible state and cascade, rather than treating local token declarations as proof of storefront geometry. |

On all four previews the first custom dropdown opened, selecting `option_1` updated its displayed value, and the sampled button swatch retained its height after selection. This is sampled coverage, not certification of every GPO control/state.

CSS generated from the local project sources and served CSS differed for all four themes. For example, the served Bijou file lacks the scoped single-quantity input rule present in the local project source. Do not overwrite working native mappings merely to make the preview resemble a possibly unapplied local draft.

For regression fixtures, keep a stable product with representative controls, expected native/GPO role mappings, settings, viewport, and loaded override identity. Add an unseen theme and a second settings configuration before making a cross-theme automation claim. Expected values must describe the approved role/state, not blindly freeze these observations.

## Zenith 1.5.3 / 3872 — dropdown effects

Observed on 2026-10-06 at desktop 1440×1000 and mobile 390×844. The native `variant-dropdown-select .dropdown-select__options` switches from `display: none` to `display: block` immediately, with zero transition duration. Its caret stays still. Option labels retain a `background-color` transition using `var(--duration-default)` (0.3s in the inspected configuration).

The first GPO match reproduced the final list appearance but retained the base `.gpo-dropdown .dropdown-list` transition of 0.3s, causing an unwanted expanding effect. The correction sets the collapsed list to `display: none`, the expanded list to `display: block`, and the list transition to `none`, while preserving option-hover transitions. Expanded image/color selectors need sufficient specificity to keep the native `30rem` maximum height over GPO's specialized base rules. Preserve the static caret and native selected checkmark.

The corrected CSS was saved in Custom CSS for the widget and verified in the served style. Ordinary, image and font dropdown opening, closing and selection were exercised on desktop/mobile; trigger-close and outside-click close were also checked. The color dropdown was absent and its specialized selector had source coverage only. Apply these values to this observed Zenith configuration; inspect each new theme or setting rather than generalizing immediate opening to all dropdowns.
