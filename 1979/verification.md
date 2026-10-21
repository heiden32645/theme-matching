# Mavon 12.8.0 — Dewy

Ngày kiểm tra: 21/10/2026 (Asia/Ho_Chi_Minh).

- Product: https://9kk41vlfycrvmn5l-69620498584.shopifypreview.com/products/vans-era-59-moroccan-geo-dress-blues
- Variant: 8 / blue, id 47372774342808.
- Identity từ script Shopify.theme trên trang: schema_name Mavon, schema_version 12.8.0, theme_store_id 1979, installed theme id 189499867288; preview bar: Dewy Trial. `/t/50/` là đường dẫn asset của bản cài, không phải theme store id.
- File chỉnh sửa: `12.8.0.css`, plain CSS, 4 spaces, flat selectors.
- Tích hợp: GPO Settings → Design → Custom CSS, đã Save. Match Shopify theme style vốn đã bật và được giữ nguyên. Custom CSS ban đầu trống theo ACE placeholder; textarea ẩn có nội dung đệm không phản ánh tài liệu. Bản CSS trước khi chỉnh thực tế được lưu trong `evidence/before-served-gpo.css`.
- Storefront: inline `#gpo-dynamic-css` chứa nguyên văn file cuối. `evidence/served-gpo-dynamic.css` lưu nội dung được phục vụ. Theme dùng `base.css` và compiled `styles.css`; các file này chỉ được đọc, không sửa.

## Đối chiếu

| GPO | Nguồn native | Kết quả / giới hạn |
| --- | --- | --- |
| Label / selected value | `variant-selects .form__label strong` / `[data-selected-value]` | Lato 16px, line-height 24px; label 700, value 400; rgba foreground .75 |
| Button swatch | `.product-form__input--pill input + label` | 36px, padding 10px 15px, 1px border, 5px radius, 14px Lato, letter-spacing 1px; selected đảo foreground/background |
| Color / image swatch | `.swatch-input__label`, `.swatch` | Vòng tròn, border foreground .15, outline cách 2px; selected 1px foreground. Giữ kích thước swatch GPO đã cấu hình (swatch màu 34px so với native 35px), ảnh dùng kích thước riêng |
| Select / custom dropdown | `.select__select`, `.select .icon-caret` trong `base.css` | Mapping từ asset: 45px + shadow ngoài 1px, radius button, Lato 12px, padding trái 15px, caret 16px bên phải 15px. Variant hiện tại dùng pill; không có variant dropdown được render để đo trực tiếp |
| Dropdown list | Fallback cho native select của theme | Native select dùng popup hệ điều hành; không tuyên bố list GPO là bản sao popup OS. List dùng màu theme, mở/đóng tức thì, caret đứng yên; hover/checked dùng foreground .08. Reset transition 0.3s kế thừa GPO. Dropdown thường, ảnh và font được thao tác trên desktop/mobile |
| Input / decorated input / dimension / phone / color | `#PopupContactFormName` trong Ask a question, `input[type=text]` | Outer wrapper 50px gồm border 1px, inner 48px. Arial 16px, radius `--button-border-radius`; focus border transparent + shadow foreground 2px. Prefix/suffix cùng box, không thêm viền kép |
| Textarea | `#PopupContactFormMessage.custom-textarea` | Typography monospace 15px/25px và border foreground .08 từ native. GPO vẫn dùng rows=4, padding 10px và resize vertical, không ép chiều cao một dòng |
| Single quantity | Product `quantity-input.quantity` colors/radius; user-requested compact geometry | 64×32px, radius button, border foreground .08; Arial 15px/500 |
| Option quantity | Product `quantity-input.quantity`, `.quantity__input`, `.quantity__button` colors/radius; user-requested compact geometry | 96×32px, input 30×28px, nút 24×28px; màu/viền như native, option chưa chọn giữ disabled GPO |
| Upload action | `.button` và `.product-form__submit` | 49px, Arial 15px/27px, padding 10px 15px, màu `--color-button`/`--color-button-text`; hover từ biến primary. Chỉ kiểm tra hình thức; chưa tải/xóa file |
| Checkbox / radio / switch / range | Theme foreground/background/border tokens | Adaptation từ theme tokens; không tuyên bố có native counterpart tương đương trên trang. Đã thao tác chọn, switch và range |
| Tabs / group | `.product__accordion.accordion summary`, heading typography | Tab ngang đang render: theme-token adaptation, đã chuyển tab. Vertical tabs và disclosure group không render nên chỉ kiểm tra source/syntax |

