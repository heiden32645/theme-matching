# Zora 2.0.2 — GPO match

- Product: https://kbdq65hblv510gof-69620498584.shopifypreview.com/products/vans-era-59-moroccan-geo-dress-blues
- Native selection: Size 8 / Color blue; variant 47372774342808 from rendered product JSON.
- Theme identity: Zora 2.0.2, theme store ID 2505, installed theme ID 189294772376; verified from the rendered Shopify.theme script.
- Editable deliverable: `../2.0.2.css`, plain CSS, four-space indentation and flat selectors.
- Integration: Settings → Design → Custom CSS, saved through the supplied Shopify admin page. The automatic match checkbox remains off; this work uses Custom CSS.
- Originally served override: Zero 2.1.2 / 3300. Backup: `before-served-gpo.css`.
- Served output: `served-gpo-dynamic.css`; GPO inserts generated settings before the custom CSS. No separate minified artifact is involved.
- Shopify returned cached HTML after ordinary reloads. Each actual saved revision was checked using a distinct `gpo_match` query value. Final verification compares the entire deliverable with the served style, not just its header.

| GPO control | Native evidence and mapping | Status |
| --- | --- | --- |
| App typography | `body`, `--font-body-family`, weight/style/spacing/line-height; current Libre Franklin, green-grey on cream | Observed |
| Label | `.form-field--select .form__label`, `.form-fieldset legend`: 0.8rem / 12.8px | Observed select label; legend source inspected |
| Select and dropdown trigger | `.form-field select`: 40.5px, 16px normal font, 5px 15px 15px 0 padding, bottom border only | Measured; GPO outer box also 40.5px |
| Caret | `.form-field--select .select-arrow`: 15px square, bottom/right borders, rotate(45deg), right 15px, bottom 18px | Source and computed style observed; fixed on opening |
| Dropdown effects | Native HTML select uses a system popup, with no theme list animation or caret rotation. GPO max-height animation is reset and hidden/open visibility is immediate | Trigger, outside-close, selection and retained value exercised; OS popup hover/animation timing cannot be measured as page DOM |
| Custom dropdown options | Theme background/primary colors adapt the system-popup role; selected GPO background has a competing `!important` setting | Corrected to theme colors; OS menu geometry is a fallback |
| Text, textarea, dimensions | Asset `.form-field input` (13px, normal line, 12px 15px padding, square border) and `.form-field textarea` (minimum 100px) | Native text input not rendered on the product: asset-based fallback. GPO wrapper 41.5px; multiline textarea retained |
| Phone | Same field fallback; `.iti` background explicitly transparent; country popup uses theme colors and stays within viewport | Menu open/close and unclipped overflow observed |
| Button choices | `.btn--primary-outline`, no native variant pills rendered. Native primary colors and focus shadow indicate selection | Documented fallback; 41.5px action geometry |
| Color/image swatches | `.input--radio.swatch .swatch`: 36px circle, 42px outer ring and shadow on selection | Native assets inspected; GPO label and inner box verified 36×36px. Inline 32px GPO swatch sizes require a local override |
| Option quantity / single quantity | `quantity-input .quantity__button` / `.quantity__input`: unbordered 30px parts, 90px stepper | Measured, increment and selection tested |
| Checkbox / radio | Theme `input[type=checkbox/radio] + label`: 15px outer marker, 10px fill, square checkbox / round radio | Native asset mapping; GPO selection tested |
| Upload action | `.product-form__submit.btn--primary-outline`: 16px, normal line, 10px 12px padding, 41.5px | Measured action; real file upload/remove not exercised |
| Switch / range | Theme primary, text and background tokens; no equivalent native product control | Theme-token adaptation; toggle and slider keyboard change tested |
| Horizontal / vertical tabs, groups | Theme body/border/heading tokens; no native product tabs/accordion rendered | Horizontal tab selection tested; vertical/group rules source-based and not rendered on this product |

## Verification

