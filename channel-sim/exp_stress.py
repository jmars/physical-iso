"""exp_stress.py — falsification stress-test of the bridge's C2 invariant.

If §3.5's clause-level claim ("the only operation that erases is the discard")
is WRONG, this finds it before a referee does. Scales the erasure-log check
to d=3, deeper corpora, and randomized seed unitaries. Grammar-world
mathematics; see README.
"""
import numpy as np
from clauses import (Obj, UNIT, C, K, iso, prepare, tensor, compose,
                     trace_out, uses_discard, is_channel, ClauseError,
                     KERNEL_TAGS, UNRESTRICTED_TAGS)

rng = np.random.default_rng(7)
fails = 0
total_k = total_u = erase_u = 0

for d in (2, 3):
    c, k = C(d), K(d)
    for trial in range(4):
        # a random Haar-ish seed unitary on the quantum object
        z = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
        q, r = np.linalg.qr(z)
        U = q @ np.diag(np.diagonal(r) / np.abs(np.diagonal(r)))
        seeds = [iso(np.eye(d), c), iso(np.eye(d), k), iso(U, c),
                 prepare(np.outer([1] + [0]*(d-1), [1] + [0]*(d-1)).astype(complex), k, KERNEL_TAGS),
                 prepare(np.eye(d).astype(complex) / d, k, KERNEL_TAGS)]
        for allowed, name in ((KERNEL_TAGS, "kernel"), (UNRESTRICTED_TAGS, "unrestricted")):
            s = list(seeds)
            if "trace_out" in allowed:
                s += [trace_out(c, allowed), trace_out(k, allowed)]
            seen, everything, frontier = set(), [], list(s)
            for x in frontier:
                seen.add(id(x)); everything.append(x)
            for _ in range(3):                       # breadth rounds
                if len(everything) > 900: break
                nxt = []
                for a in frontier:
                    for b in everything:
                        for g, f in ((a, b), (b, a)):
                            if g.dom == f.cod:
                                x = compose(g, f, allowed)
                                if id(x) not in seen:
                                    seen.add(id(x)); nxt.append(x)
                        x = tensor(a, b, allowed)
                        if id(x) not in seen:
                            seen.add(id(x)); nxt.append(x)
                frontier = nxt; everything.extend(nxt)
            # every construction must be a trace-preserving channel (implementation check)
            for x in everything:
                if not is_channel(x):
                    print(f"FAIL TP: d={d} {name} tags={x.tag}")
                    fails += 1
            # the C2 invariant
            bad = [x for x in everything if x.dom == c and x.cod == UNIT and not uses_discard(x)]
            if bad:
                print(f"FAIL C2: d={d} {name}: {len(bad)} erasing constructions without the discard")
                fails += 1
            if name == "kernel":
                total_k += len(everything)
                nk = sum(1 for x in everything if x.dom == c and x.cod == UNIT)
                if nk: print(f"unexpected kernel erasures d={d}: {nk}"); fails += 1
            else:
                total_u += len(everything)
                erase_u += sum(1 for x in everything if x.dom == c and x.cod == UNIT)

print(f"stress: kernel constructions={total_k} (0 erasing, as claimed)")
print(f"stress: unrestricted constructions={total_u}, erasing={erase_u}, ALL carry the discard")
print("STRESS:", "PASS — C2 holds at every scale tried" if fails == 0 else f"{fails} FAILURES")
