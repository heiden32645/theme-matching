# Majestic 1.3.0 / Iconic

Matched on 2026-10-14. Product: https://5er1i1lbqz3rdn8k-69620498584.shopifypreview.com/products/vans-era-59-moroccan-geo-dress-blues . Variant 8 / blue. Shopify's page script identifies schema_name Majestic, schema_version 1.3.0, theme_store_id 4874, installed name Iconic. The asset /t/35/ is an installed asset directory, not the theme store id.

Deliverable: ../1.3.0.css. Saved in Globo Product Options > Settings > Design > Custom CSS. Match Shopify theme style was checked and remains checked. The initial editor was empty, while the served dynamic style contained a Poetic 1.6.0 / 3867 override whose theme variables did not resolve. Its source is saved separately in before-served-gpo.css. No theme publication was performed.

| Component | Native source | Mapping and coverage |
| --- | --- | --- |
| Labels | .variant-picker__label | Jost, --text-small (14.4px), body weight 400, 1.4 line-height, 8px bottom gap. Native/GPO measured equal typography. Selected value weight 500. |
| Button swatches | .variant-picker__pills label | Native and GPO 40px outer height, 20px horizontal padding, 4px theme radius, --border-color (border rgb at .4 opacity), body foreground selected background. Verified desktop and mobile selection. |
| Color/image swatches | asset .variant-picker__swatch-label | Source mapping: 3px padding, transparent 1px border and .22rem radius, body foreground selected border. Keep configured GPO sizes. Two-color triangle stays intact. Native color swatches absent on this product. |
| Option stepper | .quantity-selector__wrap | Painted native product wrapper 50px outer box: 48px buttons plus 1px borders. Initial GPO stepper matched the 50px native outer box; user correction makes the GPO stepper 34px with a 32px interior while retaining theme colors. Plus 1→2 tested on mobile. |
| Single quantity | .quantity-selector__wrap and .quantity-selector__input | Native source is 50px; user correction makes the single GPO input 34px with body value font weight 500. Native sticky duplicate 48px excluded. |
| Select/custom/image/font dropdown | asset .variant-picker__dropdown .field__input | Variant native dropdown absent. Source fallback: 2.875rem (46px) height, .625rem/.875rem padding, theme input colors and form radius. Native browser select has no theme custom list. Select has no chevron, per user-confirmed native appearance. Custom dropdowns also have no chevron after user correction; the list remains a theme-token adaptation with immediate display. |
| Text, textarea, phone, dimension, color | asset .field__input | Wrapper owns one border, input fills 44px interior, total 46px. Textarea remains multiline. Phone/country and color popups have overflow visible. Pointer and Tab focus tested, focus ring resolves to 3px rgba(22,21,19,.35). |
| Checkbox | asset .check__box | 18px square, theme border at .82 opacity, smaller accent square for selected state. Radio uses a circular version of these colors. Checked radio/checkbox tested. Native counterparts not rendered. |
| Upload action | product .btn--secondary | 48px, theme button font/style, 12px/24px padding, 3.6px radius, secondary colors and hover transition. Upload/remove not exercised: no disposable upload fixture supplied. |
| Switch/range | theme-token adaptation | Foreground, input background and border colors; toggled switch and range keyboard increment verified. |
| Horizontal tabs | theme-token adaptation | Product label typography with divider and active foreground underline. Tab switch exercised. |
| Vertical tabs/group | asset .collapsible-row--product | Theme row padding, heading typography and divider source mapping. Absent on this product, not visually exercised. |

Verification:

- Actual viewports: desktop 1838×907 and 1440×1000; mobile 390×844. Override on the user-owned tab did not change its width; a temporary browser-created tab provided the confirmed responsive dimensions. Override reset after testing.
- Final served style#gpo-dynamic-css contains exactly one match header and its custom portion equals the trimmed deliverable. Editor replacement required Select All + Backspace before fill; repeated fill alone appended copies. Duplicate drafts were removed before delivery. Custom CSS persisted after admin reload. Editable/served sources remain separate.
- Plain CSS parsed with tinycss2; 124 flat rules, no declaration errors, undefined custom tokens or unused custom tokens.
- Dropdown trigger opening/closing, outside-click closing, selected regular/image/font values retained. Closed list display:none; open list display:block; transition:none; static caret. Mobile dropdown stayed within viewport horizontally and vertically in exercised state. Native variant dropdown animation cannot be visually compared because it is absent; menu behavior is a documented adaptation.
- Font-picker inline previews preserved: Roboto, Open Sans, Montserrat, Poppins and Oswald.
- Text/prefix/suffix, two-line textarea, dimension input, phone country list, color-popup opening, radio, checkbox, button, color selection, option quantity, switch, range and horizontal tab behavior exercised. Phone list was not clipped. Mobile GPO fields and product-link pills stayed inside the viewport, no GPO horizontal overflow detected.
- File upload/remove, native hover visuals, disabled/error controls, vertical tabs and groups not exercised. Hover colors inspected from theme source; browser API exposes no hover action.
- Temporary test selections are reset by reloading storefront before delivery.

