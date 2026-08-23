# 當代中文課程 · Sách 1–3 + tin tức — Graded Reader

Trình đọc phân cấp (graded reader) cho Sách 1, 2 và 3 của *當代中文課程 / A Course in
Contemporary Chinese*, dành cho người học Việt Nam, **cộng thêm mỗi ngày một bài đọc
tin tức tiếng Trung** ở mức khó nối tiếp Sách 3. Một file HTML duy nhất, chạy offline,
không gọi tài nguyên ngoài.

**Đọc trực tiếp:** mở `index.html` bằng bất kỳ trình duyệt nào.

## Có gì bên trong

| | |
|---|---|
| Bài học | 43 — giáo trình 42 (Sách 1: 15 · 2: 15 · 3: 12) + tin tức 1 |
| Bài đọc | 85 văn bản, 922 khối |
| Từ tra được | 2.125 |
| Mục ngữ pháp / điểm ngôn ngữ | 252, kèm câu ví dụ + pinyin + dịch |
| Token trong bài đọc | 21.216 — mọi chữ đều bấm tra được |

Độ phủ: nghĩa Việt đủ 2125/2125; âm Hán Việt đủ 2124/2125 — mục còn lại là `KTV`,
từ mượn viết bằng chữ Latinh nên không có âm Hán Việt. Không còn chữ Hán nào trong
bài đọc mà không tra được.

## Cách dùng

- **书架** — 43 ô trên 4 hàng (ba hàng sách + một hàng tin), đậm dần theo số từ mới
  đã mở; tiến độ lưu trong `localStorage` của máy
- **课文** — 3 tab mỗi bài: hai bài đọc + `语法`
  - `PINYIN` bật ruby pinyin cho **toàn bài**
  - `ẨN NGHĨA` che nghĩa để tự kiểm tra
  - bấm chữ nào cũng mở thẻ từ, kèm **câu thật lấy từ trong bài** và nguồn
    (ví dụ `B3-L07 · 对话一 · 何雅婷`)
  - tên nhân vật bấm ra được giới thiệu là ai
- **词库** — tra 2.125 từ theo chữ Hán / pinyin / tiếng Việt / **âm Hán Việt** / tiếng Anh,
  lọc riêng được theo từng sách hoặc theo **tin tức**.
  Không dấu cũng tìm được: `toupiao`, `bo phieu`, `dau phieu quyen` đều ra 投票权.

Giao diện tự đổi theo theme sáng/tối của máy.

## Tin tức hằng ngày

Mỗi ngày thêm một bài đọc phóng tác từ báo tiếng Trung (36氪, 零壹财经, 新华网…), chủ đề
AI · startup · kinh doanh · công nghệ · fintech · tài trợ thương mại.

Bài tin là **bản phóng tác tóm lược viết lại**, không phải bản dịch hay trích nguyên
văn. Số liệu và tên riêng giữ theo nguồn và được đối chiếu bằng nguồn thứ hai; cách
diễn đạt là của bản phóng tác. Mỗi bài có khối 来源 cuối bài ghi đủ báo, tác giả, ngày
đăng, URL và ngày truy cập.

Mật độ từ mới giữ trong khoảng **5–10% số loại từ** — nhẹ hơn giáo trình (Sách 3 chạy
22,4%) vì tin đọc hằng ngày và đọc một mình. Một cổng kiểm tra chặn bài không đạt.

```bash
pip install pypinyin jieba
python3 tools/build_lesson.py news/2026-08-23.json   # nháp -> token, đo mật độ
python3 tools/gate.py        news/2026-08-23.json    # cổng: đạt / hỏng
python3 tools/build_app.py                           # dựng lại index.html
```

Quy trình đầy đủ, ràng buộc biên tập và danh sách kiểm tra: **`tools/daily-news.md`**.

## Âm Hán Việt

Điểm khác so với sách gốc: mỗi từ mới có thêm **âm Hán Việt** bên cạnh pinyin — chỉ hiện
trong thẻ từ và kho từ, **không hiện trong bài đọc** để không làm rối mặt chữ.

Dựng từ bảng 1.266 chữ trong `build/hanviet.py`. Từ ghép lấy âm bằng cách nối âm từng chữ;
chữ đa âm có bảng ngoại lệ riêng (`WORD_HV`): 音乐 → *âm nhạc*, 银行 → *ngân hàng*.
Danh từ riêng viết hoa từng âm: 台湾 → *Đài Loan*, 郑成功 → *Trịnh Thành Công*.

