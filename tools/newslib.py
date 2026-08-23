# -*- coding: utf-8 -*-
"""Thư viện chung cho luồng tin tức hằng ngày. Hợp đồng: tools/daily-news.md"""
import os, re, json, importlib.util

ROOT    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
READER  = os.path.join(ROOT, 'data', 'reader.json')
NEWSDIR = os.path.join(ROOT, 'news')
TPL     = os.path.join(ROOT, 'build', 'template.html')
OUT     = os.path.join(ROOT, 'index.html')

NEWS_BOOK  = 4
NEWS_LABEL = {'b': NEWS_BOOK, 'title': '新闻', 'vn': 'Tin tức', 'label': 'TIN'}

HAN_RE  = re.compile(r'[㐀-䶿一-鿿]')
PUNCT   = set('，。！？；：、“”‘’（）《》〈〉…—·「」【】〔〕％'
              ',.!?;:()<>"\'')

# ────────────────────────── Hán Việt ──────────────────────────
def _mod(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

_CH = None; _W = None
def _hv_init():
    global _CH, _W
    if _CH is not None: return
    base = _mod(os.path.join(ROOT, 'build', 'hanviet.py'), 'hanviet_base')
    _CH = dict(base.load_chars())
    _W  = dict(base.WORD_HV)
    ext = os.path.join(ROOT, 'tools', 'hanviet_ext.py')
    if os.path.exists(ext):
        e = _mod(ext, 'hanviet_ext')
        for tok in e.CHARS_EXT.split():
            if ':' in tok:
                c, v = tok.split(':', 1)
                if c and v: _CH[c] = v
        _W.update(getattr(e, 'WORD_EXT', {}))

def hv(word):
    """Âm Hán Việt. Trả '' nếu có chữ chưa có âm — KHÔNG đoán."""
    _hv_init()
    if word in _W: return _W[word]
    out = []
    for c in word:
        if c in _CH: out.append(_CH[c])
        elif HAN_RE.match(c): return ''
    return ' '.join(out)

def hv_missing(word):
    _hv_init()
    if word in _W: return []
    return [c for c in word if HAN_RE.match(c) and c not in _CH]

# ────────────────────────── pinyin ──────────────────────────
def py(word):
    from pypinyin import pinyin, Style
    if not HAN_RE.search(word): return ''
    return ''.join(x[0] for x in pinyin(word, style=Style.TONE))

# ────────────────────────── dữ liệu ──────────────────────────
def load_reader():
    with open(READER, encoding='utf-8') as f: return json.load(f)

def news_files():
    if not os.path.isdir(NEWSDIR): return []
    return sorted(os.path.join(NEWSDIR, f) for f in os.listdir(NEWSDIR)
                  if re.fullmatch(r'\d{4}-\d{2}-\d{2}\.json', f))

def load_news():
    out = []
    for p in news_files():
        with open(p, encoding='utf-8') as f:
            d = json.load(f); d['_path'] = p
        out.append(d)
    return out

def known_before(path):
    """Tập từ người học đã biết TRƯỚC bài này: 42 bài sách + mọi bài tin trước đó."""
    k = set(load_reader()['dict'])
    for p in news_files():
        if os.path.basename(p) >= os.path.basename(path): break
        with open(p, encoding='utf-8') as f: k |= set(json.load(f).get('dict', {}))
    return k

# ────────────────────────── tách từ ──────────────────────────
def tokenize(text, lexicon, names=()):
    """Khớp tham lam dài nhất theo từ điển; phần còn lại trả về để người viết xử lý.

    Trả (tokens, unknown) — unknown là các đoạn chữ Hán không khớp từ điển nào.
    """
    lex = set(lexicon) | set(names)
    maxlen = max((len(w) for w in lex), default=1)
    toks, unk, i, n = [], [], 0, len(text)
    while i < n:
        ch = text[i]
        if ch.isspace(): i += 1; continue
        if ch in PUNCT:
            toks.append({'w': ch, 'k': 'punct'}); i += 1; continue
        if not HAN_RE.match(ch):                      # số, chữ Latinh, %
            j = i                                     # giữ dấu cách BÊN TRONG đoạn
            while j < n and not HAN_RE.match(text[j]) and text[j] not in PUNCT: j += 1
            seg = text[i:j].rstrip()
            toks.append({'w': seg, 'k': 'plain'}); i = i + len(seg); continue
        hit = None
        for L in range(min(maxlen, n - i), 0, -1):
            if text[i:i+L] in lex: hit = text[i:i+L]; break
        if hit:
            toks.append({'w': hit, 'k': 'name' if hit in names else 'hit'})
            i += len(hit); continue
        j = i                                          # đoạn chưa tra được
        while j < n and HAN_RE.match(text[j]):
            found = False
            for L in range(min(maxlen, n - j), 0, -1):
                if text[j:j+L] in lex: found = True; break
            if found: break
            j += 1
        unk.append(text[i:j])
        toks.append({'w': text[i:j], 'k': 'plain'})
        i = j
    return toks, unk

def suggest(seg):
    """Gợi ý cách tách một đoạn chưa tra được, bằng jieba."""
    import jieba; jieba.setLogLevel(60)
    return [w for w in jieba.cut(seg) if w.strip()]

def finish_tokens(toks, dic, vocab, names):
    """Gán k = core/extra/name/punct/plain và pinyin, theo đặc tả khuôn mẫu."""
    voc = set(vocab)
    out = []
    for t in toks:
        w = t['w']
        if t['k'] == 'punct': out.append({'w': w, 'k': 'punct'}); continue
        if t['k'] == 'name' or w in names:
            out.append({'w': w, 'p': names[w]['p'], 'k': 'name'}); continue
        if w in dic:
            out.append({'w': w, 'p': dic[w]['p'], 'k': 'core' if w in voc else 'extra'})
            continue
        out.append({'w': w, 'k': 'plain'})
    return out

# ────────────────────────── đo mật độ ──────────────────────────
def density(lesson, known):
    """(%loại từ mới, %lượt chữ mới, chi tiết) — mẫu số bỏ dấu câu và token plain."""
    real = [x for t in lesson['texts'] for b in t['blocks'] for x in b['tk']
            if x.get('k') in ('core', 'extra', 'name')]
    types = {}
    for x in real: types[x['w']] = types.get(x['w'], 0) + 1
    namew = set(x['w'] for x in real if x.get('k') == 'name')
    new_types = [w for w in types if w not in known and w not in namew]
    new_tok   = sum(types[w] for w in new_types)
    ntok, ntyp = len(real), len(types)
    return (100.0*len(new_types)/ntyp if ntyp else 0.0,
            100.0*new_tok/ntok if ntok else 0.0,
            {'tokens': ntok, 'types': ntyp, 'new_types': len(new_types),
             'new_tokens': new_tok, 'new_list': sorted(new_types)})

def han_count(lesson):
    return sum(len(HAN_RE.findall(x['w']))
               for t in lesson['texts'] for b in t['blocks'] for x in b['tk'])

# ────────────────────────── gộp ──────────────────────────
def merge():
    """reader.json + news/*.json -> db hoàn chỉnh cho template."""
    db = load_reader()
    seq = len(db['lessons'])
    for nf in load_news():
        for w, v in nf.get('dict', {}).items():
            if w in db['dict']:
                for lid in v.get('ls', []):
                    if lid not in db['dict'][w]['ls']: db['dict'][w]['ls'].append(lid)
            else:
                db['dict'][w] = v
        db['names'].update(nf.get('names', {}))
        l = nf['lesson']; seq += 1
        l['seq'] = seq; l['book'] = NEWS_BOOK
        db['lessons'].append(l)
    return db
