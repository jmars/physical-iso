# Domain 1 — Wheeler: quantum foam & pregeometry

Literature scout memo for `physical-iso/paper.md`, §5.5 "The selection reading".
Written 2026-11-16. Findings only: **no edit to `paper.md` or `citations.md`** —
seven scouts run concurrently, so shared-file edits would collide. Every
change is given as a ready-to-paste patch below.

> **Brief caveat.** The spawn brief is truncated mid-sentence at "Goal:
> establish Wheeler as the ancestor of 'foam', and". I ran the question it
> states in full (Wheeler / successors: did they propose conservation laws
> failing in the foam, or assume standard QM while geometry fluctuates?) and
> delivered the findings in the paper's own citation discipline. If the
> truncated tail asked for something else, this file is the part that stands.

## 1. Answer in one paragraph

**Wheeler is the ancestor of the foam, not of "conservation fails in the
foam".** Wheeler's foam is *quantum fluctuations of geometry and topology*
(Wheeler 1955/1957, MTW §43.4): the quantum formalism is assumed intact and
the metric is what fluctuates. His "law without law" (1979–83) is a separate
conjecture about the *status of dynamical law* (laws as statistical, not
fundamental), not a claim that unitarity or no-cloning fail inside the foam.
The proposal that conservation fails in the foam is **Hawking's** (1976–87:
virtual black holes in the foam, the superscattering operator `$`), joined by
the intrinsic-decoherence models (Ellis–Hagelin–Nanopoulos–Srednicki 1984) and
Penrose-type collapse; those fail unitarity globally or wherever a black hole
forms, **never sector-selectively**, and the post-AdS/CFT verdict — restated by
Hawking himself in 2005 — is that quantum gravity is unitary even in the foam.
**No line of this literature lets no-cloning fail**, and the loss proposals are
*linear* maps on density matrices (Page: `ρ_final = $ ρ_initial`), so the
linearity proof of no-cloning survives there too.

Consequences for §5.5: its guard sentence is **falsified as written** by
Hawking 1982/1987, and its "lossy, not a breeder" fingerprint is **not
distinctive** — it is the shape of any linear non-unitary dynamics. What
*is* defensible, and stronger, is narrower: the loss is **derived** from the
same rule set that proves no-cloning, and the boundary between regimes is one
structural rule. §5 below gives verbatim replacements.

## 2. Wheeler: what the sources actually say

**Term and picture** [MEASURED, quoted from Carlip's review, arXiv:2209.14282v3
p. 1, §1]:

> "In the mid-1950s, Wheeler made one of the first concrete conjectures about
> that small scale structure [2,3]. He argued that quantum fluctuations of the
> metric should be of order one at the Planck scale, leading to wild and
> rapidly varying fluctuations in spacetime geometry and topology, which he
> called 'spacetime foam.'"

Carlip's [2] = Wheeler, *Geons*, Phys. Rev. 97 (1955) 511; [3] = Wheeler,
*On the nature of quantum geometrodynamics*, Ann. Phys. 2 (1957) 604 — both
DOI-verified below. Wheeler's own popular description is quoted by Carlip from
Wheeler, *The Lesson of the Black Hole*, Proc. Am. Phil. Soc. 125 (1981) 25
(not read here; needs-human):

> "Space, smooth at the everyday level [...] is predicted at still smaller
> distances to show a foamlike structure."

**The formalism** [MEASURED structure, INTERPRETATION the conclusion]. The foam
is defined by *quantum fluctuations of the metric*; canonical quantum
geometrodynamics (the Wheeler–DeWitt equation) and the sum-over-histories are
the framework (Carlip §1–2). A framework in which a wave function on superspace
evolves linearly is a framework in which the quantum laws — linear amplitudes,
hence the kinematic no-cloning argument — are assumed. **I found no proposal by
Wheeler that unitarity or no-cloning fails in the foam.** That is a negative
result over the sources I could read (Carlip's review, open; Wheeler 1957 is
paywalled and was *not* read in the original); a full check of Wheeler's
collected papers is the human's, but nothing in the secondary literature I read
suggests it.

**"Law without law"** [MEASURED metadata + quoted characterization;
INTERPRETATION the reading]. It is a conjecture about *law's origin and
status*, not about conservation inside the foam. A verified critical
characterization (Deutsch, 1986; reprint 2017) reads: "Wheeler's idea that
physical 'laws' would not appear in a truly fundamental description of nature
is critically examined." A 2018 reading (Caprara & Vulpiani) treats "law
without law" as a claim about *limit theorems* — statistical emergence, not
conservation failure.

