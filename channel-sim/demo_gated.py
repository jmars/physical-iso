"""demo_gated.py — the calculus's OWN rule set: three grades of erasure.

The calculus's weak is gated to non-linear types (Typing.weak's
isLinear = false): the conserved token is spent, never weakened. That gate
makes a third clause set — the faithful one — between the kernel and the
affine world:

  kernel    — no discard at all: no erasure (demo_two_modes).
  calculus  — discard at CLASSICAL objects only: erasure of the quantum
              token remains possible, but ONLY by first carrying it into a
              discardable sector (readout) and discarding the carrier —
              Dcare.killerOf's mechanism, executable: "any non-linear output
              at the token frame is a vanishing channel."
  affine    — discard at every object: erasure anywhere (the world the
              paper's CPM table row describes at full generality).
"""
import numpy as np
from clauses import (Obj, UNIT, C, K, ClauseError, iso, prepare, tensor,
                     compose, readout, trace_out, apply, is_channel,
                     uses_discard, discard_sites,
                     KERNEL_TAGS, CALCULUS_TAGS, UNRESTRICTED_TAGS)

PASS = []
def check(name, cond):
    assert cond, f"FAILED: {name}"
    PASS.append(name)

c, k = C(2), K(2)

# --- the gate itself
try:
    trace_out(c, CALCULUS_TAGS)
    check("gated mode: direct discard of the QUANTUM token — REFUSED", False)
except ClauseError as e:
    check("gated mode: direct discard of the QUANTUM token — REFUSED", "non-linear" in str(e))
check("gated mode: discard at a CLASSICAL object — allowed", True)
tk = trace_out(k, CALCULUS_TAGS)

# --- the gated killer: readout into the classical sector, then discard there
carrier = readout(CALCULUS_TAGS)                    # C -> K (the conduit, taken as fixed)
gated_killer = compose(tk, carrier, CALCULUS_TAGS)   # C -> unit
check("the gated killer builds and uses the discard", uses_discard(gated_killer))
check("it is a trace-preserving channel", is_channel(gated_killer))
sites = discard_sites(gated_killer)
check(f"and EVERY discard site is classical ({[s.classical for s in sites]})",
      all(s.classical for s in sites))
check("the mechanism: the token is first CARRIED (readout) into a discardable sector",
      gated_killer.children[1].tag == "readout")
out0 = apply(gated_killer, np.array([[1, 0], [0, 0]], complex))
out1 = apply(gated_killer, np.array([[0, 0], [0, 1]], complex))
check("it erases: orthogonal inputs give identical outputs", np.allclose(out0, out1))

# --- the affine world, for contrast: direct discard of the token is legal
direct = trace_out(c, UNRESTRICTED_TAGS)
check("affine mode: the SAME direct discard builds (the gate lifted)",
      uses_discard(direct) and not discard_sites(direct)[0].classical)

print(f"demo_gated: {len(PASS)} ASSERTIONS PASS")
for p in PASS: print("  ✓", p)
print("\nThree grades: kernel (no erasure) / calculus (erasure via a classical")
print("carrier — the leak theorem's mechanism) / affine (erasure anywhere).")
