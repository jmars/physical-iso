"""demo_two_modes.py — C1: the kernel/outside boundary as an executable switch.

Kernel mode (the trace clause absent): a search over well-typed clause
composites finds NO channel from the structureless quantum system to the
trivial system — the empirical twin of the semantic image of
Dcare.counterexample_not_noweak (the tree's syntactic fact: the killer's
last step IS a weak).

Unrestricted mode: the killer composite builds, uses the discard, and
evaluates to an erasing channel — output independent of input.
"""
import numpy as np
from clauses import (Obj, UNIT, C, K, ot, Chan, ClauseError,
                     iso, prepare, tensor, compose, swap, copy, trace_out,
                     uses_discard, apply, is_channel,
                     KERNEL_TAGS, UNRESTRICTED_TAGS, build_killer)

PASS = []
def check(name, cond):
    assert cond, f"FAILED: {name}"
    PASS.append(name)

c, k = C(2), K(2)

def count_nodes(ch):
    return 1 + sum(count_nodes(x) for x in ch.children)

def closure(seeds, allowed, max_nodes=5):
    """All well-typed composites and tensors of the seeds (plus basis copies
    where the clause set allows) up to a node budget. Deduped by identity."""
    seen_ids, everything = set(), []
    frontier = list(seeds)
    for x in frontier:
        seen_ids.add(id(x)); everything.append(x)
    while frontier:
        nxt = []
        for a in frontier:
            for b in everything:
                for pair in ((a, b), (b, a)):
                    g, f = pair
                    if g.dom == f.cod and count_nodes(g) + count_nodes(f) + 1 <= max_nodes:
                        try:
                            x = compose(g, f, allowed)
                        except ClauseError:
                            x = None
                        if x is not None and id(x) not in seen_ids:
                            seen_ids.add(id(x)); nxt.append(x)
                if count_nodes(a) + count_nodes(b) + 1 <= max_nodes:
                    x = tensor(a, b, allowed)
                    if id(x) not in seen_ids:
                        seen_ids.add(id(x)); nxt.append(x)
        frontier = nxt
        everything.extend(nxt)
    return everything

# ---- KERNEL: no route from the quantum system to the trivial system ----
seeds = [
    iso(np.eye(2), c), iso(np.eye(2), k),
    iso(np.array([[0, 1], [1, 0]], complex), c),                 # X on C
    iso(np.array([[1, 0], [0, -1]], complex), k),                # Z on K
    prepare(np.array([[1, 0], [0, 0]], complex), k, KERNEL_TAGS),
    prepare(np.array([[.5, .5], [.5, .5]], complex), k, KERNEL_TAGS),
]
corpus = closure(seeds, KERNEL_TAGS)
erasing_kernel = [x for x in corpus if x.dom == c and x.cod == UNIT]
check(f"kernel search: {len(corpus)} well-typed composites, NONE of them C -> unit",
      len(erasing_kernel) == 0)

try:
    trace_out(c, KERNEL_TAGS)
    check("the trace clause refuses outright in the kernel set", False)
except ClauseError:
    check("the trace clause refuses outright in the kernel set", True)

# ---- UNRESTRICTED: the killer builds and erases ----
killer = build_killer(UNRESTRICTED_TAGS)
check("the killer uses the discard", uses_discard(killer))
check("the killer is a trace-preserving channel", is_channel(killer))
rho0 = np.array([[1, 0], [0, 0]], complex)
rho1 = np.array([[0, 0], [0, 1]], complex)
sup  = np.array([[.5, .5], [.5, .5]], complex)
out0, out1, outs = apply(killer, rho0), apply(killer, rho1), apply(killer, sup)
check("orthogonal inputs give identical outputs (erasure)",
      np.allclose(out0, out1) and out0.shape == (1, 1))
check("the erasing channel forgets superpositions too", np.allclose(outs, out0))

print(f"demo_two_modes: {len(PASS)} ASSERTIONS PASS")
for p in PASS: print("  ✓", p)
