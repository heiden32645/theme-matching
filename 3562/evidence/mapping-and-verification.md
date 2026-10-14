# Megastore 1.1.1 / Makeup

- Theme store ID: 3562; installed theme ID: 189166649496; asset directory: `/t/31/`.
- Product: https://vwh56w1krvs3p94u-69620498584.shopifypreview.com/products/vans-era-59-moroccan-geo-dress-blues
- Initial variant: 8 / blue, 47372774342808.
- Deliverable: `../1.1.1.css`, plain CSS with scoped theme variables.
- Integration: Globo Settings > Design > Custom CSS. Previous editor was empty. Match Shopify theme style was already enabled and remains enabled.
- Served artifact: inline `#gpo-dynamic-css`, saved separately as `served-gpo-dynamic.css`. The final served artifact contains the exact deliverable CSS. Initial reload during save still served the old settings; a subsequent reload loaded the saved CSS.

| GPO control | Native evidence | Mapping / verification |
| --- | --- | --- |
| Labels / selected values | `.product-form__group-name`, 14px, weight 400, secondary foreground, line-height 1.4 | Theme variables and 10px spacing; observed on storefront |
| Buttons | `.product-form__controls-group label.pills-type-square`, 48px, 1px border, button radius, 16px text | Final 48px; selected gray background and foreground border; selection exercised |
| Color swatches | `.color-swatch--circle`, 40px ring and 23px painted fill | Native 40/23px geometry inspected; circular styling retained, while GPO inline size now drives fill and the ring grows around it |
| Image swatches | Color swatch ring / fill adaptation | Circular adaptation with GPO inline image size; no native image variant on supplied product |
| Select / custom dropdown | `.product-parameters .dropdown-select .select-label` in secondary mini picker | 44px gray box, no border, button radius, inherited body size; native picker is hidden after GPO renders, so source-backed mapping rather than a live primary-dropdown measurement |
| Dropdown list / caret | `.select-wrapper.active`, `.icon-caret`, native option label rules | Native source: immediate display toggle, 176px list, 2px offset, 24px caret rotates immediately, option hover color/background transitions 0.25s. GPO open / trigger close / outside close / select / blur verified |
| Image dropdown / font dropdown | Same native dropdown structure | Opening and selection exercised at desktop and 390px. Font options and selected Montserrat retain their own font family |
| Text / textarea / dimension / phone / color picker | `.field input`, `.field__input`, `textarea.field__input` rules in base.css | 44px single-line fields, input background / foreground variables, 16px type, border-color outline on focus. Source-backed general-field mapping; native product text field is absent. Textarea remains multiline (109.59px for 4 rows) |
| Prefix / suffix | Field-token adaptation | One painted wrapper, no double border, prefix / suffix align in 44px box |
| Quantity | Primary `.quantity`, 103x44px, 24px buttons, 45px input | GPO option quantity 103x44px; standalone quantity 44px tall; selected option plus button increments to 2 |
| Checkbox | `.field--checkbox .field__checkbox` | 24px, configurable input radius, accent selected background; toggle exercised |
| Radio / switch / range | Theme-token adaptation | No corresponding native product controls; checked state and slider keyboard value change exercised |
| Upload | Theme fields + `.button--primary` | Default appearance inspected. Action uses primary colors / typography and width reveal hover source. No real upload / remove tested |
| Horizontal tabs | `.description-tags__tag`, active underline / foreground; heading variables | Source-backed styling, active tab switch exercised |
| Vertical tabs / group | `.product__description-wrapper[data-layout=dropdown]` rows | Source-backed rule coverage; these GPO variants are not rendered on supplied product |

## Verification

- CSS parser after swatch correction: tinycss2, 124 rules / 474 declarations, no syntax errors.
- Desktop: initial Chrome actual viewport 1838x907 (requested Chrome resize did not change storefront viewport). Final verification in the in-app browser at actual 1440x1000. Final metrics are in `desktop-final-metrics.json`.
- Mobile: actual 390x844, final saved CSS loaded. Select / text / option quantity 44px; button swatch 48px; textarea 109.59px. No rendered GPO element extends outside the viewport.
- Normal, image, and font dropdown values retained after selection: option_2 / option_2 / Montserrat. Font preview remained Montserrat. Conditional field visibility continues to respond to choices.
- Phone country list opens within viewport (left 7px, right 177.66px, height 200px); color picker popup opens; decorated fields stay aligned.
- Checkbox, radio, switch, range slider keyboard input, swatch selection, quantity increment, and horizontal tab change verified.
- Screenshots: `desktop-final.png`, `mobile-final.png`, `desktop-fields.png`, `mobile-dropdown.png`.
- Native primary controls remain scoped outside the override; final native pills 48px and native color ring 40px preserved.
- Not verified: real file upload / remove, native dropdown live opening after widget insertion, pointer hover (API has no hover), absent GPO vertical tab / group, unavailable disabled/error controls. Hover / native dropdown effects are supported by inspected stylesheet rules, not presented as exercised native behavior.

## Learning review

No skill change proposed. The existing workflow already covers the findings: hidden secondary pickers need source-backed attribution, a swatch ring and its fill must be measured separately, two-color swatches must preserve their split, and actual viewport dimensions must be checked after resize.

## Selected value correction

The first match left selected values on a separate line. Corrected label/value flow to inline, with a colon after the label, matching the native product option label. The base hidden-label rule is preserved. The normal whitespace between sibling elements supplies the approximately 4px gap. Verified selected button and color swatch values share the label baseline at desktop and actual 390x844 mobile. Evidence: `selected-value-mobile.json`, `selected-value-mobile.png`, `selected-value-desktop.png`. Syntax validation passed.
