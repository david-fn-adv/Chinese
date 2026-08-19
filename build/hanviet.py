# -*- coding: utf-8 -*-
"""Âm Hán Việt cho toàn bộ 875 chữ xuất hiện trong Sách 1 + Sách 2.
Mỗi chữ lấy âm đọc chính; các từ ghép có âm khác được ghi ở WORD_HV."""

CHARS = """
的:đích 我:ngã 了:liễu 你:nễ 一:nhất 不:bất 是:thị 好:hảo 有:hữu 美:mỹ 去:khứ 同:đồng 么:ma 安:an
如:như 中:trung 很:hẫn 在:tại 们:môn 吃:cật 得:đắc 玉:ngọc 到:đáo 要:yếu 来:lai 以:dĩ 学:học 这:giá
台:đài 天:thiên 人:nhân 大:đại 多:đa 看:khán 东:đông 上:thượng 个:cá 家:gia 都:đô 月:nguyệt 明:minh 可:khả
年:niên 就:tựu 里:lý 也:dã 太:thái 他:tha 玲:linh 想:tưởng 下:hạ 健:kiện 起:khởi 那:na 华:hoa 子:tử
谢:tạ 说:thuyết 国:quốc 跟:cân 马:mã 时:thời 还:hoàn 生:sinh 点:điểm 文:văn 什:thập 过:quá 湾:loan 会:hội
丁:đinh 吗:ma 没:một 房:phòng 田:điền 开:khai 对:đối 师:sư 路:lộ 面:diện 车:xa 啊:a 机:cơ 她:tha
新:tân 候:hậu 喜:hỷ 常:thường 觉:giác 包:bao 比:tỉ 高:cao 请:thỉnh 老:lão 回:hồi 怎:chẩm 后:hậu 见:kiến
听:thính 欢:hoan 定:định 方:phương 友:hữu 地:địa 找:trảo 做:tố 朋:bằng 作:tác 小:tiểu 运:vận 玩:ngoạn 现:hiện
西:tây 再:tái 哪:na 水:thủy 心:tâm 和:hòa 边:biên 陈:trần 先:tiên 问:vấn 呢:ni 坐:tọa 网:võng 能:năng
为:vi 真:chân 法:pháp 意:ý 然:nhiên 打:đả 样:dạng 饭:phạn 越:việt 便:tiện 教:giáo 公:công 爱:ái 吧:ba
菜:thái 所:sở 课:khóa 次:thứ 快:khoái 走:tẩu 工:công 客:khách 电:điện 经:kinh 把:bả 着:trứ 丽:lệ 怡:di
君:quân 书:thư 南:nam 北:bắc 间:gian 手:thủ 馆:quán 气:khí 日:nhật 餐:xan 错:thác 前:tiền 捷:tiệp 买:mãi
外:ngoại 用:dụng 最:tối 厅:thính 校:hiệu 近:cận 部:bộ 垃:lạp 圾:cấp 店:điếm 利:lợi 放:phóng 发:phát 拿:nã
食:thực 素:tố 早:tảo 热:nhiệt 道:đạo 但:đãn 期:kỳ 语:ngữ 张:trương 等:đẳng 较:giảo 果:quả 念:niệm 试:thí
才:tài 活:hoạt 聊:liêu 饺:giáo 李:lý 白:bạch 风:phong 刚:cương 始:thủy 事:sự 站:trạm 应:ứng 给:cấp 些:ta
两:lưỡng 晚:vãn 每:mỗi 久:cửu 习:tập 关:quan 当:đương 动:động 今:kim 带:đái 知:tri 分:phân 午:ngọ 夜:dạ
该:cai 像:tượng 喝:hát 照:chiếu 几:kỷ 五:ngũ 贵:quý 十:thập 自:tự 海:hải 算:toán 市:thị 色:sắc 住:trú
班:ban 礼:lễ 主:chủ 任:nhiệm 料:liệu 进:tiến 妳:nễ 少:thiểu 二:nhị 山:sơn 附:phụ 思:tư 服:phục 话:thoại
系:hệ 望:vọng 言:ngôn 离:ly 准:chuẩn 叫:khiếu 漂:phiêu 亮:lượng 妈:ma 母:mẫu 字:tự 球:cầu 影:ảnh 种:chủng
肉:nhục 己:kỷ 从:tòng 空:không 写:tả 物:vật 别:biệt 已:dĩ 春:xuân 练:luyện 除:trừ 搬:bàn 茶:trà 本:bản
音:âm 乐:lạc 钱:tiền 远:viễn 图:đồ 行:hành 半:bán 慢:mạn 旅:lữ 功:công 出:xuất 逛:cuống 红:hồng 因:nhân
收:thu 司:ty 希:hy 加:gia 口:khẩu 让:nhượng 第:đệ 处:xử 备:bị 虽:tuy 三:tam 妹:muội 伯:bá 帮:bang
楼:lâu 花:hoa 商:thương 题:đề 又:hựu 星:tinh 假:giả 女:nữ 租:tô 父:phụ 告:cáo 正:chính 孩:hài 黄:hoàng
线:tuyến 难:nan 门:môn 轻:khinh 只:chỉ 睡:thụy 康:khang 展:triển 岛:đảo 业:nghiệp 身:thân 极:cực 完:hoàn 泰:thái
垦:khẩn 姐:tỷ 景:cảnh 忙:mang 计:kế 决:quyết 右:hữu 传:truyền 绿:lục 诉:tố 平:bình 环:hoàn 境:cảnh 位:vị
谈:đàm 资:tư 王:vương 相:tương 游:du 杯:bôi 辣:lạt 建:kiến 往:vãng 交:giao 祝:chúc 直:trực 转:chuyển 麻:ma
烦:phiền 步:bộ 容:dung 易:dị 兴:hưng 岁:tuế 验:nghiệm 合:hợp 酒:tửu 闹:náo 儿:nhi 体:thể 迎:nghênh 片:phiến
爸:ba 名:danh 哥:ca 弟:đệ 板:bản 百:bách 支:chi 室:thất 或:hoặc 参:tham 差:sai 概:khái 特:đặc 穿:xuyên
费:phí 换:hoán 订:đính 雪:tuyết 更:cánh 医:y 病:bệnh 考:khảo 汉:hán 够:cấu 情:tình 婚:hôn 郎:lang 光:quang
而:nhi 且:thả 拳:quyền 咖:ca 啡:phi 谁:thùy 您:nâm 周:chu 末:mạt 卖:mại 牛:ngưu 昨:tạc 结:kết 钟:chung
票:phiếu 非:phi 铁:thiết 骑:kỵ 视:thị 号:hiệu 议:nghị 干:can 净:tịnh 左:tả 装:trang 划:hoạch 累:lũy 油:du
牙:nha 雨:vũ 药:dược 品:phẩm 倒:đảo 丢:đâu 趣:thú 泡:phao 煮:chử 节:tiết 泳:vịnh 四:tứ 碗:oản 怕:phạ
甜:điềm 宿:túc 头:đầu 舒:thư 代:đại 衣:y 超:siêu 林:lâm 惯:quán 付:phó 忘:vong 记:ký 脚:cước 糕:cao
约:ước 夏:hạ 讨:thảo 息:tức 拜:bái 急:cấp 松:tùng 纸:chỉ 认:nhận 化:hóa 顺:thuận 恭:cung 娘:nương 件:kiện
留:lưu 各:các 酸:toan 注:chú 全:toàn 变:biến 接:tiếp 共:cộng 宜:nghi 莲:liên 舍:xá 束:thúc 观:quan 载:tải
汽:khí 香:hương 套:sáo 成:thành 必:tất 蛋:đản 冷:lãnh 世:thế 览:lãm 巴:ba 区:khu 搭:tháp 介:giới 绍:thiệu
薪:tân 份:phần 办:bạn 适:thích 送:tống 跑:bào 坏:hoại 城:thành 鱼:ngư 味:vị 乡:hương 氛:phân 洗:tẩy 民:dân
沙:sa 速:tốc 简:giản 查:tra 研:nghiên 究:cứu 聚:tụ 夕:tịch 压:áp 踢:thích 足:túc 块:khối 万:vạn 千:thiên
汤:thang 栋:đống 六:lục 火:hỏa 故:cố 宫:cung 猫:miêu 笑:tiếu 蓝:lam 猪:trư 统:thống 底:đế 厌:yếm 流:lưu
局:cục 陪:bồi 保:bảo 提:đề 邮:bưu 背:bối 赶:cản 洲:châu 阳:dương 助:trợ 按:án 亲:thân 戚:thích 另:lánh
踏:đạp 重:trọng 惜:tích 床:sàng 低:đê 皮:bì 声:thanh 奇:kỳ 懂:đổng 力:lực 卷:quyển 破:phá 韩:hàn 尝:thường
调:điều 趟:thảng 被:bị 值:trị 摩:ma 托:thác 条:điều 堡:bảo 胖:bàn 瘦:sấu 掉:điệu 充:sung 招:chiêu 实:thực
围:vi 炉:lô 吉:cát 初:sơ 姓:tính 诚:thành 篮:lam 唱:xướng 歌:ca 银:ngân 赛:tái 九:cửu 程:trình 男:nam
窗:song 户:hộ 喂:ủy 需:nhu 奖:tưởng 金:kim 绩:tích 替:thế 冬:đông 伞:tán 湿:thấp 痛:thống 喉:hầu 咙:lung
休:hưu 脸:kiểm 吐:thổ 巷:hàng 饿:ngạ 脑:não 飞:phi 士:sĩ 通:thông 船:thuyền 选:tuyển 爬:ba 识:thức 解:giải
级:cấp 侨:kiều 形:hình 庆:khánh 宴:yến 敬:kính 桌:trác 吵:sảo 罐:quán 塑:tố 胶:giao 夫:phu 育:dục 响:hưởng
颜:nhan 庙:miếu 饮:ẩm 馅:hãm 扁:biển 材:tài 趁:sấn 拌:bán 滩:than 遍:biến 街:nhai 待:đãi 腻:nị 青:thanh
炸:tạc 麦:mạch 劳:lao 宗:tông 讯:tấn 骂:mạ 消:tiêu 透:thấu 界:giới 将:tương 毕:tất 企:xí 管:quản 理:lý
际:tế 乌:ô 龙:long 兄:huynh 棒:bổng 微:vi 波:ba 内:nội 旧:cựu 八:bát 笼:lung 臭:xú 豆:đậu 腐:hủ
旁:bàng 池:trì 古:cổ 博:bác 院:viện 芒:mang 瓜:qua 拍:phách 矮:ải 厨:trù 浴:dục 器:khí 滑:hoạt 秋:thu
叶:diệp 纽:nữu 闻:văn 停:đình 鼻:tị 胃:vị 炎:viêm 烧:thiêu 感:cảm 冒:mạo 肚:đỗ 险:hiểm 冰:băng 迷:mê
段:đoạn 灯:đăng 款:khoản 枝:chi 笔:bút 贸:mậu 场:trường 复:phức 杂:tạp 欧:âu 悠:du 卡:ca 报:báo 演:diễn
讲:giảng 噢:ô 广:quảng 暑:thử 授:thụ 亚:á 英:anh 律:luật 履:lý 历:lịch 表:biểu 答:đáp 式:thức 帅:suất
座:tọa 糖:đường 句:cú 福:phúc 河:hà 园:viên 愿:nguyện 存:tồn 随:tùy 碟:điệp 椅:ỷ 具:cụ 长:trường 论:luận
社:xã 团:đoàn 失:thất 首:thủ 尔:nhĩ 规:quy 追:truy 忽:hốt 怪:quái 袋:đại 辆:lượng 护:hộ 类:loại 瓶:bình
源:nguyên 桶:dũng 推:thôi 腿:thối 借:tá 抱:bão 怨:oán 尺:xích 总:tổng 整:chỉnh 精:tinh 神:thần 堂:đường 潜:tiềm
柠:ninh 檬:mông 镇:trấn 寓:ngụ 宽:khoan 筑:trúc 层:tằng 挤:tễ 黎:lê 雄:hùng 货:hóa 脱:thoát 鞋:hài 饱:bão
锅:oa 筷:khoái 盐:diêm 椒:tiêu 玻:pha 璃:ly 寿:thọ 其:kỳ 温:ôn 泉:tuyền 虑:lự 湖:hồ 原:nguyên 偷:thâu
潭:đàm 植:thực 躺:thảng 昏:hôn 啤:bì 浪:lãng 漫:mạn 晒:sái 欸:ai 咸:hàm 烤:khảo 拉:lạp 薯:thự 单:đơn
蒸:chưng 污:ô 染:nhiễm 严:nghiêm 卫:vệ 营:doanh 养:dưỡng 啦:lạp 糊:hồ 涂:đồ 喔:ốc 义:nghĩa 捡:kiểm 省:tỉnh
检:kiểm 立:lập 刻:khắc 呼:hô 征:trưng 求:cầu 连:liên 继:kế 续:tục 使:sử 港:cảng 济:tế 目:mục 翻:phiên
译:dịch 员:viên 专:chuyên 扰:nhiễu 祥:tường 纪:kỷ 财:tài 扫:tảo 联:liên 橘:quất 守:thủ 贴:thiếp 余:dư 升:thăng
鞭:tiên 炮:pháo 七:thất 汔:khí 短:đoản 信:tín 侯:hầu
农:nông 受:thụ 改:cải 政:chính 价:giá 购:cấu 型:hình 度:độ 元:nguyên 产:sản 术:thuật
折:chiết 居:cư 饼:bính 军:quân 治:trị 清:thanh 苦:khổ 科:khoa 反:phản 性:tính 担:đảm
修:tu 亏:khuy 季:quý 满:mãn 撞:chàng 象:tượng 销:tiêu 由:do 于:vu 职:chức 务:vụ 举:cử
凤:phượng 梨:lê 竞:cạnh 争:tranh 伤:thương 数:số 战:chiến 萝:la 卜:bốc 权:quyền
德:đức 独:độc 般:bàn 牌:bài 毛:mao 弄:lộng 退:thoái 并:tịnh 顾:cố 预:dự 跳:khiêu
幸:hạnh 鲜:tiên 祖:tổ 移:di 族:tộc 宵:tiêu 墙:tường 排:bài 煎:tiễn 木:mộc 造:tạo
塞:tắc 画:họa 及:cập 既:ký 引:dẫn 落:lạc 减:giảm 基:cơ 集:tập 尽:tận 量:lượng
善:thiện 土:thổ 持:trì 许:hứa 爷:gia 奶:nãi 领:lĩnh 紧:khẩn 阿:a 喊:hảm 率:suất
状:trạng 硕:thạc 技:kỹ 普:phổ 叔:thúc 闽:mân 警:cảnh 止:chỉ 至:chí 朝:triều 摊:than
投:đầu 核:hạch 辞:từ 捐:quyên
罗:la 珊:san 蒂:đế 何:hà 雅:nhã 婷:đình 楚:sở 羡:tiện 慕:mộ 熬:ngao 恐:khủng 迟:trì
私:tư 弃:khí 泼:bát 填:điền 申:thân 荐:tiến 扣:khấu 质:chất 择:trạch 摸:mô 羊:dương
暖:noãn 刷:loát 签:thiêm 洞:động 纠:củ 纷:phân 证:chứng 帐:trướng 括:quát 释:thích
尤:vưu 骗:biển 顿:đốn 缴:kiểu 吓:hách 敏:mẫn 萱:huyên 桥:kiều 稳:ổn 躲:đóa 零:linh
樱:anh 乎:hồ 霉:môi 凉:lương 潮:triều 闷:muộn 荷:hà 兰:lan 刮:quát 死:tử 根:căn
据:cứ 祭:tế 蚊:văn 虫:trùng 戴:đái 挂:quải 瘟:ôn 疫:dịch 圆:viên 柚:dữu 馨:hinh
端:đoan 耐:nại 仔:tử 赚:trám 无:vô 烟:yên 跨:khóa 鸡:kê 溪:khê 孔:khổng 碰:bính
迹:tích 史:sử 俗:tục 粥:chúc 窄:trách 盖:cái 欣:hân 赏:thưởng 铃:linh 赤:xích 崁:khám
唉:ai 楣:mi 奋:phấn 词:từ 震:chấn 智:trí 慧:tuệ 杀:sát 衫:sam 剧:kịch 角:giác
寄:ký 害:hại 媒:môi 吸:hấp 避:tị 免:miễn 伍:ngũ 喇:lạt 叭:bá 裤:khố 印:ấn 戏:hí
妆:trang 模:mô 浅:thiển 彦:ngạn 蔬:sơ 堆:đôi 肥:phì 辛:tân 入:nhập 润:nhuận 屋:ốc
番:phiên 茄:già 熟:thục 敢:cảm 黑:hắc 摘:trích 宁:ninh 章:chương 傅:phó 村:thôn
访:phỏng 闲:nhàn 静:tĩnh 邻:lân 狗:cẩu 嗯:ân 孤:cô 牠:tha 脏:tạng 澡:táo 乱:loạn
咬:giảo 宠:sủng 散:tán 庭:đình 跌:điệt 忍:nhẫn 姨:di 靠:kháo 强:cường 享:hưởng
伴:bạn 负:phụ 责:trách 组:tổ 此:thử 云:vân 激:kích 读:độc 辅:phụ 疯:phong 夸:khoa
遗:di 憾:hám 努:nỗ 密:mật 设:thiết 冠:quán 却:khước 拒:cự 绝:tuyệt 弹:đàn 制:chế
础:sở 穷:cùng 徒:đồ 兵:binh 烘:hồng 焙:bồi 艺:nghệ 终:chung 亿:ức 梦:mộng 录:lục
取:thủ 鼓:cổ 励:lệ 吴:ngô 宝:bảo 坡:pha 眼:nhãn 之:chi 贩:phiến 嬷:ma 宅:trạch
配:phối 搜:sưu 寻:tầm 箱:tương 须:tu 曾:tằng 占:chiếm 格:cách 府:phủ 斤:cân 旺:vượng
京:kinh 酥:tô 遵:tuân 则:tắc 诊:chẩn 骨:cốt 刀:đao 况:huống 命:mệnh 针:châm 察:sát
危:nguy 恢:khôi 哎:ai 呀:nha 祸:họa 救:cứu 增:tăng 向:hướng 遇:ngộ 倍:bội 尊:tôn
均:quân 疗:liệu 益:ích 派:phái 队:đội 甚:thậm 仗:trượng 血:huyết 喽:lâu 孙:tôn
禁:cấm 娶:thú 彩:thái 淡:đạm 郑:trịnh 帝:đế 轮:luân 败:bại 浆:tương 断:đoạn 迁:thiên
困:khốn 俭:kiệm 妇:phụ 深:thâm 蒋:tưởng 石:thạch 输:thâu 摆:bãi 烹:phanh 饪:nhâm
殖:thực 噌:tăng 歉:khiểm 衷:trung 途:đồ 劝:khuyến 达:đạt 厂:xưởng 党:đảng 宪:hiến
示:thị 映:ánh 积:tích 佳:giai 策:sách 革:cách 届:giới 暂:tạm 脉:mạch 弱:nhược
势:thế 阵:trận 版:bản
指:chỉ 隔:cách 它:tha 圣:thánh
"""

