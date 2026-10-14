# Poetic 1.6.0 — Lunara preset

Shopify theme metadata in the preview's inline script identifies schema_name Poetic, schema_version 1.6.0, theme_store_id 3867, installed theme 189211312280, role demo. The asset path /t/34/ is an installed-theme path, not the store id.

Product: https://l0989lxdurn3lu9c-69620498584.shopifypreview.com/products/vans-era-59-moroccan-geo-dress-blues

Native variant: Size 8, Color blue, variant 47372774342808. Text-input comparison: the same preview's /pages/contact.

Editable deliverable: ../1.6.0.css. Integration: GPO Settings → Design → Custom CSS. Match Shopify theme style was already enabled. The pre-existing Custom CSS was Snazzy 1.3.1; it is backed up in ../custom-css-before.txt. Previous served styles are separately recorded in ../previous-gpo-dynamic.css. No theme was published.

| GPO component | Native evidence | Mapping / coverage |
| --- | --- | --- |
| Labels and selected values | .product__variant_picker .form__label-title / .form__label-value | Anonymous Pro, normal case, selected value weight 600. Font 16px desktop / 14px mobile. |
| Button swatches | .product-variant-item input + label | 36px desktop, 30px mobile, --buttons-radius 30px, dark selected fill and page-background text. Observed in both viewports. |
| Color and image swatches | variant-selector.css .variant-swatch / .swatch | Source fallback: circular inner shape and 1px selected ring offset 2px. Native swatch type is not displayed on this product. Configured GPO image sizes preserved. |
| Select / custom dropdown | .product__variant_picker insp-dropdown details summary | Source fallback: 46px, 14px horizontal inset, --content-container-radius, 16px rendered caret on a 24px SVG viewBox. The initial inspection used hidden markup; the follow-up preview renders the native dropdowns and confirms these measurements. |
| Dropdown list | .dropdown-menu / .selector-item | Theme page background, 10px item radius, 44px desktop / 52px mobile rows, subtle hover/selected fills. GPO remains an anchored list on mobile to preserve its existing interaction model. |
| Text / phone / dimension | #ContactForm .form__group / .form__field | Outer bottom border owns geometry: 33px desktop / 30px mobile. 8px bottom padding; inner field 24px / 21px. Native variables --font-size-base and --font-body-scale retained. Prefix and suffix stay within the field. |
| Textarea | #ContactForm textarea | Four lines, 105px desktop / 93px mobile outer wrapper. Multiline input retained. |
| Option quantity | Product .quantity / .quantity__input / .quantity__button | 50px outer box, 173px width, 30px radius, separate borderless parts. Selection and plus button tested. |
| Single quantity | Product quantity shell | Supported shell adaptation without plus/minus; 50px, 30px radius. Number entry tested. |
| Radio / checkbox | theme-settings.css .form__group-radio / .form__group-checkbox | 24px radio with 0.55 inner dot; 18px checkbox with 4px radius. Selection tested. Native counterparts are source mappings. |
| Upload action | Product .btn-add-to-cart.button--secondary | 50px outline action, Jost, --buttons-radius, theme button colors. File upload and removal were not exercised. |
| Switch / range | Theme text and page-background tokens | Adaptations; switching and range ArrowRight tested. No native switch/range rendered for an exact visual comparison. |
| Horizontal tabs | theme-settings.css tabs-element .tab-title | Source mapping to underline-active tabs; tab child typography explicitly inherits to beat the theme heading declarations. Tab switching tested. |
| Group / vertical tabs | .accordion | Source fallback to heading typography, bottom line and caret; these GPO layouts are not rendered on this test product. |

Final served CSS matched the deliverable after normalizing CRLF/LF line endings. Verification used actual 1440×1000 and 390×844 viewports. Final measurements are in final-desktop.json and final-mobile.json; earlier measurement files record the investigation before the responsive-font correction. At 390px document scrollWidth was 390 and no visible non-absolute GPO child exceeded the viewport. Font samples retain Roboto, Open Sans, Montserrat, Poppins and Oswald after overriding the theme body * / .font-body * rule on descendants. Open Sans selection was retained. Regular dropdown and image dropdown both retained option_2 after blur. Select retained option_3. Text and a two-line textarea accepted input. Switch, checkbox and radio selection, option stepper increment 1 → 2, single quantity 3, horizontal tab change and range 0 → 1 were observed. Phone country menu opened by keyboard and stayed unclipped. Keyboard focus on text used the theme's 2px blue outline without changing its outer height.

The browser can read transient states during GPO initialization and smooth scrolling. State and selection were verified after a subsequent observation; temporary zero-height lists were not recorded as final results. Browser cache was disabled temporarily for reloads and restored afterward.

No disposable upload fixture was used, so upload/remove states are untested. Disabled/error and hover states were not comprehensively exercised. Source fallbacks are explicitly identified above; they are not claimed as painted matches against hidden native controls.

Learning review: the theme applies body * typography to font-picker children and heading typography to tab text. Both required explicit inheritance on the relevant descendants. The current skill already covers preserving font previews and checking actual painted geometry, so no duplicate skill rule is proposed.

## Select / dropdown icon correction

