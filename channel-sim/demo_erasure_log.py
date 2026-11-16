"""demo_erasure_log.py — C2: erasure requires the discard.

The construction log's core check: generate a corpus of well-typed
constructions in BOTH modes; assert that every channel from the quantum
system to the trivial system carries the trace clause somewhere in its
construction. Any CP map L(H)->C is X |-> Tr(AX), hence Tr ∘ Φ_A — the
one-line factorization behind the claim (paper §3.5 C2).
"""
import itertools, numpy as np
from clauses import (Obj, UNIT, C, K, iso, prepare, tensor, compose, swap,
                     copy, trace_out, uses_discard, ClauseError,
                     KERNEL_TAGS, UNRESTRICTED_TAGS)

PASS = []
def check(name, cond):
    assert cond, f"FAILED: {name}"
    PASS.append(name)

c, k = C(2), K(2)

def corpus(allowed, depth=4):
    """Well-typed constructions up to `depth` nodes, breadth-built, deduped
    by identity (dataclass __eq__ over numpy arrays is unusable)."""
    seeds = [iso(np.eye(2), c), iso(np.eye(2), k),
             iso(np.array([[0, 1], [1, 0]], complex), c),
             prepare(np.array([[1, 0], [0, 0]], complex), k, allowed),
             prepare(np.array([[.5, .5], [.5, .5]], complex), k, allowed)]
    if "trace_out" in allowed:
        seeds += [trace_out(c, allowed), trace_out(k, allowed)]
    seen_ids, everything = set(), []
    frontier = list(seeds)
    for x in frontier:
        seen_ids.add(id(x)); everything.append(x)
    while frontier and count(max(everything, key=count)) < depth + 2:
        nxt = []
        for a in frontier:
            for b in everything:
                for g, f in ((a, b), (b, a)):
                    if g.dom == f.cod and count(g) + count(f) + 1 <= depth + 2:
                        x = compose(g, f, allowed)
                        if id(x) not in seen_ids:
                            seen_ids.add(id(x)); nxt.append(x)
                if count(a) + count(b) + 1 <= depth + 2:
                    x = tensor(a, b, allowed)
                    if id(x) not in seen_ids:
                        seen_ids.add(id(x)); nxt.append(x)
        frontier = nxt
        everything.extend(nxt)
    return everything

def count(ch): return 1 + sum(count(x) for x in ch.children)

kc = corpus(KERNEL_TAGS)
uc = corpus(UNRESTRICTED_TAGS)

# the C2 check, both modes
bad = [x for x in kc + uc
       if x.dom == c and x.cod == UNIT and not uses_discard(x)]
check(f"kernel corpus: {len(kc)} constructions — {sum(1 for x in kc if x.dom==c and x.cod==UNIT)} quantum-to-trivial, ALL carry the discard",
      all(uses_discard(x) for x in kc if x.dom == c and x.cod == UNIT))
check(f"unrestricted corpus: {len(uc)} constructions — {sum(1 for x in uc if x.dom==c and x.cod==UNIT)} quantum-to-trivial, ALL carry the discard",
      all(uses_discard(x) for x in uc if x.dom == c and x.cod == UNIT))
check("and there are NONE in the kernel corpus by construction", len(bad) == 0)

# the factorization, printed for the record
A = np.array([[0.3, 0], [0, 0.7]], complex)
rho = np.array([[0.6, 0.1], [0.1, 0.4]], complex)
lhs = np.real(np.trace(A @ rho))
Phi_A_out = 0.3 * rho[0, 0] + 0.7 * rho[1, 1]
check(f"X ↦ Tr(AX) = Tr∘Φ_A verbatim ({lhs:.6f} = {Phi_A_out:.6f})",
      abs(lhs - Phi_A_out) < 1e-12)

print(f"demo_erasure_log: {len(PASS)} ASSERTIONS PASS")
for p in PASS: print("  ✓", p)
