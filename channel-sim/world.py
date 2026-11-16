#!/usr/bin/env python3
"""world.py — mini grammar-world: the two-worlds toggle, animated (pure ASCII).

A preview of the parked Tier A lane (see the project docs' grammar-world
prompts). Each frame is one TICK. The boundary (the knower source) mints one
content emission per tick; every spent token is archived, write-only.

  kernel mode    : conserve + serialize — one emission per tick, forever;
                   the archive grows; the boundary never depletes.
  unrestricted   : flip the discard ban OFF — the killer fires (information
                   traced out into a carrier and dropped) and the dynamics
                   SPIN: cost accrues, emissions stop. (Dcare.guard_halts_
                   unguarded_spins / adversary_spin_diverges / spin_pays_
                   forever_buys_nothing, as a render.)

A grammar-world render, never physics — see channel-sim/README.md.
Run:  python world.py [ticks]
"""
import sys, time

TICKS = int(sys.argv[1]) if len(sys.argv) > 1 else 24
FLIP_AT = TICKS // 2          # the toggle moment
BAR = 46

def render(t, mode, emissions, archive, cost, leaked):
    line1 = "#" * BAR
    bound = "B"                               # the boundary position: one source, never depletes
    em = "•" * min(emissions, BAR - 4)
    ar = "▓" * min(archive, BAR - 4)
    co = "¢" * min(cost, BAR - 4)
    state = ("KERNEL — conserve+serialize" if mode == "kernel"
             else "UNRESTRICTED — discard allowed: LEAK+SPIN")
    print("\x1b[2J\x1b[H" + f"tick {t:>3}  [{state}]")
    print(f"  boundary:  [{bound}]                     (one source, unchanged — holographic_budget)")
    print(f"  emissions: [{em:<{BAR-4}}] {emissions:>3}  (one per tick in the kernel)")
    print(f"  archive:   [{ar:<{BAR-4}}] {archive:>3}  (write-only — the past is inert)")
    if mode == "kernel":
        print(f"  cost:      [    ]   0")
    else:
        print(f"  cost:      [{co:<{BAR-4}}] {cost:>3}  (paying, buying nothing — the spin)")
        if leaked:
            print("  *** THE KILLER FIRED: content carried into a discardable sector and DROPPED")
            print("  *** (readout >> discard — erasure; orthogonal inputs now identical)")
    print(line1)

mode, emissions, archive, cost, leaked = "kernel", 0, 0, 0, False
for t in range(1, TICKS + 1):
    if t == FLIP_AT:
        mode, leaked = "unrestricted", True
    if mode == "kernel":
        emissions += 1          # exactly one per tick  (chain_tick_buys_one)
        archive += 1            # the spent token recorded, never read
    else:
        cost += 1               # the spin: pays, emits nothing
        emissions = emissions   # frozen
    render(t, mode, emissions, archive, cost, leaked)
    time.sleep(0.12)
print("the two-worlds theorem pair, rendered: guarded — halts, conserves, serializes;")
print("unguarded — leaks, spins, never settles. A grammar-world, not a universe.")
