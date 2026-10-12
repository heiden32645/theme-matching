# Creative 9.2.0 — GPO match

Verified 2026-10-05. Product: https://4ihaj9kf1c0g9pcl-69620498584.shopifypreview.com/products/vans-apparel-and-accessories-classic-super-no-show-socks-3-pack-white

Theme identity comes from the rendered Shopify theme script: Creative, schema version 9.2.0, theme store ID 1829, installed theme ID 188810756248, trial/demo role. The theme asset path `/t/76/` is an installed asset path, not the theme store ID.

Deliverable: `../9.2.0.css`. Integration: Globo Settings → Design → Additional → Custom CSS for the widget. The editor was originally empty. CSS was saved through the UI; the final storefront CSS includes the exact deliverable inside `style#gpo-dynamic-css`. The base “Match Shopify theme style” setting remains checked. The embedded admin preview does not supply Creative’s theme tokens; storefront appearance is the visual reference.

## Native mappings

| Component | Source and painted box | GPO mapping | Verification |
| --- | --- | --- | --- |
| App/body | `--font--body`, body weight/style, size and line-height variables | `.gpo-app` | Work Sans, 13.6px body in this configuration |
| Labels | `.product-form__swatch__title`, configurable product-form heading formula | `.gpo-label .label-content` | Both 14.5714px with 20.57px line-height |
| Variant buttons | `.product-form__swatch__item--button .product-form__swatch__label`, 2rem high, 18px horizontal padding, `--radius-variant` | `.gpo-swatches.buttons input + label` | Both 27.1953px; checked state retains height, transparent background, dark border and soft shadow |
| Color swatches | `.product-form__swatch__label__graphic`, 22px circle; selected label paints the outer ring | `.gpo-swatches.color-swatches` | 22px circles, two-color triangle scales without replacing colors; selected ring applied |
| Image swatches | Native swatch shape/ring; no separate image control on this product | `.gpo-swatches.image-swatches` | Ring/shape adaptation; retain configured 60px thumbnails |
| Select / dropdown | Theme asset `.selector-wrapper select`, 48px, text-lightest border, `--radius-form`, radius-aware `max(12px, radius / 1.5)` padding; native variant select is absent on supplied product | `.gpo-select`, `.gpo-dropdown .dropdown-button` | Both GPO outer boxes 48px. Supported asset mapping; no storefront-measured native dropdown claim |
| Arrow | Theme asset `.selector-wrapper::after`, sb-icons U+E915, 13px | Select/dropdown pseudo-element | Rendered theme glyph; base GPO icon suppressed |
| Text / dimension / phone / color | Theme generic form input assets, 48px, 22px line-height; wrapper owns GPO border | Input and dimension wrappers | 48px outer / 46px inner; prefix/suffix fit; phone’s dynamic inline dial-code padding preserved |
| Textarea | Theme textarea assets, multiline, min-height 120px, line-height 1.5 | 118px inner + 2px wrapper | Two lines retained, 120px outer |
| Option quantity | `quantity-input`, 2rem children, 1px wrapper border; 2rem buttons, 2.5rem inner field | `.gpo-ov-quantity` | Native and GPO 29.1953px outer; plus changes 1 → 2 |
| Single quantity | No separate native single bordered field; adapt native stepper outer border/height, preserve GPO width | `.gpo-quantity__input` | 29.1953px outer; 100px GPO input width |
| Checkbox | Asset `.collection-sidebar__link__box`, 16px content + 2px border, round; selected fill and 700 text | GPO checkbox pseudo-elements / checked labels | Checked state works; final checked font weight verified separately |
| Radio / switch / range | No corresponding native product controls; theme text, border and background tokens | GPO controls | Selected radio, switch and slider 0 → 1 with 1% progress observed |
| Upload action | Product `.c-btn--hollow`, 48px, button typography, inset border, button radius | `.gpo-dropzone__action`, remove adaptation | Action appearance rendered; file upload/remove interaction untested |
| Horizontal tabs | Asset `tab-triggers button`, active underline | GPO horizontal tabs | Second tab activates and panel remains visible |
| Vertical tabs / disclosure group | Product `accordion-group summary`, plus icon and dividing lines | GPO vertical tabs/group | CSS asset adaptation; these states are not rendered by supplied option set |

## Verification

- CSS parsed with tinycss2; declarations and top-level media rules checked; no nesting, duplicate rule selectors, undefined custom tokens or unused custom tokens.
- Desktop layout verified at actual 1440 × 1000; mobile layout verified at actual 390 × 844. On mobile `clientWidth = scrollWidth = 375` (scrollbar occupies 15px); sampled GPO controls remain within the viewport.
- Native select, custom dropdown and image dropdown opened/selected. Dropdown values remain after blur. Font dropdown preserves Roboto/Open Sans/Montserrat/Poppins/Oswald preview faces and selects Montserrat.
- Text input, multiline textarea, dimension input, pointer focus and keyboard Tab to textarea tested. When the theme enables keyboard focus, the ring is on the painted wrapper. GPO custom dropdowns and hidden swatch inputs inherit the app’s existing interaction/accessibility behavior; no claim of keyboard coverage for those controls.
- Phone country list opened at desktop and mobile with visible overflow; mobile list fits the viewport. Color picker opened on mobile, accepted #00ccff, and closed.
- Radio, checkbox, switch, range, button selection, color selection, quantity increment and horizontal tab activation tested. Button selection retained height. Native product controls retain their source geometry.
- File upload/removal, unrendered groups/vertical tabs, disabled/error states, tooltip hover and browser-specific Firefox behavior are untested.
- Temporary viewport override reset. User storefront reloaded to reset test selections; saved admin CSS remains available.

## Focus correction — 2026-10-05

- Native Size and Color selects are now rendered in the supplied preview. Native theme CSS suppresses outlines on fields while `body` lacks `js-using-tab`. Pressing Tab adds that class and exposes Chrome's blue `auto 1px -webkit-focus-ring-color` outline.
- The previous GPO wrapper focus rule added that ring whenever an input matched `:focus-visible`, including pointer focus. The corrected select, field, dimension, single quantity, phone flag and dropdown suggestion rules also require the theme's `body.js-using-tab` state. No independent fallback focus style was introduced.
- After a fresh reload, pointer focus on native select and GPO select/text/textarea/phone/dimension/quantity has no painted outline. Tab focus on native Color, GPO select and GPO textarea has the same blue outline. Borders and field heights remain unchanged.
- The theme's keyboard class remained present after a subsequent pointer click; GPO follows the same class rather than imposing a separate pointer/keyboard policy. A final reload and text-field click confirms the clean pointer state.
- Saved through the GPO Custom CSS editor; the storefront's dynamic style contains the exact updated deliverable. Measurements: `focus-correction.json`. Visual proof: `focus-pointer.jpg` and `focus-keyboard.jpg`.

## Learning proposal

Add a Creative row to `.agents/skills/match-theme/references/theme-cases.md`: fields/selects use 48px from assets, variant buttons use 2rem, and quantity wrappers use `calc(2rem + 2px)`. Reuse `--radius-form`, `--radius-variant`, body font variables, the product-heading formula and sb-icons U+E915. These mappings were checked on this unseen theme at desktop/mobile widths and would avoid repeating the same source inspection. A second theme-settings configuration is still needed before generalizing further.
