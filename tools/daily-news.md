# Luồng tin tức hằng ngày — bản hợp đồng

Thêm mỗi ngày **một bài đọc tin tức tiếng Trung** vào graded reader, ở mức khó nối
tiếp Sách 3. Đây là bản hợp đồng: làm đúng theo nó, không tự chế. Chỗ nào thấy nên
đổi thì **sửa file này trước**, rồi mới đổi cách làm.

> Đặc tả dữ liệu gốc nằm trong `khuon-mau-reader.html` (85 dòng, cuối file).
> File này chỉ phủ thêm phần quy trình cho bài tin. Khi hai bên mâu thuẫn,
> **đặc tả trong `khuon-mau-reader.html` thắng**.

---

## 1. Chạy

```bash
pip install pypinyin jieba
python3 tools/build_lesson.py news/YYYY-MM-DD.json   # nháp -> tokens, báo mật độ
python3 tools/gate.py        news/YYYY-MM-DD.json    # cổng, thoát != 0 nếu hỏng
python3 tools/build_app.py                           # dựng lại index.html
```

**Chỉ commit khi cổng ĐẠT.** Cổng hỏng thì dừng, báo Dương, không push.

---

## 2. Kiến trúc — dựng lại, không vá

```
data/reader.json      42 bài giáo trình — nguồn sự thật, không đụng vào
news/YYYY-MM-DD.json  một file một bài tin
build/template.html   vỏ app, có chỗ cắm __DATA__
        │
        └── tools/build_app.py ──> index.html
```

`index.html` là **sản phẩm dựng ra**, không phải file nguồn. Không bao giờ sửa tay
`index.html`; sửa xong sẽ bị ghi đè ở lần dựng sau. Đã kiểm chứng:
`template.html` + `reader.json` dựng lại ra đúng từng byte bản 42 bài trước đó.

Không dùng script vá regex vào `index.html`. Đã cân nhắc và bác: file 1,4 MB,
vá bằng regex là mong manh và không cần thiết khi đã có đường dựng lại.

---

## 3. Nguồn tin

Nguồn đã thử, đọc được toàn văn kèm ngày đăng:

| Nguồn | Mảng | Ghi chú |
|---|---|---|
| 36氪 `36kr.com` | AI · startup · công nghệ | nhiều bài/ngày, có mốc giờ |
| 零壹财经 `01caijing.com` | fintech · ngân hàng số | nhịp chậm hơn, phân tích sâu |
| 新华网 `news.cn` | công bố chính thức | dùng để **đối chiếu số liệu** |

Thêm nguồn mới thì ghi vào bảng này trước khi dùng.

**Bắt buộc đối chiếu.** Số liệu tài chính phải kiểm bằng nguồn thứ hai trước khi
đưa vào bài. Hai nguồn lệch nhau thì hoặc bỏ con số đó, hoặc ghi rõ theo nguồn nào.
Đây là tài liệu học — sai số là sai lâu dài.

> Lưu ý đã gặp: thông cáo chính thức thường **chỉ công bố những chỉ số tăng**, bỏ
> qua phần giảm. Đừng nhầm "nguồn chính thức" với "đầy đủ".

---

## 4. Chọn tin

Chủ đề, theo thứ tự ưu tiên: **AI · startup · kinh doanh · công nghệ · fintech ·
trade financing**.

Claude tự chọn, không hỏi Dương. Tiêu chí, phải thoả cả 5:

1. **Mới** — đăng trong vòng 48 giờ.
2. **Trong nhóm chủ đề** trên.
3. **Cụ thể** — có tên riêng, có số, có chuyện xảy ra. Không lấy bài bình luận chung chung.
4. **Dính tới thị trường Trung Quốc** — công ty Trung Quốc, chính sách Trung Quốc, hoặc
   tác động trực tiếp lên thị trường Trung Quốc. Tin thuần về công ty Mỹ xếp sau.
5. **Vừa ngân sách từ** — chủ đề quá hẹp về kỹ thuật sẽ ăn hết ngân sách từ mới
   (xem mục 6) và không viết nổi trong 400 chữ.

Ưu tiên tin có ích cho công việc của Dương ở Advance (cho vay SME, tài trợ thương mại,
quan hệ ngân hàng – fintech) khi các tiêu chí khác ngang nhau.

---

## 5. Biên tập

**Bài là bản phóng tác tóm lược, viết lại bằng lời mình. Không dịch, không chép.**

Hai lý do, cả hai đều cứng:

