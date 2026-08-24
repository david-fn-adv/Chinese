# -*- coding: utf-8 -*-
"""Âm Hán Việt bổ sung cho từ vựng tin tức — ngoài 1.266 chữ của build/hanviet.py.

Mỗi mục: chữ:âm, cách nhau bằng khoảng trắng. Chỉ thêm chữ THẬT SỰ xuất hiện
trong bài; không đoán, không thêm hàng loạt. Cổng kiểm tra chặn nếu thiếu.
"""

CHARS_EXT = """
布:bố 析:tích 翼:dực 据:cứ 算:toán 模:mô 投:đầu 智:trí 务:vụ 增:tăng 缓:hoãn
涨:trướng 峰:phong 谷:cốc 按:án
"""

# Từ ghép có âm khác cách ghép từng chữ
WORD_EXT = {
    '增长': 'tăng trưởng',      # 長 ở đây đọc "trưởng", không phải "trường"
}
