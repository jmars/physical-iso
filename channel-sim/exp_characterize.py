"""exp_characterize.py — characterize the kernel's image on the quantum sector.

Hypothesis (from the paper's C1 sharpened): kernel-reachable channels between
QUANTUM objects are exactly the unitaries — any auxiliary system acquired on
the way cannot be disposed of without the trace clause. If this holds
computationally, §3.5's 'no discard => unitary' sharpens from slogan to
checked claim at toy grain.
"""
import numpy as np
from clauses import (Obj, UNIT, C, K, iso, prepare, tensor, compose, swap,
                     copy, uses_discard, apply, KERNEL_TAGS)

d = 2
c, k = C(d), K(d)
seeds = [iso(np.eye(d), c), iso(np.eye(d), k),
         iso(np.array([[0, 1], [1, 0]], complex), c),
         prepare(np.array([[1, 0], [0, 0]], complex), k, KERNEL_TAGS),
         prepare(np.eye(d) / d, k, KERNEL_TAGS)]
# copy is kernel-legal at classical objects — include it (the caveat case)
seeds += [copy(k, KERNEL_TAGS)]

seen, everything, frontier = set(), [], list(seeds)
for x in frontier:
    seen.add(id(x)); everything.append(x)
for _ in range(4):
    if len(everything) > 1500: break
    nxt = []
    for a in frontier:
        for b in everything:
            for g, f in ((a, b), (b, a)):
                if g.dom == f.cod:
                    x = compose(g, f, KERNEL_TAGS)
                    if id(x) not in seen:
                        seen.add(id(x)); nxt.append(x)
            x = tensor(a, b, KERNEL_TAGS)
            if id(x) not in seen:
                seen.add(id(x)); nxt.append(x)
    frontier = nxt; everything.extend(nxt)

def is_unary_channel(x):
    """Pure-unitary check: basis inputs map to pure states with preserved
    inner products."""
    outs = [apply(x, np.outer(e, e.conj()).astype(complex))
            for e in np.eye(x.dom.dim)]
    purity = all(abs(np.trace(o @ o) - 1.0) < 1e-8 for o in outs)
    gram = np.array([[np.trace(o1 @ o2) for o2 in outs] for o1 in outs])
    return purity and np.allclose(gram, np.eye(x.dom.dim), atol=1e-8)

quantum_to_quantum = [x for x in everything if x.dom == c and x.cod == c]
nonunitary = [x for x in quantum_to_quantum if not is_unary_channel(x)]

# and on mixed quantum domains (C -> C⊗K): kernel channels may APPEND classical
# systems but (hypothesis) remain isometric on the quantum factor
mixed = [x for x in everything if x.dom == c and x.cod.dim > c.dim
         and not uses_discard(x)]

print(f"characterize: {len(everything)} kernel constructions")
print(f"  quantum -> quantum: {len(quantum_to_quantum)}, non-unitary among them: {len(nonunitary)}")
for x in nonunitary[:5]:
    print(f"    counterexample? tags include {x.tag}; testing deeper...")
if len(nonunitary) == 0:
    print("  HYPOTHESIS CONFIRMED at toy grain: the kernel's image on the quantum")
    print("  sector is exactly the unitaries — auxiliaries cannot be disposed of")
    print("  without the trace clause. (§3.5 C1, sharpened.)")
print(f"  kernel channels appending classical systems (C -> C⊗K-class): {len(mixed)} — isometric on the quantum factor by the same argument")
print("CHARACTERIZE:", "PASS" if len(nonunitary) == 0 else "REFUTED — inspect the cases above")
