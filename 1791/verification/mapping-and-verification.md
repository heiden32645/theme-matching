# Handmade 2.5.2 / Aroma — GPO match

Verified on 2026-10-09 (Asia/Ho_Chi_Minh).

Product preview: https://k288u19n9gu8vmub-69620498584.shopifypreview.com/products/vans-era-59-moroccan-geo-dress-blues

Theme identity came from the rendered Shopify script: schema_name Handmade, schema_version 2.5.2, name Aroma, theme_store_id 1791, installed theme id 189039902872. The `/t/89/` asset segment is an installed asset identifier.

Editable deliverable: `../2.5.2.css`. Integrated through GPO Settings → Design → Custom CSS for the widget. Match Shopify theme style remained enabled. The initial preview had an Epitome 1.2.0 / Daydream override; the admin editor was empty. The original served style is preserved in discovery.json. No theme was published.

## Native mappings

| Component | Native evidence | Result / coverage |
| --- | --- | --- |
| Labels | `.product-form__group-name` | Instrument Sans 11px / 16.5px, weight from `--font-button-weight`, uppercase, .075em tracking. Measured same on desktop and mobile. |
| Button choices | `.product-form__controls-group label` | 50px high, 20px horizontal padding, square joined borders, brown text. Selected/hover changes the border and color without solid fill. Selection exercised desktop; title remains 24px tall after wrap correction. |
| Select / dropdown trigger | `.product .select__select` in section-main-product.css, shared select base.css | Source mapping: 5rem, 12px/18px, weight 400, transparent, .3rem radius, 1px input border, 15px/40px padding. The product renders pills, so a native variant select and its platform popup were not visually exercised. GPO painted wrapper 50px / inner select 48px. |
| Arrow | `.select .icon-caret` and rendered SVG | Actual 10×15 viewBox ornament, displayed 12×15px at right 2rem. Static for the native select; static GPO trigger. |
| Custom lists | Theme select tokens plus explicit fallback | The native control is an OS select with no theme custom popup. Immediate list display, static arrow and token-based option colors are a documented fallback, not an observed native animation match. Ordinary/image/font GPO dropdowns opened and selected correctly on desktop. Trigger close and actual outside click exercised. |
| Text / phone / dimension | Visible Contact `main .field__input` | Measured 50px, 3px radius, 12px/18px Instrument Sans 500, .4px tracking, 15px padding. GPO 50px bordered wrapper with 48px inner input; text prefix/suffix aligned. Keyboard-focus placeholder rule follows native source. |
| Textarea | Visible Contact `main .text-area.field__input` | Native 170px, 12px padding; GPO 168px inner + 2 border pixels. Multiline value retained desktop. |
| Option quantity | `.quantity`, `.quantity__button`, `.quantity__input` | Native 50px buttons with full borders, central input with top/bottom borders; no wrapper border. GPO retains separate painted parts, 50px. Increment 1 → 2 exercised desktop, unselected options remain disabled by GPO. |
| Single quantity | `.quantity__input` | 50px, Arial 14px/normal, centered. A full border replaces the absent adjacent buttons. |
| Color swatches | `.product-form__controls-group label.color-swatch` source | 32px circular ring, 15px painted color. Inline GPO dimensions overridden only for this mapping. Color selection exercised desktop. Native color variant is a text pill in this product, so source coverage only. |
| Image swatches | `.variant-swatch--image` source | 50×66px square image; foreground border when selected. GPO selection exercised desktop; native image variant absent. |
| Upload action | Contact `.button` | 50px primary action, 2px radius, uppercase 11px/700, actual theme font variables and sliding dark hover layer. Rendered idle state inspected. Upload/remove/loading untested; no disposable upload fixture supplied. |
| Group / tabs | `.product__additional-title` colors/underline plus heading tokens | Compact `--font-heading-h5-size` adaptation, not a claim of matching the large product disclosure heading geometry. Horizontal tabs exercised desktop. Group and vertical tab controls absent from product. |
| Checkbox / radio / switch / range | Theme input border, background, accent | Token adaptations. Checkbox/radio selection exercised. Switch/range styled; no corresponding native product controls. |

## Verification

- tinycss2 parsed all 129 rules, checked scoped selectors, declaration syntax, and 16 used custom tokens. No errors.
- Desktop actual viewport: 1598×877. A requested browser viewport override did not change the actual page; no 1440px claim is made.
- Mobile actual viewport: 390×844, established with native Chrome responsive UI and confirmed from DOM. Page scrollWidth = 390; no GPO element crossed the viewport horizontally.
- Desktop: ordinary/image/font dropdown opening and selection, ordinary trigger-close and outside-close, retained text, multiline textarea, country list open/close, button/color/image selection, option stepper, checkbox/radio and horizontal tabs.
- Font picker button retained inline Montserrat preview font.
- The final short-option wrap correction changed `.gpo-ov-title > span` from theme `.break-word` behavior to normal word breaking; observed height fell from 48px to 24px inside a stable 50px button.
- Mobile layout and measurements were checked. Automated pointer interactions in responsive emulation were unreliable: commands either timed out or completed without changing choice state. These are not counted as passed mobile interaction tests. Native desktop interaction worked again after closing responsive DevTools.
- Browser viewport overrides were reset and DevTools closed before handoff. No cart submission or order created.
- The final settings save completed (no unsaved/loading/save bar). After a fresh storefront reload, the served override contains the exact final local CSS (28,807 characters); the old Epitome override is absent. The served style is preserved separately as served-gpo-dynamic.css. Final screenshot: final-desktop-fields.png.

## Learning review

Useful proposed addition to `.agents/skills/match-theme/references/theme-cases.md`: add a Handmade 2.5.2 / Aroma case documenting separately painted quantity-button / central-input borders, and short GPO button title wrapping caused by `.break-word` inside a flex label. The latter had a measured 48px title reduced to 24px with normal word breaking while preserving the 50px control. Keep this exception theme-specific; validate longer labels before adopting it as a general rule. This would avoid repeating the quantity-border investigation and manual short-label correction.
