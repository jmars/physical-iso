#!/usr/bin/env python3
"""explorer.py — the semantic bridge as a playground (self-contained; numpy only).

A derivation-of-care program artifact — the interactive companion to
"Conservation as Grammar" §3.5. Try to build a cloner: it refuses. Try to
erase in the calculus's own mode: it refuses — unless you first carry the
token into a discardable sector. Grammar-world mathematics, never physics.

Run:  python explorer.py
Help: 'help' inside.  The three modes:
  kernel    no discard at all
  calculus  the calculus's own rule set: discard at CLASSICAL objects only
  affine    discard at every object (the CPM table row at full generality)
"""
import numpy as np

# ---------------- the clause core (embedded; mirrors channel-sim/clauses.py)

class Obj:
    def __init__(self, dim, classical=False):
        self.dim, self.classical = dim, classical
    def __repr__(self):
        return ("K" if self.classical else "C") + str(self.dim)
    def __eq__(self, o):
        return isinstance(o, Obj) and self.dim == o.dim and self.classical == o.classical
    def __hash__(self):
        return hash((self.dim, self.classical))

UNIT = Obj(1, True)
def C(d=2): return Obj(d, False)
def K(d=2): return Obj(d, True)
def ot(a, b): return Obj(a.dim * b.dim, a.classical and b.classical)

KERNEL, CALCULUS, AFFINE = "kernel", "calculus", "affine"

class ClauseError(Exception): pass

class Chan:
    def __init__(self, tag, dom, cod, children=(), data=()):
        self.tag, self.dom, self.cod = tag, dom, cod
        self.children, self.data = children, data
    def __repr__(self):
        return f"({self.tag} : {self.dom} -> {self.cod})"

def gate(mode, o):
    if mode == CALCULUS and not o.classical:
        raise ClauseError("REFUSED: the calculus's discard is gated to classical "
                          "objects — the token is spent, never weakened")

def iso(U, dom, mode=None):
    U = np.asarray(U, complex)
    assert np.allclose(U @ U.conj().T, np.eye(dom.dim))
    return Chan("iso", dom, dom, (), (U,))

def prepare(sigma, cod, mode=None):
    return Chan("prepare", UNIT, cod, (), (np.asarray(sigma, complex),))

def tensor(a, b, mode=None): return Chan("tensor", ot(a.dom, b.dom), ot(a.cod, b.cod), (a, b))
def compose(g, f, mode=None):
    if f.cod is not g.dom and f.cod != g.dom:
        raise ClauseError(f"ill-typed composition {f.dom}->{f.cod} then {g.dom}->{g.cod}")
    return Chan("compose", f.dom, g.cod, (g, f))
def swap(o1, o2, mode=None):
    d1, d2 = o1.dim, o2.dim
    U = np.zeros((d1*d2, d1*d2), complex)
    for i in range(d1):
        for j in range(d2):
            U[j*d1+i, i*d2+j] = 1
    return Chan("swap", ot(o1, o2), ot(o2, o1), (), (U,))

def copy(o, mode=None):
    if not o.classical:
        raise ClauseError("REFUSED: copying needs a chosen structure — you cannot "
                          "copy along a structure you have not chosen")
    d = o.dim
    kraus = []
    for i in range(d):
        Km = np.zeros((d*d, d), complex); Km[i*d+i, i] = 1; kraus.append(Km)
    return Chan("copy", o, ot(o, o), (), tuple(kraus))

def trace_out(o, mode=AFFINE):
    if mode == KERNEL:
        raise ClauseError("REFUSED: the kernel bans the discard outright")
    gate(mode, o)
    kraus = tuple(np.eye(1, o.dim, k, dtype=complex) for k in range(o.dim))
    return Chan("trace_out", o, UNIT, (), kraus)

def readout(mode=None):
    c, k = C(2), K(2)
    kraus = []
    for i in range(2):
        v = np.eye(1, 2, i, dtype=complex).reshape(2)
        kraus.append(np.outer(v, v.conj()))
    return Chan("readout", c, k, (), tuple(kraus))