**The over-attribution in §5.5** [INTERPRETATION]. Current sentence (line 221):

> "Wheeler's spacetime foam and 'law without law' — a pre-lawful, fluctuating
> substrate from which law-like behavior emerges in stable sectors [Whe57] —"

puts three claims on one citation: (i) foam, which is [Whe57]; (ii) "law
without law", which is 1979–83, not 1957; (iii) "emerges in stable sectors",
which is **not Wheeler's mechanism at all** — his emergence is statistical and
observer-participatory, not selection-on-stability. Wheeler's 1957 paper does
not contain (ii) or (iii). Fix in §5, C1.

## 3. Successors: three classes, and who lets what fail

### (a) Standard-QM foam (QM intact, geometry fluctuates)

The mainstream. Carlip's review is the current statement of it, and it is
careful about the metaphor [MEASURED, quoted]:

> "The reader should also keep in mind that the term 'foam' is a metaphor, not
> a literal description".

The phenomenology line — Ng & van Dam's distance uncertainty, Hogan's
holographic noise, the Holometer — is built *within* standard quantum
mechanics. Ng & van Dam's own abstract [MEASURED, quoted from
arXiv:gr-qc/9906003]:

> "this distance cannot be measured with uncertainty less than (l l_P²)^{1/3},
> considerably larger than the Planck scale".

That is exactly the paper's §6.1 formula, and it confirms the paper's
attribution of the 3-D family to [NdV03] (the citation's *bibliographic* data
has a small defect — see §6).

### (b) The loss lineage — conservation *does* fail, but not sector-selectively

**Hawking**, the foam-specific version [MEASURED, quoted from Carlip §5.2]:

> "The idea that spacetime foam could lead to a failure of unitarity in quantum
> field theory dates back to work by Hawking [216,217], who argued that virtual
> black holes could form coherently and then evaporate thermally."

Carlip's [216] = Hawking, *The unpredictability of quantum gravity*, Commun.
Math. Phys. 87 (1982) 395; [217] = Hawking, *Quantum coherence down the
wormhole*, Phys. Lett. B 195 (1987) 337. The 1976 paper (*Breakdown of
predictability in gravitational collapse*, Phys. Rev. D 14, 2460) and the 1978
*Spacetime foam* (Nucl. Phys. B 144, 349) are the earlier steps.

The operator's structure [MEASURED, quoted from Page's review, arXiv:hep-th/9305040,
§1]:

> "Hawking proposed that the process would be described by a superscattering
> operator $ that would take initial density matrices into final density
> matrices in a nonunitary way [...] ρ_final_ab = $^{cd}_{ab} ρ_initial_cd
> [...] where $ would not have the usual unitary form S S̄."

**`$` is linear in ρ** — that is the whole point of writing it as an operator
on density matrices. Linearity is what keeps no-cloning alive (§4).

**Intrinsic decoherence** [MEASURED metadata; content per the LRR review]:
Ellis, Hagelin, Nanopoulos & Srednicki, *Search for violations of quantum
mechanics*, Nucl. Phys. B 241 (1984) 381. Amelino-Camelia's review states the
role [MEASURED, quoted from arXiv:0806.0339 §2.2.3]:

> "Some of the test theories used to model spacetime quantization have been
> found to provide motivation for departures from quantum mechanics in the form
> of 'decoherence', loss of quantum coherence [22, 23, 161]"

and, for the kaon test theory that descends from it [MEASURED, quoted §4.5.1]:
"beyond quantum mechanics (by allowing for decoherence)".

