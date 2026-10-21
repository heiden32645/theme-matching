# Match theme: Takeout 6.1.0 / Pantry — 2534

## Cập nhật thu gọn quantity theo yêu cầu

- `.gpo-app .gpo-ov-quantity`: 100 × 32px; mỗi nút 32px, icon 12px, số 14px.
- `.gpo-app .gpo-quantity .gpo-quantity__input`: 64 × 32px, số 14px.
- Bỏ override quantity 44px ở mobile/touch; kích thước mới áp dụng desktop và mobile. Các số đo quantity trong báo cáo gốc phía dưới đã được thay thế bởi cập nhật này.
- Đã sửa file CSS local và CSS hiện có trong admin riêng biệt, giữ các chỉnh sửa không thuộc quantity ở từng nơi.
- Đã lưu GPO, xác minh CSS được tải ở preview, đo tại 1838×907 và 390×844; cả hai kích thước đều đúng. Nút tăng hoạt động (1→2→3), input đơn nhập 3 được. CSS parse không lỗi.
- Bằng chứng: `compact-quantity-measurements.json`, `compact-quantity-desktop.png`, `compact-quantity-mobile.png`, `served-gpo-compact-quantity.css`. Bản trước sửa được lưu ở `before-compact-quantity-local.css` và `before-compact-quantity-admin.css`.

Ngày kiểm tra: 19/10/2026.

- Preview: https://kpxcq99qz771ljnw-69620498584.shopifypreview.com/products/vans-apparel-and-accessories-classic-super-no-show-socks-3-pack-white
- Variant: 47372797509784, 9.5-13 / white.
- Theme metadata: schema_name Takeout, schema_version 6.1.0, theme_store_id 2534, preset/name Pantry, installed theme id 189439901848. Asset path /t/43/ không được dùng làm theme store id.
- File chỉnh sửa: `2534/6.1.0.css`. CSS thuần, 4 dấu cách, không nesting/preprocessor.
- Đã lưu vào GPO > Settings > Design > Custom CSS; trước đó ô này trống. Match Shopify theme style đã bật sẵn.
- Bản được phục vụ nằm trong `#gpo-dynamic-css`, không có bundle minified riêng. `served-gpo-dynamic.css` chứa nguyên văn CSS cuối.
- SHA-256 CSS: f793ad984e50a5af22b27d5a2fdda730821bcb2064782177bd4d19b5f99664fa.

## Đối chiếu

| GPO | Nguồn native / token | Trạng thái |
| --- | --- | --- |
| App, label | `legend.form__label`, `--font-body-family`, `--font-body-weight`, `--color-foreground`, body 1rem/1.4 | Đã kiểm tra font DM Sans, màu, cỡ chữ |
| Button swatch | `.product-form__input input[type=radio]+label`, nền ở `::after`, border trong suốt .25rem | Outer box native/GPO 48.59375px desktop; 52px mobile. Phần nền bên trong desktop 39.59375px |
| Color/image swatch | `component-swatch-input.css`, `.swatch-input__label`, outline .2rem, offset .2rem | Source-based mapping vì native swatch không render trên sản phẩm này. GPO checked có ring; click/selected đã kiểm tra |
| Quantity option | `quantity-input.quantity`, `.quantity__button`, `.quantity__input` | Native/GPO 39.59375px desktop, 44px mobile; tăng 1 thành 2 hoạt động |
| Single quantity | Native quantity inner input và nền wrapper | 39.59375px desktop, 44px mobile |
| Select / custom dropdown | `.product-form__input select` padding .5em 2.2em .5em .8em; body line-height 1.4; native down-arrow từ `.select .icon-caret` | Suy ra từ source, không có native product select render để đo. GPO select/custom/font/image trigger 43.195px desktop, 38.398px mobile |
| Dropdown list | `.disclosure__list` / footer localization: nền theme, item nền foreground-10, selected underline; animateLocalization .4s ease, caret không xoay | Fallback theo localization, không gọi là product-select match đo trực tiếp. Animation entrance được điều chỉnh hướng xuống theo vị trí list GPO. Đóng tức thì, không còn inherited max-height transition .3s |
| Text / phone / dimension / color | `.share-button__fallback .field__input`, cùng recipient field source: min-height 2.7rem; padding .2rem .8rem | Source-based: native share input nằm trong details hidden. GPO wrapper 48.59375px desktop, 43.195px mobile. Prefix/suffix nằm trong cùng nền |
| Textarea | Theme `.text-area` / recipient textarea padding; GPO rows=4 được giữ | Nhiều dòng, resize dọc; không ép chiều cao/line-height bằng ô một dòng |
| File upload/action/remove | Nền field, action `.button`, secondary button tokens | Default/dropzone style kiểm tra; upload, remove và progress chưa kiểm thử |
| Radio/checkbox, switch, range | Thích nghi theo theme color tokens | Chọn radio/checkbox, bật switch, range ArrowRight 0 thành 1 hoạt động |
| Horizontal tabs | Thích nghi theo variant pill vì không có native horizontal tabs | Chuyển option_1/option_2 và panel thành công |
| Group / vertical tabs | `.accordion`, `.accordion summary`, arrow và divider theo source | Chưa render trên sản phẩm; chưa kiểm thử trực tiếp |