def kraus_of(ch):
    t = ch.tag
    if t in ("iso", "swap"): return ch.data
    if t == "prepare":
        s = ch.data[0]; w, v = np.linalg.eigh(s)
        return tuple(np.sqrt(max(w[i], 0)) * v[:, i:i+1] for i in range(s.shape[0]))
    if t == "tensor":
        a, b = ch.children
        return tuple(np.kron(x, y) for x in kraus_of(a) for y in kraus_of(b))
    if t == "compose":
        g, f = ch.children
        return tuple(Kg @ Kf for Kg in kraus_of(g) for Kf in kraus_of(f))
    if t in ("copy", "trace_out", "readout"): return ch.data
    raise ClauseError(f"unknown clause {t}")

def apply(ch, rho):
    out = np.zeros((ch.cod.dim, ch.cod.dim), complex)
    for K in kraus_of(ch):
        out += K @ np.asarray(rho, complex) @ K.conj().T
    return out

def uses_discard(ch):
    return ch.tag == "trace_out" or any(uses_discard(c) for c in ch.children)
def discard_sites(ch):
    s = [ch.dom] if ch.tag == "trace_out" else []
    return s + [x for c in ch.children for x in discard_sites(c)]

# ---------------- the playground

c, k = C(2), K(2)
MODE = CALCULUS
BENCH = {}
HELP = """modes:  mode kernel | calculus | affine     (currently: {mode})
build:  NAME = <expr>            where <expr> uses:
          iso eye C2 | iso X C2 | prep0 K2 | prep+ K2 | prep0 C2
          copy K2 | readout | swap A B | A * B (tensor) | A >> B (compose)
          discard OBJ            (the discard — mode-gated)
try:    try <expr>              (evaluate without keeping)
run:    run NAME on <state>     (states: z0 z1 plus iplus; prints output)
log:    log NAME                (discard use + sites)
scenes: killer | cloner | clone-approx
        scene NAME              (loads the named scene into BENCH and runs it)
help | quit"""

def parse_and_build(expr, mode):
    expr = expr.strip().replace("discard C2", "discard:C2").replace("discard K2", "discard:K2")
    toks = expr.replace(">>", " >> ").replace("*", " * ").split()
    def build1(t):
        if t == "eye": return iso(np.eye(2), c)
        if t == "X": return iso(np.array([[0, 1], [1, 0]], complex), c)
        if t == "prep0": return prepare(np.array([[1, 0], [0, 0]], complex), k)
        if t == "prep+": return prepare(np.array([[.5, .5], [.5, .5]], complex), k)
        if t == "prep0C": return prepare(np.array([[1, 0], [0, 0]], complex), c)
        if t == "copy": return copy(k)
        if t == "readout": return readout()
        if t == "C2": return c
        if t == "K2": return k
        if t.startswith("discard"):
            obj = {"C2": c, "K2": k}.get(t.split(":")[1] if ":" in t else None)
            if obj is None:
                raise ClauseError("discard needs C2 or K2")
            return trace_out(obj, mode)
        if t in BENCH: return BENCH[t]
        raise ClauseError(f"unknown atom {t}")
    # simple left-to-right with * and >> (no precedence: parenthesize by order)
    val = build1(toks[0])
    i = 1
    while i < len(toks):
        op, nxt = toks[i], toks[i+1]
        if op == "*": val = tensor(val, build1(nxt))
        elif op == ">>": val = compose(build1(nxt), val)
        i += 2
    # a lone object token means nothing built; ignore
    return val

