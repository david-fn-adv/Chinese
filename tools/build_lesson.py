# -*- coding: utf-8 -*-
"""Sinh phần `lesson` của một bài tin từ phần `draft`. Chạy lại được, kết quả giống nhau.

    python3 tools/build_lesson.py news/2026-08-23.json
"""
import sys, os, json, io
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import newslib as N

def build(path, write=True):
    with open(path, encoding='utf-8') as f: nf = json.load(f)
    d      = nf['draft']
    newd   = nf.get('dict', {})
    names  = nf.get('names', {})
    known  = N.known_before(path)
    reader = N.load_reader()

    dic = dict(reader['dict']); dic.update(newd)
    lex = set(dic) | set(reader['names']) | set(names)
    allnames = dict(reader['names']); allnames.update(names)

    blocks, unknown = [], []
    for para in d['paras']:
        toks, unk = N.tokenize(para, lex, allnames)
        unknown += unk
        blocks.append({'type': 'para',
                       'tk': N.finish_tokens(toks, dic, newd.keys(), allnames)})

    idx = [os.path.basename(p) for p in N.news_files()].index(os.path.basename(path))
    lesson = {
        'id': nf['id'], 'book': N.NEWS_BOOK, 'no': idx + 1, 'date': nf['date'],
        'seq': len(reader['lessons']) + idx + 1,
        'title': d['title'], 'py': N.py(d['title']),
        'en': d.get('en', ''), 'vn': d['vn'],
        'texts': [{'zh': '新闻', 'vn': 'TIN TỨC', 'kind': 'essay', 'blocks': blocks}],
        'grammar': d.get('points', []),
        'vocab': [w for w in newd],
        'src': nf['src'],
    }
    nf['lesson'] = lesson
    if write:
        io.open(path, 'w', encoding='utf-8', newline='\n').write(
            json.dumps(nf, ensure_ascii=False, indent=1))

    typ, tok, det = N.density(lesson, known)
    print('bài      :', lesson['id'], '·', lesson['title'])
    print('chữ Hán  :', N.han_count(lesson))
    print('token    :', det['tokens'], '| loại từ:', det['types'])
    print('từ mới   :', det['new_types'], 'loại /', det['new_tokens'], 'lượt')
    print('MẬT ĐỘ   : %.1f%% loại từ  |  %.1f%% lượt chữ' % (typ, tok))
    if unknown:
        print('\n!! CHƯA TRA ĐƯỢC', len(unknown), 'đoạn — phải thêm vào "dict":')
        seen = []
        for u in unknown:
            if u in seen: continue
            seen.append(u)
            print('   %-12s gợi ý tách: %s' % (u, ' / '.join(N.suggest(u))))
    return nf, unknown, (typ, tok, det)

if __name__ == '__main__':
    build(sys.argv[1])
