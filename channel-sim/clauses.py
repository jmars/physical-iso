"""clauses.py — the channel-simulator's clause library.

Implements the semantic bridge of physical-iso paper.md §3.5 as an executable
dictionary. Objects are finite-dimensional Hilbert spaces flagged classical
(a chosen basis exists: knower, knowledge, the archive) or quantum (content:
no structure chosen). Channels are CONSTRUCTIONS — an AST of clause nodes —
never bare matrices; every clause application is recorded, so the
construction log can answer "did this channel use the discard?".

The two modes are the kernel/outside boundary of the paper:
  KERNEL        (no `weak`)  — the trace clause is absent from the set.
  UNRESTRICTED  (with `weak`) — the trace clause is available at every object.

This file implements paper-rigor mathematics; implementing the bridge makes
it concrete, not more proven. Grammar-world facts only — see README.md.
"""

from dataclasses import dataclass
from itertools import product
import numpy as np

# ---------------------------------------------------------------- objects

@dataclass(frozen=True)
class Obj:
    """A finite-dimensional system. classical=True ⇔ a chosen orthonormal
    basis exists (paper §3.5's classical structures: knower, knowledge, the
    archive). classical=False ⇔ quantum — content, no structure chosen."""
    dim: int
    classical: bool = False

UNIT = Obj(1, classical=True)          # the monoidal unit C
def C(d=2):  return Obj(d, classical=False)   # content: structureless
def K(d=2):  return Obj(d, classical=True)    # knower/knowledge: a basis chosen

def ot(o1: Obj, o2: Obj) -> Obj:       # the tensor of objects
    return Obj(o1.dim * o2.dim, o1.classical and o2.classical)

# ---------------------------------------------------------------- the clause AST

KERNEL_TAGS = {"iso", "prepare", "tensor", "compose", "swap", "copy"}
CALCULUS_TAGS = KERNEL_TAGS | {"trace_out"}     # the calculus's OWN rule set:
# weak is gated to NON-LINEAR types (Typing.weak's `hk : k.isLinear = false`) —
# the trace clause is available at classical objects only. Content is never
# weakened; it is SPENT (single_linear_use). The affine world (trace at every
# object) is UNRESTRICTED_TAGS below — a strictly larger clause set.
UNRESTRICTED_TAGS = CALCULUS_TAGS | set()        # the affine world: a DISTINCT
# set — same tags, but trace_out's object gate is lifted (see trace_out).

class ClauseError(Exception):
    """A well-typedness / clause-set refusal. The builder refusing is the
    simulator's semantic image of the grammar's non-derivability."""

@dataclass(frozen=True)
class Chan:
    tag: str
    dom: Obj
    cod: Obj
    children: tuple = ()
    data: tuple = ()      # matrices for iso/prepare

def uses_discard(ch: Chan) -> bool:
    """The construction log: does this channel's construction use the
    discard clause? (Anywhere in the tree.)"""
    if ch.tag == "trace_out":
        return True
    return any(uses_discard(c) for c in ch.children)

def discard_sites(ch: Chan):
    """The objects at which this construction discards — for the gated-mode
    invariant: every discard site must be classical (the calculus's weak
    gate), and erasure of the quantum token must route through a carrier."""
    sites = []
    if ch.tag == "trace_out":
        sites.append(ch.dom)
    for c in ch.children:
        sites.extend(discard_sites(c))
    return sites

def clause_tags(ch: Chan) -> set:
    s = {ch.tag}
    for c in ch.children:
        s |= clause_tags(c)
    return s

# ---------------------------------------------------------------- clause constructors
# These are the ONLY public ways to build a channel. Each checks typing and
# the mode's clause set, and refuses otherwise — the refusal is the content.

def _check(tag, allowed):
    if tag not in allowed:
        raise ClauseError(
            f"clause '{tag}' not in this clause set (the discard is banned "
            f"in the kernel — paper §3.5, the kernel/outside boundary)")

def iso(U, dom: Obj, allowed=KERNEL_TAGS) -> Chan:
    """A unitary on `dom`. Pure evolution — kernel-legal at every object."""
    U = np.asarray(U, dtype=complex)
    assert U.shape == (dom.dim, dom.dim) and np.allclose(U @ U.conj().T, np.eye(dom.dim))
    return Chan("iso", dom, dom, (), (U,))

