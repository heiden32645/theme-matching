# Spark 4.1.1 — theme store ID 911

Date: 2026-10-21 (Asia/Ho_Chi_Minh).

Product: https://zt51818fz9igmfix-69620498584.shopifypreview.com/products/vans-era-59-moroccan-geo-dress-blues

Verified preview: same URL with `?gpo_match_check=911`. Variant: 8 / blue, ID 47372774342808.

Theme identity: inline theme bootstrap reports Spark v4.1.1 by Fluorescent. GPO's theme metadata reports theme_store_id 911; installed theme ID 189500260504, preset name Trendsetter. `/t/53/` is an asset installation path, not the theme store ID.

## Integration

- Editable deliverable: `../4.1.1.css`.
- Saved through GPO Settings > Design > Additional > Custom CSS. The existing Match Shopify theme style setting remains enabled.
- Before editing, Custom CSS was empty. After saving, reloading admin retained the complete CSS.
- Served inline in `style#gpo-dynamic-css`, following GPO's alignment rules. Read-only comparison confirmed the style contains the complete deliverable verbatim (25,604 characters including the trailing newline). No separate minified deliverable.
- Initial storefront reloads returned old HTML with empty custom_css. A fresh document URL returned the saved CSS; later reloads retained it. This was an integration/cache issue, not a CSS measurement failure.
- Theme source: `/cdn/shop/t/53/assets/theme.css?v=75216187407560615041792519331` and the page's inline CSS variables. Existing custom.css remains untouched.

## Native to GPO mapping

| Control | Native evidence / painted box | GPO mapping and verification |
| --- | --- | --- |
| App text | body: `--font-body`, `--font-body-weight`, `--font-size-body-base`, body spacing | `.gpo-app`, IBM Plex Sans, body font retained |
| Option label | `.product__label.ff-heading.fs-heading-4-base`: Libre Caslon Text, 700, 19px/26.6px; label wrapper bottom margin `--spacing-small` | `.gpo-label .label-content`, same typography and 12px spacing; visible desktop/mobile |
| Selected value | `.product__color-swatch-value`: body typography | `.gpo-selected-values`, body typography beside heading |
| Button swatch | `.product__chip`: height `--height-input` 48px; 8px 20px padding; 1px `--color-border`; radius `--spacing-unit` 4px; selected dark text-color background | `.gpo-swatches.buttons input + label`, observed 48px and same padding/border/radius |
| Color / image swatch | `.product__color-swatch`: 48px outer box; 6px background border; 1px shadow ring; text-color selected ring; 0.3s shadow transition | GPO color/image labels, observed 48×48px, circular, 36px inner content; selection and quantity exercised |
| Select | Hidden native variant `select#option1.input`; source `select.input`: `--height-input`, 8px 20px, 3px radius, `--color-border-input`; `.select-wrapper .icon`: 14px, right 17px | `.gpo-select` paints 1px border; child select fills 46px; observed 48px outer height, source-supported mapping since native variant selects are hidden |
| Custom / image / font dropdown | Same select geometry; native option popup uses platform UI, not an HTML theme list | `.dropdown-button` 48px, 3px radius; theme chevron path from page SVG; list uses documented theme-token fallback with immediate visibility and no caret rotation; normal/image/font open and select verified desktop/mobile; normal trigger-close and font outside-close verified |
| Text / phone / dimensions | `input.input` source: 48px, 8px 20px, 3px radius, input border; input hover/focus text border and `.input:focus` link-color 1px shadow | Border on `.gpo-input-wrap` / `.gpo-dimension-input-wrap`; inner input 46px; decorated text, phone and color wrappers observed 48px; prefixes/suffixes remain inside wrapper; focus and keyboard Tab exercised |
| Textarea | `textarea.input`: 16px padding and vertical resize; body type | `.gpo-textarea`, multiline retained after filling two lines; auto height, minimum 96px, vertical resize |
| Option quantity | `.product__quantity`: 48px bordered wrapper, radius 3px; native buttons 40px, input 30px | `.gpo-ov-quantity`: observed 112×48px; selection enables existing controls; plus action changed value 1→2; disabled/unselected opacity retained |
| Single quantity | Native quantity paints border on wrapper; GPO single field has no equivalent stepper wrapper | `.gpo-quantity__input` uses `.input` geometry as a documented adaptation; observed 48px, value editing retained |
| Checkbox | Native theme `input[type=checkbox]`: 20px square, 1px input border, solid inset when checked | `.gpo-checkbox` uses square inset, not inherited check glyph; checkbox selection verified; radio uses same theme tokens with circular dot and selection verified |
| Upload | No native file upload rendered | Field-token dropzone; action maps `.btn--primary.btn--small` and responsive submit styling; remove maps `.btn--secondary`; default rendering only |
| Switch / range | No direct native switch/range counterpart rendered | Theme color/token adaptations; switch toggled successfully; range appearance inspected, value interaction not exercised |
| Tabs / group | `.rte--product.accordion .accordion__label` source: heading family, heading-4 size, 12px/16px spacing, meta hover; accordion icon rotates 90 degrees | Horizontal tabs use a documented token adaptation and active underline; second tab selected successfully; vertical accordion CSS included from source but not rendered for live verification |

