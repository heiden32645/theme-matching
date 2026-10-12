# Soul 5.1.0 — mapping and verification

Date: 2026-10-08 (Asia/Ho_Chi_Minh).
Product: https://minky-store-one.myshopify.com/products/vans-era-59-moroccan-geo-dress-blues
Admin: https://admin.shopify.com/store/minky-store-one/apps/globo-product-options/admin/settings/general
Identity: Shopify.theme script reports Soul, schema_version 5.1.0, theme_store_id 2825, installed id 189001924760, role demo. The asset path /t/87/ is not the theme store id.
Editable deliverable: ../5.1.0.css. Integration: GPO Design > Custom CSS for the widget, existing Match Shopify theme style enabled. Prior custom CSS was Elixira 5.0.0 and is backed up in admin-before.css. The unchanged design settings are not used as native evidence.

## Mapping

| Role | Native evidence | Result and status |
| --- | --- | --- |
| App typography | --font-body-family, --font-body-style, --font-body-weight; --color-foreground and --color-background are complete colors | Tenor Sans and inherited theme scheme tokens. Verified live. |
| Label | variant-radios legend.form__label.t-capitalize.f-w-semibold | 18px, weight 600, 27px line height, .04rem letter spacing. Verified live. Selected value uses body-md 16px. |
| Button swatches | .product-form__input > input + label | 59px painted height, padding 2rem 1.8rem 1.9rem, 1px border and square radius. Hover scale overlay and selected inversion from native assets. Native and GPO selected geometry observed on desktop/mobile. |
| Color/image swatches | .swatch-input__label and native color-swatch pseudo-element | Square corners, 4px spacing and expanding selected frame. Preserve option set inline image/color sizes and diagonal two-color swatches. Selected color frame verified. Image default/selected behavior has source coverage plus default visual inspection. |
| Option quantity | main [id^="Quantity-Form"] quantity-input.quantity; .quantity__button::after | 34px, borderless wrapper, independent outlined plus/minus buttons; 169px nominal width. Verified geometry and mobile increase to 2. |
| Single quantity | .quantity__input geometry | 34px height, 18px mobile / 20px desktop value size. Standalone bordered adaptation because native page renders a full stepper. |
| Select/custom dropdown | .product-form__input--dropdown .select__select and .select::after in native assets | Asset fallback: inner 6rem + two 1px margins gives 62px painted select. Exclude sticky-cart select (different geometry). GPO measured 62px desktop/mobile. Main product renders radios, so native variant select opening/closing could not be observed. |
| Dropdown menu/effect | Browser-native select adaptation; fixed .select .icon-caret transform from assets | GPO list opens/closes immediately, static caret, option selection and marker visible. Ordinary, image and font dropdowns selected on desktop/mobile; retained values after blur; Poppins/Open Sans previews preserve font family. Trigger close and desktop outside click verified. Native OS menu animation and hover are unverified; menu styling is an explicitly documented fallback. |
| Text/phone/dimension | .field__input native base assets and painted .field::after | Asset fallback: 62px mobile / 72px desktop. Field label reserves 4rem above the field in native markup; this is not part of painted input height. GPO wrapper owns one border, input fills remaining height. Live geometry, text typing, dimension input, prefix/suffix alignment and pointer/keyboard focus verified. |
| Textarea | native .text-area assets | 140px multiline child, 142px GPO outer wrapper. Focus retains multiline geometry. |
| Focus/hover | .field__input:focus and --focused-base-box-shadow; .field:hover::after | Theme shadow on focused wrapper, additional painted 1px on hover without geometry changes. Verified live text and keyboard textarea focus. |
| Phone country menu | GPO phone base and theme input tokens | Visible wrapper overflow; menu opens within viewport on desktop and mobile. |
| Upload action | .product-form__submit.button--primary.button--gradient source | Theme action geometry/typography, ancestor color scheme adaptation; native submit can use its own narrower color scheme. Default action inspected. No file uploaded. |
| Checkbox/radio/switch/range | Theme-token adaptations | No native product counterparts. Live checked state, checkbox checkmark, switch value and keyboard slider value verified on desktop. |
| Tabs | .product-tabs .tabs .tab-title; .toggle-title .toggleLink | Horizontal bordered tabs and animated 4px active underline; selection verified desktop/mobile. Native font breakpoints 22/26/30px. GPO uses narrower padding minimum of 2rem for the product column. Vertical version is asset-derived and absent from supplied fixture. |
| Groups | .accordion summary source | Responsive padding 1.68/2.28/4.1rem and .44 foreground borders. Not rendered on supplied storefront. |

