# Elixira 5.0.0 / 3264

Inspected on 2026-10-06. Product: https://5jdnwynzho9akz1t-69620498584.shopifypreview.com/products/vans-era-59-moroccan-geo-dress-blues . Native variant 8 / blue. Identity is confirmed by the storefront `Shopify.theme` script: schema name Elixira, schema version 5.0.0, theme store id 3264. `/t/84/` is the installed asset path, not the theme store id.

Deliverable: `../5.0.0.css`. At the user's subsequent request, the exact file was saved in GPO General settings → Design → Custom CSS for minky-store-one. The editor was initially empty (`admin-before.css`); the app confirmed “Settings saved”. The fresh storefront's `gpo-dynamic-css` now contains the entire deliverable unchanged, plus 1,907 characters of generated alignment CSS (30,841 characters total). `live-served-gpo-dynamic.css` records the applied artifact separately from the initial `served-gpo-dynamic.css`. The widget arrived after its asynchronous initial load; production checks below were performed after it appeared.

## Mappings

| Role | Native evidence / painted owner | GPO owner | Result / limitation |
| --- | --- | --- | --- |
| Option label | `variant-selects .product-form__label.h6.fw-500`, Jost 500, 20px desktop / 16px mobile, letter-spacing `--letter-spacing-h6` | `.gpo-label .label-content` | Same fonts and responsive theme variables in the isolated fixture. |
| Select and custom dropdown trigger | `variant-selects .select` paints border through `::after`; its select is 56px and has 1px margins, making the wrapper 58px. Mobile: 50px child / 52px wrapper. Black `--color-foreground`, white `--color-background`, 40px radius; caret is 10×6 at 16px from the outside edge | `.gpo-select`, `.gpo-dropdown .dropdown-button`; inner select subtracts wrapper borders | Native storefront measurements and exact saved CSS fixture agree at 1440×1000 and 390×844. |
| Select focus | `.product-form__input--dropdown:focus-within .select__select`: 2px outline, 3px offset, white separation and grey shadow | Wrapper `:focus-within` / expanded dropdown trigger | Visible in fixture screenshots; no layout size changes. |
| Text / phone / dimension | Generic `.field__input` in native base.css: 4.5rem plus 1px margins; `.field::after` owns border | `.gpo-input-wrap`, `.gpo-dimension-input-wrap` | 47px outer / 45px inner verified in fixture. This is an asset-based mapping, not a native product text field measured on the store. Phone retains inline country-code padding. Country-list ancestor has visible overflow. |
| Textarea | `.text-area`: at least 10rem, `--textarea-radius` | `.gpo-textarea` | Captured GPO rows retained; two-line value and vertical resize verified in fixture. Height is not forced to the single-line input height. |
| Button swatch | `.product-form__input--pill input + label` in variant-picker asset: 1.55rem × 2.4rem padding, `--f-size-text-sm`, 500 weight, 0.1rem spacing, selected black/white | `.gpo-swatches.buttons input + label` | Asset-based mapping. Native pills not rendered in main product. GPO fixture default/selection sampled; inline font previews remain intact. |
| Color / image swatch | `.swatch-input__label .swatch` in swatch assets: circle, hover 2px translucent outline, selected 1px foreground outline, 4px offset | Color/image label and inner swatch | Asset-based mapping. Existing configured GPO image/color size retained. No native main-product swatch rendered. |
| Quantity | `quantity-input.quantity`, 202px wide; outer height `--button-height + 2 × --inputs-border-width`, 56px desktop / 50px mobile; 45px buttons | `.gpo-ov-quantity`, `.gpo-quantity__input` | Exact outer heights and option stepper width verified in fixture. Preserve GPO's inactive quantity opacity and pointer behavior. Single quantity keeps its configured width. |
| Upload action | `.product-form__submit.button--outline`, 56/50px, 11px outer radius; hover theme button colors/radius | `.gpo-dropzone__action` | Default visual fixture check. Upload/remove request was not sent; uploaded and removal states are source-covered only. |
| Vertical tabs / disclosure | `.accordion summary`, 24px vertical padding, `.accordion__title` h6, round 24px plus/minus with 10×2px bars | `.gpo-tabs-vertical`; group border/heading | Asset-based mapping. Vertical tabs were not in captured GPO markup. Horizontal tabs use a documented theme-token fallback. |
| Checkbox, radio, switch, range | Theme color/font/border variables | Corresponding GPO rules | Token adaptations; no corresponding native product controls were available. |

