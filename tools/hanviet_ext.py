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
降:giáng 判:phán
软:nhuyễn 盘:bàn 醒:tỉnh
宣:tuyên 审:thẩm 批:phê 效:hiệu 泄:tiết 露:lộ 监:giám 储:trữ 晓:hiểu
临:lâm 标:tiêu
惠:huệ 衡:hành 乘:thừa 采:thái
盈:doanh 披:phi 幅:phúc
扩:khuếch 缩:súc
供:cung 旦:đán 链:liên 巨:cự 徽:huy 豪:hào 杨:dương 蓉:dung 瑜:du 朱:chu 炯:quýnh
构:cấu 锁:tỏa 唯:duy 伟:vĩ
呆:ngai 浦:phố 曹:tào 频:tần 兽:thú 络:lạc
驾:giá 驶:sử 测:trắc 矿:khoáng 葛:cát 辰:thần 韬:thao 弘:hoằng 毅:nghị 苹:bình 疆:cương 蒙:mông 氪:khắc
债:trái 涛:đào
峡:hiệp 杰:kiệt
"""

# Từ ghép có âm khác cách ghép từng chữ
WORD_EXT = {
    '增长': 'tăng trưởng',      # 長 ở đây đọc "trưởng", không phải "trường"
    '央行': 'ương hàng',        # 行 = ngân hàng đọc "hàng", không phải "hành"
    '行长': 'hàng trưởng',      # 行 = ngân hàng, 長 = người đứng đầu
    '支行': 'chi hàng',         # 行 = ngân hàng
    '分行': 'phân hàng',        # 行 = ngân hàng
    '参与': 'tham dự',
    '交易额': 'giao dịch ngạch', # 易 trong 交易 đọc "dịch", không phải "dị"
    '用处': 'dụng xứ',          # 处 = chỗ, chốn, đọc "xứ"          # 与 trong 参与 đọc "dự" (thanh 4), không phải "dữ"
}
