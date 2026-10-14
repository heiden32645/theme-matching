# Snazzy 1.3.1 / 4141 — Snugly

Matched on 2026-10-13. Preview: https://ngapk3a2ogd3p9ay-69620498584.shopifypreview.com/products/vans-era-59-moroccan-geo-dress-blues

Shopify script identifies schema_name Snazzy, schema_version 1.3.1, theme_store_id 4141, installed theme name Snugly, installed theme id 189209903256, demo role. Product variant: 8 / blue. The `/t/33/` CDN path is not the theme store id.

Deliverable: `4141/1.3.1.css`. Saved in GPO Settings > Design > Custom CSS. Match Shopify theme style remains enabled. The initial editor was empty, while the initial served dynamic style contained a Megastore 1.1.1 / 3562 override. After saving, the served stylesheet contains a single Snazzy header and the exact trimmed deliverable. No separate minified output was created. Previous served CSS and the initial blank custom CSS are retained here.

## Mapping

| GPO role | Native evidence | Mapping / status |
| --- | --- | --- |
| Labels | `legend.product-variant-picker-from_label` | Assistant; 14px, weight 500, 0.42px letter spacing, uppercase, 16px bottom spacing. Observed. |
| Button swatch | `.font-product-form__input--pill input + label` | 44px desktop / 36px mobile, 14px value, 20px line height, 11px/7px vertical padding, `--btn-style-rds-four`, theme button color variables. Observed selected state. |
| Select/custom/image/font dropdown | `.snzz-variant-select .select__select` in theme assets | Asset fallback; native variant select not rendered on this product. 18px value, 10px 20px padding, 10px theme radius. Explicit 52px outer box and 30px line height are an adaptation, not a measured native select. Theme 24px caret shape inspected. |
| Text/textarea/phone/dimension | Contact page `#ContactForm-name`, `#ContactForm-body` | Observed contact input 63px, Assistant 16px, padding 20px 24px, 1px foreground border, `--btn-style-rds-three`. GPO wrapper owns border; inner field 61px. Multiline textarea retains flexible height and resize. |
| Single / option quantity | Product `quantity-input.quantity` | Observed 56px desktop / 48px mobile, secondary background, 10px radius, borderless inner parts. Option stepper width 188px like native container; plus/minus remain functional. |
| Color/image swatches | `.swatch` / `.swatch-input__input:checked + .swatch-input__label .swatch:after` | Asset mapping, round configurable swatches and 1px foreground ring 2px outside the GPO borderless swatch. Native color swatches not rendered on this product. |
| File action | `.product-form__submit.buy-buttons-font-form__submit` | Observed 56px desktop button, Oswald 14px/700 uppercase, padding 13px 25px, button color variables and 10px radius. Upload/remove state not exercised. |
| Checkbox/radio/switch/range | Theme foreground/background variables | Adaptation; corresponding native controls not rendered. Choice state, switch toggle and range keyboard input exercised. |
| Horizontal tabs | `snazzy-tab .snazzy-tab-button` | Theme asset mapping: body font, secondary button colors, round corners, responsive padding and size. GPO active tab switches successfully. |
| Vertical tabs/group | `.accordion summary`, `.main-product-font-accordion-title` | Asset mapping; these GPO controls are absent from supplied product. Not visually exercised. |

## Verification

- CSS parsed with tinycss2: 109 rules, no syntax errors, undefined or unused generated tokens; all selectors scoped to GPO.
- Actual DOM viewports checked: 1440×1000 desktop and 390×844 mobile. The initial browser viewport helper did not change `innerWidth`; CDP emulation was used and cleared after checks.
- Native and GPO pills: 44px desktop / 36px mobile. Native and GPO quantity: 56px desktop / 48px mobile. GPO input wrappers: 63px. Select/custom dropdown: 52px supported asset adaptation.
- Select and custom dropdown choices retained their values after blur; expanded and collapsed dropdown observed. Collapsed list returns to 0px after its transition.
- Image dropdown selected a value and displayed its outside thumbnail. Font picker selected Open Sans; per-option inline font samples remain intact.
- Text and textarea accepted values including two lines; keyboard Tab focus gave the textarea wrapper the visible 1px foreground shadow without changing geometry.
- Swatch selection, radio, checkbox, switch, range ArrowRight, and active horizontal tab verified. A selected color swatch's plus button changed quantity from 1 to 2.
- Suffix `px` repaired with nonshrinking inline flex and nowrap. Country menu repaired from about 69px to 320px with a viewport limit; opens outside the phone wrapper.
- Mobile: no sampled GPO input, textarea, dropdown button or option stepper exceeds viewport width; document scrollWidth 375px at innerWidth 390px.
- Upload/remove and drag/drop, hover, error states and absent group/vertical tabs were not exercised. No file was uploaded and no cart submission was made.
- Latest served CSS includes the exact trimmed deliverable and one match header. Admin save bar disappeared after save. No theme publication was performed.

## Đề xuất cải thiện skill

Quan sát: editor Ace của Custom CSS dùng textarea nhập tạm; gọi `fill()` lần tiếp theo có thể nối CSS vào vị trí con trỏ (đã thấy 1811 dòng). Chọn toàn bộ bằng Ctrl+A, Backspace rồi nhập bản cuối đưa editor về 913 dòng ở bản cuối; stylesheet cuối có đúng một header và khớp nội dung file.

Đề xuất cho `references/automation.md`, phần Generate and integrate: khi dùng editor Ace, chọn toàn bộ tài liệu trước khi thay CSS và kiểm tra số header cùng nội dung stylesheet sau khi Save hoàn tất. Việc này tránh lưu nhiều bản override cạnh tranh. Đã xác minh ở settings hiện tại; cần thử editor khác trước khi mở rộng thành quy tắc chung.

Quan sát theme: Snazzy dùng `--font-family-body`, `--font-family-heading`, `--color-secondary-background` và các token `--btn-style-rds-*`; preset Snugly có geometry riêng cho pill/input/quantity. Có thể ghi mapping này vào `references/theme-cases.md` để lần sau không nhầm với các theme dùng tên biến tương tự. Một cấu hình theme thứ hai vẫn cần kiểm tra trước khi khái quát các hằng số geometry.


## Product Links correction

The wrapper .gpo-pdLinks--item and its inner label both painted 1px borders and 11px 25px padding, producing a 68px outer box around a 44px label. Removed the wrapper from the button/hover/mobile geometry rules and reset only its border, padding, margin, minimum height, background and shadow. The inner label continues to use the shared button swatch rules.
