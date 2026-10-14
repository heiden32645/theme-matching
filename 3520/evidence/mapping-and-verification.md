# Nova 1.4.0 / Orion — GPO match

Verified 2026-10-12. Theme store ID 3520; installed demo theme ID 189163569304 (asset /t/29/ is not the theme store ID). Identity comes from the storefront Shopify.theme script: schema_name Nova, schema_version 1.4.0, display name Orion. Product: VANS ERA 59 MOROCCAN GEO/DRESS BLUES, initial size 8 / color blue.

Preview: https://bd6i3js4dqxnnk3k-69620498584.shopifypreview.com/products/vans-era-59-moroccan-geo-dress-blues
Admin: https://admin.shopify.com/store/minky-store-one/apps/globo-product-options/admin/settings/general

## Integration

Initial Custom CSS was empty; Match Shopify theme style was enabled, but the preview had only GPO base and direction CSS, without a Nova override. Saved the deliverable 3520/1.4.0.css through Globo Design > Custom CSS. The final served #gpo-dynamic-css contains the exact deliverable. All rules are scoped to body[data-gpo-theme-store-id="3520"] to keep the theme mapping local to Nova.

The editable file and served CSS are separate artifacts. Source assets: native-lib-core.css and theme-inline.css; GPO base saved as gpo-base.css. No theme files or publication settings were changed.

## Mapping

| GPO control | Native evidence / fallback | Result |
| --- | --- | --- |
| App/body | --glob-body-font, --glob-body-font-weight; color-scheme variables in product ancestors | Lato 19.2px, 400; inherited theme colors |
| Labels / selected values | .product-variant-picker__option-heading-name (.7 opacity), sibling value (full color) | 1rem, .5rem bottom space, inline selected value |
| Button choices | .product-variant-picker__option-value-title / .product-variant-picker__option-value-pill | Same 65.4375px outer height, .8rem 1rem padding, 21.12px type, 2px border; selection changes border only |
| Custom/native/font dropdown | Source .product-variant-picker__drop-header; this product renders pills, not native variant dropdowns | Source-supported 65.4375px box; static caret for native select; custom caret .2s linear rotation |
| Dropdown list | Source .drop-down__drop and .product-variant-picker__option-drop-value | Immediate list visibility, max min(400px, 50vh), theme shadow, row separators, bold selected row; no source hover fill |
| Text / textarea / dimensions / phone | Source .form-control__input / .form-control__textarea (not rendered in main product) | 45.1953px single-line outer wrapper; .375rem .75rem padding; 1px theme border; dark border on focus; multiline textarea preserved |
| Decorated text | GPO prefix/suffix structure, theme form input tokens | Wrapper owns border; icon and suffix align inside the 45.1953px field |
| Single quantity | .product-qty--enlarge .product-qty__inner and .product-qty__input | 47px outer height; the single input uses a bounded 100px GPO width |
| Option quantity | Same native enlarged stepper | 119px x 47px outer box, 36px buttons, 45px inner height; quantity update retained |
| Color swatch | Source .product-variant-picker__swatch--pill and .product-variant-picker__swatch__bg (native page uses image swatches) | 50px box, 5px total inset, theme configurable rounding |
| Image swatch | Rendered .product-variant-picker__image | 80px box; 70px image and 5px total inset; dark 2px selected border |
| Upload action | Rendered product .button--variant--outline.button--size--lg | Oswald 24px, uppercase; 80.7969px action height, outlined button and theme-colored hover adaptation |
| Radio, checkbox, switch, range, upload area | Theme-color adaptation; no equivalent main-product control | Scoped theme colors while retaining GPO behavior |
| Horizontal tabs | Source .tabs__nav-item__button | Muted inactive title, full-color underlined active title, no boxed tab fill |
| Vertical tabs / groups | .collapse / .collapse__header source; disclosure rendered below product | Theme border rows and heading font; vertical GPO tabs/group disclosure not rendered |

Native geometry and source formulas differ by role. The native universal line-height is calc(1em + .5rem): 1.1rem variant text yields 1.6rem line-height, not 1.65rem. Preserve this formula for variants; text fields use the 1rem / 1.5rem form geometry.

## Verification

Actual desktop viewport 1440 x 1000 and mobile 390 x 844. An earlier resize targeted the admin tab, so measurements at 1838px were treated as desktop only; final 1440px measurements are recorded separately. No horizontal overflow at either final viewport. Control wrappers, single/option quantities, color/image swatches, upload action, and native pills compared using computed styles and painted boxes.

