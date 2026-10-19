# Fullframe 1.1.0 — Florence / theme store id 3530

Inspected 2026-10-16. Installed Shopify theme id 189339205784; asset directory /t/41/ is not the theme store id. Product variant 47372797509784 (9.5–13 / white).

Product: https://hiwlja3cd5c994uf-69620498584.shopifypreview.com/products/vans-apparel-and-accessories-classic-super-no-show-socks-3-pack-white

## Integration

- Deliverable: ../1.1.0.css, plain CSS, scoped to GPO.
- The existing Custom CSS editor was empty. “Match Shopify theme style” was already enabled and was preserved.
- Main override was saved through Settings → Design → Custom CSS. A fresh product tab served it in `style#gpo-dynamic-css`; copy retained in served-gpo-dynamic.css.
- The final local revision additionally sets `.gpo-app .gpo-input-prefix svg { fill: currentColor; }` to correct a black prefix icon on the dark field. This one rule is NOT in the served copy. The application became blank after reloading its admin iframe. Reload, a fresh tab, opening the app from the sidebar, and the embedded app URL did not restore the editor. No API or DOM injection was used to bypass the UI.
- Initial product tab retained an old dynamic stylesheet immediately after save. A fresh product tab confirmed the saved CSS; the initial absence was a caching/loading finding, not a failed CSS match.

## Mapping

Theme variables resolve inside the GPO product section: foreground 221,209,202; background 4,43,53; border 74,99,105; primary button 227,200,198; primary button text 50,26,26. Body family Poppins; action text uses the heading family Arapey. Relative sizes and theme scale variables are preserved.

| GPO role | Native source | Result / status |
| --- | --- | --- |
| Option label | `.xo-product-variant__inner-name`, including product wrapper opacity .7 | 14px, weight 500, 19.88px line height; muted foreground. Native observed. |
| Button swatch | `.xo-field-radio--boxed .xo-field-radio__label` | 32px at 1440px and 390px; matching selected foreground/background. Source retains 992–1399px padding change. |
| Native select | `.xo-field-select__select` | 56px, 29px radius, half-opacity border. Source mapping; no native variant select rendered on socks page. |
| Custom dropdown | `.xo-field-select-custom__trigger` in theme CSS | 55.3px = 15px × 1.42 + 32px padding + 2px border; 12px radius. Product geometry is a source mapping, not measured against a rendered product dropdown. |
| Dropdown effects | Collection sort dropdown using same component | Open/close observed; native fade-up, 300ms, translateY(50px), hidden opacity 0; caret rotates 180° in .5s. GPO uses opacity/transform transitions rather than base max-height expansion. Collection has separate borderless sort styling; that styling was not copied to product triggers. Native easing `decay` is approximated with cubic-bezier(0,0,.3,1). |
| Text / dimension / phone / color | `.xo-field-input` and `.xo-field-input__input` | Outer wrappers 56px, children 54px. Product does not render equivalent ordinary text fields; mapping comes from assets. Body font applied intentionally for GPO consistency. |
| Textarea | `.xo-field-textarea` / `__textarea` | Bottom border, transparent surface, multiline vertical resize preserved. Asset mapping. |
| Single quantity | Complete `.xo-quantity--md` | 40px outer height, 28px radius. Body font adaptation; native quantity input itself computes Arial. |
| Option stepper | `.xo-quantity--md`, `__number`, `__button` | 150 × 40px outer box; 28px buttons; selection gating from GPO preserved. |
| Color / image swatch | `.xo-field-color__item` / `__fill` | Round swatch and 1px selected outline, from assets. GPO selected outline uses button color as palette adaptation, rather than deriving arbitrary swatch colors. |
| Radio / checkbox | `.xo-field-radio`, `.xo-field-checkbox` | Source mapping: round radio; square checkbox with rounded corners and button palette. |
| File upload | Theme field tokens, `.xo-btn--primary` / `__content` | Upload surface adapted; action uses theme button palette, radius and heading font. No native upload counterpart. Hover colors have source coverage; native slide-up text animation is not reproduced. |
| Range | `.xo-field-price__range` | Accent track and outlined thumb from theme assets. |
| Horizontal tabs | Theme text/border tokens | GPO tabs render and switch; native horizontal tabs absent, so palette adaptation only. |
| Vertical tabs / group | `.xo-collapse__trigger` | Border, heading and plus/minus source adaptation. GPO vertical tabs and disclosure group header are absent in this option set. |
| Switch | Theme field/button palette | Adaptation; native equivalent absent. |

## Verification

Actual CSS viewports: desktop 1440×1000, mobile 390×844. User-owned tabs initially ignored viewport overrides; measurements there were recorded as 1837px desktop, never relabeled mobile. A separate agent-created product tab accepted the requested viewport sizes.

- Syntax and selector checks: tinycss2 + cssselect2; browser pseudo-elements allowed explicitly. See syntax-validation.json.
- Served override identity verified; measured winning declarations for select, dropdown, text, phone, quantity and button swatches.
- Native and GPO pill height 32px at desktop and mobile. Single quantity and option stepper 40px. Text wrapper 56px / inner input 54px. Custom dropdown 55.296875px.
- No page overflow at 1440px. At 390px the document layout width is 375px (scrollbar present); sampled GPO inputs and triggers stay within the viewport.
- Ordinary dropdown: open, trigger-close, outside-click close, select option_2 and retain value after blur. Native select changed to option_2.
- Image dropdown: open/select on desktop and mobile; option_2 then option_3 retained.
- Font dropdown: Montserrat on desktop, Open Sans on mobile; the selected value's inline font family remains intact.
- Text and textarea: text retained after blur; two textarea lines retained; textarea stays about 109.6px tall. Focus outline does not alter the 56px field geometry. Tab from text reaches textarea.
- Button swatch selection changes to option_2 without height changes.
- Phone country menu opens on mobile; measured bounds left 17px/right 225.93px, height 200px; wrapper overflow visible. Escape closes it.
- Hover appearance inspected in source, not exercised by a browser hover API. Error/disabled states not rendered; upload/remove not exercised (no disposable upload fixture). Color popup, switch/range interaction, stepper increment, and vertical tabs were not functionally exercised.
- Tests modified values only in the temporary product tab; no cart submission or product content change.

## Learning review

No skill update proposed. The skill already requires measuring painted wrappers, distinguishing quantity roles, verifying real viewport sizes and separating served CSS from the local deliverable. The observed findings are retained here for a later requested update.

## Requested select / quantity correction (2026-10-16)

The user requested less rounding on Select and smaller option/single quantity controls. The current product now renders `.xo-product-info-content__variant .xo-field-select-custom__trigger`, measured at 55.296875px high with a 12px radius. Existing GPO Select had a 29px radius. Measurements are retained in before-size-correction.json.

Updated local `../1.1.0.css`:
- Select radius uses its own `--gpo-theme-select-radius: 1.2rem`, preserving the 29px text-field radius.
- Shared compact quantity height: 3.2rem (32px at the inspected root size), reduced from 4rem.
- Option quantity: width 11rem (110px), 24px buttons, 14px icons/type, and smaller padding.
- Single quantity: width 8rem (80px), height/min-height 32px, 14px type, smaller padding.
- Existing behavior and disabled selection gating remain unchanged.

CSS parsed successfully: 120 rules, 489 declarations, no errors. The GPO app iframe remains blank in a fresh admin tab, so this correction is LOCAL ONLY and has not been saved to GPO or visually verified after application. Existing served copy is retained separately. The prior final prefix-icon correction is also still local only.
