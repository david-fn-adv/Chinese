# -*- coding: utf-8 -*-
"""artifact_reader.html — cùng nội dung với bản đầy đủ, chỉ bỏ vỏ tài liệu
(<!doctype>/<html>/<head>/<body>) vì nền tảng Artifact tự bọc lại.
Token màu và bảng màu tối nằm trong template.html (nguồn duy nhất)."""
import io, json, os, re

TITLE = '<title>當代中文課程 · Sách 1–2</title>'


def build():
    src = io.open('template.html', encoding='utf-8').read()
    assert 'prefers-color-scheme:dark' in src, 'template thiếu bảng màu tối'

    body = re.sub(r'^.*?<title>.*?</title>', TITLE, src, count=1, flags=re.S)
    body = body.replace('</head>\n<body>', '', 1)
    body = re.sub(r'\n</body>\s*</html>\s*$', '\n', body)
    for bad in ('<!DOCTYPE', '<html', '</html>', '<head>', '</head>', '<body>', '</body>', '<meta '):
        assert bad not in body, 'còn sót vỏ tài liệu: ' + bad

    db = json.load(open('reader.json', encoding='utf-8'))
    from assemble import VN_TITLE
    for l in db['lessons']:
        l['vn'] = VN_TITLE.get(l['id'], '')
    payload = json.dumps(db, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    out = body.replace('__DATA__', payload)
    assert '__DATA__' not in out

    io.open('artifact_reader.html', 'w', encoding='utf-8', newline='\n').write(out)
    print('artifact_reader.html  %.2f MB  title@byte=%d  %s'
          % (os.path.getsize('artifact_reader.html') / 1048576.0,
             out.index('<title>'), re.search(r'<title>(.*?)</title>', out).group(1)))


if __name__ == '__main__':
    build()
