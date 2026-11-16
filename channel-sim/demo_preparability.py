"""demo_preparability.py — C3: you cannot copy along a structure you have
not chosen.

The Wootters–Zurek unknown-state clause, executable: basis states (blanks —
the closed inhabitants of paper §3.1) copy perfectly along a chosen
structure; superpositions (unknowns) do not; and the builder refuses the
copy clause outright on a quantum object.
"""
import numpy as np
from clauses import C, K, ClauseError, copy, apply

PASS = []
def check(name, cond):
    assert cond, f"FAILED: {name}"
    PASS.append(name)

k = K(2)
copier = copy(k)   # contr at the classical sort: legal, measure-and-prepare

# blanks copy perfectly: the closed inhabitants (T4's 'nil' is the blank record)
for i, basis_state in enumerate([np.array([[1, 0], [0, 0]], complex),
                                 np.array([[0, 0], [0, 1]], complex)]):
    out = apply(copier, basis_state)
    target = np.zeros((4, 4), complex); target[i*2 + i, i*2 + i] = 1.0   # |ii><ii|
    check(f"basis state |{i}> copies with fidelity 1",
          abs(np.trace(out @ target)) > 1 - 1e-9)

# unknowns do not: the superposition comes out as the dephased mixture
sup = np.array([[.5, .5], [.5, .5]], complex)
out = apply(copier, sup)
plus_plus = np.outer([1/np.sqrt(2), 1/np.sqrt(2), 0, 0],
                     [1/np.sqrt(2), 1/np.sqrt(2), 0, 0]).astype(complex)
fid = np.real(np.trace(out @ plus_plus))
check(f"a superposition does NOT copy (fidelity {fid:.3f} < 0.99)", fid < 0.99)
mixture = np.diag([0.5, 0, 0, 0.5]).astype(complex)
check("what the copier does instead: the measure-and-prepare mixture",
      np.allclose(out, mixture))

# the builder refuses the quantum object outright
try:
    copy(C(2))
    check("copy on a quantum object: REFUSED", False)
except ClauseError as e:
    check("copy on a quantum object: REFUSED", "not chosen" in str(e))

print(f"demo_preparability: {len(PASS)} ASSERTIONS PASS")
for p in PASS: print("  ✓", p)