- *Bản quyền* — repo này không giữ nội dung có bản quyền của người khác. Xem mục
  Bản quyền trong `README.md`.
- *Sư phạm* — không thể khống chế từ vựng trên văn của người khác. Muốn giữ mật độ
  từ mới trong band thì phải tự viết từng câu.

Giữ nguyên: **số liệu, tên riêng, thuật ngữ chuyên ngành**. Đó là phần có giá trị
nghề nghiệp. Đơn giản hoá: cấu trúc câu, cách nối ý, từ nối.

Cuối bài **luôn** có khối 来源 với đầy đủ: báo, tác giả, ngày đăng, URL, ngày truy cập,
và ghi chú rằng đây là bản phóng tác. App tự dựng khối này từ trường `src`.

---

## 6. Ngân sách từ mới — chốt với Dương 2026-08-23

**5–10% số LOẠI TỪ** (không phải số lượt chữ). Cổng chặn cứng ngoài band.

Số đo tham chiếu của giáo trình, để biết mình đang đứng ở đâu:

| | từ mới / lượt chữ | từ mới / loại từ | độ dài |
|---|---|---|---|
| Sách 1 | 38,0% | 42,0% | 166 token |
| Sách 2 | 16,7% | 23,4% | 402 token |
| Sách 3 | 14,3% | 22,4% | 746 token |
| **bài tin** | ~10% | **5–10%** | ~290 token |

Bài tin **nhẹ hơn giáo trình có chủ ý**: đọc hằng ngày, đọc một mình, không có thầy.

Cách đo: mẫu số là mọi token `core`/`extra`/`name`, bỏ dấu câu và token `plain`
(số, chữ Latinh). Tên riêng **không** tính là từ mới. "Đã biết" = 2.112 từ của
giáo trình **cộng** mọi từ đã ra ở các bài tin trước — vốn từ cộng dồn theo ngày.

Tỉ lệ thực đo: **~0,30 loại từ trên mỗi chữ Hán**. Bài 400 chữ ≈ 130–140 loại từ
≈ **ngân sách 7–14 từ mới**. Rất chặt — phải chọn từ có chủ đích.

Cách tiêu ngân sách cho đúng:

- Ưu tiên từ **dùng lại được hằng ngày** (同比, 增长, 业务, 数据) hơn từ chỉ đúng
  cho một bài (某个芯片型号).
- Từ ghép mà **từng chữ đã biết** thì không tốn ngân sách — bộ tách từ tự cắt ra
  (过去 → 过 + 去). Tận dụng chỗ này.
- Muốn hạ mật độ thì **viết dài thêm bằng từ đã biết**, đừng bỏ từ mới đáng học.
- Tên công ty, tên sản phẩm cho vào `names`, không cho vào `dict`.

---

## 7. Hình dạng bài — chốt với Dương 2026-08-23

- **350–450 chữ Hán.** Cổng cảnh báo nếu ra ngoài (mềm, không chặn).
- **Một đoản văn**, `kind: "essay"`, không hội thoại. Hội thoại phải bịa người nói —
  không làm.
- **Tab thứ ba là 语言点**, 2–3 điểm ngôn ngữ **rút từ chính bài này**.
  Câu ví dụ phải là câu **có thật trong bài**, kèm pinyin và bản dịch.
  Không bịa câu ví dụ. Ưu tiên cấu trúc báo chí – kinh tế dùng lại được
  (同比, A占B的X%, 真正…的是…).
- Tiêu đề: chữ Hán + bản Việt. `en` không bắt buộc.

---

## 8. Âm Hán Việt

Mọi mục `dict` phải có `hv` khác rỗng — cổng chặn cứng.

Bảng gốc: `build/hanviet.py` (1.266 chữ). **Không sửa file đó** — nó thuộc phần
giáo trình. Chữ mới thêm vào `tools/hanviet_ext.py`:

```python
CHARS_EXT = """ 布:bố 析:tích 翼:dực """
WORD_EXT  = { '增长': 'tăng trưởng' }    # khi ghép từng chữ ra sai âm
```

`hv_of` trả về rỗng nếu thiếu dù chỉ một chữ — **không đoán**. Thiếu thì tra rồi
thêm tay, không được đoán bừa cho qua cổng.

Danh từ riêng: Viết Hoa Từng Âm (天翼云 → *Thiên Dực Vân*).

---

## 9. Định dạng `news/YYYY-MM-DD.json`