## Verification

CSS parsed using css-tree: 140 flat scoped rules and 566 declarations. No preprocessors or nested selectors.
Desktop actual viewport 1598×933, mobile actual viewport 390×844. The viewport override did not affect the original claimed user tab; a new temporary tab received the override, and innerWidth/innerHeight were checked before recording mobile results. Overrides reset afterward.
Mobile document scrollWidth was 390px. No rendered GPO descendants exceeded the viewport, including swatches, option steppers, dimension fields, menus and tabs. Desktop default and selected native controls retained their appearance.
The exact saved deliverable was verified inside #gpo-dynamic-css; served stylesheet saved separately. This is GPO widget integration, not publishing or purchasing the trial Shopify theme.

Limitations: no main native variant dropdown is rendered; native OS dropdown effects are not certified. Native text fields rely on inspected source fallback. No file upload/removal fixture, GPO vertical tabs or group rendered states, or rendered error/disabled field test. Default upload styles and native unavailable/disabled styles have source coverage only. The supplied Contact page was blocked by the browser; existing theme field assets provided the fallback.

## Learning review proposal

Add a Soul 5.1.0 / 2825 case to .agents/skills/match-theme/references/theme-cases.md: its main quantity wrapper has no border, while each .quantity__button::after paints its own 1px border; the main stepper is 34px, independently of the 62px select and 62/72px text field. This live/source mapping avoids repeating investigation and incorrectly copying a full wrapper border or field height onto Soul quantity controls. The case should also note the native .field's 4rem label reservation above the painted input. Verified on this configuration at desktop/mobile; inspect again if theme settings/version change. No skill file was edited for this request.

## Choose file and switch follow-up

The user requested the full Soul button effect and removal of switch border radii. The previous override had lift/glow but omitted the native outlineIn/outlineOut keyframes. The corrected action reuses those inspected native animations at 1.5s, cubic-bezier(.19,1,.22,1), with a 5px upward transform and native inner/outer glow. A separate inset 1px edge remains visible while the animated outline fades. Focus is applied via .gpo-dropzone:focus-within because the visible action is a div and the file input is the interactive control.

The transparent .gpo-dropzone__input covers the visible action. Hover is therefore on .gpo-dropzone, with animation on its child action. A pointer drag starting on nearby empty space and ending over the action exercised hover without opening a chooser or uploading a file. Live computed values confirmed outlineOut, translateY(-5px), 13.5px outline offset partway through animation, and native glow. Exiting hover restored outlineIn and no transform. Screenshots: button-switch-corrected-desktop.png and button-switch-corrected-mobile.png.

The base GPO switch has a 60px label radius, 50px track radius and 100% thumb radius; the initial Soul file reset only the track. All three are now explicitly 0. Checked and unchecked desktop states retained their behavior; checked mobile state at actual 390x844 remained square, with document scrollWidth 390. The exact updated CSS was verified in #gpo-dynamic-css. Prior CSS backed up in before-button-switch-correction.css and admin-before-button-switch-correction.css. See button-switch-correction.json for observed values.

Learning review: the existing skill already requires inspection of painted parts and interaction behavior. This correction is covered by those instructions; preserve the concrete file-input hover ownership and switch pseudo-element evidence here for future theme-case reuse. No skill files changed.

## Choose file black/white hover follow-up

The user requested a black background and white text on hover. The existing parent hover rule now uses background #000 and color #fff, preserving the Soul outlineOut animation, glow and 5px lift. The exact saved source was verified in #gpo-dynamic-css. Live pointer hover confirmed rgb(0, 0, 0) background and rgb(255, 255, 255) text. CSS parses without errors: 140 rules, 566 declarations. See choose-file-black-white-hover.json and choose-file-black-white-hover.png. Prior local and admin CSS are backed up separately. The existing skill covers this explicit color preference; no new skill instruction is needed.
