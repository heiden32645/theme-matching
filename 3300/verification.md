# Zero 2.1.2 — Tattoo preset (theme store id 3300)

Product: https://etwsbq1ajxro3k5e-69620498584.shopifypreview.com/products/vans-era-59-moroccan-geo-dress-blues
Variant: Size 8 / Blue. Shopify script reports schema_name Zero, schema_version 2.1.2, theme_store_id 3300; installed theme 189293625496, asset path t/38.

Deliverable: `2.1.2.css`, saved to GPO Settings → Design → Custom CSS. Previous Sampo CSS is backed up in `evidence/before-served-gpo.css`. Match Shopify theme style remains disabled. Other design settings preserved. The exact final CSS was compared against the served custom section and matched; the dynamic served stylesheet is recorded separately.

## Mapping and verification

| Component | Native evidence / mapping | Coverage |
| --- | --- | --- |
| Labels | `.product-common_variant-title`: Syne 700, 14px / 24px, widget foreground | Measured native and GPO agree; selected values use body font |
| Button swatches / product links | `.product-variant-option_label--simple`, inner `.product-variant-option_text`: Poppins 500, 12px / 20px; 8px 18px padding; square 36px box; dark selection with widget-border shadow | Default / selected measured; selection exercised; inline font previews preserved |
| Color / image swatches | Asset fallback `.product-variant-option_label`: 3px transparent inset border and selected widget ring | Rendered and color selection exercised; sizes retained from configuration |
| Quantity | `.quantity-input input[type=number]`: 31px, Poppins 300 14px / 21px, square; stepper has three separate border cells | Single and option quantities measured 31px desktop/mobile, matching native; plus increments 1 to 2 |
| Dropdown / select | Native dropdown absent on product. Source `.dropdown-variant_opener`: 12px padding, 14px / 21px, input-border-width, widget-border-color, input-corner-radius | Source-derived 47px; GPO regular/image/font measured 47px desktop/mobile |
| Dropdown effects | `.dropdown-component_wrapper` / `.dropdown--open` use opacity, visibility, clip without a list transition; `.product-variant-option_btn-submit` inverts input colors on hover/active | GPO transition none, stationary caret, exact theme SVG path; trigger open/close, selection, regular/image outside close exercised. Native variant dropdown/caret motion cannot be observed on this product; this is source coverage |
| Text / textarea / dimension | Theme input source: `--input-height:5.2rem`, `--input-font-size:1.4rem`, `--input-line-height:2.1rem`, `--input-padding-x:2.2rem`; painted wrapper owns one border | 52px single fields; 110px textarea outer; two-line entry and keyboard Tab focus observed; prefix/suffix align |
| Phone / color picker | Same field source; remove inner phone border; input text token used on dark background | Phone 52px outer; country menu within mobile viewport; color popup left 48/right 298 at width 390 |
| Upload action | `.product-common_atc-btn`: Syne 600 12px / 20px, square, 11px 30px padding, theme primary colors | Both native and GPO 44px; caption contrast checked. No file upload/remove performed |
| Checkbox / radio | `.custom-checkbox-input` source geometry and theme colors, radio as token adaptation | Both selection states exercised. No rendered native product equivalent |
| Switch / range | Theme-token adaptation | Rendered default inspected; no native correspondence claimed |
| Horizontal tabs | Product pill treatment adapted to tab controls | Tab changes exercised desktop/mobile |
| Group / vertical tabs | `.abc_row .collapsible-row_opener` typography and row spacing | Source only; not rendered in this product fixture |

## Results

Actual viewports: desktop 1440×1000, mobile 390×844. Page scroll width 1425 / 375 respectively (scrollbar excluded), with no GPO element horizontal overflow on mobile. Temporary viewport overrides reset. Native product pills and quantity retained their styling. Saved screenshots cover fields, options, dropdown, country menu and final desktop view.

Final custom CSS equals the saved file after asynchronous save/CDN synchronization. The first immediate reload still served the previous revision; subsequent fresh test tab confirmed the latest exact content. No guessed asset URLs were used.

CSS parser checked every selector and declaration: 122 rules, no syntax errors, no duplicate declarations, no unscoped selectors, no nesting. Hover declarations inspected from sources, no hover API exercised. Disabled/error states and upload/remove not induced. Group/vertical tabs are source-covered only.

Learning review: widget and input color variables differ in the Tattoo scheme (`--section-widget-foreground-color` dark on the light widget; `--section-input-text-color` white on dark fields). Scope and painted-wrapper checks in the existing skill already cover this finding; no new skill instruction proposed.

## Selected-value colon correction

Added `: ` with a ::before pseudo-element on nonempty .gpo-selected-values and removed the extra 6px left margin. The observed markup contained only the value and no existing colon. Local CSS parses as 123 rules without errors. Store application is pending: the refreshed Shopify Globo iframe stayed blank, a fresh admin tab also stayed blank, and direct Globo access redirected to login. No further store settings were changed in this correction.
