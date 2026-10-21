# -*- coding: utf-8 -*-
"""Âm Hán Việt bổ sung cho từ vựng tin tức — ngoài 1.266 chữ của build/hanviet.py.

Mỗi mục: chữ:âm, cách nhau bằng khoảng trắng. Chỉ thêm chữ THẬT SỰ xuất hiện
trong bài; không đoán, không thêm hàng loạt. Cổng kiểm tra chặn nếu thiếu.
"""

CHARS_EXT = """
布:bố 析:tích 翼:dực 据:cứ 算:toán 模:mô 投:đầu 智:trí 务:vụ 增:tăng 缓:hoãn
涨:trướng 峰:phong 谷:cốc 按:án 贷:thải 良:lương
融:dung 估:cổ 股:cổ 芯:tâm 额:ngạch
募:mộ 截:tiệt 者:giả 券:khoán 江:giang 丰:phong 旭:húc 创:sáng
抵:để 押:áp 耗:hao 评:bình 央:ương 显:hiển
董:đổng 损:tổn
纺:phưởng 织:chức 账:trướng 币:tệ 登:đăng 浙:chiết 州:châu 县:huyện 确:xác
汇:hối 允:doãn 潘:phan 坛:đàn
"""

# Từ ghép có âm khác cách ghép từng chữ
WORD_EXT = {
    '增长': 'tăng trưởng',      # 長 ở đây đọc "trưởng", không phải "trường"
    '央行': 'ương hàng',        # 行 = ngân hàng đọc "hàng", không phải "hành"
    '行长': 'hàng trưởng',      # 行 = ngân hàng, 長 = người đứng đầu
}