## Kiểm thử

- Desktop thực tế 1440×1000 và mobile thực tế 390×844; số đo nằm trong `desktop-measurements.json` và `mobile-measurements.json`. Đã xác minh innerWidth/innerHeight, không dùng kích thước yêu cầu làm số đo.
- Mobile scrollWidth=390; không tìm thấy phần tử GPO hiển thị vượt viewport.
- Default/selected: native pills không bị tác động; GPO button/color/image/radio/checkbox đã chọn thử.
- Select, dropdown thường, ảnh và font chọn được, giữ giá trị sau blur. Đã mở/đóng bằng trigger, chọn item, và đóng khi bấm ngoài cho cả ba custom dropdown.
- Native localization đã mở/đóng để đối chiếu source, animation .4s và caret giữ nguyên. Hover chỉ đối chiếu source/computed; API không có hover trực tiếp.
- Font dropdown và font pills giữ font preview riêng; chọn Oswald làm font liên kết cho text vẫn hoạt động.
- Text có prefix/suffix đã nhập thử. Textarea nhận hai dòng; keyboard Tab tạo outline 2px foreground-20 quanh wrapper. Menu quốc gia mở không bị clip. Popup color picker mở trong viewport. Dimension nhập 10 thành công.
- Option quantity tăng 1 thành 2; switch, range và tabs hoạt động.
- CSS parser tinycss2: 117 qualified rules (gồm keyframes), không lỗi cú pháp/declaration. Selector parser đã kiểm tra; vendor pseudo-elements dùng riêng từng rule.
- Nội dung CSS cuối đã được xác minh nguyên văn trong stylesheet storefront và trạng thái admin đã lưu.
- Upload/remove chưa chạy vì không có disposable fixture được chỉ định. Disabled/error, group và vertical tabs chưa có tình huống render để kiểm tra.
- Các viewport thử nghiệm đã được reset; tab kiểm thử riêng đã đóng. Trang preview và admin gốc vẫn mở.

## Sửa xung đột đã chứng minh

1. Base GPO `.gpo-select select` ép background-color:inherit và gradient caret bằng `!important`; đã dùng transparent và background-image:none cùng `!important` để tránh hai lớp nền và hai caret.
2. Theme `*:focus-within:not(:focus-visible), .no-focus *` ép outline:0!important. Trước sửa, selected color swatch có outline-style:none, width:0. Sau sửa checked outline bằng !important, mobile settled có ring solid 3px (theme .2rem ở root 16px, làm tròn theo renderer), offset 3px. Không dùng kết quả giữa transition để kết luận trạng thái cuối.

## Đề xuất bổ sung skill

- Quan sát: Takeout 6.1.0 có global `.no-focus * { outline:0!important }`, làm mất ring selected của GPO color/image swatch sau pointer input dù rule outline-color đã thắng. Đã chứng minh bằng matching CSS rules và computed style; sau sửa, ring vẫn hiện trên desktop/mobile.
- Đề xuất thêm case Takeout vào `.agents/skills/match-theme/references/theme-cases.md`: “When adapting Takeout swatches, keep the .2rem selected outline and offset, and override the theme's important pointer-focus outline reset on checked swatches only. Verify the settled outline after a pointer click.”
- Lợi ích: tránh bỏ sót trạng thái chọn và tránh sửa lại thủ công. Đã kiểm tra preset Pantry 6.1.0; cần kiểm tra một preset/settings khác trước khi mở rộng kết luận. Chưa sửa skill trong tác vụ này.