## Verification

- CSS parsed with tinycss2: 118 qualified rules, zero syntax/declaration errors; flat CSS and ordinary top-level media query.
- Actual desktop viewport in Chrome: 1598×933. A requested override there did not change innerWidth, so it was not counted as the requested size. Override reset.
- Additional actual desktop viewport in IAB: 1440×1000, no horizontal overflow.
- Actual mobile viewport in IAB: 390×844, document clientWidth=scrollWidth=390; app box x=23..367, controls x=28..362; select, dropdown, text/phone/color and option quantity retain 48px height. Override reset afterward.
- Native controls retained measured geometry and appearance. CSS is scoped to GPO.
- Normal, image and font dropdowns retain values after selection/blur on desktop and mobile. Font label and selected preview still use Montserrat/Roboto rather than losing font-preview styles.
- Dropdown transition computed as `none`; normal list opens to 278px and closes to 0px. Native variant select popup effects cannot be visually compared because the variant selects are hidden; custom list treatment is a supported adaptation, not a measured native-popup match.
- Phone country list opens, scrolls and stays unclipped. Color picker popup opens. Radio, checkbox, switch and horizontal tabs respond correctly. Textarea remains multiline. Quantity increment and direct input work.
- No file was uploaded, so uploading/progress/remove are untested. Native-equivalent hover was source/computed-style inspected rather than visually exercised with pointer hover. Error states and vertical tabs were not available for live verification. No claim of full keyboard support for GPO custom dropdowns, which use the app's existing interaction semantics.
- Test values on the user's Chrome storefront tab were cleared by reloading after verification. No cart or purchase action was performed.

Screenshots: `final-desktop.png`, `desktop-1440.png`, `mobile.png`, `choices.png`.

## Learning review

The skill already covers checking served versus editable CSS and verifying actual viewport size. The two integration findings above reinforce those existing checks; no additional skill rule is proposed.

## Follow-up: two-color swatch and compact quantities

This section supersedes the initial quantity sizes and parser totals above.

The original override resized `.swatch-top` to 36px while `.swatch-bottom` retained its inline 32px triangular borders. The mismatch distorted the two-color split. The final CSS keeps clipping on `.gpo-swatch__inner`, leaves the first layer square inside it, and sets both triangle border widths to the same `calc(var(--swatch-size) - 12px)`. Both painted layers now measure 36 by 36px, retaining the original lime/purple colors and diagonal split.

By user request, quantity height is now 32px. The option stepper measures 80 by 32px with 24px buttons, a 30px input and 12px icons. The single quantity input measures 72 by 32px with 16px text and 4px/10px padding. Native product quantity remains unchanged.