**Penrose-type collapse and collapse models in foamy regions** [MEASURED
metadata + Carlip's summary]: Penrose, *On gravity's role in quantum state
reduction*, Gen. Rel. Grav. 28 (1996) 581; Carlip §5.2: "there are other
proposals in which quantum gravitational effects can lead to decoherence,
especially if, as Penrose has suggested, quantum gravity requires fundamental
modifications of quantum mechanics".

**Effective (open-system) decoherence** — the weakest claim, and the one that
keeps unitarity at the fundamental level [MEASURED, quoted from Carlip §5.2]:

> "even if black hole evaporation and similar processes are unitary, it remains
> possible that spacetime foam could lead to *effective* decoherence and
> nonunitarity. Fields in a foamy spacetime may behave as open systems [...]"

(E.g. Garay, *Quantum evolution in space–time foam*, Int. J. Mod. Phys. A 14
(1999) 4079 — master equations with decoherence and mode-dependent shifts.)

### (c) The modern verdict: unitarity restored

[MEASURED, quoted from Hawking 2005, arXiv:hep-th/0507171, abstract]:

> "Elementary quantum gravity interactions do not lose information or quantum
> coherence."

and, from its introduction: "it was claimed that the issue was settled in
favor of conservation of information by ADS-CFT [...] Since the conformal field
theory is manifestly unitary the argument is that string theory must be
information preserving."

Carlip's summary [MEASURED, quoted §5.2]: "I think it is fair to say that most
physicists currently working on quantum gravity expect that the process is
ultimately unitary, but the question is still hotly debated". Page's review
(1993) and the firewall debate (AMPS, *Black holes: complementarity or
firewalls?*, JHEP 2013(2) 062) treat unitarity as one of the assumptions to be
defended: AMPS argue "the following three statements cannot all be true: (i)
Hawking radiation is in a pure state, ..." [MEASURED, quoted from the arXiv
abstract].

**So the mainstream foam picture does keep the quantum laws while geometry
fluctuates — §5.5's second clause is right. Its first clause is not:** accounts
with conservation failing *do* exist, they are just not sector-selective.

## 4. The negative result: no-cloning never fails

**Searches run** (recorded so the negative claim has a denominator):
Crossref `query.bibliographic` = "no-cloning space-time foam Planck scale",
"cloning unknown quantum state Planck scale gravity", "unitarity violation
spacetime foam", "no-cloning black hole complementarity"; OpenAlex `search` =
"no-cloning quantum foam", "no-cloning spacetime foam"; full-text grep for
`clon` in Carlip 2023 (0 hits), Amelino-Camelia LRR 2013 (0 hits), Mathur's
information-paradox review arXiv:0909.1038 (0 hits). **No proposal in which
foam permits cloning was found.** This is a negative result over those searches,
not a theorem about the literature.

**Why it is structurally expected** [INTERPRETATION, premise MEASURED]. The
no-cloning proof needs only *linearity* of the state map. The loss proposals
are linear on density matrices (`ρ → $ρ`, Page above). The only route to
cloning is a *nonlinear* evolution of ρ — which Page lists as a separate option
[MEASURED, quoted]: "(E) Evolution of density matrices deterministically but
nonlinearly. I don't see any clear motivation for this, but why not leave it on
the table as an open possibility?" A generic nonlinear modification of QM
(the Weinberg/Czachor line) is a different literature and is empirically
squeezed; no foam account takes it up.

**Consequence for the paper.** "Lossy, not a breeder" is a property of the
*linear non-unitary class*, not a fingerprint of this calculus. It is exactly
what Hawking's `$` does too. The tree-checkable claim that survives is
different: here the loss **and** the retention of no-cloning are both theorems
of **one rule set**, and the sector boundary is a single structural rule.
§5, C3.

## 5. Consequences for §5.5 — verbatim text, problem, replacement

### C1 — the ancestry sentence (line 221)

Current:

> "There is a distinguished lineage in fundamental physics with this general
> shape: Wheeler's spacetime foam and "law without law" — a pre-lawful,
> fluctuating substrate from which law-like behavior emerges in stable sectors
> [Whe57] — and the selection-on-stability family of ideas descended from it
> and from the anthropic literature [Car74]."

Problem: [Whe57] is quantum geometrodynamics/foam; "law without law" is
1979–83; "emerges in stable sectors" is not Wheeler's mechanism; and Carter's
anthropic principle is selection-on-observers, not selection-on-stability —
the paper itself disowns fine-tuning two sentences later.

Proposed:

> "There is a distinguished lineage in fundamental physics with this general
> shape: Wheeler's spacetime foam — a geometry that fluctuates quantum
> mechanically at the Planck scale [Whe55, Whe57] — and his later conjecture
> that dynamical law itself is not fundamental, "law without law" [Whe83].
> Wheeler's emergence of law is statistical and observer-participatory; the
> selection shape used here is not his, and it is not the anthropic selection
> of the cosmological literature [Car74] either. It needs no observer and no
> fine-tuning argument; the selection is theorem-shaped:"

