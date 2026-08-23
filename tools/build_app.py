# -*- coding: utf-8 -*-
"""Dựng lại index.html từ template + data/reader.json + news/*.json.

    python3 tools/build_app.py

Dựng lại, KHÔNG vá. Chạy bao nhiêu lần cũng ra cùng một file.
"""
import sys, os, io, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import newslib as N

BOOKS_BASE = [{'b': 1, 'title': '基础', 'vn': 'Nền tảng'},
              {'b': 2, 'title': '生活', 'vn': 'Đời sống'},
              {'b': 3, 'title': '社会', 'vn': 'Xã hội'}]

def main():
    db = N.merge()
    books = list(BOOKS_BASE)
    if any(l['book'] == N.NEWS_BOOK for l in db['lessons']):
        books.append(dict(N.NEWS_LABEL))
    db['books'] = books

    tpl = io.open(N.TPL, encoding='utf-8').read()
    payload = json.dumps(db, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    html = tpl.replace('__DATA__', payload)
    assert '__DATA__' not in html, 'template thiếu chỗ cắm __DATA__'
    io.open(N.OUT, 'w', encoding='utf-8', newline='\n').write(html)

    nnews = sum(1 for l in db['lessons'] if l['book'] == N.NEWS_BOOK)
    print('index.html   %.2f MB' % (os.path.getsize(N.OUT) / 1048576.0))
    print('bài          %d  (giáo trình %d + tin %d)'
          % (len(db['lessons']), len(db['lessons']) - nnews, nnews))
    print('từ điển      %d' % len(db['dict']))
    print('tên riêng    %d' % len(db['names']))
    print('kệ           %d hàng — %s' % (len(books), ', '.join(
        (b.get('label') or 'B%d' % b['b']) for b in books)))
    tok = sum(len(b['tk']) for l in db['lessons'] for t in l['texts'] for b in t['blocks'])
    print('token        %d' % tok)

if __name__ == '__main__':
    main()