Verified the complete final CSS (26,050 bytes) is present in the storefront, with exactly one Spark match header. Custom CSS was replaced in full through the editor to remove the earlier revision. Parser: 121 qualified rules, zero errors. Actual desktop 1598 by 933 and mobile 390 by 844: no horizontal overflow; selection, increment/decrement and direct entry pass. Mobile increment produced 2; desktop increment/decrement produced 1 to 2 to 1. Screenshots: `swatch-quantity-fixed-desktop.png` and `swatch-quantity-fixed-mobile.png`.

Learning proposal for `references/theme-cases.md`: record the GPO two-color swatch's `.swatch-bottom` border triangle and require its horizontal/vertical border widths to track the first layer whenever resizing `.swatch-top`; verify a two-color option, not only a solid swatch. This prevents the 32px/36px mismatch seen here. Verified for Spark 4.1.1's current GPO markup; other multi-color implementations require their own inspection.

## Follow-up: preserve configurable swatch sizes

The user requests that GPO controls own color/image swatch sizes. Removed all theme-derived width/height overrides for `.swatch-top` and `.swatch-image`, plus the triangle border-width overrides on `.swatch-bottom`. GPO's inline dimensions and matching two-color triangle now control their own size. Round clipping, theme ring styling and compact quantities remain. This supersedes the earlier theme-size synchronization proposal: no theme `--swatch-size` reference remains in the deliverable. Parser: 119 qualified rules, zero errors; targeted declaration inspection finds no swatch size overrides.

Live check: exact deliverable is loaded with one Spark header. Color layers both follow GPO's inline 32px size, while image swatches follow their independently configured 60px size. Two-color selection remains intact; quantity controls remain 32px high. Screenshot: `configured-swatch-sizes.png`.

## Follow-up: visible select on Composite Fence Panels

Product: https://zt51818fz9igmfix-69620498584.shopifypreview.com/products/composite-fence-panels

The visible native `.product__option-select-wrapper select#option1.input` confirms the 48px height, 3px radius, 18px IBM Plex Sans text and input border colors. Its `.select-wrapper .icon` uses a filled triangle (`m0 6 12 12L24 6z`), not the stroked chevron previously taken from a different page control. The icon is a 14 by 24px SVG box, positioned 17px from the wrapper's outer right edge. Select border transition is `border-color 0.3s ease-in-out`; focus shadow is immediate.

Added a separate `--gpo-theme-select-caret` for the verified select triangle. GPO select and all custom dropdown triggers now use that exact path and SVG dimensions. Their pseudo-element has right:16px inside the 1px bordered wrapper, matching the native 17px outer inset. Kept accordion's separate chevron. Aligned select/dropdown border transition and removed their previous focus-shadow fade. Existing configurable swatch sizes and compact quantities remain untouched.

Verified complete deliverable is loaded. Native select, GPO select and GPO dropdown all measure 48px and use the same font and border transition. Keyboard Tab reaches `#select-1`, showing the theme link-color 1px focus shadow. Normal, image and font dropdowns open/select/close and retain option_2, option_1 and Montserrat after blur on desktop and mobile. Font preview remains Montserrat. Lists retain immediate visibility and fixed caret direction. Native popup is OS-rendered and was not captured by the storefront screenshot, so no claim of identical platform option-menu rendering. Hover behavior is source/computed-style covered; no pointer hover test API was used.

Desktop actual viewport: 1598 by 933. Mobile actual viewport: 390 by 844, no horizontal overflow; native and GPO selects remain 48px. Temporary viewport reset. Parser: 119 qualified rules, zero errors. Screenshots: `composite-select-matched.png`, `composite-select-mobile.png`.

Learning review: this corrects a violation of the skill's existing instruction to inspect the actual native counterpart. The visible product select provides stronger evidence than the earlier footer SVG; no duplicate general skill instruction is proposed.