(The bullets that follow stay unchanged.)

### C2 — the guard sentence (line 230) — **this one is false as written**

Current:

> "No established account — foam, landscape, eternal inflation — has the
> conservation laws themselves failing outside a stable sector; mainstream
> treatments assume quantum mechanics holds everywhere and let geometry
> fluctuate."

Problem: Hawking's superscattering operator is a proposal *within the foam
lineage* in which unitarity fails (Carlip: "dates back to work by Hawking"),
and EHNS 1984 / Penrose 1996 propose fundamental modifications. A referee will
kill the sentence with Hawking 1982. The second clause is fine and now has
strong support (Hawking 2005; Carlip).

Proposed:

> "The guard, stated once more for the record: this is *structural ancestry*,
> not identification. The loss proposals in this lineage are real but
> differently shaped: Hawking's superscattering operator [Haw82, Haw87], the
> intrinsic-decoherence models [EHNS84], and Penrose-type collapse [Pen96]
> fail unitarity globally, or wherever a black hole forms — not selectively
> outside a stable sector — and the mainstream verdict since [Page93],
> restated by Hawking himself [Haw05], is that quantum gravity is unitary even
> in the foam. The mainstream foam picture therefore keeps the quantum laws
> and lets geometry fluctuate. The calculus offers a rigorous object with the
> shape of the old intuition — conservation failing in the pre-lawful regime
> while the kinematic law survives — and it does not claim the intuition was
> about this object. **[INTERPRETATION]**"

### C3 — the signature paragraph (line 228) — the distinctiveness claim

Current ending:

> "Wheeler's foam fluctuates geometry and keeps the quantum laws; this
> reading's outside breaks the conservation laws first, and keeps the kinematic
> ones. That inversion is the reading's one distinctive, tree-checkable
> fingerprint."

Problem: the inversion is exactly the shape of a linear non-unitary operator
(Hawking `$`), where no-cloning also survives by linearity. It cannot be the
*distinctive* fingerprint, and "distinguishes it from every generic foam story"
overreaches: it distinguishes it from the mainstream (QM-intact) foam only.

Proposed ending:

> "Wheeler's foam fluctuates geometry and keeps the quantum laws; this
> reading's outside breaks the conservation laws first and keeps the kinematic
> ones. That inversion is not new — it is the shape of a linear but non-unitary
> evolution, such as Hawking's superscattering operator [Haw82, Haw87], in
> which no-cloning also survives, by linearity [Page93]. What is distinctive is
> its status: here the loss and the retention of no-cloning are both theorems
> of one rule set, and the boundary between the regimes is one structural
> rule — the discard. **[MEASURED (the anchors) + INTERPRETATION (the
> reading)]**"

And narrow the opening of that paragraph from "distinguishes it from every
generic foam story" to "distinguishes it from the foam picture in which quantum
mechanics holds everywhere".

### C4 — otherwise a nice, checkable point worth adding (optional)

Wheeler's foam is a *metaphor* (Carlip, quoted §3a), and the paper's §5.5 could
use that: it is the same discipline the paper applies to its own reading. One
sentence, [INTERPRETATION], no new citation beyond [Carlip23].

Also available (verified, currently unused): Wheeler 1980 *Pregeometry:
motivations and prospects* — the program of deriving spacetime and law from
something deeper. It is about law's *origin*, like "law without law"; it does
not propose conservation failing. Cited only if §5.5 wants the pregeometry word
in the title of its lineage.

## 6. `citations.md`: corrections and additions (ready to paste)

### Corrections (data wrong today)

