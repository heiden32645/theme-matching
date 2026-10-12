# Zenith 1.5.3 / 3872

Matched on 2026-10-05 for:
https://ruy2ky1e88xng26a-69620498584.shopifypreview.com/products/vans-era-59-moroccan-geo-dress-blues

Theme identity came from the storefront's Shopify.theme script. Installed theme id 188912959640 and asset path /t/82/ are separate from theme store id 3872. The native variant remained Size 8 / Color blue.

The app's existing Match Shopify theme style setting was enabled. The Custom CSS editor was empty before this change. CSS was saved through that editor on the requested Shopify admin page; a copy read back through the editor matched 1.5.3.css exactly, and the Save button was absent after saving. The exact final deliverable is present inside served-gpo-dynamic.css. No separate minified override was generated.

## Native mappings

| Component | Native evidence | Mapping / coverage |
| --- | --- | --- |
| App typography | Theme body variables | Archivo, body family/style/weight, scale and line height; colors remain theme variables. |
| Labels / selected values | ProductInfo legend.product-form__group-name.body-small and its span | 12px label, weight 600, 6px bottom gap; selected value weight 400. |
| Buttons / product links | ProductInfo .product-form__controls-group label and checked/hover rules | 32px outer height, button font 12px/500, 1px border, radius 4px, 10px gaps. Selected black/white; unselected theme secondary background. Native and GPO boxes observed at desktop and mobile. |
| Color / image swatches | Visible .variant-swatch--portrait and .variant-swatch-value | 50x66px outer box, 48x64px inner color/image, 4px radius. Selected border uses theme foreground. |
| Select / dropdown / font dropdown | Native section-main-product.css .product-parameters .dropdown-select__current and .select-label | 4.4rem outer box, 14px body value, 1px theme border, radius min(input radius, 8px). Native dropdown was absent during the October 5 match; it was visible and directly inspected during the October 6 correction. GPO outer height verified 44px. |
| Dropdown arrow / options | Observed .icon-caret SVG; .dropdown-select__options and option labels from theme CSS | 18px caret, 1.5 stroke; list gap 4px, no shadow, 14px values. Ordinary, image and font dropdown selection exercised. |
| Text / dimension / phone / color | base.css .field .field__input and .text-area | 44px outer / 42px inner field, 12px text, theme border/radius. The theme uses floating labels; GPO keeps external labels and centers its value. Textarea outer min-height 100px and multiline behavior retained. Prefix/suffix align with the 42px inner field. |
| Quantity | base.css .quantity / .quantity__button / .quantity__input | Supported asset mapping, native quantity absent on this product. Borderless 24px height; 24px action buttons. Both GPO quantity roles observed; plus action updates selected swatch quantity from 1 to 2. |
| Checkbox / radio | base.css .field--checkbox | Checkbox 14px border and 8px round selected dot; round radio is a theme-color adaptation. Pointer checked states exercised. GPO hides these inputs in its base CSS, so their keyboard focus state was not verified. |
| File upload | Theme input colors; .button--primary / .button--secondary | Initial dropzone and action verified visually. No actual file was uploaded; uploading, successful file card and removal states untested. |
| Switch / range | Theme foreground/background/border tokens | No native product equivalent. Pointer switch and keyboard range update exercised. |
| Horizontal tabs | Variant button mapping | Supported fallback; no native horizontal tabs on this product. GPO tab selection changes active panel. |
| Vertical tabs / group | .product-accordion__toggle | Styles provided from inspected native accordion typography. Vertical GPO tabs and disclosure group not rendered here; their expanded state untested. |

## Observed checks