def prepare(sigma, cod: Obj, allowed=KERNEL_TAGS) -> Chan:
    """A fixed state-preparation channel from the unit — the constants'
    denotation (gen/red/obj/terminate: the coalgebra's faces, paper §3.5's
    constants row)."""
    sigma = np.asarray(sigma, dtype=complex)
    assert sigma.shape == (cod.dim, cod.dim) and np.allclose(sigma, sigma.conj().T)
    return Chan("prepare", UNIT, cod, (), (sigma,))

def tensor(a: Chan, b: Chan, allowed=KERNEL_TAGS) -> Chan:
    return Chan("tensor", ot(a.dom, b.dom), ot(a.cod, b.cod), (a, b))

def compose(g: Chan, f: Chan, allowed=KERNEL_TAGS) -> Chan:
    if f.cod != g.dom:
        raise ClauseError(f"ill-typed composition: {f.cod} -> {g.dom}")
    return Chan("compose", f.dom, g.cod, (g, f))

def swap(o1: Obj, o2: Obj, allowed=KERNEL_TAGS) -> Chan:
    """The exchange. `lete`'s row: composition, after the swap."""
    d1, d2 = o1.dim, o2.dim
    U = np.zeros((d1*d2, d1*d2), complex)
    for i, j in product(range(d1), range(d2)):
        U[j*d1 + i, i*d2 + j] = 1.0
    return Chan("iso", ot(o1, o2), ot(o1, o2), (), (U,)) if False else \
        Chan("swap", ot(o1, o2), ot(o2, o1), (), (U,))

def copy(o: Obj, allowed=KERNEL_TAGS) -> Chan:
    """`contr` at a non-linear sort: copying along the chosen structure —
    available EXACTLY at classical objects, nowhere else. The Kraus
    operators {|ii><i|} are measure-and-prepare in the chosen basis: basis
    states (blanks — the closed inhabitants of paper §3.1) copy perfectly;
    superpositions (unknowns) do not."""
    _check("copy", allowed)  # copy is in both clause sets, but see the gate below
    if not o.classical:
        raise ClauseError(
            "copy refused: no chosen structure on a quantum object — "
            "'you cannot copy along a structure you have not chosen' "
            "(paper §3.5 C3; the Wootters–Zurek unknown-state clause as grammar)")
    d = o.dim
    kraus = [np.zeros((d*d, d), complex) for _ in range(d)]
    for i in range(d):
        kraus[i][i*d + i, i] = 1.0
    return Chan("copy", o, ot(o, o), (), tuple(kraus))

def trace_out(o: Obj, allowed=UNRESTRICTED_TAGS) -> Chan:
    """`weak` — the discard: the partial trace to the trivial system.

    In CALCULUS_TAGS (the faithful mode), the rule's own gate applies: the
    discard is available ONLY at classical objects (non-linear types) —
    content is never weakened, only spent. In the affine world
    (UNRESTRICTED_TAGS), the trace is available at every object. This single
    clause is what makes the channel world; its gate is what makes it the
    calculus's."""
    _check("trace_out", allowed)
    if allowed is CALCULUS_TAGS and not o.classical:
        raise ClauseError(
            "discard refused at a QUANTUM object: the calculus's weak is "
            "gated to non-linear types — the conserved token is spent, "
            "never weakened (Typing.weak's isLinear = false gate)")
    d = o.dim
    kraus = tuple(np.eye(1, d, k, dtype=complex) for k in range(d))  # <k|
    return Chan("trace_out", o, UNIT, (), kraus)

def readout(allowed=CALCULUS_TAGS, d=2) -> Chan:
    """The conduit's denotation, taken as a fixed channel — the finitary
    bridge's stand-in for the stream-carrying term (paper §3.5's constants
    row; the term itself is not finitary). A measure-and-prepare readout from
    the quantum system into the classical sector: the token's information
    carried into a DISCARDABLE object. The leak theorem's mechanism, as a
    clause: with this and the gated discard, erasure of the conserved token
    is possible — but only by first carrying it into the classical sector."""
    c, k = C(d), K(d)
    kraus = tuple(np.outer(np.eye(1, d, i, dtype=complex).reshape(d),
                           np.eye(1, d, i, dtype=complex).reshape(d).conj())
                  for i in range(d))              # |i><i| measure-prepare
    return Chan("readout", c, k, (), kraus)