| key | current row | corrected row |
|---|---|---|
| `Hog12` | "Interferometers as probes of Planckian phenomenology and holographic noise. *Classical and Quantum Gravity* 29, 195012" | **Hogan, C. J. (2012). *Interferometers as probes of Planckian quantum geometry.* Physical Review D 85, 064007. DOI 10.1103/physrevd.85.064007** — `verified (Crossref, 2026-11-16)`. There is no CQG 29, 195012 holographic-noise paper (searched CQG v29 by container+year). |
| `Hol16` | vague: "The Fermilab Holometer collaboration (2015–2016) [...] *Physical Review Letters* (to be verified)" | split into two verified rows: `Chou17` (instrument) and `Chou16` (the cross-spectrum result) — see below. |
| `VPF13` | "Limits on spacetime quantum 'foam' models from observations of GRB 090510. *PRD* 87, 122001" | **Vasileiou, V., et al. (2013). *Constraints on Lorentz invariance violation from Fermi-Large Area Telescope observations of gamma-ray bursts.* Physical Review D 87, 122001. DOI 10.1103/physrevd.87.122001** — `verified (Crossref)`. **The title is wrong today, and so is the claim the row carries:** this paper constrains *linear vacuum dispersion* (Lorentz violation), not foam accumulation. The foam-fuzziness constraint is `AMNC15` below. |
| `NdV03` | "Measuring the foaminess of space-time: foundation and interpretation. *Foundations of Physics* 30, 795" | same paper, correct title: *Measuring the foaminess of space-time with gravity-wave interferometers*, Found. Phys. 30, 795–805, DOI 10.1023/a:1003745212871 — `verified (Crossref)`. (The key says 03 but the paper is 2000; leave the key — keys are stable — or rename deliberately in one pass.) |

Also upgrade to `verified (Crossref, 2026-11-16)` (data checked, DOIs resolve):
`Bek73` (10.1103/physrevd.7.2333), `Haw75` (10.1007/bf02345020), `Car74`
(10.1017/s0074180900235638).

### Additions (all DOI-verified 2026-11-16 unless marked)

| key | used in | claim it carries | full citation | status |
|---|---|---|---|---|
| Whe55 | §5.5 | The first concrete Planck-scale metric-fluctuation conjecture; ancestor of the foam picture | Wheeler, J. A. (1955). *Geons.* Physical Review 97, 511–536. DOI 10.1103/physrev.97.511 | verified (Crossref) |
| Whe57 | §5.5 | Quantum geometrodynamics: the foam is quantized geometry — standard QM applied to the metric | Wheeler, J. A. (1957). *On the nature of quantum geometrodynamics.* Annals of Physics 2, 604–614. DOI 10.1016/0003-4916(57)90050-7 | verified (Crossref) |
| Whe83 | §5.5 | "Law without law": dynamical law not fundamental — about law's origin, not conservation in the foam | Wheeler, J. A. (1983). *Law without law.* In J. A. Wheeler & W. H. Zurek (Eds.), *Quantum Theory and Measurement* (pp. 182–213). Princeton University Press. Book DOI 10.1515/9781400854554 | needs-human (page range; book DOI verified) |
| Whe80 | (unused; optional) | Pregeometry: deriving spacetime and law from something deeper | Wheeler, J. A. (1980). *Pregeometry: motivations and prospects.* In *Quantum Theory and Gravitation* (pp. 1–11). DOI 10.1016/b978-0-12-473260-5.50005-x | verified (Crossref) |
| Haw76 | §5.5 | Breakdown of predictability: gravitational collapse may destroy information | Hawking, S. W. (1976). *Breakdown of predictability in gravitational collapse.* Physical Review D 14, 2460–2473. DOI 10.1103/physrevd.14.2460 | verified (Crossref) |
| Haw78 | §5.5 | Spacetime foam: virtual black holes as the decoherence mechanism | Hawking, S. W. (1978). *Spacetime foam.* Nuclear Physics B 144, 349–362. DOI 10.1016/0550-3213(78)90375-9 | verified (Crossref) |
| Haw82 | §5.5 | The superscattering operator $: non-unitary but linear evolution of density matrices | Hawking, S. W. (1982). *The unpredictability of quantum gravity.* Communications in Mathematical Physics 87, 395–415. DOI 10.1007/bf01206031 | verified (Crossref) |
| Haw87 | §5.5 | Wormhole-mediated loss of coherence — the foam-specific loss proposal | Hawking, S. W. (1987). *Quantum coherence down the wormhole.* Physics Letters B 195, 337–343. DOI 10.1016/0370-2693(87)90028-1 | verified (Crossref) |
| EHNS84 | §5.5 | Intrinsic decoherence: a fundamental non-unitary term (the α,β,γ test theory) | Ellis, J., Hagelin, J. S., Nanopoulos, D. V., & Srednicki, M. (1984). *Search for violations of quantum mechanics.* Nuclear Physics B 241, 381–405. DOI 10.1016/0550-3213(84)90053-1 | verified (Crossref) |
| Pen96 | §5.5 | Gravitationally induced state reduction: fundamental modification of QM | Penrose, R. (1996). *On gravity's role in quantum state reduction.* General Relativity and Gravitation 28, 581–600. DOI 10.1007/bf02105068 | verified (Crossref) |
| Page93 | §5.5 | `$` defined as a linear non-unitary map on ρ; information can come out in the radiation | Page, D. N. (1993). *Information in black hole radiation.* Physical Review Letters 71, 3743–3746. DOI 10.1103/physrevlett.71.3743; the `$` definition and the (A)–(F) option list are in *Black hole information*, arXiv:hep-th/9305040, §§1, 5 | verified (Crossref + arXiv full text) |
| Haw05 | §5.5 | Hawking's later position: quantum gravity is unitary even in the foam | Hawking, S. W. (2005). *Information loss in black holes.* Physical Review D 72, 084013. DOI 10.1103/physrevd.72.084013 (arXiv:hep-th/0507171) | verified (Crossref + arXiv full text) |
| Carlip23 | §5.5 | Review: Wheeler's foam; §5.2 the decoherence/unitarity debate in the foam | Carlip, S. (2023). *Spacetime foam: a review.* Reports on Progress in Physics 86, 066001. DOI 10.1088/1361-6633/acceb4 (arXiv:2209.14282) | verified (Crossref + arXiv full text) |
| AMPS13 | §5.5 (optional) | Unitarity as one of three assumptions the firewall argument makes incompatible | Almheiri, A., Marolf, D., Polchinski, J., & Sully, J. (2013). *Black holes: complementarity or firewalls?* JHEP 2013(2) 062. DOI 10.1007/jhep02(2013)062 | verified (Crossref + arXiv abstract) |
| AMNC15 | §6.2 | Planck-scale limit on spacetime fuzziness / stochastic Lorentz violation from GRB timing — the foam-fuzziness channel | Vasileiou, V., Granot, J., Piran, T., & Amelino-Camelia, G. (2015). *A Planck-scale limit on spacetime fuzziness and stochastic Lorentz invariance violation.* Nature Physics 11, 344–346. DOI 10.1038/nphys3270 | verified (Crossref) |
| Chou17 | §6.2 | The Holometer instrument | Chou, A., et al. (2017). *The Holometer: an instrument to probe Planckian quantum geometry.* Classical and Quantum Gravity 34, 065005. DOI 10.1088/1361-6382/aa5e5c | verified (Crossref) |
| Chou16 | §6.2 | The Holometer cross-spectrum result / upper limits | Chou, A. S., et al. (2016). *First measurements of high frequency cross-spectra from a pair of large Michelson interferometers.* Physical Review Letters 117, 111102. DOI 10.1103/PhysRevLett.117.111102 (arXiv:1512.01216) | verified (Crossref + arXiv abstract) |
| AC13 | (optional) | The phenomenology review: foam-induced decoherence as a departure from QM | Amelino-Camelia, G. (2013). *Quantum-spacetime phenomenology.* Living Reviews in Relativity 16, 5. DOI 10.12942/lrr-2013-5 (arXiv:0806.0339) | verified (Crossref + arXiv full text) |

