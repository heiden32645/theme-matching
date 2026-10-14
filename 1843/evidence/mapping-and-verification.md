# Kairo 3.0.0 — theme store id 1843

Matched on 2026-10-12 to the supplied Vans Era preview. Installed theme id 189165699224; asset path `/t/30/` is not the theme store id. Identity was read from the rendered Shopify.theme script.

Preview: https://ahewj9gf6h3ut29l-69620498584.shopifypreview.com/products/vans-era-59-moroccan-geo-dress-blues
Admin: https://admin.shopify.com/store/minky-store-one/apps/globo-product-options/admin/settings/general

Deliverable: `../3.0.0.css`. Saved into Globo Design > Custom CSS; Match Shopify theme style was already enabled. Previous Custom CSS was empty. The served `#gpo-dynamic-css` contains the exact final file plus GPO alignment settings; recorded separately in `served-gpo-dynamic.css`. No theme publication was performed.

| GPO role | Native evidence | Mapping / status |
| --- | --- | --- |
| Labels / values | `fieldset.product-form__input .form__label` | Dosis, 1.3rem, weight 700, 0.04rem tracking, 8px label gap; supporting text uses theme body colors |
| Button swatches / product links | `.ml_variants_label` | 48px painted box at scale 1, 16px padding, 8px radius, accent border and selected fill; verified rendered |
| Color swatches | `.ml_color_swatches input + label` and `::after` | 44px box, 8px radius, 38px inset gray selected ring with 11px radius; rendered selection verified |
| Image swatches | Color-swatch box adaptation | No native image swatch on supplied product; same theme box, preserving GPO images and tooltips |
| Select / custom dropdown | `.select__select` in base.css; live `#SortBy` on `/collections/all` | 4.5rem painted field, inputs radius, 1px theme border, 1.2rem value text; product variant dropdown absent, mapping supported by common source |
| Dropdown caret | `.select .icon-caret`, live `#SortBy + svg` | 10x6 SVG, static on open; suppressed GPO's `display:contents !important` icon to avoid duplicate triangles |
| Dropdown list | Browser-native select has no theme-authored list animation | Immediate GPO list opening and closing, static caret; custom menu colors are an explicit theme-token adaptation. OS option popup appearance is not claimed pixel-identical |
| Text / textarea | Live `#ContactForm-name`, `#ContactForm-body` on `/pages/contact` | 45px text painted field with 4px radius, textarea stays auto height and multiline; native field wrapper adds 1px margin outside the 45px painted input |
| Dimension / prefix / suffix / phone / color | `.ml_textfield` plus GPO decorated wrappers | 45px outer field; border only on wrapper; phone and color popups retain visible overflow; verified rendered |
| Single quantity | Product `quantity-input.quantity .quantity__input` | 50px box, compiled 8px radius, #ebebeb border, Arial 14px weight 500, opacity .85; verified |
| Option quantity | Native quantity's 50px field and 44px plus/minus buttons | Wrapper paints one border, buttons made static to override Kairo's absolute `.quantity__button` positioning; increment from 1 to 2 verified |
| Checkbox / radio | `.recipient-form .ml_check_box` source | Checkbox 4px corners and accent border; radio is documented token adaptation |
| Upload action | `.ml_button.button_primary`, live Contact Send | 50px action, 16px/32px padding, accent fill, 8px corners; visual appearance verified. Upload, uploading and removal states not exercised without a disposable fixture |
| Group / vertical tabs | `ml-collider .ml_collider_opener` | Accent .1 background, heading font, 20px/16px padding, rotating disclosure caret; GPO disclosure header/vertical tabs absent in supplied option set, source mapping only |
| Horizontal tabs | Variant-pill token adaptation | Active tab and corresponding panel changed correctly on interaction |
| Switch / range | Theme-token adaptation | Checked switch and range keyboard increment verified; no identical native switch/range claimed |

Verification used the exact served CSS at actual 1440×1000 and 390×844 viewports in the in-app browser. Initial Chrome resize requests left its preview at 1838×963, so those requests were not counted as mobile coverage. Theme and GPO loaded before measurements.

- CSS parser and selector/declaration checks pass; no nested rules, undefined generated tokens or unused generated tokens.
- Normal, image and font dropdowns open, select, close and retain values after blur. Trigger-close and outside-close verified; caret stays static and list transition is none. Font labels retain Roboto/Open Sans/Montserrat/Poppins/Oswald rather than being reset to Dosis.
- Native select and GPO select/text painted heights are 45px; variant button/GPO button heights are 48px; quantity boxes are 50px with 44px buttons.
- Text focus keeps 45px geometry and changes border to accent. Keyboard Tab moves from Text to Textarea. Three textarea lines retained after blur.
- Phone country menu stays within the narrow viewport; decorated input and dimension alignment checked. Color-picker popup inspected on desktop.
- Mobile page has no horizontal overflow. GPO controls remain within their container; product-link labels wrap within available width.
- Swatch selection, option quantity increment, tabs, switch and range interaction pass. Native product controls retain their original styles.
- Hover rules were inspected in source/computed styles; pointer-hover states were not exercised with an unavailable hover API. No disabled/error fixture, uploaded file, GPO vertical tabs or disclosure header was available, so those states are not marked passed.

Evidence: `native-measurements.json`, `native-input-focus.json`, `focus-and-values.json`, `desktop-metrics.json`, `mobile-metrics.json`, `dropdown-checks.json`, `mobile-checks.json`, `syntax-validation.json`, and screenshots. Source styles are in the same directory.

## Double-color correction

The initial audit missed a visual regression in dual-color swatches. `.swatch-top` was expanded to 44px, while `.swatch-bottom` retained its inline 32px border triangle; the shared reset also rounded the triangle itself. This made the second color appear as a small rounded wedge. The correction uses one 44px token for the wrapper and both triangle border widths, preserves the inline color and transparent left border, and leaves rounding only on the outer clipped wrapper.

Saved to the same local CSS and Globo Custom CSS. The current admin CSS was read and matched the previous local file before replacement. The final served CSS contains the exact corrected deliverable. Parser checks pass. Verified selected double color at desktop 1838×963 and mobile 390×844: wrapper 44×44, triangle border widths 44px, triangle radius 0, selected ring retained, mobile no horizontal overflow. Single-color and image swatches remain visually intact. Evidence is in `double-color-correction-desktop.json`, `double-color-correction-mobile.json`, `double-color-fixed.png` and `double-color-fixed-mobile.png`.

Learning proposal for `references/automation.md`, native-to-GPO mapping and verification: when resizing color swatches, explicitly inspect and exercise a dual-color example. Border-drawn color halves must share the outer swatch dimensions; preserve their inline border colors and transparent borders, and apply corner clipping on the outer wrapper. This would catch the demonstrated 44px/32px mismatch and interior rounding before delivery. Verified for Kairo 3.0.0 with this GPO markup; other multicolor implementations still need inspection. The skill itself has not been edited.