def scene(name):
    global MODE
    if name == "killer":
        MODE = CALCULUS
        killer = compose(trace_out(k, MODE), readout(), MODE)
        print("mode=calculus. The gated killer: readout (carry) >> discard K2 (drop the carrier).")
        print("  construction:", killer)
        out0 = apply(killer, np.array([[1, 0], [0, 0]], complex))
        out1 = apply(killer, np.array([[0, 0], [0, 1]], complex))
        print(f"  orthogonal inputs -> identical outputs: {np.allclose(out0, out1)}  (erasure)")
        print(f"  discard sites all classical: {[s.classical for s in discard_sites(killer)]}")
        print("  direct discard of C2 in this mode:")
        try:
            trace_out(c, MODE)
        except ClauseError as e:
            print("   ", e)
    elif name == "cloner":
        print("trying to clone the quantum token:")
        try:
            copy(c)
        except ClauseError as e:
            print("   ", e)
        print("cloning along a chosen basis (classical):")
        copier = copy(k)
        rho = np.array([[.5, .5], [.5, .5]], complex)
        out = apply(copier, rho)
        print("   superposition -> measure-and-prepare mixture diag", np.round(np.real(np.diag(out)), 3))
    elif name == "clone-approx":
        print("the lab-optimal approximate single-clone channel (fidelity 5/6), as data:")
        q = (1 - 2/3) / 4
        ks = [np.sqrt(1 - 3*q) * np.eye(2)] + [np.sqrt(q) * s for s in
             (np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex),
              np.array([[1, 0], [0, -1]], complex))]
        dep = Chan("iso", c, c, (), tuple(ks))
        for nm, vec in (("z0", [1, 0]), ("plus", [1, 1])):
            v = np.array(vec, complex); v = v / np.linalg.norm(v)
            rho = np.outer(v, v.conj())
            print(f"   fidelity for {nm}: {np.real(np.trace(apply(dep, rho) @ rho)):.4f}  (5/6 = 0.8333)")
        print("   the grammar's line is exactness; this is standard QM, not grammar evidence.")
    else:
        print("scenes: killer | cloner | clone-approx")

STATES = {"z0": np.array([[1, 0], [0, 0]], complex),
          "z1": np.array([[0, 0], [0, 1]], complex),
          "plus": np.array([[.5, .5], [.5, .5]], complex)}

print("the semantic bridge, interactive — 'help' for commands; 'scene killer' to start")
while True:
    try:
        line = input(f"[{MODE}]> ").strip()
    except (EOFError, KeyboardInterrupt):
        print(); break
    if not line: continue
    if line == "quit": break
    if line == "help":
        print(HELP.format(mode=MODE)); continue
    if line.startswith("mode "):
        m = line.split()[1]
        if m in (KERNEL, CALCULUS, AFFINE):
            MODE = m; print(f"mode = {MODE}")
            if m == KERNEL: print("  (the discard is banned outright)")
            if m == CALCULUS: print("  (the discard at classical objects only — the calculus's own gate)")
            if m == AFFINE: print("  (the discard at every object — the affine world)")
        continue
    if line.startswith("scene "):
        try: scene(line.split()[1])
        except Exception as e: print("  error:", e)
        continue
    try:
        if "=" in line and not line.startswith("try"):
            name, expr = [s.strip() for s in line.split("=", 1)]
            ch = parse_and_build(expr, MODE)
            BENCH[name] = ch
            print("built:", ch)
        elif line.startswith("try "):
            ch = parse_and_build(line[4:], MODE)
            print("evaluates to:", ch)
        elif line.startswith("log "):
            name = line.split()[1]
            ch = BENCH[name]
            print(f"  uses discard: {uses_discard(ch)}; sites: "
                  f"{[(str(s), 'classical' if s.classical else 'QUANTUM') for s in discard_sites(ch)]}")
        elif line.startswith("run "):
            parts = line.split()
            name = parts[1]
            st = parts[3] if len(parts) > 3 else "z0"
            out = apply(BENCH[name], STATES[st])
            print("  output:\n", np.round(out, 4))
        else:
            print("  (unknown command — 'help')")
    except ClauseError as e:
        print("  REFUSED:", e)
    except Exception as e:
        print("  error:", e)