- Syntax parser: all final rules parse as flat CSS, no invalid declaration or nesting, every generated token is defined and used.
- Desktop 1440x1000: exact final override loaded; native size/color controls retained their measured geometry. GPO select, all dropdown buttons, text/phone/color/dimension wrappers 44px; button swatches 32px; color/image swatches 50x66px; option and single quantities 24px.
- Dropdown opens and retains option_2 after blur; native select accepts option_1; image dropdown accepts option_1.
- Pointer text focus and keyboard Tab into textarea show the native foreground border without changing field height. Two textarea lines remain intact.
- Font dropdown Oswald updates the target text input to Oswald. Separate font button previews retain Roboto/Open Sans/Montserrat/Poppins/Oswald; no blanket font reset replaces them.
- Button selection keeps 32px height. Radio, checkbox and switch change state; range advances from 0 to 1 with ArrowRight. Horizontal tabs activate the requested panel.
- Phone menu opens outside its input wrapper without clipping on desktop and mobile. Native color picker popup opens and is visually visible; no color was committed.
- Mobile 390x844: page scroll width 375px (scrollbar), GPO app width 345px, no GPO element extends beyond the viewport. Dropdown list stays within x=20..355. Country menu stays within viewport. Mobile field focus and swatch selection exercised.
- Actual early measurements were 1219x963 and 1838x907 because viewport overrides on already claimed tabs affected a different selected tab. The stated 1440x1000 and 390x844 checks were subsequently performed in a fresh verification tab and confirmed with innerWidth/innerHeight.

## Correction and possible skill addition

GPO's two-color .swatch-bottom is a zero-content border triangle, not a rectangular color tile. Setting its width/height to 100% broke the second color after changing the swatch to the native portrait size. The final correction retains zero content dimensions, sets border-bottom-width to 64px and border-left-width to 48px via rem formulas, and preserves inline border colors. The mobile screenshot confirms the diagonal fills the 48x64px inner swatch.

A concrete addition to match-theme/references/theme-cases.md would document this Zenith mapping and direct future matches to resize .swatch-bottom border widths rather than its content box when native swatches have a different aspect ratio. This avoids repeating the two-color correction. Verified on Zenith 1.5.3 with this portrait setting; broader theme/configuration validation remains pending. The skill was not changed.

The verification tab viewport was reset and the temporary tab closed. The existing preview was reloaded with the final override. An earlier 1440x1000 override on the admin tab remained; native Chrome interaction to focus/reset that tab was refused because the user was actively interacting with Chrome. No further native UI attempt was made.

## Dropdown effect correction — 2026-10-06

The visible native variant dropdown uses display:none when closed and display:block when open. Its list has a zero-duration transition and the caret does not rotate. GPO's base list instead retains a 0.3s transition on max-height and other properties; this remained in the first override and caused the reported effect mismatch.

The correction explicitly hides the collapsed GPO list, displays the expanded list immediately, and resets the list transition to none. Ordinary, image, color and font dropdown selectors retain the native 30rem maximum height. Option backgrounds retain their 0.3s hover transition. The selected checkmark SVG now uses the native path M5 9.5L8 12.5L13 6. No other mappings changed.

- Saved through Custom CSS for the widget. The original editor content matched the previous local version before updating; the updated editor content matched the deliverable exactly after saving.
- The exact corrected deliverable is included in the live #gpo-dynamic-css style. All 128 rules and declarations pass the CSS parser; every generated token is defined and used.
- Desktop 1440x1000 and mobile 390x844: ordinary, image and font lists have display:block when expanded, display:none when collapsed, transition:none, and unchanged 44px buttons and static carets. All open lists remain within the viewport.
- Button-close, outside-click close, and value selection were exercised. Image option selection and Oswald/Poppins font selection continue to work; the font previews retain their own families. No color dropdown exists on this product, so that specialized selector is covered by source inspection only.
- Evidence: dropdown-effect-before.json, dropdown-effect-correction.json, dropdown-corrected-desktop.jpg and dropdown-corrected-mobile.jpg. Temporary viewport sizing was reset after the responsive checks in the new browser session.

A useful addition to match-theme/references/theme-cases.md would record Zenith's immediate list opening and closing, and require checking GPO's inherited max-height transition when the theme uses display:none/block. This is a proposed skill improvement only; the skill was not edited.