Learning review: the stale served override and wrapper measurements are already covered by the skill's discovery/cascade checks; no new generalized skill rule is needed. Keep browser-specific slider pseudo-elements in separate rules so unsupported pseudo-elements cannot invalidate the matching browser's thumb styling.

## User correction: Select and compact quantities

Removed .gpo-select::after and the unnecessary right arrow inset; user confirmed the theme Select has no chevron. Reduced the two dedicated quantity tokens from 50px to 34px, with stepper buttons/value at 32px inside the 1px borders. Native product quantity is unchanged. Backup: before-select-quantity-correction.css. CSS parser passes with 125 flat rules. Live measurements, selection behavior and screenshots are in select-quantity-correction.json / .jpg.

Correction verified at actual desktop 1332×907 and mobile 390×844: all three GPO quantity boxes measure 34px; Select pseudo-element display:none and background-image:none; option_2 selection retained, quantity plus 1→2 works. Served custom CSS equals the deliverable with one header. The current preview now renders native variant selects; their inspected mobile metrics are retained in select-quantity-mobile.json.

## User correction: dropdown chevron and click border

Removed the trigger chevron and arrow inset from all .gpo-dropdown variants, including image/color/font controls. Opening applies the same --focus-ring as Select. Verified desktop regular/image/font triggers: no pseudo-element chevron, 1px rgb(218,213,201) border and 3px rgba(22,21,19,.35) ring. Closed dropdown returns to no ring, selection persists, outer height stays 46px. Confirmed mobile 390×844 with no horizontal overflow in the trigger. Served CSS equals the editable deliverable, one header, 123 parsed rules without errors. Evidence: dropdown-chevron-focus.json / .jpg and dropdown-chevron-focus-mobile.json. Backup: before-dropdown-chevron-focus.css.

## Font correction after rendering native variant Select

User noticed the GPO Select/dropdown value size differed. The live native .variant-picker__dropdown .field__input measured Jost 14.4px / 20.16px desktop; GPO measured Jost 16px / 22.4px. The earlier asset extraction flattened the source context: the theme 16px field override is inside @supports (-webkit-touch-callout:none) and @media (max-width:999px) and (hover:none) and (pointer:coarse), not a general input rule.

Select, dropdown triggers, options and search input now consume --gpo-theme-select-font-size:var(--text-small). The theme's conditional iOS touch override is reproduced with 16px. Desktop 1334×907 confirmed native/GPO 14.4px / 20.16px; mobile 390×844 confirmed native/GPO 12.96px / 18.144px. Theme family Jost and weight 400 are preserved; field outer height remains 46px. iOS device behavior was sourced, not exercised on a physical device. Exact served custom CSS equals the deliverable with one header. CSS parser: 124 qualified rules including the conditional override, no errors. Evidence: dropdown-font-before.json, dropdown-font-desktop.json, dropdown-font-mobile.json and dropdown-font-corrected.jpg. Backup: before-dropdown-font-correction.css.

Learning review: preserve enclosing @supports/@media when inspecting winning source declarations; the skill already requires scoped source and responsive formulas, so no duplicate generic rule is proposed.

## Text-input font correction

Text, textarea, phone, dimension and the decorated-input wrapper now use --gpo-theme-input-font-size:var(--text-small), with the same conditional iOS touch 16px override as native .field__input. This also aligns the visible suffix and country dial code. Before: 16px across GPO inputs, native 14.4px desktop. After: desktop 1334×963 native/GPO 14.4px / 20.16px; mobile 390×844 native/GPO 12.96px / 18.144px. Text field outer box remains 46px. Text and multiline textarea entry exercised; test values reset by reload. Exact served CSS matches the deliverable with one header. CSS syntax passes (124 qualified rules). Backup: before-input-font-correction.css. Evidence: input-font-before.json, input-font-desktop.json, input-font-mobile.json and input-font-corrected.jpg. The conditional iOS rule is source-verified, not tested on a physical iOS device. No further skill rule is proposed; this is the same source-scope correction already recorded above.
