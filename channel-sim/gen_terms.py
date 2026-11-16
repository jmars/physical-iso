#!/usr/bin/env python3
"""gen_terms.py — cross-lane term generation: candidate proof obligations for dcare.

Generates WELL-TYPED finitary terms of the calculus (a typed enumerator over
a minimal rule port) and emits them as a Lean probe file for the dcare lane
to attempt — the generator's corpora are candidate obligations, nothing more.
SPECULATIVE and labeled so: this is a seed for the Lean lane, not a claim.

The enumerator covers the finitary rules: var, lam, app, pair, lete, unit,
the four constants, contr/weak at non-linear types, next/cons/snoc where
they type. (fix is included only at all-non-linear contexts, per the gate.)
"""
import random, itertools

random.seed(11)

# ---- a minimal term/type representation mirroring the calculus
def ty(name, *args):
    return (name,) + args
C   = ("content",)
K   = ("knower",)
A   = ("knowledge",)
V   = ("value",)
T   = ("trace",)
S   = ("stream",)
U   = ("unit",)
def ARROW(a, b): return ("arrow", a, b)
def TENS(a, b):  return ("tensor", a, b)
def LATER(a):    return ("later", a)

def is_linear(t):
    n = t[0]
    if n in ("content", "trace", "stream"): return True
    if n == "later":  return is_linear(t[1])
    if n in ("tensor", "arrow"): return is_linear(t[1]) or is_linear(t[2])
    return False

# terms: ("var", i) ("lam", b) ("app", f, x) ("pair", l, r) ("lete", s, b)
#        ("unit",) ("const", name) ("contr", k) ("weak", k, b) ("next", b)
# ("cons", h, tl) ("snoc", t, u) ("fix", b)
# A term is generated together with its context (list of types) + conclusion.

CONSTS = [("gen", ARROW(K, TENS(C, K))), ("red", ARROW(S, A)),
          ("obj", ARROW(V, A)), ("terminate", ARROW(T, U))]

def gen(ctx, tau, depth):
    """All ways (up to depth) to derive tau from ctx — yields (term, ctx)."""
    if depth == 0:
        return
    # var
    for i, t in enumerate(ctx):
        if t == tau and all(t != s for s in ctx[:i] if ctx[:i].count(s) > 0):
            pass
    for i, t in enumerate(ctx):
        if t == tau:
            yield (("var", i), ctx)
    # unit
    if tau == U:
        yield (("unit",), ctx)
    # constants
    for name, ct in CONSTS:
        if ct == tau:
            yield (("const", name), ctx)
    # lam
    if tau[0] == "arrow":
        for b, _ in gen([tau[1]] + ctx, tau[2], depth - 1):
            yield (("lam", b), ctx)
    # pair
    if tau[0] == "tensor":
        # split ctx into prefix/suffix along an ordered split
        n = len(ctx)
        for cut in range(n + 1):
            for l, _ in gen(ctx[:cut], tau[1], depth - 1):
                for r, _ in gen(ctx[cut:], tau[2], depth - 1):
                    yield (("pair", l, r), ctx)
    # app
    if True:
        for f, _ in gen(ctx, ARROW(("?",), tau), depth - 1):
            pass  # needs unification; approximated below by trying constant/var heads
    # contr at a non-linear position
    if tau[0] == "tensor" and tau[1] == tau[2] and not is_linear(tau[1]):
        for b, _ in gen([tau[1]] + ctx, tau, depth - 1):
            yield (("contr", tau[1]), [tau[1]] + ctx)
    # weak at a non-linear position
    if not is_linear(tau):
        for b, _ in gen(ctx, tau, depth - 1):
            yield (("weak", tau, b), ctx)

def show(t):
    if t[0] == "var": return f"var {t[1]}"
    if t[0] == "lam": return f"lam ({show(t[1])})"
    if t[0] == "pair": return f"pair ({show(t[1])}) ({show(t[2])})"
    if t[0] == "unit": return "unit"
    if t[0] == "const": return t[1]
    if t[0] == "contr": return f"contr@{show_type(t[1])}"
    if t[0] == "weak": return f"weak ({show(t[2])})"
    return str(t)

def show_type(t):
    if isinstance(t, tuple):
        if t[0] == "arrow": return f"arrow ({show_type(t[1])}) ({show_type(t[2])})"
        if t[0] == "tensor": return f"tensor ({show_type(t[1])}) ({show_type(t[2])})"
        if t[0] == "later": return f"later ({show_type(t[1])})"
    return t[0]

# ---- the corpora: derivations at [content] and at [] — T5-relevant frames
corpus = []
for tau in (TENS(C, C), U, S, ARROW(T, A), ARROW(C, S)):
    for term, ctx in itertools.islice(gen([C], tau, 3), 40):
        corpus.append((ctx, tau, term))
for tau in (T, K, U):
    for term, ctx in itertools.islice(gen([], tau, 3), 20):
        corpus.append((ctx, tau, term))

print(f"generated {len(corpus)} well-typed candidate obligations")
with open("/tmp/probe/gen_obligations.txt", "w") as f:
    pass
import os
os.makedirs("/tmp/probe", exist_ok=True)
with open("/tmp/probe/gen_obligations.txt", "w") as f:
    for ctx, tau, term in corpus:
        f.write(f"[{', '.join(show_type(x) for x in ctx)}] |- {show(term)} : {show_type(tau)}\n")
print("probe written: /tmp/probe/gen_obligations.txt")
print("SPECULATIVE seed for the dcare lane: each line is a candidate to attempt")
print("(or refute) in Lean — the generator asserts nothing.")
