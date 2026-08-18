# -*- coding: utf-8 -*-
"""Extractor v3 -- texts detected independently of vocab groups. -> raw3.json"""
import sys, os, re, glob, json, difflib
from pptx import Presentation
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract2 import (BOOKS, CJK, CJKC, TONE, LAT, VNO, GNO, DIVIDERS, ROMAN,
                      clean, cjkonly, slide_texts, vocab_marker, parse_vocab, SPK)

EXER = re.compile(r'(（\s*）|\(\s*\)|是非题|True or False|'
                  r'^\d+\s*[\.．]|Please |Listen |Answer |Read the|Fill in|练习|'
                  r'Complete |Match |Write |Rearrange|Choose )')

def is_exercise(ls):
    txt = ' '.join(ls)
    if re.search(r'（\s{0,3}）|\(\s{0,3}\)', txt): return True
    if re.search(r'(True or False|是非题)', txt): return True
    n_num = sum(1 for l in ls if re.match(r'^[\(（]?\s*\d+\s*[\)）\.．]', l))
    if n_num >= 3: return True
    if re.match(r'^\d+\s*[\.．]\s*(Please|Listen|Read|Answer|Look|Fill|Complete|Match|Write)', txt): return True
    return False

def collect_texts(slides, vslide, gram_from):
    blocks = []
    for i in range(0, gram_from):
        if i in vslide: continue
        for s in slides[i]:
            ls = [l for l in s['lines'] if l and l not in DIVIDERS]
            if not ls: continue
            if GNO.match(ls[0]): continue
            cjk = sum(len(CJK.findall(l)) for l in ls)
            if cjk < 20: continue
            lat = sum(1 for l in ls if TONE.search(l))
            if lat > len(ls) / 2.0: continue
            if re.match(r'^第[一-鿿\d]+课$', ls[0]): continue
            if is_exercise(ls): continue
            blocks.append({'slide': i, 'lines': ls, 'norm': cjkonly(' '.join(ls))})
    # dedupe: exact containment, then near-duplicates
    keep = []
    for b in sorted(blocks, key=lambda x: (-len(x['norm']), x['slide'])):
        dup = False
        for k in keep:
            if b['norm'] in k['norm']:
                dup = True; break
            r = difflib.SequenceMatcher(None, b['norm'], k['norm']).quick_ratio()
            if r > 0.86 and difflib.SequenceMatcher(None, b['norm'], k['norm']).ratio() > 0.86:
                dup = True; break
        if not dup: keep.append(b)
    keep.sort(key=lambda x: x['slide'])
    # group slides that are adjacent (gap <= 1) into one text unit
    units = []
    for b in keep:
        if units and b['slide'] - units[-1]['slides'][-1] <= 1:
            units[-1]['lines'].extend(b['lines']); units[-1]['slides'].append(b['slide'])
        else:
            units.append({'lines': list(b['lines']), 'slides': [b['slide']]})
    return units

def split_speakers(block):
    joined = '  '.join(block)
    hits = [m for m in SPK.finditer(joined)]
    good = []
    for m in hits:
        pre = joined[:m.start()].rstrip()
        # a speaker tag starts a line (after our marker) or the string
        if pre == '' or pre.endswith('') or pre.endswith('。') or pre.endswith('！') \
           or pre.endswith('？') or pre.endswith('?') or pre.endswith('!'):
            good.append(m)
    if len(good) >= 2:
        out = []
        for i, m in enumerate(good):
            end = good[i+1].start() if i + 1 < len(good) else len(joined)
            body = re.sub(r'\s+', ' ', joined[m.end():end].replace('', ' ')).strip()
            if body: out.append({'sp': re.sub(r'\s', '', m.group(1)), 'zh': body})
        return out
    return [{'zh': re.sub(r'\s+', ' ', l).strip()} for l in block if len(cjkonly(l)) > 4]

def extract(book, lid, path):
    prs = Presentation(path)
    slides = [slide_texts(s) for s in prs.slides]
    vocab = []; vslide = {}
    for i, sts in enumerate(slides):
        m = vocab_marker(sts)
        if not m: continue
        v = parse_vocab(sts, m)
        vslide[i] = m
        if v is None or (not v['w'] and not v['p']): continue
        v['slide'] = i; vocab.append(v)
    gram = []
    for i, sts in enumerate(slides):
        if i in vslide: continue
        for s in sts:
            ls = [l for l in s['lines'] if l]
            if ls and GNO.match(ls[0]):
                gram.append({'slide': i, 'head': ls[0],
                             'body': [l for s2 in sts for l in s2['lines'] if l and l != ls[0]]})
                break
    gram_from = gram[0]['slide'] if gram else len(slides)
    title = {'zh': None, 'py': None, 'en': None, 'no': None}
    for sts in slides[:5]:
        flat = [l for s in sts for l in s['lines'] if l]
        for j, l in enumerate(flat):
            if re.match(r'^第[一-鿿]+课$', l) or re.match(r'^第\s*\d+\s*课$', l):
                title['no'] = l
                for r in flat[j+1:]:
                    if CJK.search(r) and title['zh'] is None and len(r) < 26: title['zh'] = r
                    elif TONE.search(r) and title['py'] is None: title['py'] = r
                    elif LAT.match(r) and title['en'] is None and len(r) > 3: title['en'] = r
        if title['zh']: break
    units = collect_texts(slides, vslide, gram_from)
    texts = []
    for u in units:
        turns = split_speakers(u['lines'])
        nsp = sum(1 for t in turns if t.get('sp'))
        if not turns: continue
        texts.append({'kind': 'dialogue' if nsp >= 2 else 'essay', 'nsp': nsp,
                      'slides': u['slides'], 'turns': turns})
    return {'id': lid, 'book': book, 'title': title, 'vocab': vocab,
            'texts': texts, 'grammar': gram, 'nslides': len(slides), 'gram_from': gram_from}

if __name__ == '__main__':
    out = {}
    for b, d in sorted(BOOKS.items()):
        for f in sorted(glob.glob(os.path.join(d, '*.pptx'))):
            lid = os.path.basename(f).replace('.pptx', '')
            r = extract(b, lid, f); out[lid] = r
            bad = [v for v in r['vocab'] if not v['w'] or not v['p']]
            print("%-8s %-13s v=%-3d bad=%-2d texts=%s g=%d" % (
                lid, (r['title']['zh'] or '??')[:13], len(r['vocab']), len(bad),
                [(t['kind'][:3], len(t['turns']), t['slides'][0]) for t in r['texts']], len(r['grammar'])))
    json.dump(out, open('raw3.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('\nVOCAB:', sum(len(v['vocab']) for v in out.values()),
          ' BAD:', sum(1 for v in out.values() for x in v['vocab'] if not x['w'] or not x['p']),
          ' TURNS:', sum(len(t['turns']) for v in out.values() for t in v['texts']),
          ' TEXTS:', sum(len(v['texts']) for v in out.values()))