Exercised native select selection; ordinary, image, and font dropdown selection and trigger closing on desktop/mobile; font preview family retained (Montserrat desktop, Oswald mobile). All three custom dropdown lists have transition:none, hidden/0px closed and visible/400px open at desktop; .2s linear caret rotation retained. Native variant dropdown opening behavior is source-inferred because that variant presentation is absent.

Exercised pointer focus and keyboard Tab into textarea; dark wrapper focus border retained. Text and two-line textarea retained typed content. Phone country list opens without clipped ancestors. Found and repaired a 76.27px country list caused by max-width:100% relative to the flag container; final width 320px, left 20.5px / right 340.5px at mobile 390px. Color popup fits the mobile viewport (250px wide).

Exercised button choice, color swatch, quantity increment 1 to 2, radio, checkbox, switch, range keyboard increment, and horizontal tab activation. No cart submission. Temporary test values existed only in the browser; the disposable verification tab was closed. Both original task tabs had their temporary viewport overrides reset; admin restored to 1838 x 907.

CSS parsed using css-tree: 118 flat rules, 446 declarations, zero parse errors. Exact CSS present in served dynamic stylesheet. Validation record: css-validation.json. Screenshots: desktop-match.jpg, mobile-match.jpg.

Not visually exercised: native variant dropdown list, hover states (no hover API), disabled/error fixtures, actual upload/remove, GPO vertical tabs and group disclosure. These remain source-supported mappings or untested states, not passed visual checks.

## Learning review

Potential addition to match-theme references/theme-cases.md: Nova 1.4.0 uses global calc(1em + .5rem) line-height; preserve the role-specific variant/text formulas and the enlarged 45px quantity input. A phone menu can be nested inside the narrow flag container: max-width:100% constrains it to that container rather than the full phone field. Use a viewport-bounded explicit menu width and verify its painted bounds. The viewport measurement and wrapper inspection workflow already covers the general rule; this is a theme-case example rather than a new universal rule.

## Selected-value punctuation correction

Added a colon to label/dimension-label only when the adjacent selected-values element has .has-value. Removed the extra .25rem left margin so the regular inline space follows the colon. Required markers remain intact; labels without selected values have no added colon. Verified Select: option_2 and required Dropdown *: option_2 on the saved storefront. Current local file keeps its pre-existing unscoped selectors; the admin override keeps its existing body theme-ID scope. Both were parsed successfully. Evidence: selected-value-colon.json, selected-value-colon.jpg.

## Dropdown chevron correction

Verified against the rendered native variant dropdown on VANS APPAREL AND ACCESSORIES CLASSIC SUPER NO SHOW SOCKS 3 PACK WHITE in the same Orion preview. Native .drop-down__header-icon is a 12px SVG using #svg-icon-arrow-down: viewBox 0 0 256 256, polyline 208 96 / 128 176 / 48 96, rounded caps/joins, stroke-width 16. The earlier --glob-svg-arrow-down token is a different 16-unit SVG with stroke-width 2; at 12px its stroke is 1.5px and painted centerline width 9px, versus native .75px and 7.5px. The native opacity is 1 and color is #282828, so no arbitrary opacity adjustment was added.

Replaced the dropdown mask with the actual native symbol geometry in --gpo-theme-chevron and moved the icon inset from .75rem to 1rem to match the native summary padding. Applied to select, ordinary/image/font dropdowns. Kept the 12px box and .2s linear 180-degree rotation. Local CSS retains its existing unscoped form; live admin CSS retains its existing Nova body scope.

Verified loaded token, native/GPO icon box, color, mask, inset and open rotation on desktop and actual mobile 390 x 844. Both local and served CSS parse without errors. Saved chevron-match.jpg, native-dropdown-chevron.json, chevron-comparison.json, chevron-states.json and chevron-css-validation.json. Temporary check/admin tabs were closed and viewport reset; the user's theme editor tab was preserved.

Learning proposal for references/theme-cases.md: Nova's --glob-svg-arrow-down and #svg-icon-arrow-down are different assets. For product dropdowns use the inspected symbol, not the form-select mask variable. A matching 12px outer box alone does not establish the same painted chevron; compare viewBox, path bounds, stroke width and caps. This case is verified against a rendered native dropdown.
