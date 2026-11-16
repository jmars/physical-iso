# channel-sim — the semantic bridge, executable

*A derivation-of-care program artifact — the Tier B channel-simulator, implementing the
bridge of "Conservation as Grammar" §3.5 as a working dictionary. A grammar-world fact
factory: what runs here is mathematics about the calculus's dictionary, never physics.*

## What this is

Objects are finite-dimensional Hilbert spaces flagged **classical** (a chosen orthonormal
basis exists — the paper's knower/knowledge/archive) or **quantum** (no structure chosen —
content). Channels are **constructions**: an AST of clause nodes, never bare matrices, so
the construction log can always answer *"did this channel use the discard?"*

The two modes are the paper's kernel/outside boundary, as a switch:

- **kernel** (`weak` banned) — the trace clause is absent from the set;
- **unrestricted** (`weak` allowed) — the trace is available at every object: the channel world.

## The clause dictionary (paper §3.5's table)

| clause | denotation | modes |
|---|---|---|
| `iso` | a unitary (pure evolution) | both |
| `prepare` | the constants — fixed state preparations (the coalgebra's faces) | both |
| `tensor` / `compose` / `swap` | the monoidal structure; `lete` = composition after the swap | both |
| `copy` | `contr` at a non-linear sort: measure-and-prepare **along the chosen basis** — refused outright on quantum objects | both (type-gated) |
| `trace_out` | `weak`: the partial trace — the discard | unrestricted only |

## The demonstrations (`./check.sh` runs all five)

1. **`demo_two_modes`** — C1 + the killer. Kernel: a search over **570** well-typed
   composites finds **no** channel from the structureless system to the trivial one (the
   empirical twin of the semantic image of `Dcare.counterexample_not_noweak`);
   unrestricted: §5.1's killer composite builds, uses the discard, and evaluates to an
   **erasing channel** — orthogonal inputs give identical outputs.
2. **`demo_preparability`** — C3, the Wootters–Zurek clause executable: basis states (the
   blanks — the closed inhabitants of paper §3.1) copy with fidelity **1**; the
   superposition comes out as the measure-and-prepare mixture (fidelity **0.25**); and the
   builder refuses `copy` on a quantum object outright — *you cannot copy along a structure
   you have not chosen.*
3. **`demo_erasure_log`** — C2 over a corpus: **911** unrestricted constructions, **37**
   of them quantum-to-trivial, **every one carrying the discard** (0 in the kernel corpus);
   plus the one-line factorization verified numerically (any CP map L(H)→ℂ is X ↦ Tr(AX),
   hence Tr ∘ Φ_A).
4. **`demo_serialization`** — the stretch: one application and one emission per tick
   (25 = 25), minting from an unchanged reservoir — the arithmetic of
   `Dcare.holographic_budget` and the discrete shadow of `Dcare.chain_tick_buys_one`.

## Epistemic labels (the paper's discipline, carried into code)

- Everything here is **fact-about-the-grammar-world**: implementing the bridge makes it
  *concrete*, not more *proven* — the bridge stays paper-rigor (physical-iso paper.md §3.5).
- `▷` in the serialization demo is a **design decision** (a render clock), not a
  denotation: quantum guarded domain theory is open (paper §3.6).
- The refusal messages in `clauses.py` are the semantic images of the grammar's
  non-derivabilities — each cites the paper section or `Dcare.*` theorem it twins.
- No claim in this artifact is about physics. Small dimensions only; no scalability claims.

## Run

```
./check.sh        # all five demos, all assertions — CHANNEL-SIM: ALL DEMOS PASS
```

Stack: Python 3 + numpy (installed via pacman in this container). No other dependencies.

## The experiments (`exp_*.py`, run separately from the gate — minutes each)

- **`exp_stress`** — C2 falsified-at-scale: 19,472 kernel constructions (zero erasing);
  82,240 unrestricted (1,960 erasing), **all carrying the discard**; d ∈ {2,3}, randomized
  Haar seeds, every construction trace-preserving-checked. The invariant holds.
- **`exp_characterize`** — the discovery: the kernel's quantum-sector image is **exactly
  the unitaries** (170/170 quantum-to-quantum constructions unitary). §3.5 C1's sharpened
  claim, checked here, provable by the same type-arithmetic that carries C2.
- **`exp_cloner`** — the cloning line: the exact cloner is refused by the clause set; the
  lab-optimal approximate single-clone channel (depolarizing shrink 2/3, fidelity 5/6
  verified numerically) is legal channel data. The grammar's line is exactness — the
  Wootters–Zurek line. Consistency-with-QM texture, explicitly NOT evidence.

These results are cited in physical-iso paper.md §3.5 as [CCS-sim].

## The third mode (the calculus's own rule set) — `demo_gated`

The human's question surfaced a fidelity gap, now a feature: the sim's original
"unrestricted" mode was the AFFINE world (trace at every object). The calculus's
own rule set is a THIRD clause set — `CALCULUS_TAGS`: weak gated to non-linear
types (`Typing.weak`'s isLinear = false), the trace available at classical
objects only. Three grades of erasure, executable:

- **kernel** — no discard: no erasure.
- **calculus** — direct discard of the quantum token REFUSED; erasure remains
  possible ONLY by first carrying the token into a discardable sector (the
  `readout` clause — the conduit's denotation, taken as fixed) and discarding
  the carrier: every discard site classical. `Dcare.killerOf`'s mechanism,
  as a switch.
- **affine** — trace at every object (the paper's CPM table row at full
  generality): erasure anywhere.

## `exp_guarded` — QGDT wall 3 at toy grain (the newest experiment)

Guarded equations X = ⟨σ₀, G ∘ ▷X⟩ over ω-indexed state streams: the unique productive
solution, guess-independent (3 wild guesses → identical streams), prefix-stabilizing;
contractive G converges geometrically (d_t = η^t·d₀ to the digit). Against it: instant
self-reference is guess-dependent (no unique solution); the anti-guarded future-reading
equation never stabilizes. The §3.6 target's solvability hope, computationally checked —
walls 1–2 untouched. (An in-flight catch: the first trace-distance formula was identically
zero on density matrices — vacuous check; the printed d₀ gave it away. The metric is now
the true trace norm.)