## Dropdown effects

Native variants are browser-native `<select>` controls. The theme has no DOM list or CSS option-menu animation. Its caret is static. Browser/OS menu animation, option hover colors and keyboard popup rendering could not be measured through screenshots; the GPO custom list is explicitly a themed fallback. The override removes GPO's inherited 0.3s max-height transition and inherited caret rotation only for the custom dropdown list/caret. It uses immediate display none/block and theme colors; this is not a claim of identical OS popup rendering.

The isolated fixture uses captured storefront markup, native CSS/fonts, captured GPO base CSS and the exact saved deliverable. Fixture helpers toggle existing GPO classes and radio values. They do not reproduce or certify production app logic. Ordinary, image and font dropdowns were opened and selected at 390×844; all retained their selected values after blur. Display block/none, 0s list transition and static caret were observed. Trigger-close and outside-click close were also sampled at 1440×1000. Font family inline previews remain Roboto. Hover styles have source coverage; no visual hover exercise was available.

## Verification

- `syntax-validation.json`: tinycss2 parsed 127 rules with no syntax/declaration errors. Plain CSS, flat selectors and scoped tokens.
- Fixture viewport was explicitly checked after resize: 1440×1000 and 390×844. Document scroll width equalled viewport width at both sizes.
- At desktop/mobile, dropdowns match native outer heights 58/52px, text and dimension wrappers are 47px, quantities match native 56/50px.
- Input focus, button selection, multiline textarea, visible country-list ancestor overflow and quantity alignment were sampled. Screenshots and measurements are alongside this file.
- Native product input sizes were measured separately from GPO. Native selectors must exclude `.gpo-app`, because GPO option steppers reuse `.quantity__input` and `.quantity__button`.
- Original fixture-only limitations were superseded by the applied storefront checks below. Still not verified: conditional rules, OS popup hover/animation, upload/remove, absent color dropdown, vertical tabs, disabled/error states beyond preserved base behavior.

## Applied storefront verification

Tested the saved override at 1440×1000 and 390×844 using the production widget, without fixture helpers or CSS injection. `live-desktop.json`, `live-mobile.json` and `live-dropdown-effects.json` contain computed measurements; screenshots use the `live-` prefix.

- Native select wrappers and GPO select/dropdown triggers measured 58px desktop and 52px mobile. Native quantity and GPO option stepper measured 56px desktop and 50px mobile, with 202px width. Text wrappers remained 47px and textarea remained multiline (138px wrapper / 136px child).
- Ordinary, image and font dropdowns opened and selected successfully. Trigger-close and outside-click close worked; selected option_2 and Montserrat persisted after blur. Font previews retained their inline family, and the configured font picker changed the decorated text input to Montserrat.
- Dropdown lists used display block/none with no transition or animation; the 10×6px caret had no transform. Open lists remained within the viewport. Hover remains source/computed-style coverage rather than a visually exercised hover state.
- Native GPO select changed to option_2. Button option_2 and color swatch option_1 were selected through the live UI. The active option stepper changed 1 → 2 → 1 on both desktop and mobile; the inactive sibling remained 1. Horizontal tab selection changed to option_2.
- The phone country list opened without ancestor clipping. The textarea accepted two lines. At 390px the document scroll width was exactly 390px. The configured image preview intentionally uses `.gpo-dropdown-image-outside`; its separate thumbnail and narrower trigger were preserved.
- Test text was cleared after verification. No cart submission or upload was performed. No additional CSS correction was needed after the live checks.

## Learning proposal

Observed during discovery: a broad `product-info .quantity__input` query returned GPO's 28px inner stepper rather than the native 56px product quantity. The corrected selector was `quantity-input .quantity__input`. The captured GPO markup in `source.json` includes both shared class names.

Propose adding to `references/automation.md`, “Build the native-to-GPO map automatically”: **Exclude descendants of `.gpo-app` from native candidates, even when they reuse native class names such as `.quantity__input` or `.quantity__button`.** This explicit exclusion would prevent the misleading initial quantity measurement. It was verified against this Elixira product; no skill files were edited.