The follow-up storefront renders the native variant dropdown. Its SVG has width/height attributes of 24, but the winning `insp-dropdown details summary .icon-caret` rule paints a 16×16px icon and uses `transition: transform 0.5s`. The initial override incorrectly used the intrinsic SVG dimensions. Corrected only the GPO select/dropdown arrow dimensions and rotation transition; the existing SVG path, 0.55 foreground alpha and 14px inner edge inset are unchanged. Native and GPO icons now both measure 16×16px at 1440×1000 and 390×844. Native outer edge distance is 15px; GPO uses a 14px inset plus its 1px border. Native icon is vertically centered and GPO uses translateY(-50%). Open dropdown rotation reached 180 degrees, and option_2 remained selected after closing. See icon-before.json, icon-desktop.json, icon-mobile.json and icon-desktop.png.

Learning review: measure the computed SVG size rather than trusting width/height attributes. This is already covered by the skill's painted-geometry inspection rule, so no duplicate instruction is proposed.

## Image swatch and selected-value correction

The preview's loaded product-card.css declares the global `.swatch-image` class as `display: none; position: absolute; top: 0; left: 0; width: 100%; height: 100%`. This collides with GPO's image class, initially hiding the image; restoring display alone still leaves a zero-width label because the absolute image cannot size its ancestors. Added a scoped GPO image reset for both display:block and position:static. Configured inline image dimensions remain unchanged. Both images now load (naturalWidth 90) and paint at 60×60px, with a 60×60px clickable label and a selected 1px ring offset 2px.

Before correction the selected-value box began 12.734px beyond the label: 8.734px HTML whitespace plus a 4px margin. Native `.form__label-value` starts immediately after the label and supplies only the `: ` prefix. Groups with a visible selected value now use wrapping flex layout so inter-element whitespace creates no gap; the value margin has no left inset. Other group children retain a full-width row. Selected values for radio, button and image swatch have zero horizontal gap and aligned top positions at 1440×1000 and 390×844. Mobile document width remains 390px with no observed GPO overflow. Image selection was changed from option_1 to option_2 and the correct ring/value were observed.

Evidence: swatch-spacing-before.json, swatch-spacing-desktop.json, swatch-spacing-mobile.json, swatch-spacing-mobile.png. The pre-change Custom CSS is separately backed up as custom-css-before-swatch-spacing-fix.css. Final CSS syntax validation passed and the served stylesheet matches the deliverable. Learning review: these are specific winning-declaration and spacing findings, already covered by the skill's cascade/painted-geometry verification rules; no duplicate general instruction is proposed.

## Dropdown animation correction — 2026-10-14

The user clarified that Select needs no animation change. All temporary select `:open` rules were removed and its previous focus styling restored. Final editable CSS and the served custom CSS match (normalized FNV-1a 199077625); Shopify displayed “Settings saved”.

Native `global.js` Dropdown toggles the details `open` attribute immediately. Native base CSS declares opacity/transform transitions but supplies no alternate values; live opening showed opacity 1, transform none, animation none. The menu therefore appears/disappears immediately. Only the caret rotates over 0.5s. GPO instead inherited `transition: .3s` while animating max-height 0 to 450px/480px. The scoped override now uses display none/block and transition none on the list. Existing max-height, scrolling, stacking and image/font behavior are retained. Option hover uses the inspected native `background-color var(--duration-short) ease` (0.1s). Hover appearance was covered by source/computed style, not a pointer-hover interaction.

Verified on the actual desktop viewport 1838×907: regular dropdown opening and trigger closing, image dropdown outside-click closing, regular/image option_2 retained, Open Sans font selection retained and all five font previews preserved. Caret rotation reached 180 degrees and retained transform 0.5s. Final CSS parses without errors (128 rules; all scoped; all tokens used). Evidence: animation-final-desktop.jpg / .json; pre-change backup: custom-css-before-animation-fix.css.

Mobile interaction was not verified in this follow-up: the browser viewport capability applied to the admin tab while the product viewport remained 1838×907, so attempted widths were not treated as mobile results. Temporary overrides were reset. The existing mobile anchored-list layout was retained. No new general skill instruction is proposed: the current dropdown-effects workflow already requires inspecting actual transitions and native open/close behavior.

## Blue outline and compact option quantities — 2026-10-14

User requested removal of the blue hover border and smaller `.gpo-ov-quantity`. Live inspection identifies the blue line as the theme `:focus-visible` outline (rgba(21,156,228,.9), 2px), reproduced on the GPO text wrapper. Suppressed the inherited outline inside GPO and removed the four explicit blue wrapper/label outlines. Selected swatch rings remain. This is an intentional user appearance override of the prior native-focus mapping.

The option stepper now measures 110×34px instead of 173×50px, with 20px buttons, 14px numerals and 3px/8px padding. A separate option quantity height token keeps the product quantity and standalone GPO quantity at 50px. Verified plus 1→2 and minus 2→1, no outline on the focused text field/wrapper or option quantity button. CSS parser passed (129 rules); saved/served CSS exactly matches `../1.6.0.css`. Actual verification viewport 1838×907; mobile and pointer-hover states were not exercised in this correction. Evidence: compact-quantity.jpg / .json; backup: custom-css-before-compact-quantity.css.

## Compact standalone quantity — 2026-10-14

User requested a shorter `.gpo-app .gpo-quantity .gpo-quantity__input`. Changed its dedicated height token from 50px to 34px, set the height explicitly and reduced vertical padding from 9px to 4px. Typography, width and option stepper remain as previously configured. Backup: custom-css-before-single-quantity.css. CSS parser passed (129 scoped rules, no errors). Live results are recorded in single-quantity.json / .jpg.