```jsonc
{
  "date": "2026-08-23",
  "id":   "N-20260823",              // luôn là N- + YYYYMMDD
  "draft": {                          // PHẦN NGƯỜI VIẾT — nguồn sự thật
    "title": "中国电信的算力生意",
    "vn":    "Cuộc làm ăn mới của China Telecom: bán sức tính toán",
    "en":    "",
    "paras": ["đoạn 1…", "đoạn 2…"],
    "points": [ { "h": "I. 同比 — …", "b": ["Cách dùng:", "câu Hán", "pinyin", "dịch"] } ]
  },
  "names": { "中国电信": { "w":…, "p":…, "hv":…, "note":… } },
  "dict":  { "同比":     { "w":…, "p":…, "hv":…, "pos":…, "en":…, "vn":…,
                           "kind":"core", "no":"", "ls":["N-20260823"] } },
  "src":   [ { "role":"primary", "outlet":"零壹财经", "author":"…",
               "title":"…", "date":"2026-08-21", "url":"https://…",
               "accessed":"2026-08-23" } ],
  "lesson": { … }                     // SINH TỰ ĐỘNG — không sửa tay
}
```

`draft` là thứ người viết sửa. `lesson` do `build_lesson.py` sinh ra từ `draft`.
**Sửa `lesson` bằng tay là sai** — cổng có kiểm tra riêng bắt việc này (mục 10.9).

`src` cần ít nhất một mục `role: "primary"`. Mục đối chiếu để `role: "secondary"`.

---

## 10. Cổng kiểm tra

Không có điểm phần trăm tổng hợp. Mỗi mục là **ĐẠT hoặc HỎNG**. Một con số kiểu
"95,7%" chỉ tạo cảm giác an tâm giả — nhìn thì yên tâm mà không biết cái gì đang hỏng.

Lỗi **cứng** (chặn, không được commit):

1. Token `core`/`extra` không có trong `dict`; token `name` không có trong `names`.
2. Từ trong `vocab` không có trong `dict`.
3. Mục `dict` thiếu `vn`, `hv`, hoặc `p`.
4. Token có nghĩa mà thiếu pinyin.
5. Ghép lại token không ra đúng nguyên văn `draft` (dấu cách giữa chữ Latinh
   phải khớp đúng; dấu cách cạnh chữ Hán được bỏ qua).
6. Còn đoạn chữ Hán chưa tra được.
7. Mật độ từ mới ngoài band 5–10% loại từ.
8. Nguồn: thiếu, thiếu trường, URL không hợp lệ, hoặc không có `role: primary`.
9. `lesson` trong file không khớp bản dựng lại từ `draft` (file cũ hoặc bị sửa tay).
10. Từ khai trong `dict` nhưng không xuất hiện trong bài.

Lỗi **mềm** (cảnh báo, vẫn qua): số chữ Hán ngoài khoảng 350–450.

---

## 11. Những chỗ dễ sai

- **Đừng sửa `index.html`.** Nó là sản phẩm dựng ra.
- **Đừng sửa `data/reader.json`.** 42 bài giáo trình đóng băng.
- **Đừng sửa `build/hanviet.py`.** Chữ mới đi vào `tools/hanviet_ext.py`.
- **Đừng bịa câu ví dụ trong thẻ từ.** Giao diện tự quét bài đọc mà ra.
- **Đừng nới band cho bài dễ qua cổng.** Muốn đổi band thì sửa mục 6 của file này
  và nói với Dương, đừng lặng lẽ đổi con số trong `gate.py`.
- **Đừng tin số liệu một nguồn.** Xem mục 3.

---

## 12. Nhật ký quyết định

| Ngày | Quyết định | Ai chốt |
|---|---|---|
| 2026-08-23 | Mật độ 5–10% **loại từ** (không phải lượt chữ) | Dương |
| 2026-08-23 | 350–450 chữ Hán, một đoản văn, không hội thoại | Dương |
| 2026-08-23 | Claude tự chọn tin, không cần duyệt trước | Dương |
| 2026-08-23 | Tab 3 là 语言点 rút từ chính bài | Dương |
| 2026-08-23 | Phóng tác tóm lược, không dịch nguyên văn | Claude (bản quyền + sư phạm) |
| 2026-08-23 | Dựng lại `index.html`, bỏ hướng vá regex | Claude (đã kiểm chứng byte-identical) |
| 2026-08-23 | Cổng đạt/hỏng, bỏ điểm phần trăm tổng hợp | Claude |