**Status vocabulary.** The ledger today defines `verified` narrowly (checked
against an in-tree verified source). Crossref checking is stronger than
`needs-human` but is not that. Proposal: add one legend line —
`verified (Crossref)` — "DOI metadata (title, authors, venue, volume, pages,
year) checked against Crossref's API record on the date named; the *claim* the
row carries is still an interpretation unless separately sourced." Then the
nine `needs-human` rows that this memo verified can be promoted, and the ones
that are still memory-written stay `needs-human`.

## 7. Adjacent finding, outside this domain (§6.2 — belongs to the §6 scout)

Not mine to fix, but found while verifying Ng & van Dam and must be reported:

1. **The "picosecond" attribution cannot be the volumetric family.**
   §6.2 says: "$L ≈ (l_p²R)^{1/3}$ at $5×10^{-15}$ m [...] its signature
   accumulates along cosmological path lengths — picosecond-scale timing
   structure [...]". Arithmetic [MEASURED]: $5×10^{-15}\,\mathrm{m}/c =
   1.7×10^{-23}\,\mathrm{s}$, eleven orders below a picosecond. The
   picosecond figure is what the *transverse* $\sqrt{l_pR}$ form gives at
   $R=4.4×10^{26}$ m: $\sqrt{l_pR}=8.4×10^{-5}$ m, $/c = 2.8×10^{-13}$ s ≈
   0.28 ps. So the sentence gives the demoted family's scale to the headline
   family — the two sentences of §6.2 contradict each other.
