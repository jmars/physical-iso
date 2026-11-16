"""exp_cloner.py — the cloning line: exact refused, approximate is physics.

The calculus refuses the exact cloner everywhere (no_contraction_content and
kin). Standard quantum information — and the laboratory cloning program —
permits the OPTIMAL approximate 1->2 universal cloner, whose single-clone
output is the depolarizing channel with shrink 2/3 (fidelity 5/6 for every
pure input; the Buzek-Hillery class). Here: the refusal is exercised in the
clause set, and the 5/6 channel is EVALUATED AS DATA (its Kraus form) — we
do not claim a clause construction of it in this file.

Consistency with the formalism, NOT evidence for the grammar: the channel
layer is standard QM (see README).
"""
import numpy as np
from clauses import C, K, ClauseError, copy, KERNEL_TAGS, Chan, Obj, kraus, is_channel, apply

PASS = []
def check(name, cond):
    assert cond, f"FAILED: {name}"
    PASS.append(name)

c = C(2)

# --- the exact cloner: refused in the clause set
try:
    copy(c, KERNEL_TAGS)
    check("exact cloner refused on the quantum object (kernel set)", False)
except ClauseError:
    check("exact cloner refused on the quantum object (kernel set)", True)

# --- the optimal approximate single-clone channel, as DATA
# eta = 2/3 depolarizing: rho -> (2/3) rho + (1/3) I/2 = (5/6) rho + (1/6) rho~,
# single-clone fidelity 5/6 for every pure input.
eta = 2/3
paulis = [np.eye(2), np.array([[0, 1], [1, 0]], complex),
          np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]
# isotropic form: sum_i p_i sigma_i rho sigma_i with p_I = 1-eta=... use the
# Pauli-twirl form: p_I = 1/2+eta/4...? Use the direct Kraus: eigen-decomposition
# of the map rho -> eta rho + (1-eta) I/2 * Tr(rho): Kraus K0=sqrt(3eta/4) I, Ki=sqrt((1+eta)/4) sigma_i? 
# Standard: Kraus {sqrt(1-3p/4) I, sqrt(p/4) sigma_i} gives the Pauli channel with
# p_i = p/4; Pauli channel with p=... set 1-3q = eta_shrink? Pauli channel shrink
# for Bloch: (1-2q_total_nonidentity... For isotropic depolarizing eta, take
# q such that (1 - 3q/... simplest correct: eta = 1 - 4q with Kraus weights:
# K0 = sqrt(1-3q) I, Ki = sqrt(q) sigma_i gives Bloch shrink 1-4q... let q=(1-eta)/4.
q = (1 - eta) / 4
kraus_ops = [np.sqrt(1 - 3*q) * np.eye(2)] + [np.sqrt(q) * s for s in paulis[1:]]
dep = Chan("iso", c, c, (), tuple(kraus_ops))       # evaluated as data (tag irrelevant)

check("the 5/6 channel is trace-preserving (a legal channel)", is_channel(dep))
check("...and its Kraus set is exactly the Pauli form with shrink 2/3",
      abs(kraus(dep)[0][0, 0] ** 2 - (1 - 3*q)) < 1e-12)

for vec in [np.array([1, 0]), np.array([0, 1]),
            np.array([1, 1]) / np.sqrt(2), np.array([1, 1j]) / np.sqrt(2)]:
    rho = np.outer(vec, vec.conj()).astype(complex)
    out = apply(dep, rho)
    f = np.real(np.trace(out @ rho))
    check(f"input [{vec[0]:.2f},{vec[1]:.2f}] clones at fidelity {f:.4f} (5/6 = {5/6:.4f})",
          abs(f - 5/6) < 1e-9)

print(f"exp_cloner: {len(PASS)} ASSERTIONS PASS")
for p in PASS: print("  ✓", p)
print("\nThe grammar's line is exactness: the exact cloner is refused outright;")
print("the optimal approximate machine's single-clone channel (5/6, the measured")
print("laboratory ceiling) is legal channel data. Consistent with the formalism;")
print("NOT evidence for the grammar — the layer is standard QM.")
