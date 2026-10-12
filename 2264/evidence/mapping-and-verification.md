# Unicorn 5.0.0 / Cargo — theme store id 2264

Preview: https://gvvcbtr3u74z5f7w-69620498584.shopifypreview.com/products/vans-era-59-moroccan-geo-dress-blues

Theme identity is from the rendered Shopify.theme script: name Cargo, schema_name Unicorn, schema_version 5.0.0, theme_store_id 2264. Installed asset path /t/92/ is not the theme store id. Initial viewport 1598×933, variant 8 / blue.

## Mapping

| GPO role | Native evidence | Mapping |
| --- | --- | --- |
| Labels | `.product-form__input .form__label` | Inter heading, 600, h5 variables, 18px/23px observed; 1rem bottom margin |
| Selected value | `[data-selected-value]` | Accent RGB variable |
| Select/custom dropdown | `.select__select` in base-start.css | 5rem outer box; 1px input border, 8px variable radius; 14px/18px normal body font. Footbar is a separate 4rem override, excluded from main geometry. No main variant select rendered; geometry supported by same-theme source. |
| Text/dimension/phone | Ask a question dialog `.field__input` | 50px visible outer field, input colors/border/radius; 700 medium size. GPO has external labels so native floating-label padding is adapted. Native inputs currently compute Arial (browser default); the override deliberately inherits theme Inter. |
| Textarea | Dialog `.text-area.field__input` | 150px visible, 14px normal Inter, multiline; editable resize retained |
| Button swatches | `.swatch` + `.swatch__overlay` | 50px observed outer box, 16px vertical padding and 18px line-height; inset 2px border; selected dark outer and white inner 5px ring |
| Color/image swatches | `.swatches--square-picture .swatch` | Source radius and inset ring; keep GPO configured image dimensions |
| Quantity | Main `.quantity__input` + `.quantity__button` | 50px height, 128px outer stepper, circular 46px overlay buttons; GPO shared wrapper paints border instead of duplicating field border |
| Checkbox | `.styled-checkbox__checkmark` | 22px box, input colors and selected theme base fill, white check |
| Radio/switch/range | Theme color variables | Token adaptations, no corresponding rendered product control |
| Upload | Primary button tokens | Theme minimum height/padding/font/colors; native icon-dependent hover displacement is not reproduced |
| Horizontal tabs | `.tabs__button`/`.tabs__border` | 10px vertical padding, normal body type, active blue 4px underline |
| Vertical tabs/group | `.animated-dropdown__button` | Heading type, 2rem padding, native caret |

## Dropdown source evidence

Native `.animated-dropdown .animated-dropdown__dropdown` uses display:none/block; children transition opacity with `--dropdown-transition-duration` (400ms) and timing cubic-bezier(.215,.61,.355,1). Theme-select caret rests at -90deg and active state resets it. Native theme-select caret has no transition in computed style. Options use blue selected/hover text and a growing underline, not a colored background or checkmark. GPO base uses max-height expansion; override replaces that with display toggle and child opacity transitions, preserving list scrolling. Native CSS @starting-style and a discrete display transition keep the list rendered during the 400ms close fade. Observed open opacity 0.810926 while entering, close opacity 0 with display:block during exit, then settled display:none. Caret is static -90deg when closed and resets when open. Older browsers without discrete display transitions fall back to immediate closing.

## Verification

Final CSS parsed recursively (including media/starting-style) with tinycss2 and selectors checked with cssselect2: 124 selector rules, 484 declarations, no parse errors. Vendor browser pseudo-elements excluded from cssselect2's unsupported-pseudo validation.

Saved in Globo Settings → Design → Custom CSS for the widget. Reloading admin confirmed persistence. A newly opened preview loaded the entire override in #gpo-dynamic-css. The original user preview initially retained the old CSS; its stale state was not used to assess the saved match.

Verified actual 1440×1000 desktop and 390×844 mobile. Viewport override did not affect the pre-existing user tab; the agent-created preview tab reported the correct dimensions. Override reset at completion.

- Select/custom dropdown/text/phone/color/dimension wrappers and quantities: 50px. Textarea corrected from 152px to 150px outer height by subtracting wrapper borders.
- Mobile button swatches: two 170px columns, 50px height, matching native two-column source behavior. Page scrollWidth equals 390px; no GPO descendants cross viewport right edge.
- Ordinary/image/font dropdown opening, trigger close, selection and retained values exercised on desktop/mobile. Montserrat selected preview preserves its own font family. Source/computed coverage for hover; no live hover API available.
- Pointer text focus and keyboard Tab to textarea exercised; focus border blue, height unchanged. Multiline text value retains newline.
- Phone country list opened and closed; 200px menu inside viewport, unclipped.
- Radio, checkbox, switch, button/color swatch selection, quantity plus/minus, and rendered horizontal tab changes exercised. Native controls retain their appearance.
- File upload/removal not exercised because no disposable upload fixture was requested. Color dropdown, vertical tabs/group disclosure, disabled/error transitions not rendered or not activated; stylesheet/source coverage only.

A final screenshot exposed GPO option quantity buttons inheriting native `.quantity__button { margin-top: -2.3rem }`. Setting margin:0 in the GPO quantity-button rule corrected the vertical position. Mobile proof: outer 128×50px, both buttons 46×46px and inset 2px from the outer top/bottom. Increment to 2 and desktop decrement to 1 verified after the final saved override loaded.

## Learning proposal

Add a Unicorn 5.0.0 / Cargo case to `.agents/skills/match-theme/references/theme-cases.md`: GPO reuses `.quantity__button`, so native negative centering margins can survive an otherwise scoped position override. When transferring geometry to a shared bordered GPO wrapper, reset native margin-top and verify both button rectangles lie within the 50px box. Evidence: final mobile screenshot and quantity-correction.json; source in native-base-extended.css. This avoids repeated manual quantity alignment fixes. This case is theme-specific; no skill files changed.