## Dựng lại

`index.html` là **sản phẩm dựng ra**, không phải file nguồn — đừng sửa tay, sẽ bị ghi đè.

```bash
python3 tools/build_app.py     # build/template.html + data/reader.json + news/*.json
```

`data/reader.json` giữ 42 bài giáo trình đã đóng băng; `news/*.json` mỗi file một bài tin.
Dựng lại từ `template.html` + `reader.json` cho ra đúng từng byte bản 42 bài trước đó.

### Rút lại từ file bài giảng gốc

Chỉ cần khi muốn dựng lại `data/reader.json` từ đầu. Nội dung được rút tự động từ 42
file `.pptx` bài giảng gốc. **Các file `.pptx` không có trong repo này** (tài liệu có
bản quyền, và rất nặng).

```bash
pip install python-pptx pypinyin
cd build
export CCC_SOURCE=/duong/dan/toi/thu-muc-chua-BOOK-1-2-3
python extract3.py        # 42 pptx  -> raw3.json
python normalize.py       # vá dữ liệu, tách biến thể -> clean.json
python build_data.py      # + nghĩa Việt, Hán Việt, token hoá -> reader.json
python assemble.py        # -> reader-ccc-book1-3.html (bản đầy đủ)
python make_artifact.py   # -> artifact_reader.html (bản bỏ vỏ tài liệu)
```

Thư mục của từng cuốn được **tự dò**: bất kỳ thư mục con nào chứa `.pptx` và có
`book 1` / `book 2` / `book 3` trong đường dẫn. File tạm `~$*.pptx` của PowerPoint bị bỏ qua.

Các file viết tay (không sinh tự động): `gloss_a…g.txt` (nghĩa Việt),
`hanviet.py` (1.266 âm Hán Việt), `supp.txt` + `supp_b3.txt` (từ hỗ trợ ngoài bảng từ),
`names.txt` (49 nhân vật), `b3l07_text.py` (xem bên dưới).

## Hai chỗ dữ liệu gốc có vấn đề

Ghi lại để người sau khỏi tưởng là lỗi chương trình:

1. **B3-L07 課文一 không có dưới dạng chữ trong file .pptx** — nó là ảnh chụp trang sách
   (slide 2–3, bản 簡體字版). Phần này được **chép tay từ ảnh**, để trong
   `build/b3l07_text.py`. Đây là chỗ duy nhất trong cả bộ không rút tự động được.
2. **B3-L09 gõ nhầm `风梨` 5 lần** trong khi cùng bài dùng `凤梨` 13 lần
   (风 = gió, 凤 = phượng, chỉ 凤梨 mới là quả dứa). Đã sửa qua `TEXT_FIX` trong
   `build/normalize.py`.

Ngoài ra định dạng slide Sách 3 khác Sách 1–2 ở hai điểm, extractor đã xử lý: tên người
nói bị giãn cách (`李 文 彦：`) và vài slide bảng từ trông giống đoạn văn.

## Khuôn mẫu cho giáo trình khác

`khuon-mau-reader.html` (53 KB) là bản khuôn: nguyên giao diện, nhưng thay dữ liệu thật
bằng một bài mẫu ngắn, kèm **đặc tả schema 85 dòng nhúng ngay trong file**. Đưa file này
cho một trợ lý AI cùng với file bài giảng của bạn và bảo nó *chỉ thay phần dữ liệu, giữ
nguyên giao diện* — dùng lại được cho bất kỳ giáo trình nào.

Câu ví dụ trong thẻ từ do giao diện **tự quét bài đọc** mà ra, không nằm trong dữ liệu —
nên AI không thể bịa câu ví dụ.

## Bản quyền

Nội dung bài học — hội thoại, đoản văn, bảng từ mới, mục ngữ pháp — thuộc bản quyền của
**當代中文課程 / A Course in Contemporary Chinese** (國立臺灣師範大學 · National Taiwan
Normal University). Repo này chỉ là công cụ đọc, làm cho mục đích học tập cá nhân, không
thay thế việc mua sách.

Bài đọc tin tức là **bản phóng tác tóm lược viết lại**, không phải bản dịch hay trích
nguyên văn bài báo gốc; mỗi bài ghi đủ nguồn ở cuối. Bản quyền bài báo gốc thuộc về
tờ báo và tác giả được ghi tên.

Phần tự viết trong repo — mã nguồn, nghĩa tiếng Việt, bảng âm Hán Việt, văn bản phóng
tác — dùng tự do cho việc học.
