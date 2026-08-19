# 當代中文課程 · Sách 1–3 — Graded Reader

Trình đọc phân cấp (graded reader) cho Sách 1, 2 và 3 của *當代中文課程 / A Course in
Contemporary Chinese*, dành cho người học Việt Nam. Một file HTML duy nhất, chạy offline,
không gọi tài nguyên ngoài.

**Đọc trực tiếp:** mở `index.html` bằng bất kỳ trình duyệt nào.

## Có gì bên trong

| | |
|---|---|
| Bài học | 42 (Sách 1: 15 · Sách 2: 15 · Sách 3: 12) |
| Bài đọc | 84 — mỗi bài 2 văn bản (hội thoại / đoản văn), 914 khối |
| Từ tra được | 2.112 |
| Mục ngữ pháp | 249, kèm câu ví dụ + pinyin + dịch Anh |
| Token trong bài đọc | 20.861 — mọi chữ đều bấm tra được |

Độ phủ: pinyin, nghĩa Việt và âm Hán Việt đều đủ 2112/2112. Không còn chữ nào trong bài
đọc mà không tra được.

## Cách dùng

- **书架** — 42 ô đậm dần theo số từ mới đã mở; tiến độ lưu trong `localStorage` của máy
- **课文** — 3 tab mỗi bài: hai bài đọc + `语法`
  - `PINYIN` bật ruby pinyin cho **toàn bài**
  - `ẨN NGHĨA` che nghĩa để tự kiểm tra
  - bấm chữ nào cũng mở thẻ từ, kèm **câu thật lấy từ trong bài** và nguồn
    (ví dụ `B3-L07 · 对话一 · 何雅婷`)
  - tên nhân vật bấm ra được giới thiệu là ai
- **词库** — tra 2.112 từ theo chữ Hán / pinyin / tiếng Việt / **âm Hán Việt** / tiếng Anh.
  Không dấu cũng tìm được: `toupiao`, `bo phieu`, `dau phieu quyen` đều ra 投票权.

Giao diện tự đổi theo theme sáng/tối của máy.

## Âm Hán Việt

Điểm khác so với sách gốc: mỗi từ mới có thêm **âm Hán Việt** bên cạnh pinyin — chỉ hiện
trong thẻ từ và kho từ, **không hiện trong bài đọc** để không làm rối mặt chữ.

Dựng từ bảng 1.266 chữ trong `build/hanviet.py`. Từ ghép lấy âm bằng cách nối âm từng chữ;
chữ đa âm có bảng ngoại lệ riêng (`WORD_HV`): 音乐 → *âm nhạc*, 银行 → *ngân hàng*.
Danh từ riêng viết hoa từng âm: 台湾 → *Đài Loan*, 郑成功 → *Trịnh Thành Công*.

## Dựng lại

Nội dung được rút tự động từ 42 file `.pptx` bài giảng gốc. **Các file `.pptx` không có
trong repo này** (tài liệu có bản quyền, và rất nặng).

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

Phần tự viết trong repo — mã nguồn, nghĩa tiếng Việt, bảng âm Hán Việt — dùng tự do cho
việc học.