2. **`VPF13` is the wrong citation for "already constrained".** It constrains
   linear vacuum dispersion, not accumulation. The foam-fuzziness constraint
   is `AMNC15` (Nature Physics 2015). For the volumetric family's *angular*
   blurring there is also a recent GRB test: Steinbring, E. (2023).
   *Holographic quantum-foam blurring is consistent with observations of
   GRB221009A.* Galaxies 11, 115. DOI 10.3390/galaxies11060115 — note its
   abstract says the blurring "would not result in photon loss", which is a
   different signature from the paper's loss story.
3. Consequence to hand to the §6 writer: the honest sentence is *not* "already
   constrained"; at $1.7×10^{-23}$ s the volumetric projection is far below any
   current timing sensitivity, and the constrained model classes are different
   ones. If that changes the abstract's promise, the human decides.

## 8. What a human must still verify (honestly needs-human)

- **Wheeler 1957 was not read** (paywalled). The foam characterization rests on
  Carlip's review (open, verified) and Wheeler's own quoted description (via
  Carlip). If the paper wants a direct Wheeler claim, someone with library
  access should read 1957 §1 and Wheeler 1983.
- Wheeler 1983 "Law without law": page range 182–213 from memory; the book's
  DOI is verified. The 1985 NATO version (*Bohr's "Phenomenon" and "Law Without
  Law"*, pp. 363–378, DOI 10.1007/978-1-4613-2443-0_25) is fully verified and
  is an acceptable substitute.
- Wheeler 1981 *The Lesson of the Black Hole* (Proc. Am. Phil. Soc. 125, 25) —
  quoted via Carlip, not read.
- Hawking 1982 / 1987 and EHNS 1984 abstracts — metadata verified via Crossref,
  *content* read via Page's and Amelino-Camelia's reviews, not the originals.
- MTW §43.4 page numbers (Foam section) — Carlip cites it; not read here.
- `Wig59` (Wigner's book) — untouched by this memo.

## 9. Method / verification log (what ran, so the claims above are auditable)

- Crossref `api.crossref.org/works` (DOI lookups and `query.bibliographic`):
  all metadata in §6 quoted from responses received 2026-11-16.
- OpenAlex `api.openalex.org` for abstracts/locations where Crossref has none.
- Fetched and text-extracted (ghostscript `txtwrite`), read directly:
  - Carlip 2023, arXiv:2209.14282v3 (full review; §1 Wheeler, §5.2
    decoherence/unitarity, §5.3 divergences, references [2]–[6], [216]–[230]);
  - Amelino-Camelia 2013, arXiv:0806.0339 (§2.2.3–2.2.4, §4.5.1);
  - Page 1993 review, arXiv:hep-th/9305040 (abstract, §1, option list (A)–(F));
  - Hawking 2005, arXiv:hep-th/0507171 (abstract + introduction);
  - Ng & van Dam 2000, arXiv:gr-qc/9906003 (abstract + the (l l_P²)^{1/3}
    derivation);
  - Carroll's GR notes, arXiv:gr-qc/9712019 (the Bianchi → conservation
    derivation, §4: "automatically conserved [...] which always obeys
    ∇_μG^μν=0") — background for the "conservation as structural identity"
    reading, not cited in any proposed patch;
  - Steinbring 2023, arXiv:2311.10168 (abstract + α parametrization);
  - AMPS 2013, arXiv abstract (HTML).
- Searches returning nothing relevant: the no-cloning list in §4.
- `memo` itself: not gated (prose). `paper-check.sh` / `sync-check.sh` were run
  on the untouched tree to confirm this unit changed nothing the gates see.

## 10. Bottom line for the planner

1. Adopt C1, C2, C3 in `paper.md` §5.5 — C2 is a factual error, not a style
   preference.
2. Apply the §6 citation corrections and additions to `citations.md`; add the
   `verified (Crossref)` legend line.
3. Send §7 to the §6 scout / human; do not let §6.2 ship with "picosecond" on
   the volumetric family or with `VPF13` as the constraint citation.
4. Nothing here needs a Lean change; no gate movement is implied beyond the
   paper's own two scripts (word count stays in range; new forbidden-pattern
   hits: none — checked by inspection of the proposed sentences).
