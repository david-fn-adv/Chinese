# -*- coding: utf-8 -*-
"""Cổng kiểm tra một bài tin. Thoát khác 0 nếu có lỗi cứng.

    python3 tools/gate.py news/2026-08-23.json

Không chấm điểm phần trăm tổng hợp: mỗi kiểm tra là ĐẠT hoặc HỎNG.
Một con số duy nhất chỉ tạo cảm giác an tâm giả.
"""
import sys, os, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import newslib as N
from build_lesson import build

BAND = (5.0, 10.0)          # % loại từ mới — chốt với Dương 2026-08-23
HAN_RANGE = (350, 450)      # số chữ Hán mỗi bài

def gate(path):
    hard, soft = [], []
    nf, unknown, (typ, tok, det) = build(path, write=False)
    L, dic, names = nf['lesson'], nf.get('dict', {}), nf.get('names', {})
    basedic, basenames = N.upto(path)
    full = dict(basedic); full.update(dic)
    fullnames = dict(basenames); fullnames.update(names)

    # ── 1..4: bốn điều kiện bắt buộc của đặc tả khuôn mẫu ──
    for t in L['texts']:
        for b in t['blocks']:
            for x in b['tk']:
                if x['k'] in ('core', 'extra') and x['w'] not in full:
                    hard.append('token "%s" không có trong dict' % x['w'])
                if x['k'] == 'name' and x['w'] not in fullnames:
                    hard.append('tên riêng "%s" không có trong names' % x['w'])
                if x['k'] != 'punct' and x['k'] != 'plain' and not x.get('p'):
                    hard.append('token "%s" thiếu pinyin' % x['w'])
    for w in L['vocab']:
        if w not in full: hard.append('vocab "%s" không có trong dict' % w)
    for w, v in dic.items():
        if not v.get('vn'): hard.append('dict "%s" thiếu nghĩa Việt' % w)
        if not v.get('hv'): hard.append('dict "%s" thiếu âm Hán Việt (chữ thiếu: %s)'
                                        % (w, ''.join(N.hv_missing(w))))
        if not v.get('p'):  hard.append('dict "%s" thiếu pinyin' % w)
    # ghép lại token phải ra đúng nguyên văn bản nháp
    def norm(t):
        t = re.sub(r'\s+', ' ', t.strip())
        return re.sub(r'\s*([\u3400-\u4dbf\u4e00-\u9fff])\s*', r'\1', t)
    for para, b in zip(nf['draft']['paras'], L['texts'][0]['blocks']):
        joined = ''.join(x['w'] for x in b['tk'])
        if norm(joined) != norm(para):
            hard.append('ghép token không khớp nguyên văn:\n    gốc  %s\n    ghép %s'
                        % (para[:60], joined[:60]))
    if unknown:
        hard.append('%d đoạn chữ Hán chưa tra được: %s'
                    % (len(unknown), ' '.join(sorted(set(unknown)))))

    # bài đã lưu trong file phải KHỚP với bản dựng lại từ nháp.
    # Không có kiểm tra này thì phép so khớp trên là vòng tròn: dựng từ nháp
    # rồi so với chính nháp thì không bao giờ hỏng. Đây mới là chỗ bắt được
    # file cũ chưa dựng lại, hoặc phần "lesson" bị sửa tay.
    with open(path, encoding='utf-8') as f:
        stored = json.load(f).get('lesson')
    if stored is None:
        hard.append('file chưa có phần "lesson" — chạy build_lesson.py trước')
    elif json.dumps(stored, ensure_ascii=False, sort_keys=True) != \
         json.dumps(L, ensure_ascii=False, sort_keys=True):
        hard.append('phần "lesson" trong file KHÔNG khớp bản dựng lại từ "draft" '
                    '— file cũ hoặc đã bị sửa tay; chạy lại build_lesson.py')

    # ── 5: mật độ từ mới ──
    if not (BAND[0] <= typ <= BAND[1]):
        hard.append('mật độ %.1f%% loại từ, ngoài band %.0f–%.0f%%' % (typ, *BAND))

    # ── 6: độ dài ──
    hc = N.han_count(L)
    if not (HAN_RANGE[0] <= hc <= HAN_RANGE[1]):
        soft.append('%d chữ Hán, ngoài khoảng %d–%d' % (hc, *HAN_RANGE))

    # ── 7: nguồn ──
    if not L.get('src'): hard.append('không có nguồn')
    for s in L.get('src', []):
        for k in ('outlet', 'title', 'date', 'url', 'accessed'):
            if not s.get(k): hard.append('nguồn thiếu trường "%s": %s' % (k, s.get('url', '?')))
        if not str(s.get('url', '')).startswith('http'):
            hard.append('URL không hợp lệ: %s' % s.get('url'))
    if not any(s.get('role') == 'primary' for s in L.get('src', [])):
        hard.append('chưa đánh dấu nguồn chính (role: primary)')

    # ── 8: mỗi từ mới phải xuất hiện thật trong bài ──
    used = set(x['w'] for t in L['texts'] for b in t['blocks'] for x in b['tk'])
    for w in dic:
        if w not in used: hard.append('từ mới "%s" khai trong dict nhưng không có trong bài' % w)

    print('\n' + '─'*62)
    for m in soft: print('  ⚠  ' + m)
    if hard:
        print('  ✗ HỎNG — %d lỗi:' % len(hard))
        for m in hard: print('     · ' + m)
        print('─'*62); return 1
    print('  ✓ ĐẠT — mật độ %.1f%% loại từ · %.1f%% lượt chữ · %d chữ Hán · %d nguồn'
          % (typ, tok, hc, len(L['src'])))
    print('─'*62); return 0

if __name__ == '__main__':
    sys.exit(gate(sys.argv[1]))
