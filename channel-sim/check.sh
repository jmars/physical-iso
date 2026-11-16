#!/usr/bin/env bash
# check.sh — the channel-simulator's gate: every demo's assertions must pass.
set -u
cd "$(dirname "$0")"
PY="${PYTHON:-python3}"
command -v "$PY" >/dev/null || { echo "FAIL: no python3 on PATH (set PYTHON)"; exit 1; }
fail=0
for d in demo_two_modes demo_preparability demo_erasure_log demo_serialization demo_gated; do
  echo "=== $d ==="
  if "$PY" "$d.py"; then :; else echo "FAIL: $d"; fail=1; fi
done
echo "----------------------------------------"
[ "$fail" -eq 0 ] && echo "CHANNEL-SIM: ALL DEMOS PASS" || echo "CHANNEL-SIM: FAILURES ABOVE"
exit $fail