Desktop was inspected at the actual 1838×907 Chrome viewport and 1440×1000 in-app browser viewport; mobile at a verified 390×844. Chrome viewport requests initially affected the active admin tab, so their requested dimensions were not used as storefront measurements; the temporary override was reset. In-app viewport dimensions were read back explicitly.

Observed: select/dropdown box match, separate text geometry, multiline text, preserved font-picker previews and linked field font, prefix/suffix, image-dropdown thumbnails, selected radio/checkbox/button/swatches, quantity increment, horizontal tabs, switch and range. No GPO input/label/tab crossed the mobile viewport. Keyboard focus shadow is visible on the decorated wrapper. Native product selectors are untouched by the scoped override.

Not exercised: real upload/remove, unavailable options, validation errors, vertical tabs, app groups. Hover rules were inspected in source/computed styles; the tool exposes no direct hover action. Native system-menu hover and exact OS popup animation are not claimed as matched.

## Learning review

Observation: Zora's global radio-label pseudo-elements appeared as stray circles inside GPO dropdown options. Its native text fields, select, and quantity also have distinct geometry. These findings are covered by the skill's existing cascade and separate-control measurement rules, so no duplicate general instruction is proposed.

Useful theme-specific addition, if requested later: add a Zora 2.0.2 case to `references/theme-cases.md` with the bottom-only select, fixed 15px CSS caret, 30px unbordered quantity, and global radio-marker collision. The saved native CSS and desktop/mobile measurements support this mapping; another Zora preset should be checked before generalizing color assumptions.

## Two-color swatch correction

User reported the two-color choice was malformed. The earlier CSS enlarged `.swatch-top` to 36px but left `.swatch-bottom` at its inline 32px border dimensions. The lower triangle therefore stopped 4px before the circle edge. The fix shares `--gpo-theme-swatch-size: 36px` between the swatch label and the triangle's `border-bottom-width` / `border-left-width`, preserving the configured inline border colors.

Verified on the served override at 1838×963 and 390×844: label, inner, top color and bottom triangle all measure 36×36px at identical coordinates. Green and purple form equal diagonal halves, selected and unselected. Single-color and image swatches retain their 36px circular box. CSS syntax check: 128 rules, zero parse errors. See `two-color-verification.json`, `two-color-fixed-desktop.jpg` and `two-color-fixed-mobile.jpg`. Final saved CSS is again identical to the CSS inside the served GPO style.

Proposed reusable addition to the workflow's swatch checks: whenever changing color-swatch dimensions, inspect and scale both the fill box and any border-based second-color triangle; verify the two-color sample selected and unselected at desktop and mobile widths. This would have caught the missed inline triangle before delivery. Do not overwrite its configured border colors. No skill source was modified.

## Image swatch size correction

Per user instruction, removed image swatches from every custom width/height rule, including the inner wrapper's 100% sizing. Only color swatches retain the native fixed size and synchronized two-color triangle. Image swatches now derive their dimensions from GPO's image settings. Current rendered image has inline `width:60px;height:60px`; label, inner wrapper and image each measure 60×60px, with no clipping and selection retained. The color swatch's two layers still both measure 36×36px. This supersedes the earlier 36px image geometry described above. Syntax validation reports zero errors and no image-swatch dimension overrides. See `image-size-verification.json` and `image-size-result.jpg`.

## Color swatch size correction

Per the user's follow-up, removed the fixed color-swatch size token and all custom size rules on the label, inner wrapper, `.swatch-top`, and the `.swatch-bottom` border triangle. Both color and image swatches now use GPO's configured sizes. The original inline dimensions of both color layers remain aligned without custom scaling. This supersedes the earlier fixed 36px color-swatch mapping. Syntax validation reports zero errors and no dimension overrides for either color or image swatches.

## Quantity border and type size

Per user request, added the theme field border to `.gpo-app .gpo-quantity .gpo-quantity__input` and the outer `.gpo-app .gpo-ov-quantity` wrapper. Quantity text now uses 0.875rem (14px at the current root size), reduced from 1.3rem (20.8px). The outer height remains 30px; stepper children subtract the two wrapper borders so they fit inside the box. This supersedes the earlier unbordered native quantity mapping.
