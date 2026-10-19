# Sampo 6.0.0 — Resonance, theme store id 3470

Product: https://4gjui3089rjs7hb0-69620498584.shopifypreview.com/products/vans-era-59-moroccan-geo-dress-blues
Variant: 8 / blue. Installed theme asset path t/37 is not the theme store id.

Deliverable: 6.0.0.css. Applied to GPO Settings → Design → Custom CSS.
Automatic Match Shopify theme style was disabled because it served the previous Poetic 1.6.0 stylesheet. The prior Custom CSS editor was empty; before-served-gpo.css records the previous served styling. Other design values were preserved. Final custom CSS equals the served custom section after save synchronization.

| Control | Evidence and mapping | Verification |
| --- | --- | --- |
| Labels / selected values | .product-option .option-label, Inter 300, bold selected value, 0.4rem bottom margin | Desktop 16px / mobile 14px; colon spacing corrected and observed |
| Button options | .product-option input[type=radio] + label; 8px 12px padding, theme background, black selected border, --button-border-radius | 34px desktop / 32px mobile; selection exercised |
| Color / image swatches | Asset fallback .product-option .swatch; 2px inner padding, round box, theme border | Rendered, configured sizes retained; color selection exercised, image default inspected |
| Quantity | quantity-input / .quantity__button, white inset shadow, pill radius, 120px outer width | Native 46.781px / GPO 46.797px desktop; option plus increments 1 to 2 |
| Single quantity | Same native quantity box without plus/minus | Outer height / colors / shadow inspected |
| Select / dropdown | Source fallback .field__input + .product-option .select select; no variant dropdown exists on this product | 54.266px desktop / 53.844px mobile; white background, 6px radius, #ddd border, Inter 16px |
| Dropdown effects | Theme uses an OS native select in inspected assets, no custom variant list | Immediate list and stationary caret are a documented fallback, not a live measured native-list match. GPO regular/image/font opening, selection and closing exercised; regular/image outside close exercised |
| Input / textarea / decorated fields / phone | Source .field__input, outer wrapper owns one border; no product-native text field | Padding/box/shadow observed; multiline textarea and keyboard focus observed; prefix/suffix aligned; phone menu opens within mobile viewport |
| Font picker | Preserve inline font-family previews | Montserrat / Oswald selected and retained; inline previews resolve to individual fonts |
| Checkbox / radio / switch / range | Theme-token adaptation; no equivalent product-native controls | Rendered default states inspected; no live native correspondence claimed |
| Upload action | .btn.btn--primary | Action font / colors / radius / 46.781px height agree; actual upload/remove not exercised |
| Horizontal tabs | .tab-title.btn--link, blue underline and subdued inactive tab | GPO tab changes exercised on mobile |
| Vertical tabs / group disclosure | Product details summary fallback | Not rendered in the storefront fixture; source coverage only |

Viewport checks: actual 1440×1000 desktop and 390×844 mobile. No page or GPO-group horizontal overflow. The viewport API initially targeted the admin tab; those observations were not counted as mobile. A dedicated preview tab provided verified viewport dimensions and was closed after testing. Temporary overrides reset.

Focus: native accessibility.css 4pt ridge #2158ee retained for keyboard focus; a single outline is painted around decorated fields. Pointer focus and keyboard Tab to textarea checked on desktop/mobile.

No hover API was available; hover declarations were reviewed from sources rather than visually exercised. Disabled/error/upload/remove states were not induced. Native product pills and product quantity retained their original appearance.

CSS parser: 128 rules, no syntax errors. Exact final custom CSS served verified. Screenshots and measurements are in evidence/.

Learning review: loaded-style detection, important GPO design declarations and viewport confirmation are already covered by the skill; no new skill rule proposed.

## Focus and compact quantity correction

The product now renders native variant dropdowns (.product-option .field select.field__input). Pointer opening the native select gives a 4pt ridge #2158ee outline (computed 5px) while its border remains 1px #ddd. The previous GPO inner select had this outline, but .gpo-select overflow:hidden clipped it. The corrected CSS paints one outline on the outer .gpo-select:has(select:focus-visible), suppresses the inner outline, and applies the same outline to the expanded GPO dropdown button. Native inner field and corrected GPO outer field compute the same focus outline. Closing the regular dropdown removes its outline; selected option_2 is retained.

Both quantity roles are now 34px outer height at the user's request, with 32px inner buttons/input. This intentionally replaces the previous full product quantity height. Width and colors retained. Option plus increments 1 to 2.

Desktop actual 1838×963; mobile actual 390×844. Mobile select focus and 34px quantities checked; no horizontal overflow. Image and font dropdowns show the same blue ridge outline when expanded after dismissing the newsletter popup. Initial popup-obstructed click observations were not counted as passed. Screenshots saved with corrected names in evidence/. Temporary viewport reset; test tabs closed.

Final CSS: 129 rules, no parser errors, exact served custom CSS match.

## Requested white option backgrounds

Button options, product-link pills and google-font buttons now use #ffffff in default, hover and selected states. Product-link outer wrappers remain transparent because the inner labels paint the pills. Font dropdown trigger already uses the white input background. Live computed backgrounds for all 10 rendered button/link/font labels are rgb(255,255,255); selected option_1 and Montserrat checked, individual font previews preserved. Exact served custom CSS matched. CSS parser remains 129 rules with no errors. Screenshot: evidence/white-options-final.png. Hover covered by CSS declarations; no hover interaction API available.

## White background request reverted

At the user's request, restored the exact pre-white-background CSS backup. The only differences are the button section comment and its two background declarations, returned to var(--color-background). Button options, product-link pills and font-picker buttons all compute rgb(239,244,249). Both quantity roles remain 34px and the corrected select/dropdown focus rules are preserved. Exact served custom CSS match verified after save. Screenshot: evidence/reverted-white-options.png.
