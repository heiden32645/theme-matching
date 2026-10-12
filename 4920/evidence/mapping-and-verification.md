# GenZ / Gravity 1.1.6

Matched on 2026-10-06 using the match-theme skill. Theme store ID: 4920; Shopify theme ID: 188956508312; preview assets: `/t/85/`.

Preview: https://6e1n3938ctsuty60-69620498584.shopifypreview.com/products/vans-era-59-moroccan-geo-dress-blues

The app Custom CSS field was initially blank (`admin-before.css`). The new `../1.1.6.css` was pasted into that field and saved through the Shopify app UI, which displayed “Settings saved”. The existing Match Shopify Theme setting was retained. After reload, `served-gpo-dynamic.css` contains the exact complete override, with additional generated app settings preceding it. No theme files or option definitions were edited.

## Native mappings

| GPO control | Native evidence and resulting mapping |
| --- | --- |
| Typography / label | Urbanist, weight 500; `.main_product_options_header .h6`: 16px, line-height 25.6px |
| Button options | `.main_product_option_values_wrapper label`: 30px outer height, olive 1px border, 5px radius; selected black background and white text |
| Image swatches | `.swatch_label.square.use_variant_image`: 40px outer box, 3px padding, 1px border, 32px inner image, 5px radius |
| Quantity stepper | `.main_product_quantity_wrapper .quantity_inner`: 122 × 42px; 40px inner controls; square border and dividers |
| Single quantity | Native quantity input role: 40px tall, 16px text |
| Select / dropdown | `.main_product_select select` in product CSS: 4rem (40px), square olive border, 1rem inset; full-width GPO layout retained |
| Text / phone / color / dimension | Contact page `.main_contact_form_wrapper .input_field_wrapper`: 50px outer height, 1px bottom olive border, 10px radius, gray inner field. Native input: 49px, 12px text, 10px padding |
| Textarea | Native multiline input family, vertical resize; GPO's configured rows retained (106.34px outer box), rather than forcing single-line height |
| Focus | Browser focus ring as observed on native contact input; final GPO keyboard focus computes `rgb(0, 95, 204) auto 1px` |
| File action | `.btn`: 2px border, 10px radius, 14px heading font, theme primary/secondary colors and 0.3s color transitions |
| Group / vertical tabs | `.main_product_collapsible_tab_wrapper`: 1px olive separators, 15px 5px header padding, responsive 20–24px heading; native arrow with 180-degree expanded rotation |
| Checkbox / radio / switch / range / horizontal tabs | Theme token adaptations, because corresponding rendered native product controls were absent |

Root variables supply text, background, olive border, input gray, fonts, radii, and action colors. The malformed native `--color-input-border` value was not used. Native snapshots and CSS assets are kept in this directory.

## Verification

Desktop 1440 × 1000 and mobile 390 × 844 were verified against the actual browser viewport. No horizontal page overflow was observed. Final screenshots: `final-preview.png` and `final-mobile.png`; final measurements: `final-geometry.json` and `final-mobile.json`.

Dropdown, image dropdown, and font dropdown were opened, closed through their triggers, and selected. The ordinary dropdown also closed on outside click. Values and image thumbnails remained intact; the list opens immediately (`display: block`, transition 0s), closes to `display: none`, and the caret remains static. Native select selection also worked. The native variant select is absent from this product's rendered form, so its source mapping and the custom-list/caret fallback are explicitly identified in CSS comments; no native OS-list animation equivalence is claimed.

Radio, checkbox, button option, image/color swatch, switch, range keyboard input, single quantity, option stepper, dimension entry, multiline textarea, font selection, and horizontal tab selection were exercised. The phone menu opened and selected Australia (+61); the color picker opened and accepted a color. Five font samples retain their own font families, including the inner spans. Earlier desktop state checks are in `final-desktop.json`; their black focus outline predates the final focus-color correction, which is verified in `final-mobile.json`.

On mobile, the country list originally inherited the 69.85px flag-trigger width. It now measures 350px, from x=14 to x=364, inside the 390px viewport. The decorated text suffix is 33.35 × 49px, `white-space: nowrap`, with no shrinking; “px” stays on one line. These corrections were checked after saving and reloading.

The final file parses as 111 CSS rules with zero syntax errors, undefined tokens, or unused generated tokens (`syntax-validation.json`). Hover styling was compared with native source rules, but visual pointer-hover checks were unavailable. Uploaded-file/remove states were not exercised because there was no authorized disposable upload fixture. Group and vertical-tab adapters were source-based and not rendered on this product. Disabled/error states were not induced.

## Learning proposal

Product Links follow-up (2026-10-06): the shared button rule also targeted `.gpo-pdLinks--item.buttons`, while its nested label matched `.gpo-swatches.buttons input + label`. Both painted a 1px border and 10px horizontal padding. Removed the wrapper from the default and hover selector groups; the label remains the sole painted control. After saving and reloading, all three wrappers compute border 0 and padding 0, labels retain a single olive 1px border, and outer height is 30px. Verified at the default desktop viewport and 390 × 844 mobile with no overflow. Evidence: `product-links-before.json`, `product-links-after.json`, `product-links-mobile.json`, and `product-links-corrected.png`. Product-link destinations were preserved; selection/navigation was not triggered for this border-only correction. The existing skill already instructs inspecting painted parents and avoiding double borders, so this correction needs no new general skill rule.

Add a Gravity 1.1.6 case to `.agents/skills/match-theme/references/theme-cases.md`: its global `span { font-family: var(--font-body-family) }` overrides the font picker's child preview spans even when the label has the selected font inline. Add the scoped rule `.gpo-app .gpo-font-picker label > span { font-family: inherit; }`, and verify each inner span's computed font. This was verified for Roboto, Open Sans, Montserrat, Poppins, and Oswald. Recording the exact cascade exception would avoid repeating the font investigation on this theme. Keep this theme-specific until another theme reproduces the same cause. No skill files were changed by this match.
