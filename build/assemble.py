# -*- coding: utf-8 -*-
"""Chèn reader.json vào template.html -> file HTML cuối cùng."""
import json, io, os, re

VN_TITLE = {
 'B1-L01': 'Chào mừng bạn đến Đài Loan',
 'B1-L02': 'Gia đình tôi',
 'B1-L03': 'Cuối tuần làm gì?',
 'B1-L04': 'Xin hỏi tổng cộng bao nhiêu tiền',
 'B1-L05': 'Mì bò ngon thật',
 'B1-L06': 'Trường của họ ở trên núi',
 'B1-L07': 'Chín giờ sáng đi KTV',
 'B1-L08': 'Đi tàu hỏa xuống Đài Nam',
 'B1-L09': 'Nghỉ lễ đi chơi ở đâu?',
 'B1-L10': 'Trái cây Đài Loan rất ngon',
 'B1-L11': 'Tôi muốn thuê nhà',
 'B1-L12': 'Bạn học tiếng Trung ở Đài Loan bao lâu?',
 'B1-L13': 'Chúc mừng sinh nhật',
 'B1-L14': 'Trời lạnh thế này!',
 'B1-L15': 'Tôi thấy rất không khỏe',
 'B2-L01': 'Xin hỏi, đến Sư Đại đi thế nào?',
 'B2-L02': 'Hay là đi tàu điện đi!',
 'B2-L03': 'Tiếng Trung của bạn tiến bộ rồi!',
 'B2-L04': 'Tôi làm thêm, tôi dạy tiếng Pháp',
 'B2-L05': 'Đi ăn tiệc cưới',
 'B2-L06': 'Tôi dự định dọn đến gần trường',
 'B2-L07': 'Xe rác đến rồi!',
 'B2-L08': 'Học công phu',
 'B2-L09': 'Thành phố ấy đẹp quá',
 'B2-L10': 'Mời đến nhà tôi gói bánh chẻo',
 'B2-L11': 'Đài Loan nhiều chỗ chơi thật',
 'B2-L12': 'Ăn thế nào mới khỏe?',
 'B2-L13': 'Tôi mất điện thoại rồi',
 'B2-L14': 'Tôi sắp bắt đầu tìm việc',
 'B2-L15': 'Ăn Tết Nguyên Đán',
 'B3-L01': 'Khai giảng rồi',
 'B3-L02': 'Giảm từ 20% trở lên',
 'B3-L03': 'Áo khoác, mang theo chưa?',
 'B3-L04': 'Tôi yêu tình người Đài Loan',
 'B3-L05': 'Bây giờ đang mốt gì?',
 'B3-L06': 'Về quê ở một đêm!',
 'B3-L07': 'Người "nhà" thân nhất của tôi',
 'B3-L08': 'Tôi muốn được là chính mình',
 'B3-L09': 'Thời đại mua sắm online',
 'B3-L10': 'Tôi nằm viện',
 'B3-L11': 'Chuyện Đài Loan',
 'B3-L12': 'Tôi đi bỏ phiếu',
}

# Noi ghi file HTML hoan chinh. Dat CCC_OUT de doi.
OUT = os.environ.get("CCC_OUT", "reader-ccc-book1-3.html")

def main():
    db = json.load(open('reader.json', encoding='utf-8'))
    miss = []
    for l in db['lessons']:
        l['vn'] = VN_TITLE.get(l['id'], '')
        if not l['vn']: miss.append(l['id'])
    if miss: print('  ! thiếu tiêu đề VN:', miss)
    tpl = io.open('template.html', encoding='utf-8').read()
    payload = json.dumps(db, ensure_ascii=False, separators=(',', ':'))
    # an toàn khi nhúng vào <script type="application/json">
    payload = payload.replace('</', '<\\/')
    html = tpl.replace('__DATA__', payload)
    assert '__DATA__' not in html
    io.open(OUT, 'w', encoding='utf-8', newline='\n').write(html)
    print('WROTE', OUT)
    print('size  %.2f MB' % (os.path.getsize(OUT) / 1048576.0))
    # sanity
    print('lessons', len(db['lessons']),
          'dict', len(db['dict']), 'names', len(db['names']))
    tot_blocks = sum(len(t['blocks']) for l in db['lessons'] for t in l['texts'])
    tot_tok = sum(len(b['tk']) for l in db['lessons'] for t in l['texts'] for b in t['blocks'])
    tot_gram = sum(len(l['grammar']) for l in db['lessons'])
    print('blocks', tot_blocks, 'tokens', tot_tok, 'grammar points', tot_gram)

if __name__ == '__main__':
    main()
