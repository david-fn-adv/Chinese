# -*- coding: utf-8 -*-
"""Segment every running text against the cumulative vocabulary of the two books.
Reports leftover (un-lookupable) material so it can be closed out."""
import json, re, collections
from pypinyin import pinyin, Style

CJK = re.compile('[㐀-䶿一-鿿]')
PUNCT = set('。，、！？：；（）「」『』“”‘’—…·《》〈〉．,.!?:;()"\'-–~～/／　 ')

def load():
    return json.load(open('clean.json', encoding='utf-8'))

def build_dict(data):
    """headword -> {p, lessons:set, pos, en}"""
    D = {}
    order = sorted(data.keys())
    for lid in order:
        L = data[lid]
        for v in L['vocab']:
            variants = [re.sub(r'[＋+~～\s]', '', x).strip()
                        for x in re.split('[/／（）()、]', v['w'])]
            pys = [x.strip() for x in re.split(r'[/／]', v['p'] or '')]
            for i, part in enumerate(variants):
                if not part: continue
                if not (CJK.search(part) or re.match(r'^[A-Z0-9]+$', part)): continue
                p = pys[i] if i < len(pys) and pys[i] else (pys[0] if pys else '')
                e = D.setdefault(part, {'p': p, 'lessons': [], 'pos': v['pos'],
                                        'en': v['en'], 'no': v['no'], 'first': lid})
                if lid not in e['lessons']: e['lessons'].append(lid)
                if not e['p'] and p: e['p'] = p
    return D

def py_of(s):
    return ' '.join(x[0] for x in pinyin(s, style=Style.TONE, errors=lambda c: [[c]]))

def segment(s, D, maxlen=6):
    """longest-match-first over D; falls back to single chars"""
    out = []; i = 0; n = len(s)
    while i < n:
        c = s[i]
        if c in PUNCT:
            out.append({'w': c, 'k': 'punct'}); i += 1; continue
        if not CJK.match(c):
            j = i
            while j < n and not CJK.match(s[j]) and s[j] not in PUNCT: j += 1
            out.append({'w': s[i:j], 'k': 'plain'}); i = j; continue
        hit = None
        for L in range(min(maxlen, n - i), 0, -1):
            cand = s[i:i+L]
            if cand in D: hit = cand; break
        if hit:
            out.append({'w': hit, 'k': 'dict'}); i += len(hit)
        else:
            out.append({'w': c, 'k': 'raw'}); i += 1
    return out

def main():
    data = load()
    D = build_dict(data)
    print('dictionary entries:', len(D))
    leftover = collections.Counter()
    lev_ctx = {}
    tok_total = 0
    for lid, L in sorted(data.items()):
        for t in L['texts']:
            for turn in t['turns']:
                for tk in segment(turn['zh'], D):
                    tok_total += 1
                    if tk['k'] == 'raw':
                        leftover[tk['w']] += 1
                        lev_ctx.setdefault(tk['w'], (lid, turn['zh'][:34]))
                if turn.get('sp'):
                    for tk in segment(turn['sp'], D):
                        if tk['k'] == 'raw':
                            leftover[tk['w']] += 1
                            lev_ctx.setdefault(tk['w'], (lid, 'SPEAKER ' + turn['sp']))
    print('tokens:', tok_total)
    print('leftover distinct chars:', len(leftover), ' occurrences:', sum(leftover.values()))
    rows = []
    for ch, n in leftover.most_common():
        rows.append({'c': ch, 'n': n, 'py': py_of(ch), 'lid': lev_ctx[ch][0], 'ctx': lev_ctx[ch][1]})
    json.dump(rows, open('leftover.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for r in rows[:60]:
        print('  %s x%-3d %-8s %-8s %s' % (r['c'], r['n'], r['py'], r['lid'], r['ctx']))
    json.dump({k: {'p': v['p'], 'lessons': v['lessons'], 'pos': v['pos'], 'en': v['en'],
                   'no': v['no'], 'first': v['first']} for k, v in D.items()},
              open('dict.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

if __name__ == '__main__':
    main()
