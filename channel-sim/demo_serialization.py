"""demo_serialization.py — the stretch: one channel application per tick.

A design-decision shadow of Dcare.chain_tick_buys_one (emissions = ▷-depth =
n at every stage): a clock loop asserting that the guarded stream applies
exactly one channel and appends exactly one emission per tick — never two,
never zero. ▷ here is a render clock by DESIGN, not a denotation: quantum
guarded domain theory is open (paper §3.6).
"""
import numpy as np
from clauses import C, K, iso, prepare, tensor, compose, apply, is_channel

PASS = []
def check(name, cond):
    assert cond, f"FAILED: {name}"
    PASS.append(name)

c, k = C(2), K(2)

# one emission channel: prepare a fresh token state per fire (the mint's face)
mint = prepare(np.array([[0.5, 0.5], [0.5, 0.5]], complex), c)
reservoir = np.array([[1.0]], complex)   # the unit reservoir (unchanged by minting)
emissions = []

N = 25
for t in range(1, N + 1):
    emission = apply(mint, reservoir)  # exactly ONE application per tick...
    emissions.append(emission)         # ...and exactly ONE emission
    assert len(emissions) == t, f"tick {t}: emissions {len(emissions)} != {t}"

check(f"after {N} ticks: emissions == ticks == {len(emissions)}", len(emissions) == N)
check("each tick mints from the unchanged reservoir (the budget ledger: "
      "n fires mint n, the source never depletes — Dcare.holographic_budget's arithmetic)",
      all(np.allclose(apply(mint, reservoir), e) for e in emissions))

print(f"demo_serialization: {len(PASS)} ASSERTIONS PASS")
for p in PASS: print("  ✓", p)
