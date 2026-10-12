# Epitome 1.2.0 / Daydream — GPO match

Product: https://2rogq9v8fuekv7wo-69620498584.shopifypreview.com/products/vans-era-59-moroccan-geo-dress-blues

Settings: https://admin.shopify.com/store/minky-store-one/apps/globo-product-options/admin/settings/general

Verified Shopify.theme: schema_name Epitome, schema_version 1.2.0, preset/name Daydream, theme_store_id 4693, installed id 189040001176, role demo. `/t/90/` is the installed asset path, not the theme store id. The prior custom CSS was Lyra 1.0.9 / 3533; its exact editor backup is `admin-before.css`.

## Mapping

| GPO role | Native evidence | Result / qualification |
| --- | --- | --- |
| Main type | Body variables | Instrument Sans 14px, 1.6 line height; secondary text 12px |
| Labels | `.product-form__group-name.subtitle` | Jost 14px / 16.8px, weight 500, muted color, -0.28px letter spacing |
| Button options | `.product-form__controls-group input + label` | 27.195px outer height, 4px 6px padding, no border or radius, black selected background |
| Color/image swatches | `.color-swatch.swatch_size-standard` and its pseudos | 24×24 painted swatch, 24×29 outer box, bottom selected underline. Image uses the same geometry as a documented adaptation |
| Quantity | Main product `.quantity` | 100×36px including border, 30px buttons, 12px value. Option quantity was corrected from 122px to 100px; final loaded measurement confirms 100×36 |
| Select/custom dropdown | `.product-parameters .select__select`, `.dropdown-select .select-label`, `ul.active` source | 36px field; 1px input border/background, square corners. Native dropdown is not rendered on this product, so this is source-based matching |
| Dropdown effect | `.dropdown-select ul` / `ul.active` and caret source | Open max-height 0.2s ease-in; close has no list transition; caret rotates 180deg; selected/hover option background uses color-border at 40%. Live native timing unavailable |
| Text, prefix/suffix, phone, color, dimension | `.field input[type=text]` source | 34px outer field, 3px radius, body font; theme variables. No rendered native text/contact form was available |
| Textarea | `.field textarea` source | Multiline, minimum 10rem, 1rem 1.6rem padding. GPO rows preserved |
| Upload action | Native primary `.button` source | 36px, Jost 10px, weight 600, uppercase, 0.6px tracking; primary foreground/background and diagonal overlay |
| Group / vertical tabs | `.about__accordion-toggle` source | 12px vertical padding, subtitle type, theme divider color |
| Horizontal tabs | Product option pill adaptation | Same palette and text geometry, preserving tab behavior |
| Checkbox | `.field--checkbox` source | 14px square, theme foreground border and check |
| Radio, switch, range | Theme-token adaptation | No matching native rendered counterpart; retain GPO functionality |

## Applied and verified

- Saved in GPO Settings → Design → Custom CSS. Existing “Match Shopify theme style” remains enabled. No theme publish action was performed.
- Final served `#gpo-dynamic-css` contains the exact deliverable CSS. Snapshot saved separately as `served-gpo-dynamic.css`.
- CSS parser: 126 rules, no syntax errors, no unused/undefined generated tokens, all selectors scoped to GPO. See `syntax-validation.json`.
- Desktop measurements: initially 1598×933; final 1598×877 after browser toolbar changes. Final record is `final-desktop-metrics.json`.
- Mobile actual viewport: iPhone SE 375×667, confirmed using innerWidth/innerHeight; document width 375, GPO outer width 345 with controls inside it; no visible descendant horizontal overflow. Mobile measurements and screenshot were taken before the final option-quantity reduction to 100px, which was subsequently verified on desktop and reduces the required width.
- Exercised desktop plain dropdown opening/trigger closing/selection, image dropdown opening/selection/image loading, font dropdown opening/selection/distinct font previews. Open caret settled at 180 degrees; opening transition computed 0.2s ease-in and closed list height 0 with no transition.
- Native select choice, phone country-menu opening/Escape, text entry with suffix, multiline textarea, radio/checkbox/switch choices, selected swatch quantity increase 1→2 and decrease 2→1, and tab switch were exercised. Test entries were cleared by reload after verification.
- Final screenshots: `desktop-final.png` (open dropdown), `desktop-final-closed.png` (default), `mobile-fields.png` (mobile fields).

## Limits

- Mobile layout was visually verified; dropdown interactions in touch emulation could not be reliably exercised because browser input commands timed out. Desktop interaction checks passed after restoring normal mode and reloading. Temporary viewport override and native device toolbar were reset.
- Hover was inspected in source/CSS rather than exercised with a supported hover action. No rendered native dropdown was available to compare its animation live.
- Upload/remove were not exercised with an uploaded fixture. No error/disabled states, color dropdown, vertical-tab variant, or disclosure group were rendered in the supplied option set; their CSS is source-based coverage, not a passed storefront test.

## Learning review

The skill already covers the observed wrapper/pseudo-element geometry, source-only fallback, quantity roles, served-vs-editor CSS distinction, and mobile viewport confirmation. No additional general instruction is proposed from this match.