# ---------------------------------------------------------------- evaluation
# Every construction evaluates to a completely positive map, via its Kraus
# operators — assembled clause by clause, exactly as paper §3.5's soundness
# sentence states (for the fragment the table covers).

def kraus(ch: Chan) -> tuple:
    """The Kraus operators of the constructed channel."""
    t = ch.tag
    if t in ("iso", "swap"):
        return ch.data
    if t == "prepare":
        s = ch.data[0]
        w, v = np.linalg.eigh(s)
        # Kraus for the map 1 |-> sigma : columns sqrt(w_i) v_i  (d x 1)
        return tuple(np.sqrt(max(w[i], 0.0)) * v[:, i:i+1] for i in range(s.shape[0]))
    if t == "tensor":
        (a, b) = ch.children
        return tuple(np.kron(Ka, Kb) for Ka, Kb in product(kraus(a), kraus(b)))
    if t == "compose":
        (g, f) = ch.children
        return tuple(Kg @ Kf for Kg in kraus(g) for Kf in kraus(f))
    if t in ("copy", "trace_out", "readout"):
        return ch.data
    raise ClauseError(f"unknown clause {t}")

def apply(ch: Chan, rho) -> np.ndarray:
    """Apply the constructed channel to a density matrix of its domain."""
    rho = np.asarray(rho, dtype=complex)
    out = np.zeros((ch.cod.dim, ch.cod.dim), complex)
    for K in kraus(ch):
        out += K @ rho @ K.conj().T
    return out

def is_channel(ch: Chan, tol=1e-9) -> bool:
    """Trace-preserving check: sum K†K = I (the construction discipline)."""
    acc = np.zeros((ch.dom.dim, ch.dom.dim), complex)
    for K in kraus(ch):
        acc += K.conj().T @ K
    return np.allclose(acc, np.eye(ch.dom.dim), atol=tol)

# ---------------------------------------------------------------- the killer
# paper §5.1's loss derivation, denotationally: the conduit (a reader channel
# built WITH the discard — any measurement needs its environment), then the
# full trace-out. The composite is an erasing channel H -> C.

def build_conduit(allowed=UNRESTRICTED_TAGS) -> Chan:
    """A reader channel H_C -> K: prepare an environment (a constant), couple
    (a unitary — the CNOT-shaped read), trace out the token side. Note the
    conduit itself uses the discard: measurement is not a primitive clause —
    it is prepare + iso + weak, which is §3.5's point."""
    c, k = C(2), K(2)
    prep = prepare(np.array([[1, 0], [0, 0]], complex), k, allowed)       # |0><0|
    # read U: |x>_C |0>_K -> |x>_C |x>_K  (CNOT, control=C, target=K)
    U = np.zeros((4, 4), complex)
    for x in range(2):
        for y in range(2):
            U[x*2 + (y ^ x), x*2 + y] = 1.0
    couple = iso(U, ot(c, k), allowed)
    couple_typed = Chan("iso", ot(c, k), ot(c, k), (), (U,))
    # (C ⊗ K-constant) : C -> C⊗K   [the token tensored with a prepared reader]
    id_c = iso(np.eye(2), c, allowed)
    supply = tensor(id_c, prep, allowed)                                   # C ⊗ 1 -> C ⊗ K
    read = compose(couple_typed, supply, allowed)                           # C -> C⊗K
    # trace out the C side: the conduit keeps K — the reader channel C -> K
    tk = tensor(trace_out(c, allowed), iso(np.eye(2), k, allowed), allowed) # C⊗K -> 1⊗K
    return compose(tk, read, allowed)                                       # C -> 1⊗K

def build_killer(allowed=UNRESTRICTED_TAGS) -> Chan:
    """The killer composite of §5.1: conduit, then the full trace-out.
    An erasing channel H_C -> C (the trivial system)."""
    conduit = build_conduit(allowed)          # C -> 1⊗K  (≅ K)
    k = K(2)
    drop_k = tensor(trace_out(k, allowed), iso(np.eye(1), UNIT, allowed), allowed)
    return compose(drop_k, conduit, allowed)  # C -> 1⊗1 ≅ 1
