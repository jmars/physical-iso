#!/usr/bin/env bash
# sync-check.sh — every Dcare.<name> in the physical-iso paper matches a real
# top-level declaration somewhere in the companion Lean development — the WHOLE
# tree, including Dcare/Kernel/ and Dcare/Adversarial/ (the sibling
# isomorphism-paper script searched only Dcare/*.lean and would fail the
# Guarded-kernel anchors).
# Every Typed./Term./Ty. constructor must match a real constructor.
# A dead name (e.g. the deleted unrestricted `no_vanishing`) fails here.
#
# The companion is a separate repository (github.com/jmars/coglib). Point at a
# checkout of it with DCARE_LEAN; the default is a sibling ../coglib/lean.
# A missing tree is reported as NOT CHECKED (exit 2) — never as a pass.
#
#   DCARE_LEAN=~/coglib/lean ./scripts/sync-check.sh
#
# Exit 0 = green, 1 = a dead anchor, 2 = no Dcare tree to check against.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
PAPER="${1:-$HERE/../paper.md}"
LEAN="${DCARE_LEAN:-$HERE/../coglib/lean}"
fail=0
red()   { printf '\033[31m%s\033[0m\n' "$*"; }
green() { printf '\033[32m%s\033[0m\n' "$*"; }

[ -f "$PAPER" ] || { red "FAIL: no paper at $PAPER"; exit 1; }
if [ ! -d "$LEAN" ]; then
  red "NOT CHECKED: no Lean development at $LEAN"
  red "  the companion lives at github.com/jmars/coglib — point DCARE_LEAN at it:"
  red "  DCARE_LEAN=/path/to/coglib/lean $0"
  exit 2
fi

# Dcare.<name> — must be a top-level theorem/def/class/structure/inductive
# anywhere under the companion tree. Namespaced cites (Dcare.SC.lamArm_false)
# are normalized to their LAST component before matching.
names=$(rg -o 'Dcare\.[A-Za-z0-9_.]*[A-Za-z0-9_]' "$PAPER" | sed 's/^Dcare\.//; s/.*\.//' | sort -u)
if [ -z "$names" ]; then red "FAIL: no Dcare.* citations found"; exit 1; fi
while IFS= read -r n; do
  [ -z "$n" ] && continue
  if rg -q "^(theorem|def|class|structure|inductive) $n\b" "$LEAN" -g '*.lean'; then
    green "PASS Dcare.$n"
  else
    red "FAIL Dcare.$n — no such declaration under $LEAN"; fail=1
  fi
done <<< "$names"

# Typed./Term./Ty. constructors — must exist as a constructor or def
ctors=$(rg -o '(Typed|Term|Ty)\.[a-z][A-Za-z0-9_]*' "$PAPER" | sort -u)
while IFS= read -r c; do
  [ -z "$c" ] && continue
  base="${c%%.*}"; nm="${c#*.}"
  if rg -q "\| $nm\b" "$LEAN" -g '*.lean' || rg -q "^(def|inductive) $nm\b" "$LEAN" -g '*.lean'; then
    green "PASS constructor $c"
  else
    red "FAIL constructor $c not found in dcare sources"; fail=1
  fi
done <<< "$ctors"

echo "----------------------------------------"
[ "$fail" -eq 0 ] && green "SYNC-CHECK: ALL GREEN" || red "SYNC-CHECK: FAILURES ABOVE"
exit $fail