## Kiểm tra đã thực hiện

- Desktop viewport thực: 1598×933. Mobile viewport thực: 390×790 qua Chrome DevTools responsive; thử viewport API ban đầu không đổi innerWidth và không được tính là kiểm tra mobile. Đã tắt chế độ thiết bị, đóng DevTools và tab kiểm tra riêng sau khi xong.
- Dropdown thường, image dropdown, font dropdown: mở, đóng bằng trigger, chọn option; giá trị được giữ sau blur; desktop có thêm đóng bằng click ngoài. Image thumbnails còn 32px; font Open Sans được giữ trên preview, không bị font reset đè.
- List transition computed: none; closed visibility hidden/height 0, expanded visibility visible với chiều cao theo nội dung; caret giữ transform translateY(-50%). Native popup OS và native variant dropdown không được quan sát nên không xác nhận tương đương animation tuyệt đối.
- Native select GPO đã chọn option_3. Input test, textarea nhiều dòng; focus bằng pointer và Tab sang textarea có shadow 2px và không đổi box height.
- Phone menu mở, wrapper overflow visible, menu không bị cắt. Color picker popup mở và đóng khi click ngoài, giữ overflow visible.
- Radio, checkbox, pill, color swatch, option quantity, switch, range, dimension và tab đều giữ hoạt động. File upload/remove, error state, native disabled variant, vertical tab và group disclosure không có coverage thao tác.
- Mobile: document scrollWidth=390; các input wrapper, dimension, quantity và dropdown button không vượt viewport. Select 45px, input outer 50px, option quantity 45px và pill 36px. Các dropdown/image/font đều chọn được, option quantity tăng lên 2. Phone menu trong viewport.
- Hover và một số disabled/focus selector được đối chiếu source/computed CSS; không có API hover nên không đánh dấu đã test hover bằng chuột.
- CSS đã parse bằng tinycss2: không có lỗi stylesheet/declaration; toàn bộ token tự định nghĩa đều có sử dụng, không có token thiếu. Served CSS chứa nguyên văn file cuối.
- Native pill vẫn 36px, native product quantity vẫn 45px sau tích hợp.

Ảnh: `evidence/desktop-result.png`, `evidence/desktop-dropdown.png`, `evidence/mobile-dropdown.png`, `evidence/mobile-options.png`. Các số đo và kết quả thao tác lưu cùng thư mục evidence.

## Learning review

Các phát hiện về shadow ngoài của select, chiều cao khác nhau theo vai trò, font reset và viewport thực đã nằm trong quy trình hiện có. Không sửa skill và không đề xuất quy tắc trùng lặp.

## Compact quantity and selected separator correction

Theo yêu cầu tiếp theo của người dùng: option stepper đổi từ 120×45px sang 96×32px; single quantity đổi từ 100×45px sang 64×32px. Giữ màu/viền/radius đã mapping, dùng token chiều cao 32px riêng của GPO. Thêm dấu `:` trên label chỉ khi phần selected value kế tiếp có `.has-value`; bỏ margin-left 4px của selected value để giữ khoảng cách tự nhiên. Required marker giữ nguyên.

Đã Save vào GPO, storefront tải nguyên văn CSS mới (cache có độ trễ sau lần lưu). Desktop xác nhận 96×32 và 64×32, native quantity vẫn 45px, tăng option quantity 1→2 hoạt động; selected Button và Color Swatch có dấu `:`, Dropdown chưa chọn không có dấu. Mobile viewport thực 390×790: kích thước như desktop và không tràn ngang. CSS parse lại không lỗi. Đã tắt chế độ thiết bị và đóng DevTools.

Bằng chứng: `evidence/compact-quantity-result.png`, `evidence/compact-quantity-mobile.png`, `evidence/compact-quantity-checks.json`. Bản CSS trước sửa: `evidence/before-compact-quantity.css`.
