# 當代中文課程 · Sách 1–2 — Graded Reader

Trình đọc phân cấp (graded reader) cho Sách 1 và Sách 2 của *當代中文課程 / A Course in
Contemporary Chinese*, dành cho người học Việt Nam. Một file HTML duy nhất, chạy offline,
không gọi tài nguyên ngoài.

**Đọc trực tiếp:** mở `index.html` bằng bất kỳ trình duyệt nào.

## Có gì bên trong

| | |
|---|---|
| Bài học | 30 (Sách 1: 15 · Sách 2: 15) |
| Bài đọc | 60 — mỗi bài 2 văn bản (hội thoại / đoản văn), 628 lượt thoại |
| Từ tra được | 1.242 (1.162 từ mới + 80 từ bổ trợ) |
| Mục ngữ pháp | 162, kèm câu ví dụ + pinyin + dịch Anh |
| Token trong bài đọc | 10.938 — mọi chữ đều bấm tra được |

Độ phủ: pinyin 1242/1242 · nghĩa Việt 1242/1242 · âm Hán Việt 1241/1242
(`KTV` không có âm Hán Việt vì không phải chữ Hán).

## Cách dùng

- **书架** — 30 ô đậm dần theo số từ mới đã mở; tiến độ lưu trong `localStorage` của máy
- **课文** — 3 tab mỗi bài: hai bài đọc + `语法`
  - `PINYIN` bật ruby pinyin cho **toàn bài**
  - `ẨN NGHĨA` che nghĩa để tự kiểm tra
  - bấm chữ nào cũng mở thẻ từ, kèm **câu thật lấy từ trong bài** và nguồn
    (ví dụ `B1-L01 · 对话一 · 明华`)
  - tên nhân vật bấm ra được giới thiệu là ai
- **词库** — tra 1.242 từ theo chữ Hán / pinyin / tiếng Việt / **âm Hán Việt** / tiếng Anh.
  Không dấu cũng tìm được: `jieyun`, `tau dien`, `tiep van` đều ra 捷运.

Giao diện tự đổi theo theme sáng/tối của máy.

## Âm Hán Việt

Điểm khác so với sách gốc: mỗi từ mới có thêm **âm Hán Việt** bên cạnh pinyin — chỉ hiện
trong thẻ từ và kho từ, **không hiện trong bài đọc** để không làm rối mặt chữ.

Dựng từ bảng 875 chữ trong `build/hanviet.py` — đúng bằng số chữ Hán xuất hiện trong hai
cuốn. Từ ghép lấy âm bằng cách nối âm từng chữ; chữ đa âm có bảng ngoại lệ riêng
(`WORD_HV`): 音乐 → *âm nhạc*, 银行 → *ngân hàng*. Danh từ riêng viết hoa từng âm:
台湾 → *Đài Loan*, 陈月美 → *Trần Nguyệt Mỹ*.

## Dựng lại

Nội dung được rút tự động từ 30 file `.pptx` bài giảng gốc. **Các file `.pptx` không có
trong repo này** (tài liệu có bản quyền, và ~300 MB).

```bash
pip install python-pptx pypinyin
cd build
python extract3.py        # 30 pptx  -> raw3.json
python normalize.py       # vá dữ liệu, tách biến thể -> clean.json
python build_data.py      # + nghĩa Việt, Hán Việt, token hoá -> reader.json
python assemble.py        # -> reader-ccc-book1-2.html (bản đầy đủ)
python make_artifact.py   # -> artifact_reader.html (bản bỏ vỏ tài liệu)
```

Sửa đường dẫn `ROOT` trong `extract2.py` cho khớp thư mục chứa pptx của bạn.

Các file viết tay (không sinh tự động): `gloss_a/b/c.txt` (1.162 nghĩa Việt),
`hanviet.py` (875 âm Hán Việt), `supp.txt` (80 từ bổ trợ), `names.txt` (31 nhân vật).

## Bản quyền

Nội dung bài học — hội thoại, đoản văn, bảng từ mới, mục ngữ pháp — thuộc bản quyền của
**當代中文課程 / A Course in Contemporary Chinese** (國立臺灣師範大學 · National Taiwan
Normal University). Repo này chỉ là công cụ đọc, làm cho mục đích học tập cá nhân, không
thay thế việc mua sách.

Phần tự viết trong repo — mã nguồn, nghĩa tiếng Việt, bảng âm Hán Việt — dùng tự do cho
việc học.
