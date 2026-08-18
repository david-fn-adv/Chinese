# -*- coding: utf-8 -*-
"""Ghép tất cả nguồn thành reader.json: từ điển + bài đọc đã token hoá."""
import json, re, io, os, sys, collections
from pypinyin import pinyin, Style
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from hanviet import load_chars, hv_of, WORD_HV

CJK = re.compile('[㐀-䶿一-鿿]')
PUNCT = set('。，、！？：；（）「」『』“”‘’—…·《》〈〉．,.!?:;()"\'-–~～/／　 ')
HV = load_chars()

# ── nguồn ────────────────────────────────────────────────────────────────────
def read_tsv(path, n):
    rows = []
    for line in io.open(path, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line.strip() or line.lstrip().startswith('#'): continue
        parts = line.split('\t')
        if len(parts) < n:
            print('  ! bad row in %s: %r' % (path, line[:60])); continue
        rows.append(parts[:n])
    return rows

def load_gloss():
    g = {}
    for f in ('gloss_a.txt', 'gloss_b.txt', 'gloss_c.txt'):
        for w, vn in read_tsv(f, 2):
            g[w.strip()] = vn.strip()
    return g

def py_of(s):
    return ' '.join(x[0] for x in pinyin(s, style=Style.TONE, errors=lambda c: [[c]]))

def hv_word(w, py=''):
    """âm Hán Việt; danh từ riêng (pinyin viết hoa) thì viết hoa từng âm"""
    if w in WORD_HV:
        hv = WORD_HV[w]
    else:
        parts = [HV[c] for c in w if c in HV]
        if len(parts) != len([c for c in w if CJK.match(c)]): return ''
        hv = ' '.join(parts)
    first = (py or '').strip()[:1]
    if first and first.isupper():
        hv = ' '.join(s[:1].upper() + s[1:] for s in hv.split(' '))
    return hv


def merge_grammar(items):
    """gộp các slide ngữ pháp liền nhau có cùng tiêu đề thành một mục"""
    out = []
    for g in items:
        head = re.sub(r'\s+', ' ', g['head']).strip()
        body = [re.sub(r'\s+', ' ', x).strip() for x in g['body']]
        body = [x for x in body if x and x != head]
        if out and out[-1]['h'] == head:
            for x in body:
                if x not in out[-1]['b']: out[-1]['b'].append(x)
        else:
            out.append({'h': head, 'b': body})
    # bỏ dòng trùng trong cùng một mục, giữ nguyên thứ tự
    for g in out:
        seen_l = set(); keep = []
        for x in g['b']:
            if x in seen_l: continue
            seen_l.add(x); keep.append(x)
        g['b'] = keep
    return out

# ── xây từ điển ──────────────────────────────────────────────────────────────
def build():
    data = json.load(open('clean.json', encoding='utf-8'))
    gloss = load_gloss()
    LESSONS = sorted(data.keys())
    seq = {lid: i + 1 for i, lid in enumerate(LESSONS)}

    D = {}          # headword -> entry
    warn_nogloss = []
    for lid in LESSONS:
        L = data[lid]
        for v in L['vocab']:
            variants = [re.sub(r'[＋+~～\s]', '', x).strip()
                        for x in re.split('[/／（）()、]', v['w'])]
            pys = [x.strip() for x in re.split(r'[/／]', v['p'] or '')]
            for i, w in enumerate(variants):
                if not w: continue
                if not (CJK.search(w) or re.match(r'^[A-Za-z0-9]+$', w)): continue
                p = pys[i] if i < len(pys) and pys[i] else (pys[0] if pys else py_of(w))
                e = D.get(w)
                if e is None:
                    e = D[w] = {'w': w, 'p': p, 'hv': hv_word(w, p), 'pos': v['pos'] or '',
                                'en': v['en'] or '', 'vn': gloss.get(w, ''),
                                'kind': 'core', 'no': v['no'], 'ls': []}
                    if not e['vn']: warn_nogloss.append(w)
                if lid not in e['ls']: e['ls'].append(lid)
                if not e['p']: e['p'] = p
                if not e['en'] and v['en']: e['en'] = v['en']
    # từ bổ trợ
    for w, p, pos, vn, en in read_tsv('supp.txt', 5):
        w = w.strip()
        if w in D: continue
        D[w] = {'w': w, 'p': p.strip(), 'hv': hv_word(w, p.strip()), 'pos': pos.strip(),
                'en': en.strip(), 'vn': vn.strip(), 'kind': 'extra', 'no': '', 'ls': []}
    # tên nhân vật
    NAMES = {}
    for w, p, note in read_tsv('names.txt', 3):
        NAMES[w.strip()] = {'w': w.strip(), 'p': p.strip(), 'hv': hv_word(w.strip(), p.strip()),
                            'note': note.strip()}
    print('dict %d  names %d  no-gloss %d' % (len(D), len(NAMES), len(warn_nogloss)))
    if warn_nogloss: print('  MISSING GLOSS:', ' '.join(warn_nogloss[:40]))

    # ── token hoá ────────────────────────────────────────────────────────────
    NAMEKEYS = sorted(NAMES, key=len, reverse=True)
    DKEYS = D
    def seg(s, lesson_vocab):
        out = []; i = 0; n = len(s)
        while i < n:
            c = s[i]
            if c in PUNCT:
                out.append({'w': c, 'k': 'punct'}); i += 1; continue
            if not CJK.match(c):
                j = i
                while j < n and not CJK.match(s[j]) and s[j] not in PUNCT: j += 1
                chunk = s[i:j]
                if chunk in DKEYS:
                    out.append({'w': chunk, 'p': DKEYS[chunk]['p'],
                                'k': 'core' if chunk in lesson_vocab else 'extra'})
                else:
                    out.append({'w': chunk, 'k': 'plain'})
                i = j; continue
            hit = None
            for L in range(min(6, n - i), 1, -1):          # tên riêng >= 2 chữ
                if s[i:i+L] in NAMES: hit = ('name', s[i:i+L]); break
            if not hit:
                for L in range(min(6, n - i), 0, -1):
                    cand = s[i:i+L]
                    if cand in DKEYS: hit = ('dict', cand); break
            if hit and hit[0] == 'name':
                w = hit[1]
                out.append({'w': w, 'p': NAMES[w]['p'], 'k': 'name'}); i += len(w); continue
            if hit:
                w = hit[1]
                out.append({'w': w, 'p': DKEYS[w]['p'],
                            'k': 'core' if w in lesson_vocab else 'extra'}); i += len(w); continue
            out.append({'w': c, 'p': py_of(c), 'k': 'plain'}); i += 1
        return out

    TYPO = {'如王': '如玉', '知王': '如玉'}
    lessons = []
    stat_plain = collections.Counter()
    for lid in LESSONS:
        L = data[lid]
        lesson_vocab = set()
        for v in L['vocab']:
            for x in re.split('[/／（）()、]', v['w']):
                x = re.sub(r'[＋+~～\s]', '', x).strip()
                if x: lesson_vocab.add(x)
        texts = []
        for t in L['texts']:
            blocks = []
            for turn in t['turns']:
                sp = turn.get('sp')
                if sp: sp = TYPO.get(sp, sp)
                zh = turn['zh']
                for a, b in TYPO.items(): zh = zh.replace(a, b)
                blk = {'type': 'line' if sp else 'para', 'tk': seg(zh, lesson_vocab)}
                if sp:
                    blk['sp'] = sp
                    blk['spp'] = NAMES.get(sp, {}).get('p', py_of(sp))
                    blk['spn'] = NAMES.get(sp, {}).get('note', '')
                blocks.append(blk)
                for x in blk['tk']:
                    if x['k'] == 'plain' and CJK.search(x['w']): stat_plain[x['w']] += 1
            texts.append({'zh': t['zh_label'], 'vn': t['vn_label'],
                          'kind': t['kind'], 'blocks': blocks})
        gram = merge_grammar(L['grammar'])
        lessons.append({
            'id': lid, 'book': L['book'], 'no': int(lid.split('-L')[1]), 'seq': seq[lid],
            'title': L['title']['zh'] or lid, 'py': L['title']['py'] or '',
            'en': L['title']['en'] or '', 'vn': '',
            'texts': texts, 'grammar': gram,
            'vocab': [v['w'] for v in L['vocab']
                      for v in [dict(v, w=re.sub(r'[＋+~～\s]', '',
                                                 re.split('[/／（）()、]', v['w'])[0]).strip())]],
        })
    print('un-lookupable plain chars left:', len(stat_plain), sum(stat_plain.values()),
          ''.join(list(stat_plain)[:40]))
    out = {'dict': D, 'names': NAMES, 'lessons': lessons}
    json.dump(out, open('reader.json', 'w', encoding='utf-8'), ensure_ascii=False,
              separators=(',', ':'))
    print('reader.json %.1f KB' % (os.path.getsize('reader.json') / 1024.0))
    nohv = [w for w, e in D.items() if not e['hv'] and CJK.search(w)]
    print('no hanviet:', len(nohv), ' '.join(nohv[:20]))

if __name__ == '__main__':
    build()