# từ ghép dùng âm đọc khác âm chính của chữ
WORD_HV = {
    '音乐': 'âm nhạc', '银行': 'ngân hàng', '长大': 'trưởng đại', '校长': 'hiệu trưởng',
    '照相': 'chiếu tướng', '照相机': 'chiếu tướng cơ', '一起': 'nhất khởi',
    '睡觉': 'thụy giáo', '不错': 'bất thác', '差不多': 'sai bất đa',
    '快乐': 'khoái lạc', '可乐': 'khả lạc', '行李': 'hành lý',
    '银': 'ngân', '首都': 'thủ đô', '重要': 'trọng yếu',
    '只': 'chỉ', '教': 'giáo', '为': 'vi',
    '安德思':         'An Đức Tư',
    '罗珊蒂':         'La San Đế',
    '何雅婷':         'Hà Nhã Đình',
    '陈敏萱':         'Trần Mẫn Huyên',
    '高桥健太':        'Cao Kiều Kiện Thái',
    '李文彦':         'Lý Văn Ngạn',
    '吴宝春':         'Ngô Bảo Xuân',
    '蒋介石':         'Tưởng Giới Thạch',
    '郑成功':         'Trịnh Thành Công',
    '荷兰':          'Hà Lan',
    '新加坡':         'Tân Gia Ba',
    '东京':          'Đông Kinh',
    '淡水':          'Đạm Thủy',
    '平溪':          'Bình Khê',
    '孔庙':          'Khổng Miếu',
    '赤崁楼':         'Xích Khám Lâu',
    '红毛城':         'Hồng Mao Thành',
    '闽南语':         'Mân Nam ngữ',
    '闽南人':         'Mân Nam nhân',
    '大清帝国':        'Đại Thanh đế quốc',
    '明朝':          'Minh triều',
    '清朝':          'Thanh triều',
    '元宵':          'nguyên tiêu',
    '元宵节':         'Tết Nguyên Tiêu',
    '端午节':         'Tết Đoan Ngọ',
    '农历':          'nông lịch',
    '快乐':          'khoái lạc',
    '音乐':          'âm nhạc',
    '乐团':          'nhạc đoàn',
    '行行出状元':       'hành hành xuất trạng nguyên',
    '数一数二':        'sổ nhất sổ nhị',
    '少数':          'thiểu số',
    '长':           'trường',
    '长大':          'trưởng đại',
    '种':           'chủng',
    '得票率':         'đắc phiếu suất',
    '失业率':         'thất nghiệp suất',
    '分之':          'phân chi',
}

def load_chars():
    m = {}
    for tok in CHARS.split():
        if ':' not in tok: continue
        c, v = tok.split(':', 1)
        if c and v: m[c] = v
    return m

def hv_of(word, chars=None):
    """âm Hán Việt của một từ: ưu tiên WORD_HV, sau đó ghép âm từng chữ"""
    if chars is None: chars = load_chars()
    if word in WORD_HV: return WORD_HV[word]
    parts = []
    for c in word:
        if c in chars: parts.append(chars[c])
        elif c.strip(): return ''      # có chữ chưa có âm -> bỏ, không đoán
    return ' '.join(parts)

if __name__ == '__main__':
    import json, re, sys
    m = load_chars()
    need = [l.strip() for l in open('chars.txt', encoding='utf-8') if l.strip()]
    missing = [c for c in need if c not in m]
    dup = len(m)
    print('table entries :', dup)
    print('chars needed  :', len(need))
    print('MISSING       :', len(missing), ''.join(missing))
    extra = [c for c in m if c not in need]
    print('EXTRA         :', len(extra), ''.join(extra))
    json.dump(m, open('hanviet.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
