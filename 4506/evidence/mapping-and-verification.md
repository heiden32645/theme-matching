# Renovate 1.1.3 — Portrait

Kiểm tra ngày 16/10/2026. Theme schema: Renovate, version 1.1.3, theme store ID 4506; preset/title Portrait. Installed theme ID 189336912024, asset path t/40 (không phải theme store ID).

Sản phẩm: https://p34v0jniu6w8owqd-69620498584.shopifypreview.com/products/vans-era-59-moroccan-geo-dress-blues

Variant gốc khi đo: Size 8, Color blue. Layout sản phẩm: `.main_product_inner.horizontal`.

CSS chỉnh sửa: `../1.1.3.css`. Đã lưu toàn bộ vào GPO Settings → Design → Custom CSS; Match Shopify theme style giữ bật. Custom CSS trước đó trống. Bản storefront là inline dynamic stylesheet, lưu riêng tại `served-gpo-dynamic.css`; xác nhận chứa nguyên văn CSS cuối (`font-verification.json`). Không có bước bundle/minify tại workspace.

| Thành phần | Nguồn theme / phần vẽ | Ánh xạ và trạng thái |
| --- | --- | --- |
| Nhãn | `.product_options_header p strong` | Arimo qua `--font-heading-family`, 14px, 700; đối chiếu giao diện |
| Select / dropdown | `.product_select select` tự vẽ viền | Outer 30px, 1px rgb(118,118,118), radius 4px, font 13.3333px Roboto Mono, padding trái 7px; GPO wrapper vẽ viền, select con 28px; desktop/mobile đều 30px |
| Caret | `.product_select svg` | Khung 10px, cách phải 1rem, màu `--color-text`, giữ cố định khi mở |
| Dropdown list | Native HTML select dùng popup của trình duyệt/OS | GPO mở ngay, tắt transition 0.3s kế thừa, caret cố định; list/hover/selected dùng màu theme như fallback. Không xác nhận pixel hoặc màu hover popup OS vì ảnh không ghi được popup đó |
| Text / textarea | `.input_field_wrapper` trong styles.css, gift-card input/textarea trong main-product.css | Token outer 3.3rem, không viền, `--color-input-background`, text `--color-input-text`; body font cho gift-card. Fallback theo asset cùng theme, không gọi newsletter/footer 58px là native product field. Textarea giữ nhiều dòng, resize dọc |
| Button swatch | `.product_values_wrapper label:not(.swatch_label)` | Border 1px, padding 1rem 1.4rem, selected border màu text. Native pill không render trên sản phẩm này; mapping theo CSS gốc của layout ngang |
| Color/image swatch | `.swatch_label.circle` | Sizing from Globo settings; no width/height override on inner, swatch-top or swatch-image, and no border-width override on the two-color triangle. Selected outline 1px, offset 2px. Verified color 32px and image 60px match their inline settings. |
| Quantity | `.quantity_inner input / button` | Input 50×30px Arimo, button 30×30px radius 2px màu secondary-background, gap 10px; cả single quantity và option stepper 30px |
| Checkbox / radio | Gift-card checkbox `.giftcard_recipients_input_main_wrapper input` | 15px outline và inset fill; radio dùng cùng màu theme. Theo asset, radio là adaptation |
| Upload action | `.btn` / `.add_to_cart_btn` | Padding 1.1rem 2.9rem, border 2px, button variables và radius token; remove theo màu secondary action |
| Switch/range | Theme color variables | Adaptation theo màu theme vì không có control gốc tương ứng trên trang |
| Tabs/group | `.product_tabs_heading`, `.product_tabs_content` | Heading font, divider, active padding, nền secondary; horizontal tabs có tương tác đã thử. Vertical/group không render trong storefront, chưa xác nhận giao diện thực tế |
| Focus | styles.css `:focus-visible` | Outline 1px `--color-text`, offset 2px; wrapper giữ focus của ô nhập có prefix/suffix và phone |
| Font picker | Inline font trên label, `span` chịu global font của theme | Đã phát hiện label đúng nhưng span vẫn Roboto Mono; sửa span inherit cục bộ cho dropdown và button font picker; xác nhận cả 10 font label/span trùng nhau |

Đã kiểm tra storefront ở Chrome desktop 1837×907 và IAB desktop 1440×1000, mobile 390×844. Chrome viewport override không đổi innerWidth; không dùng lần thử đó làm bằng chứng mobile. Kiểm tra mobile thực hiện trong IAB riêng có innerWidth được xác nhận.

Các thao tác đã quan sát: mở/đóng dropdown bằng trigger, đóng bằng click ngoài, chọn option và giữ giá trị sau blur; dropdown ảnh giữ thumbnail, font dropdown giữ font; nhập text có prefix/suffix và textarea hai dòng; mở/đóng phone menu không bị co hẹp, không clip; chọn color/image swatch, swatch hai màu và quantity từ 1 lên 2; checkbox, radio, switch; range từ 0 lên 1; chuyển tab; focus bàn phím từ text sang textarea. Ở mobile mọi painted control chính nằm trong x=15…365, document scrollWidth 380 ≤ innerWidth 390.

CSS parser: 90 rules, 335 declarations, không lỗi; vendor range pseudo-elements được nhận diện riêng vì selector parser không hỗ trợ chúng. Chromium computed styles và tương tác range đã kiểm tra; không kiểm tra Firefox.

Giới hạn: chưa upload/remove file vì không có disposable fixture được yêu cầu; chưa thử lỗi validation, group và vertical tabs không render. Hover của dropdown có kiểm tra rule nguồn, chưa thao tác hover trực tiếp bằng API. Không xác nhận độ giống popup select OS; màu list tùy biến là adaptation đã ghi rõ. Không thử mua hàng hoặc gửi form.

Learning review: các lỗi painted wrapper, dropdown transition, inline swatch geometry và font preview đều đã thuộc quy tắc hiện có của skill; không cần thêm quy tắc trùng lặp. Các bằng chứng cụ thể được lưu để dùng khi có yêu cầu cập nhật theme cases.

User correction: removed all swatch sizing overrides, including percentage !important dimensions and triangle border widths. Saved to GPO and verified the served CSS matches the local file exactly. Color swatches render at 32px and image swatches at 60px according to Globo configuration; selection works. New evidence: swatch-sizing-verification.json and swatch-sizes-from-globo.png. Admin size settings were not changed for testing. Earlier screenshots document the previous iteration.
