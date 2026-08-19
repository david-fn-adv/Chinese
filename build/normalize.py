# -*- coding: utf-8 -*-
"""Normalise raw3.json -> clean.json : patch bad vocab, drop pseudo-texts,
split variant headwords, attach lesson metadata."""
import json, re, collections

CJK = re.compile('[㐀-䶿一-鿿]')

# hand-patched entries the parser could not resolve (checked against the slides)
PATCH = {
    ('B1-L07', 'I-2'):   dict(w='KTV',   p='KTV',            pos='N',   en='karaoke (KTV)'),
    ('B1-L09', 'II-2'):  dict(w='月', p='yuè',      pos='N',   en='month of a year (number + 月)'),
    ('B1-L09', 'II-3'):  dict(w='号', p='hào',      pos='N',   en='date, day of a month (number + 号)'),
    ('B1-L13', 'II-14'): dict(w='哪里哪里', p='nǎlǐ nǎlǐ', pos='Idiom',
                              en="Don't mention it. It's my pleasure."),
    ('B2-L02', 'I-18'):  dict(w='台北101', p='Táiběi yāo líng yāo', pos='N',
                              en='Taipei 101, the tallest building in Taiwan'),
    ('B2-L02', 'I-20'):  dict(w='2号线', p='èr hào xiàn', pos='N',
                              en='Line 2 (of the Taipei MRT)'),
    ('B2-L03', 'II-3'):  dict(w='练习', p='liànxí', pos='V', en='to practice'),
    ('B2-L14', 'II-11'): dict(w='语法', p='yǔfǎ', pos='N', en='syntax, grammar'),
    ('B3-L08', 'II-49'): dict(w='分之', p='fēn zhī', pos='Ptc',
                              en='X 分之 Y, pattern for fractions and percentages'),
}

# loi chinh ta trong slide goc (da doi chieu voi phan con lai cua chinh bai do)
TEXT_FIX = {
    # B3-L09 dung 凤梨 13 lan va 风梨 5 lan trong cung mot bai -> 风 la go nham
    '风梨': '凤梨',
}

def fix_text(z):
    for a, b in TEXT_FIX.items(): z = z.replace(a, b)
    return z

# vocabulary-review list slides masquerading as texts
def is_wordlist(turns):
    if any(t.get('sp') for t in turns): return False
    joined = ' '.join(t['zh'] for t in turns)
    if not joined: return True
    seps = joined.count('、') + joined.count('；')
    return seps >= 6 and seps * 3 > len(CJK.findall(joined)) / 3.0

BOOK_TITLE = {1: ('基础', 'Nền tảng'), 2: ('生活', 'Đời sống'),
              3: ('社会', 'Xã hội')}

def main():
    raw = json.load(open('raw3.json', encoding='utf-8'))
    out = {}
    for lid, L in raw.items():
        vs = []
        for v in L['vocab']:
            key = (lid, v['no'])
            if key in PATCH: v = dict(v, **PATCH[key])
            if not v['w']: continue
            vs.append(v)
        for t in L['texts']:
            for tu in t['turns']: tu['zh'] = fix_text(tu['zh'])
        texts = [t for t in L['texts'] if not is_wordlist(t['turns'])]
        # 課文一 cua B3-L07 nam duoi dang anh trong .pptx -> dung ban chep tay
        if lid == 'B3-L07':
            from b3l07_text import as_text
            if not any(t['kind'] == 'dialogue' for t in texts):
                texts = [as_text()] + texts
        # label the texts
        labelled = []
        for i, t in enumerate(texts):
            if t['kind'] == 'dialogue':
                lab = ('对话一', 'HỘI THOẠI 1') if i == 0 else ('对话二', 'HỘI THOẠI 2')
                if L['book'] == 2 and i == 0: lab = ('对话', 'HỘI THOẠI')
            else:
                lab = ('短文', 'ĐOẠN VĂN')
            labelled.append(dict(t, zh_label=lab[0], vn_label=lab[1], idx=i))
        out[lid] = dict(L, vocab=vs, texts=labelled)
    json.dump(out, open('clean.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

    nv = sum(len(L['vocab']) for L in out.values())
    bad = [(lid, v['no']) for lid, L in out.items() for v in L['vocab'] if not v['w'] or not v['p']]
    print('lessons', len(out), 'vocab', nv, 'bad', len(bad), bad[:5])
    print('texts  ', sum(len(L['texts']) for L in out.values()))
    for lid, L in out.items():
        if len(L['texts']) != 2:
            print('  !! texts=', len(L['texts']), lid, [t['kind'] for t in L['texts']])
    # unique headwords, splitting variants
    words = collections.OrderedDict()
    for lid, L in out.items():
        for v in L['vocab']:
            for part in re.split('[/／（）()、]', v['w']):
                part = re.sub(r'[＋+~～\s]', '', part).strip()
                if part and (CJK.search(part) or re.match(r'^[A-Z0-9]+$', part)):
                    words.setdefault(part, []).append(lid)
    print('unique headwords', len(words))
    json.dump(list(words.items()), open('headwords.json', 'w', encoding='utf-8'), ensure_ascii=False)

if __name__ == '__main__':
    main()
