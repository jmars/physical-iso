#!/usr/bin/env bash
# paper-check.sh — structural/label/register gate for the physical-iso paper
# (the physics Rosetta Stone). Adapted from the isomorphism-paper lane's gate;
# the forbidden patterns are the PHYSICS-register overclaims this lane must
# never ship, and the required sentences are the scope hedges that make the
# correspondence honest. Exit 0 = green.
set -u

HERE="$(cd "$(dirname "$0")" && pwd)"
PAPER="${1:-$HERE/../paper.md}"
CITS="${2:-${PAPER%/*}/citations.md}"
fail=0
red()   { printf '\033[31m%s\033[0m\n' "$*"; }
green() { printf '\033[32m%s\033[0m\n' "$*"; }

[ -f "$PAPER" ] || { red "FAIL: no paper at $PAPER"; exit 1; }
[ -f "$CITS" ] || { red "FAIL: no citations ledger at $CITS"; exit 1; }

# --- 1. required sections -----------------------------------------------
for s in "Epistemic framing" "The calculus and its guarded kernel" \
         "The two conservation correspondences" "The refutation" \
         "The selection reading" "Experimental signatures" \
         "Scope and limits" "References"; do
  if rg -q "$s" "$PAPER"; then green "PASS section: $s"
  else red "FAIL section missing: $s"; fail=1; fi
done

# --- 2. mandatory plain scope sentences (the honesty hedges) -------------
for s in "The bridge is a mirror, not a derivation" \
         "dictionary, not an isomorphism" \
         "The guard fixes no scale"; do
  if rg -qF "$s" "$PAPER"; then green "PASS scope sentence: '$s'"
  else red "FAIL scope sentence missing: '$s'"; fail=1; fi
done

# --- 3. labels legend + per-section coverage ------------------------------
if rg -q "MEASURED" "$PAPER" && rg -q "INTERPRETATION" "$PAPER" && rg -q "PROJECTION" "$PAPER"; then
  green "PASS labels legend terms present"
else red "FAIL label legend incomplete"; fail=1; fi

count_labels() { # start-regex end-regex
  awk -v a="$1" -v b="$2" '
    $0 ~ a {insec=1} $0 ~ b {insec=0}
    insec {n+=gsub(/MEASURED|INTERPRETATION|PROJECTION/,"&")} END{print n+0}' "$PAPER"
}
n3=$(count_labels '^## 3[.]' '^## 4[.]')
n4=$(count_labels '^## 4[.]' '^## 5[.]')
n5=$(count_labels '^## 5[.]' '^## 6[.]')
n6=$(count_labels '^## 6[.]' '^## 7[.]')
i=3
for v in "$n3" "$n4" "$n5" "$n6"; do
  if [ "$v" -ge 3 ]; then green "PASS labels in section $i: $v"
  else red "FAIL section $i has only $v label markers (need >=3)"; fail=1; fi
  i=$((i+1))
done

# --- 4. FORBIDDEN patterns: physics-register overclaims -------------------
patterns=(
  "exact mathematical isomorphism"
  "exact isomorphism"
  "proves quantum mechanics"
  "proves that quantum"
  "derives the laws of physics"
  "the universe runs"
  "must run the"
  "instantly decohere"
  "decay rate"
  "instanton"
  "refresh rate"
  "serializes hawking"
  "is the event horizon"
  "false vacuum decay"
  "quantum foam is"
  'sqrt\{R/3'
  'l_p\s*\\sqrt'
)
for p in "${patterns[@]}"; do
  if rg -qi "$p" "$PAPER"; then red "FAIL forbidden pattern present: '$p'"; fail=1
  else green "PASS forbidden absent: '$p'"; fi
done

# --- 5. the dead unrestricted name must never appear unqualified ----------
bad=$(rg -n -P 'no_vanishing(?!_)' "$PAPER" || true)
if [ -n "$bad" ]; then
  red "FAIL bare 'no_vanishing' (deleted in the tree; only _restricted/_armed/_unrestricted_refuted exist):"; echo "$bad"; fail=1
else green "PASS no bare no_vanishing"; fi

# --- 6. no line-number citations (they drift; cite names + files) ---------
bad=$(rg -n '\.(lean|md|tex):[0-9]+' "$PAPER" || true)
if [ -n "$bad" ]; then red "FAIL line-number citation(s):"; echo "$bad"; fail=1
else green "PASS no line-number citations"; fi

# --- 7. citation discipline: every References key has a ledger row and ----
#     appears in the body at least once outside References.
keys=$(awk '/^## References/{ref=1} ref && /^- \[/{print}' "$PAPER" | rg -o '\[[A-Za-z]+[0-9]{0,2}\]' | sort -u)
if [ -z "$keys" ]; then red "FAIL: no References keys found"; fail=1; fi
body=$(awk '/^## References/{exit} {print}' "$PAPER")
# body keys: expand bracket groups ([A] and [A, B] both count) to one key per line
bodykeys=$(printf '%s\n' "$body" | rg -o '\[[A-Za-z0-9 ,&–-]+\]' | sed 's/^\[//; s/\]$//' | tr ',' '\n' | sed 's/^ *//; s/ *$//' | sort -u)
while IFS= read -r k; do
  [ -z "$k" ] && continue
  kk="${k//[][\\]/}"
  if rg -qF "$k" "$CITS" || rg -qF "| $kk " "$CITS"; then :; else
    red "FAIL reference $k has no citations.md row"; fail=1; continue; fi
  if rg -qxF "$kk" <<<"$bodykeys"; then green "PASS reference used in body: $k"
  else red "FAIL reference $k never cited in body"; fail=1; fi
done <<< "$keys"

# --- 8. word count ---------------------------------------------------------
wc=$(wc -w < "$PAPER")
if [ "$wc" -ge 5500 ] && [ "$wc" -le 11000 ]; then green "PASS word count: $wc"
else red "FAIL word count $wc outside 5500-11000"; fail=1; fi

echo "----------------------------------------"
[ "$fail" -eq 0 ] && green "PAPER-CHECK: ALL GREEN" || red "PAPER-CHECK: FAILURES ABOVE"
exit $fail
