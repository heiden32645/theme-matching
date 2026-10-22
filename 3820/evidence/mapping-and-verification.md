# Mix 1.2.3 — GPO theme match

Verified 2026-10-22 (Asia/Ho_Chi_Minh).

Product: https://ahlx0ixhryqx7fhn-69620498584.shopifypreview.com/products/vans-era-59-moroccan-geo-dress-blues

Theme identity from the rendered Shopify theme script: installed name Camp, schema name Mix, version 1.2.3, theme store ID 3820, installed theme ID 189541679256, demo role. `/t/54/` is the installed asset path, not the theme store ID. Native variant at initial load: Size 8 / blue.

Deliverable: `../1.2.3.css`. Saved through Globo Settings → Design → Custom CSS. The editor was originally empty. Match Shopify theme style remains checked. The storefront `style#gpo-dynamic-css` contains the exact final file. No separate bundled/minified deliverable is used. Settings saved notification was observed; CDN propagation required a later reload. The embedded admin preview lacks the storefront theme variables and is not the visual reference.

## Native mappings

| Component | Evidence and painting element | Mapping and coverage |
| --- | --- | --- |
| App and label | Body / `.product-form__group-name`; DM Sans 500, theme body scale × .9rem below 750px, × 1rem above | Native/GPO label 16px and 22.398px high at desktop; 14.4px mobile, 8px bottom space. Selected value 700 weight from native legend span. |
| Button options | `.product-form__controls-group input[name=Size] + label` | 44px outer height, 10px `--border-radius-large`, transparent fill, 1px border and extra 1px accent shadow selected/hover. Desktop 16px / mobile 14px. Selection retains geometry. |
| Color swatches | `.color-swatch::after` owns fill, inset shadow and 2px accent selected border | Adapt the ring and circular shape, preserve GPO's configured 32px color sizes. Native sample is 44px. Two-color diagonal remains intact. |
| Image swatches | Asset `.variant-swatch--image`, 8px radius and dark selected border | Source mapping; retain configured 60px image sizes. Native image swatches are absent on this product. |
| Select and dropdown | Asset `.product-parameters .select__select`: min-height 4.4rem, 1px input border, input background, 10px button radius, 4px vertical / 20px left padding | Source-supported fallback because native variant select is absent on the supplied product. GPO select, custom dropdown and font dropdown measure 44px. `.select .icon` / `.icon-caret` supplies 20px arrow box, 14px right inset. |
| Dropdown effects | Native variant select is browser-owned; source has no custom list or caret rotation. Custom theme disclosure menu supplies list color, hover background and typography adaptation | GPO inherited .3s max-height transition removed in normal/image/font dropdowns; visibility toggles immediately, caret stays still. Trigger close, outside close, option selection and retained values observed. Native browser-menu opening animation cannot be compared because a native variant select is not rendered. Hover is supported by inspected theme CSS; no separately exercised hover API. |
| Text, dimension, decorated input, phone and color | Asset `.field .field__input`, 2px border, .9rem × 1.6rem padding, min-height 4.4rem, input colors and hover/focus border | Wrapper owns border; inner input is borderless. GPO outer box 44.398px with 22.4px line height. Native product text input absent; mapping uses generic field source, not the header search override. Prefix/suffix remain aligned and phone inline dial-code padding survives. |
| Textarea | `.field textarea.field__input`, 6px radius, 18px × 20px padding | Multiline content retained; min-height is not used as line-height. Rendered outer height 129.594px with current rows configuration. |
| Quantity | Native `.quantity`, 120 × 44px, 1px border, 10px radius, transparent; `.quantity__button` 42px with 18px accent icon | Option quantity wrapper matches 120 × 44px. Single quantity uses native outer border and height, retains GPO 100px limit. Increment 1 → 2 observed. Inactive option quantity opacity/pointer behavior preserved. |
| Checkbox | Asset `.field--checkbox`: 16px box, 2px radius, border/background theme tokens, yellow selected fill with button-text check | Selected/unselected behavior observed. Radio has no equivalent native product control and adapts theme accent/border tokens. |
| Upload | `.product-form__submit.button--secondary`: DM Sans button family/weight/size, .25s transition, secondary background/text and 10px radius | Action rendered. File selection, upload and removal untested; no disposable upload fixture supplied. |
| Switch / range | No native product equivalent | Theme accent, background and border adaptation. Switch checked, slider 0 → 1 and 1% progress observed. |
| Horizontal tabs | No native horizontal product tabs | Theme-pill adaptation. Corrected parent h3 font size so tab inherits app font (16px desktop, 14.4px mobile). Second tab opens. |
| Vertical tabs / group | `.about__accordion-toggle`, native body typography, 16px vertical padding and border tokens | Source mapping only; vertical tabs/disclosure groups are not rendered by supplied option set. |

## Verification

- Final CSS syntax/declarations parsed with tinycss2. Selectors checked with cssselect2; vendor slider pseudo-elements documented separately. No undefined or unused `--gpo-theme-` tokens. No preprocessor or nested selector syntax.
- Exact final file is included in served dynamic CSS. Admin save was successful.
- Desktop test tab actual viewport 1440 × 1000; mobile test tab actual viewport 390 × 844. Original user tab was also inspected at its actual 1598 × 877. Viewport capability did not resize the claimed user tab, so responsive checks used an agent-created tab with confirmed actual dimensions.
- At mobile width document clientWidth = scrollWidth = 390; no GPO element outer box overflows. Phone country menu and color picker remain visible within viewport.
- Native GPO select selected option_2. Custom dropdown trigger close and outside close tested; image dropdown and Google font dropdown opened and selected on desktop/mobile. Values retained after blur. Font labels preserve Roboto, Open Sans, Montserrat, Poppins and Oswald previews.
- Text input, keyboard Tab into textarea, multiline text, dimension value, radio, checkbox, button option, color and image swatch, single quantity, option stepper, tab, switch, range and color-picker acceptance observed. No product was added to cart.
- CSS focus/hover rules inspected; pointer and keyboard text focus exercised. GPO hidden-input swatches and custom dropdown keyboard support were not expanded beyond existing app behavior.
- Native controls remain scoped outside the override; final desktop metric record includes native label, Size and quantity geometry.
- Upload/remove, unavailable/error states, unrendered vertical tabs/group disclosure, Firefox and exhaustive accessibility behavior are untested.
- Temporary viewport override reset; original storefront reloaded to clear test values.

## Learning review

Existing workflow already addresses painted wrappers, separate quantity geometry, font-preview preservation and verifying actual viewport. No new general rule is needed. A future theme-cases entry could retain these Mix-specific mappings (44px selects/quantity, distinct 1px/2px borders, source fallback for native variant dropdown, Size-specific 44px pills); verification here covers one theme-settings configuration.

## Compact quantity revision — 2026-10-22

User requested smaller `.gpo-ov-quantity` and `.gpo-quantity .gpo-quantity__input`. Quantity height reduced from 44px to 32px; stepper width 120px → 90px with 28px buttons, 14px icons/text; single input width 100px → 70px with 14px text. Vertical quantity-mix allocation updated to the new stepper width. Comments now describe this deliberate compact adaptation. Saved to Globo and exact updated CSS verified in storefront. The editor was replaced in full to consolidate duplicate prior CSS; served file now has one Mix override. Desktop measured boxes: 90 × 32px and 70 × 32px. Increment and numeric input both retained value 2. Syntax parsed without errors. Evidence: compact-quantity-verification.json and compact-quantity-desktop.png.
