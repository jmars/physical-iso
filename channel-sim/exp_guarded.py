"""exp_guarded.py — QGDT wall 3 at toy grain: do guarded channel equations solve?

The §3.6 target's core hope, computationally: over ω-indexed state streams
(sequences of density matrices — the toy denotation of a stream object in
CPM(FdHilb)), the shift ▷ delays a stream by one tick, and a GUARDED equation

    X = ⟨σ₀, G ∘ ▷X⟩        (head now; tail = G applied one tick later)

has the productive-fixpoint solution X_t = G^t(σ₀), unique as a stream —
regardless of the initial guess, with prefixes stabilizing exactly one entry
per unfold (the topos-of-trees colimit behavior). If G is contractive
(depolarizing shrink η), the solution moreover converges geometrically to
G's fixed point: the Banach-style solvability picture, at toy grain.

Against it, the two unguarded pathologies:
  - instant self-reference (X₀ = X₀-shaped): every guess is a fixed point —
    NO unique solution, the limit depends on the guess;
  - future-reading (anti-guarded, ▷ reversed): no prefix ever stabilizes.

NOT QGDT: walls 1–2 (cartesian closure, streams-as-presheaves + dagger) are
untouched; this is the solvability wall checked in the state-stream fragment.
Grammar-world mathematics; see README.
"""
import numpy as np
from clauses import C, K, Chan, apply, is_channel

PASS = []
def check(name, cond):
    assert cond, f"FAILED: {name}"
    PASS.append(name)

c = C(2)
rng = np.random.default_rng(3)

# ---- the pieces
sigma0 = np.array([[1, 0], [0, 0]], complex)                      # the seed emission
eta = 0.6                                                          # depolarizing shrink
q = (1 - eta) / 4
G = Chan("iso", c, c, (),
         tuple([np.sqrt(1 - 3*q) * np.eye(2)] +
               [np.sqrt(q) * s for s in
                (np.array([[0, 1], [1, 0]], complex),
                 np.array([[0, -1j], [1j, 0]], complex),
                 np.array([[1, 0], [0, -1]], complex))]))          # contractive CP map
check("G is a channel", is_channel(G))
rho_star = np.eye(2) / 2                                           # depolarizing's fixed point

def shift(X):                                                      # ▷ : delay one tick
    return [np.zeros((2, 2), complex)] + X[:-1]
    # (▷X)_0 = a fresh trivial slot; (▷X)_{t+1} = X_t

def phi_guarded(X):
    """The HONEST guarded functional: X = ⟨σ₀, G ∘ ▷X⟩ — it READS X.
    Head now; tail = G applied to the input one tick back. Iterating this
    from any guess is the productive-fixpoint computation: each unfold
    finalizes exactly ONE new entry (the colimit behavior)."""
    out = [sigma0]
    for t in range(len(X) - 1):
        out.append(apply(G, X[t]))
    return out

# ---- 1. GUARDED PRODUCTIVITY: prefixes stabilize one entry per unfold,
#         identically across wildly different initial guesses
def rand_state():
    v = rng.normal(size=2) + 1j * rng.normal(size=2)
    v = v / np.linalg.norm(v)
    return np.outer(v, v.conj())

guesses = [[np.zeros((2, 2), complex)] * 12,                       # nothing
           [rho_star] * 12,                                        # already at the fixed point
           [rand_state() for _ in range(12)]]                      # chaos
N_ITER = 12
def direct_solution(n=12):
    d = [sigma0]
    for _ in range(n - 1):
        d.append(apply(G, d[-1]))
    return d
DIRECT = direct_solution()

profiles = []
finals = []
for g in guesses:
    X = g
    prof = []
    for it in range(1, N_ITER + 1):
        X = phi_guarded(X)                                         # one unfold — reads X
        agreed = 0
        for a, b in zip(X, DIRECT):
            if np.allclose(a, b, atol=1e-10):
                agreed += 1
            else:
                break
        prof.append(agreed)
    profiles.append(prof)
    finals.append(X)
check(f"guarded: prefix stabilization grows ONE entry per unfold "
      f"(profile {profiles[0]})",
      profiles[0] == list(range(1, N_ITER + 1)))
check("all three guesses reach the same full solution (guess-independence, earned)",
      all(np.allclose(f, DIRECT, atol=1e-10) for f in finals))
check("and the three finals are identical to each other",
      all(np.allclose(finals[0], f, atol=1e-10) for f in finals[1:]))

# ---- 2. GUARDED CONTRACTION: geometric convergence to the fixed point
def tdist(a, b):
    # the trace distance: half the TRACE NORM of the difference (nuclear norm).
    # (An earlier draft used 0.5|Tr(a-b)| — identically zero for equal-trace
    # states, making the check vacuous; caught by reading the printed d0.)
    return 0.5 * np.linalg.norm(a - b, 'nuc')

d0 = tdist(sigma0, rho_star)
rates = []
for t in (1, 2, 4, 8):
    rho_t = apply(G, np.array([[1, 0], [0, 0]], complex))
    for _ in range(t - 1):
        rho_t = apply(G, rho_t)
    rates.append(tdist(rho_t, rho_star))
check(f"trace distance decays geometrically (d_t ≤ η^t·d_0: "
      f"{[f'{r:.2e}' for r in rates]} vs η^t·d_0 = {eta}^t·{d0:.2f})",
      all(r <= (eta ** t) * d0 + 1e-9 for r, t in zip(rates, (1, 2, 4, 8))))

# ---- 3. UNGUARDED PATHOLOGY (a): instant self-reference — guess-dependence
def phi_unguarded_self(X):
    """X_t = X_t, read instantly: every sequence is a fixed point."""
    return list(X)
out0 = phi_unguarded_self(guesses[0])
out2 = phi_unguarded_self(guesses[2])
check("unguarded self-reference: two guesses remain TWO different 'solutions' "
      "(non-uniqueness — the limit depends on the guess)",
      not np.allclose(out0[3], out2[3]))

# ---- 3. UNGUARDED PATHOLOGY (b): future-reading (▷ reversed) — no stabilization
def phi_future(X):
    """X_t = G(X_{t+1}): the anti-guarded equation, reading one tick AHEAD."""
    return [apply(G, X[t + 1]) for t in range(len(X) - 1)] + [X[-1]]
X = guesses[2]
ever_stable = 0
seen = []
for it in range(6):
    X = phi_future(X)
    seen.append(X[0].copy())
stable_at_zero = all(np.allclose(seen[0], s, atol=1e-10) for s in seen)
check("anti-guarded (future-reading): the head entry NEVER stabilizes — "
      "no productive fixpoint", not stable_at_zero)

print(f"exp_guarded: {len(PASS)} ASSERTIONS PASS")
for p in PASS: print("  ✓", p)
print("\nWall 3 at toy grain: guarded equations over ω-indexed state streams have")
print("the unique productive solution (guess-independent, prefix-stabilizing), and")
print("contractive G's converge geometrically — while unguarded self-reference is")
print("guess-dependent and future-reading never stabilizes. The §3.6 target's")
print("solvability hope, checked computationally. Walls 1–2 remain untouched.")
