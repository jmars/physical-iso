# Conservation as Grammar

Artifact for the paper `paper.md`:

> *Conservation as Grammar: No-Cloning and Unitarity as Structural Theorems of a
> Guarded Linear Calculus, with a Holographic Resolution Bound*

**Published: concept doi [10.5281/zenodo.24281490](https://doi.org/10.5281/zenodo.24281490)** —
it always resolves to the latest archived version. Cite the paper by the concept DOI.
Each release is archived automatically by Zenodo.

A guarded, sorted linear calculus in which no-cloning and (in the guarded kernel)
no-vanishing are **structural** theorems — properties of which well-formed
processes exist, prior to any dynamics — together with a translation manual into
the language of observables, tensor networks and structural holography, a
semantic bridge into completely positive maps for the finitary fragment, and a
projection onto a holographic resolution bound.

## Layout

| path | contents |
|---|---|
| `paper.md` | the paper (markdown — the source of truth) |
| `paper.pdf` | the arXiv rendering (`latex/main.pdf`), 10 pages |
| `latex/` | the LaTeX sources of that rendering (`main.tex`, `guarded-syntax.sty`) |
| `channel-sim/` | **[CCS-sim]**, the companion simulator: the bridge's clause dictionary as executable code, with its demos and experiments |
| `scripts/paper-check.sh` | the structural/register gate: required sections, claim labels, physics-register overclaims absent, scope hedges present, word count |
| `scripts/sync-check.sh` | the anchor gate: every `Dcare.*` name cited in the paper exists as a declaration in the companion Lean development, and every `Typed.`/`Term.`/`Ty.` constructor exists as one |
| `citations.md` | the citation ledger |
| `litreview/` | the literature record the ledger is drawn from |
| `scouting/` | the same, for the Wheeler/foam domain |

## Running the artifact

The paper's gates need only `bash` and `ripgrep`:

```
./scripts/paper-check.sh          # structural + register gate
./scripts/sync-check.sh           # anchors vs the companion Lean tree
```

`sync-check.sh` checks the paper against the companion mechanization
(`github.com/jmars/coglib`), which is a separate repository. Point it at a
checkout; with no tree present it reports **NOT CHECKED** and exits 2 rather
than passing:

```
DCARE_LEAN=../coglib/lean ./scripts/sync-check.sh
```

The simulator needs Python 3 and NumPy:

```
python3 -m venv .venv && .venv/bin/pip install -r channel-sim/requirements.txt
PYTHON=.venv/bin/python bash channel-sim/check.sh     # every demo's assertions
```

Individual demos and experiments run standalone, e.g.
`.venv/bin/python channel-sim/demo_gated.py`,
`.venv/bin/python channel-sim/exp_guarded.py`.

To rebuild the PDF: `cd latex && pdflatex main.tex && pdflatex main.tex`.

## Scope

The paper's *Scope and limits* section states what the correspondence is and is
not: the bridge is a mirror, not a derivation; the counting model is
natural-number-valued and carries no amplitudes; the calculus contains no
geometry; and §6's bound is a projection with named instruments, constraining no
experiment. `paper-check.sh` enforces that those hedges stay in the text.

## License

- **`paper.md`, `paper.pdf`, `latex/`** — CC-BY-NC-SA-4.0 (see `LICENSE-paper`).
- **`channel-sim/`, `scripts/`, and the literature record** — AGPL-3.0-or-later
  (see `LICENSE`).

NonCommercial, ShareAlike and network copyleft are deliberate: the companion
mechanization is dual-use, and this work is not offered for commercial
incorporation.

## Status

Prepared for public release as a preprint plus its runnable artifact. Copyright
holder Jaye Timothy Marshall, ORCID
[0009-0002-5209-8161](https://orcid.org/0009-0002-5209-8161). `.zenodo.json`
carries the deposit metadata. The latest record is
[10.5281/zenodo.24288235](https://doi.org/10.5281/zenodo.24288235) (v1.0.1); the concept DOI
above covers later versions, which the release webhook deposits automatically.

**One step the webhook cannot do.** The Zenodo GitHub integration deposits the release
archive only, so `paper.pdf` is not previewable in the record until it is added as a
separate file. After each release's deposit lands, add it:

```
curl -X POST -H "Authorization: Bearer $ZENODO_TOKEN" \
  https://zenodo.org/api/deposit/depositions/<new-id>/actions/edit
curl -X PUT -H "Authorization: Bearer $ZENODO_TOKEN" -H "Content-Type: application/octet-stream" \
  --data-binary @paper.pdf <bucket-url>/paper.pdf
```

The bucket is locked once the record is published, so if the deposit has already gone
through, the PDF goes into a new version instead.
