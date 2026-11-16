# Domain 3 — local and sector-dependent unitarity

**The question.** Is there literature proposing that unitarity is *emergent* or *sector-specific* — holding inside some sector, failing globally or at some scale — rather than a universal postulate? Ranked by proximity to this paper's structure: *unitarity is the boundary condition of a sector; it holds in a stable sector and fails outside, where the outside is characterized by a formal rule-set* (paper.md §5.5).

**Method and label discipline.** Bibliographic metadata below was fetched this session from the INSPIRE-HEP API and the Crossref API; every such fact is marked **[FETCHED]**, and quotes are from the **fetched abstract**, not from the paper body. Nothing was read in full text — see "What a human should still check", item 8. Items from model knowledge are marked **[MEMORY]** and are not load-bearing. No DOI, page range or author list below is invented; where a fetched field looked internally inconsistent it is flagged `needs-human` in the citation table rather than silently repaired.

One correction up front, because it propagates: the lead as briefed — "Banks–Peskin–Susskind 1984, *Limitations on quantum mechanics from black holes*" — **[FETCHED]** does not resolve. Crossref search on that title returns nothing on point, and INSPIRE's 1984 record for those three authors is *Difficulties for the Evolution of Pure States Into Mixed States*, Nucl. Phys. B **244** (1984) 125–134, DOI 10.1016/0550-3213(84)90184-6, authors in the order **Banks, Susskind, Peskin** (fetched author list: "Banks, Tom; Susskind, Leonard; Peskin, Michael E."). That paper is the real 1984 target and is cited as such below.

---

## Direct answer

**Yes — the conversation exists, it is mainstream rather than fringe, and it divides into four strands. None of them occupies this paper's position, and one of them is close enough that §5.5's guard sentence, as currently written, is refutable by a single citation.**

Strand 1 — unitarity **fails, fundamentally** (Hawking 1976; Banks–Susskind–Peskin 1984; Unruh–Wald 1995; Penrose 1996; Gambini–Porto–Pullin 2007). These are the load-bearing precedents for the paper's *premise* that conservation is something a world must achieve rather than something it is handed (§1). They establish that the failing regime is physically describable and, in the later cases, mechanically characterized — Penrose with an explicit rate, Gambini–Porto–Pullin with a modified Schrödinger equation, Hawking with a named replacement for the S-matrix. What none of them does is make the failing regime a **sector separated from a lawful sector by a rule**.

Strand 2 — unitarity is **emergent** ('t Hooft's cellular-automaton interpretation; Adler's trace dynamics; Zanardi–Campos Venuti's dissipation-projected dynamics; Xi et al. on quasi-Hermitian systems). Here unitarity is derived or approximate rather than axiomatic — exactly the paper's move — but the thing it emerges *from* is a deterministic substrate or a dissipative projection, not a lawless region. The outside is a deeper lawful layer, not an unlawful one.

Strand 3 — unitarity is **sector-restricted and positively characterized**. This is the closest structural precedent, and it is in JHEP/PRL-class venues: Cotler–Jensen find the de Sitter infinite-time evolution operator "is not unitary, although we find that it acts unitarily on a subspace"; Akers–Engelhardt–Harlow–Penington–Vardhan show that in the black-hole interior "there can be no isometric (i.e. inner-product preserving) encoding" of the effective interior into the fundamental degrees of freedom, and characterize the failure precisely (null states, complexity); Bender's PT-symmetric quantum mechanics defines its sector by a **formal criterion** — unbroken PT symmetry — inside which "the spectrum is real" and "one can construct a time-independent inner product with a positive-definite norm", with the broken phase outside it. Every element of "unitarity holds on a sector, fails off it, and the boundary is formal" has a precedent here.

Strand 4 — unitarity is **not global** because the global state does not exist: Ellis argues that "generically only local wave functions exist", that "there is no single wave function for a cat or macroscopic object … let alone for the Universe as a whole". This is the closest anyone comes to denying that global unitarity is even well-formed — and the weakest on formalism, since it is a reading of quantum theory rather than a calculus.

**What no fetched account contains**, and what this paper therefore actually owns: (i) the boundary between lawful and lawless is a **syntactic restriction of the theory's own rule-set** (a discard ban), not a parameter, a scale, a topological process or an eigenvalue reality condition; (ii) the outside is characterized by a **formal rule-set in which conservation fails while no-cloning still holds** — the "lossy, not a breeder" fingerprint of §5.5 has no counterpart in the fetched literature; (iii) the restriction is **derived from instability** — the unrestricted dynamics provably never settles, so the restriction is selected rather than imposed. Hawking and BPS show that generalizing the dynamics is necessary; BPS shows it costs locality or energy conservation; nobody fetches shows the unrestricted world failing to settle and therefore selecting its own lawful sector.

**The finding that matters for the paper.** §5.5 currently reads: *"No established account — foam, landscape, eternal inflation — has the conservation laws themselves failing outside a stable sector; mainstream treatments assume quantum mechanics holds everywhere and let geometry fluctuate."* Read strictly, Cotler–Jensen (JHEP, 2021) is a counterexample to the first clause: a published account in which the global evolution is not unitary and unitarity holds on a subspace. The sentence is defensible only once it is tightened to the *combination* claim, which survives every fetched precedent. A suggested replacement is in "What a human should still check", item 1.

---

## Closest precedents

Ranked by proximity to the target structure. "Lacks" names precisely what keeps each one from being this paper's claim.

### Tier 1 — the sector/criterion structure is present

**1. Cotler & Jensen, *Emergent unitarity in de Sitter from matrix integrals*** — JHEP **12** (2021) 089, DOI 10.1007/JHEP12(2021)089, arXiv:1911.12358 **[FETCHED]**

> "There is a Hilbert space of asymptotic states and an infinite-time evolution operator between the far past and far future. **This evolution is not unitary, although we find that it acts unitarily on a subspace** up to non-perturbative corrections. These corrections come from processes which involve changes in the spatial topology, including the nucleation of baby universes. … the bulk quantum mechanics, including the Hilbert space and approximately unitary evolution, emerge from a classical integral."

This is the single closest sentence in the fetched literature to "unitarity holds on a sector and fails off it" — and it is in de Sitter, this paper's own setting. Proximity: **high on the shape, low on the mechanism.** Lacks: the subspace is not a *stable* sector in any selection sense; the failure is a specific non-perturbative process (topology change, baby universes), not a rule-set; there is no no-cloning half, so no asymmetry claim; and unitarity is emergent from a matrix integral, i.e. from a deeper *lawful* structure.

**2. Akers, Engelhardt, Harlow, Penington & Vardhan, *The black hole interior from non-isometric codes and complexity*** — JHEP **06** (2024) 155, DOI 10.1007/JHEP06(2024)155, arXiv:2207.06536 **[FETCHED]**

> "at late times the apparent number of interior degrees of freedom in effective field theory can vastly exceed the true number of fundamental degrees of freedom, so **there can be no isometric (i.e. inner-product preserving) encoding** of the former into the latter. … via the idea of 'non-isometric codes protected by computational complexity'."

The closest precedent for the paper's *positive* characterization of the failing regime: non-unitarity is not a defect to be removed but a structure with a name, a mechanism (null states) and a control parameter (complexity). Proximity: **high on "the failing region is characterized", and it reverses the paper's hierarchy** — here the fundamental theory stays unitary and the *effective* description fails; in this paper the failing regime is the fundamental one and the sector is the effective one. That reversal is the honest gap, and a referee will see it.

**3. Bender, *Making sense of non-Hermitian Hamiltonians*** — Rep. Prog. Phys. **70** (2007) 947, DOI 10.1088/0034-4885/70/6/R03, arXiv:hep-th/0703096 **[FETCHED]**

> "If H has an unbroken PT symmetry, then the spectrum is real. … Using C, one can construct a time-independent inner product with a positive-definite norm. Thus, PT-symmetric Hamiltonians describe a new class of complex quantum theories having positive probabilities and unitary time evolution."

The only fetched account where the sector boundary is a **formal criterion** rather than a physical process: unbroken PT symmetry in, real spectrum and unitary evolution out. Structurally this is the closest thing to "unitarity as a boundary condition", and it is the precedent to answer if a referee asks "isn't the sector idea just PT symmetry?". Proximity: **high on formality, absent on conservation.** Lacks: no no-cloning claim, no claim that a conservation law fails outside (the broken phase's pathology is complex energies, not information loss), and the sector is a parameter region rather than a rule-set. Note the paper does *not* claim unitarity fails off-sector as a conservation-law failure, and neither should ours by analogy.

### Tier 2 — unitarity fails, with the failure characterized

**4. Hawking, *Breakdown of Predictability in Gravitational Collapse*** — Phys. Rev. D **14** (1976) 2460, DOI 10.1103/PhysRevD.14.2460 **[FETCHED]**

> "Because part of the information about the state of the system is lost down the hole, the final situation is represented by a density matrix rather than a pure quantum state. This means **there is no S matrix** for the process of black-hole formation and evaporation. Instead one has to introduce a new operator, called the **superscattering operator**, which maps density matrices … to density matrices."

The origin of the whole conversation, and — importantly for the ranking — the first instance of the paper's *positive-characterization* move: the failing dynamics is not left as an absence, it is given a formal replacement (density-matrix maps). Proximity: **high on "unitarity is not universal and the outside has a formal description", zero on "sector".** There is no lawful sector here at all; the failure is claimed for a region of spacetime, not for a region of a rule-space.

**5. Banks, Susskind & Peskin, *Difficulties for the Evolution of Pure States Into Mixed States*** — Nucl. Phys. B **244** (1984) 125–134, DOI 10.1016/0550-3213(84)90184-6 **[FETCHED]**

> "Motivated by Hawking's proposal that the quantum-mechanical density matrix ϱ obeys an equation more general than the Schrödinger equation, we study the general properties of evolution equations for ϱ. We argue that **any more general equation for ϱ violates either locality or energy-momentum conservation**."

Structurally the closest precedent to this paper's *cost argument*: a proposed generalization of the dynamics is shown to be paid for in a named currency. §5.3's "diverges and pays forever, delivers nothing" is the same rhetorical form in a proof assistant. Proximity: **medium-high as an argument-shape, low as a sector claim.**

**6. Unruh & Wald, *On evolution laws taking pure states to mixed states in quantum field theory*** — Phys. Rev. D **52** (1995) 2176, DOI 10.1103/PhysRevD.52.2176, arXiv:hep-th/9503024 **[FETCHED]**

> "we give a simple class of examples of evolution laws where rapid evolution from pure states to mixed states occurs for a wide class of states with appropriate properties at the 'Planck scale', suitable locality and causality properties hold for all states, and the deviations from ordinary dynamics … are unobservably small for all states which one could expect to produce in a laboratory."

Proximity: **the closest on "the failing regime is invisible inside the stable one".** This is the cleanest statement that non-unitary evolution can be confined to a corner of state space while ordinary physics recovers. Lacks: the corner is defined by energy scale, not by an explicit rule; and there is no claim that the corner is where *conservation* fails while kinematics survives.

**7. Penrose, *On gravity's role in quantum state reduction*** — Gen. Rel. Grav. **28** (1996) 581–600, DOI 10.1007/BF02105068 **[FETCHED]**

> "the definition of the time-translation operator for the superposed space-times involves an inherent ill-definedness, leading to an essential uncertainty in the energy of the superposed state … This is consistent with a suggested finite lifetime of the order of ħ/E_Δ for the superposed state."

Proximity: **medium.** The collapse is explicitly non-unitary and — unusually — carries a rate, i.e. the outside of unitary evolution is quantitatively characterized. Lacks: the trigger is gravitational self-energy, a mass criterion, not a rule; and the paper's own §5.4 fence (no rate, no mechanism) means this precedent is *contra*, not *pro*, if leaned on carelessly — cite it for "non-unitary collapse is a live hypothesis", never for "our unrestricted calculus predicts a rate".

**8. Gambini, Porto & Pullin, *Fundamental decoherence from quantum gravity: a pedagogical review*** — Gen. Rel. Grav. **39** (2007) 1143, DOI 10.1007/s10714-007-0451-1, arXiv:gr-qc/0603090 **[FETCHED]**

> "We present a discussion of **the fundamental loss of unitarity** that appears in quantum mechanics due to the use of a physical apparatus to measure time. … We derive the modified Schrödinger equation that arises in quantum mechanics with real clocks."

Proximity: **medium-high on mechanism, low on sector.** Unitarity fails fundamentally, for a structural reason, with an explicit replacement dynamics. Lacks: the failure is argued to affect *all* states, so there is no stable sector at all — it is the opposite partition from this paper's.

### Tier 3 — unitarity as emergent, from something lawful

**9. 't Hooft, *The Cellular Automaton Interpretation of Quantum Mechanics*** — arXiv:1405.1548; Fundam. Theor. Phys. **185**, Springer **[FETCHED; year/volume field inconsistent — see table]**

> "Quantum mechanics is looked upon as **a tool, not as a theory**. Examples are displayed of models that are classical in essence, but can be analysed by the use of quantum techniques, and we argue that even the Standard Model, together with gravitational interactions, might be viewed as a quantum mechanical approach to analyse a system that could be classical at its core."

Proximity: **high as a philosophical precedent for "unitarity is not fundamental", low as a sector claim** — the substrate is deterministic, hence maximally lawful. This is the precedent that makes the paper's "grammar is prior to dynamics" move legible to a physicist, and it should be cited for exactly that and nothing more.

**10. Adler, *Quantum Theory as an Emergent Phenomenon: The Statistical Mechanics of Matrix Models as the Precursor of Quantum Field Theory*** — Cambridge University Press, 2004, DOI 10.1017/cbo9780511535277 **[FETCHED]**

Trace dynamics: quantum theory (including its unitarity) as the thermodynamic limit of a deeper classical matrix dynamics. Proximity: **medium.** Same "unitarity is derived" posture, same absence of a lawless region. Cite alongside 't Hooft as the two canonical "emergent quantum mechanics" programs.

**11. Zanardi & Campos Venuti, *Geometry, robustness, and emerging unitarity in dissipation-projected dynamics*** — Phys. Rev. A **91** (2015) 052324, DOI 10.1103/PhysRevA.91.052324, arXiv:1412.6198 **[FETCHED]**

> "the dynamics inside the SSS is governed by an effective, dissipation-projected, Hamiltonian. … **in some cases an effective unitary dynamics can emerge out of purely dissipative interactions.**"

Proximity: **medium — and this one has a genuine sector.** Unitarity emerges inside a subspace (the steady-state set), from dynamics that is not unitary outside it. That is the paper's shape in an open-quantum-system key. Lacks: no fundamental claim, no rule-set boundary, no no-cloning asymmetry.

**12. Xi, Zhang & Gu, *Classification of topological phases in one dimensional interacting non-Hermitian systems and emergent unitarity*** — Sci. Bull. **66** (2021) 1447, DOI 10.1016/j.scib.2021.04.027, arXiv:1911.01590 **[FETCHED]**

> "the many-body topological Berry phase, which is well defined for all interacting **quasi-Hermitian systems (non-Hermitian systems that have real energy spectrum)**."

The same formal sector criterion as Bender (reality of the spectrum), used as a working classification tool in condensed matter. Proximity: **medium** — evidence that "a formally-defined sector in which unitarity holds" is a *normal* move in physics, which is the useful thing to be able to say to a referee.

### Tier 4 — unitarity is not a global fact

**13. Ellis, *Quantum physics and biology: the local wavefunction approach*** — J. Phys. Conf. Ser. **2533** (2023) 012019, DOI 10.1088/1742-6596/2533/1/012019, arXiv:2301.06516 **[FETCHED]**

> "I claim that instead, in the real Universe, **generically only local wave functions exist**. Non-local wave functions occur for carefully engineered contexts such as Bell experiments, but there is no single wave function for a cat or macroscopic object such as a brain, let alone for the Universe as a whole."

**14. Ellis, *On the philosophy of cosmology*** — Stud. Hist. Phil. Sci. B **46** (2014) 5, DOI 10.1016/j.shpsb.2013.07.006 **[FETCHED]** (the brief's "Ellis 2012/2014" lead; the same author's earlier *Issues in the philosophy of cosmology*, astro-ph/0602280 [FETCHED], is the companion.)

Proximity for 13–14: **high on the conclusion, weak on the formalism.** If no wavefunction of the universe exists, global unitary evolution is not a well-formed statement — which is the paper's conclusion reached from the opposite direction (Ellis subtracts the global state; this paper shows the global rule-set is lawless). Lacks: no calculus, no derivation, no sector boundary. Cite only if the paper wants a philosophy-of-physics ally; it invites a philosophy referee in exchange.

---

## Novelty verdict

**PARTIALLY-NOVEL.** Preceded in every component; unprecedented in the combination and in one specific argumentative move.

**Preceded.** (a) "Unitarity is not a postulate but something a world achieves" — Hawking 1976, BPS84, Unruh–Wald 1995, 't Hooft, Adler, all fetched. (b) "Unitarity holds on a subspace and fails off it" — Cotler–Jensen, fetched, in JHEP, in de Sitter. (c) "The sector boundary is a formal criterion" — Bender, Xi et al., fetched. (d) "The failing regime is positively characterized by a formal rule-set" — Hawking's superscattering operator, non-isometric codes' null states, fetched. (e) "Unitarity is not global" — Ellis, fetched. A referee who wants to say "this is all known" has five independent citations for four of the five components.

**Not preceded, and defensibly ours.**

1. **The boundary is syntactic, not parametric.** Every fetched precedent locates the boundary in a parameter (PT symmetry unbroken/broken; Planck-scale states; gravitational self-energy; dissipative gap; spatial topology; radiation-reality of the spectrum). None locates it in a *restriction on which derivations exist*. "The boundary between them is one rule: the discard" (paper.md §5.5) has no fetched counterpart. This is the paper's strongest novelty claim and it is machine-checkable against the tree, which no precedent is.
2. **The asymmetry fingerprint.** No fetched account claims that the failing regime preserves no-cloning while losing conservation. Cotler–Jensen's failure is approximate and correction-suppressed; non-isometric codes' failure is complexity-protected and the fundamental theory is unitary; Bender's outside has complex energies. The "lossy, not a breeder" property — `Dcare.no_contraction_content` holding at the full unrestricted grain — is a falsifiable-against-the-tree prediction about the outside, and nothing fetched predicts anything similar. This is the one place where the paper says something about the lawless region that is *not* a restatement of an existing position.
3. **Selection by non-termination.** BPS84 shows a generalization of the dynamics *costs* locality or energy conservation. Nobody fetched shows the unrestricted dynamics **failing to settle**, and therefore nobody derives the necessity of the restriction from instability rather than positing it. "A stable sector and a lawful sector are the same sector" is, in this form, novel — provided the paper keeps the claim structural (`adversary_spin_diverges`, `spin_pays_forever_buys_nothing`) and does not dress it as a physical selection mechanism.

**Where the paper currently overclaims, and must not.** The sentence *"No established account … has the conservation laws themselves failing outside a stable sector"* is false as written: Cotler–Jensen is such an account, fetched, published, in the paper's own cosmological setting. The defensible claim is narrower and survives all fourteen precedents: no established account derives the lawful/lawless boundary from a restriction on the theory's own rules, nor characterizes the lawless side by a rule-set that preserves the kinematic law while dropping the dynamical one. Fixing this sentence is not cosmetic — it is the difference between a claim a referee kills with one citation and a claim a referee has to argue with.

---

## Proposed citation rows

EXACTLY the ledger format (`key | used in | claim it carries | full citation | status`), for insertion into `citations.md` by whoever owns that file. `used in` names proposed placement in `paper.md`; every row is a *new* row (none duplicates an existing key). `status` is `verified [FETCHED]` where the fetched record's fields are internally consistent, `needs-human` where a fetched field is inconsistent or partial.

| key | used in | claim it carries | full citation | status |
|---|---|---|---|---|
| Haw76 | §1, §5.5 | Unitarity fails in black-hole evaporation: no S-matrix, density matrices in, a superscattering operator as the replacement dynamics — the original "conservation must be achieved, not assumed" precedent, and the first positive formal characterization of a non-unitary regime | Hawking, S. W. (1976). *Breakdown of Predictability in Gravitational Collapse.* Physical Review D 14, 2460. DOI 10.1103/PhysRevD.14.2460 | verified [FETCHED INSPIRE] |
| BPS84 | §1, §5.5 | Generalizing the density-matrix evolution beyond the Schrödinger equation costs either locality or energy-momentum conservation — the cost-argument shape that §5.3's divergence theorems mirror | Banks, T., Susskind, L., & Peskin, M. E. (1984). *Difficulties for the Evolution of Pure States Into Mixed States.* Nuclear Physics B 244, 125–134. DOI 10.1016/0550-3213(84)90184-6 | verified [FETCHED INSPIRE] |
| UW95 | §1, §5.5 | Non-unitary (pure-to-mixed) evolution can be confined to Planck-scale states while ordinary laboratory physics stays unitary and causal — the precedent for "the failing regime is invisible inside the stable one" | Unruh, W. G., & Wald, R. M. (1995). *On evolution laws taking pure states to mixed states in quantum field theory.* Physical Review D 52, 2176. DOI 10.1103/PhysRevD.52.2176. arXiv:hep-th/9503024 | verified [FETCHED INSPIRE] |
| Pen96 | §5.5 | Gravitationally induced state reduction is explicitly non-unitary, with a characteristic lifetime of order ħ/E_Δ — cited for "non-unitary collapse is live", NOT for any rate this paper derives | Penrose, R. (1996). *On gravity's role in quantum state reduction.* General Relativity and Gravitation 28, 581–600. DOI 10.1007/BF02105068 | verified [FETCHED INSPIRE] |
| GPP07 | §5.5 | Unitarity is lost *fundamentally* (not environmentally) when time is measured by a physical clock, with a modified Schrödinger equation as the replacement — non-unitarity as a structural consequence, not a defect | Gambini, R., Porto, R. A., & Pullin, J. (2007). *Fundamental decoherence from quantum gravity: a pedagogical review.* General Relativity and Gravitation 39, 1143. DOI 10.1007/s10714-007-0451-1. arXiv:gr-qc/0603090 | verified [FETCHED INSPIRE] |
| Ben07 | §5.5 | The closest formal sector criterion: unbroken PT symmetry gives a real spectrum, a positive-definite inner product and unitary evolution; the sector boundary is a symmetry condition, not a process | Bender, C. M. (2007). *Making sense of non-Hermitian Hamiltonians.* Reports on Progress in Physics 70, 947. DOI 10.1088/0034-4885/70/6/R03. arXiv:hep-th/0703096 | verified [FETCHED INSPIRE] |
| CJ19 | §5.5 | The closest precedent to the paper's own structure: in a de Sitter model the infinite-time evolution "is not unitary, although it acts unitarily on a subspace", with the failure traced to topology change — forces the §5.5 guard sentence to be narrowed | Cotler, J., & Jensen, K. (2021). *Emergent unitarity in de Sitter from matrix integrals.* Journal of High Energy Physics 12 (2021) 089. DOI 10.1007/JHEP12(2021)089. arXiv:1911.12358 | verified [FETCHED INSPIRE] |
| AEHPV22 | §5.5 | Non-unitarity as a characterized structure rather than an absence: no isometric encoding of the black-hole interior exists, and the failure is organized by null states and computational complexity — the strongest precedent for positively characterizing a non-unitary regime | Akers, C., Engelhardt, N., Harlow, D., Penington, G., & Vardhan, S. (2024). *The black hole interior from non-isometric codes and complexity.* Journal of High Energy Physics 06 (2024) 155. DOI 10.1007/JHEP06(2024)155. arXiv:2207.06536 | verified [FETCHED INSPIRE] |
| Zan15 | §5.5 | Effective unitary dynamics can emerge inside a subspace (the steady-state set) out of purely dissipative, non-unitary dynamics outside it — the paper's sector shape in an open-systems key | Zanardi, P., & Campos Venuti, L. (2015). *Geometry, robustness, and emerging unitarity in dissipation-projected dynamics.* Physical Review A 91, 052324. DOI 10.1103/PhysRevA.91.052324. arXiv:1412.6198 | verified [FETCHED INSPIRE] |
| Xi21 | §5.5 | "Quasi-Hermitian systems (non-Hermitian systems that have real energy spectrum)" are a working, formally-defined sector in condensed matter — evidence that a formally-delimited unitary sector is a normal move in physics | Xi, W., Zhang, Z.-H., & Gu, Z.-C. (2021). *Classification of topological phases in one dimensional interacting non-Hermitian systems and emergent unitarity.* Science Bulletin 66, 1447. DOI 10.1016/j.scib.2021.04.027. arXiv:1911.01590 | verified [FETCHED INSPIRE] |
| tHooft | §1, §5.5 | Quantum mechanics as "a tool, not a theory": unitary quantum evolution emergent from a deterministic classical substrate — the canonical "unitarity is derived" program, and the precedent that makes a grammar-prior-to-dynamics claim legible | 't Hooft, G. *The Cellular Automaton Interpretation of Quantum Mechanics: A View on the Quantum Nature of our Universe, Compulsory or Impossible?* Fundamental Theories of Physics 185, Springer. DOI 10.1007/978-3-319-41285-6. arXiv:1405.1548 | needs-human (INSPIRE returns volume 185 with year 2006; the Springer volume is 2016 — verify year, and whether to cite the arXiv or the book) |
| Adl04 | §1, §5.5 | Quantum theory, unitarity included, as the statistical-mechanical limit of a deeper classical matrix dynamics (trace dynamics) — the second canonical "unitarity is emergent" program | Adler, S. L. (2004). *Quantum Theory as an Emergent Phenomenon: The Statistical Mechanics of Matrix Models as the Precursor of Quantum Field Theory.* Cambridge University Press. DOI 10.1017/cbo9780511535277 | verified [FETCHED Crossref, monograph] |
| Ell23 | §5.5 | "Generically only local wave functions exist"; there is no wavefunction of the universe — so global unitary evolution is not a well-formed statement: the paper's conclusion reached from the opposite direction | Ellis, G. F. R. (2023). *Quantum physics and biology: the local wavefunction approach.* Journal of Physics: Conference Series 2533, 012019. DOI 10.1088/1742-6596/2533/1/012019. arXiv:2301.06516 | verified [FETCHED INSPIRE] |
| Ell14 | §5.5 | The philosophy-of-cosmology context in which the non-globality of the quantum state is argued — the brief's "Ellis 2012" lead, resolved to this record | Ellis, G. F. R. (2014). *On the philosophy of cosmology.* Studies in History and Philosophy of Modern Physics B 46, 5. DOI 10.1016/j.shpsb.2013.07.006 | needs-human (fetched page field is "5", which may be an article number rather than a first page — verify pages) |

**Existing row that must change.** `citations.md`'s `Whe57` and `Car74` rows stay as they are; but if `CJ19` and `AEHPV22` are adopted, §5.5's guard sentence must be edited in the same commit or the paper ships a claim its own reference list contradicts.

---

## What a human should still check

1. **The §5.5 guard sentence — the one substantive defect this review found.** Replace *"No established account — foam, landscape, eternal inflation — has the conservation laws themselves failing outside a stable sector; mainstream treatments assume quantum mechanics holds everywhere and let geometry fluctuate."* with something that survives CJ19 and AEHPV22, e.g.: *"Sector-restricted and emergent unitarity are established ideas — a de Sitter model whose global evolution is not unitary but acts unitarily on a subspace [CJ19], non-isometric encodings of the black-hole interior [AEHPV22], PT-symmetric quantum mechanics with its formal unbroken-sector criterion [Ben07]. What is not established is a boundary drawn by a restriction on the theory's own rule-set, or a lawless side that loses conservation while keeping no-cloning."* That version is defensible and strictly stronger as a novelty claim, because it names the near-misses instead of denying they exist.
2. **Whether to cite the near-misses at all.** Q2 of the plan kept §4 anchor-light. These 14 rows are all §5.5/§1, none is AdS/CFT-metric-load-bearing, so the constraint is respected — but CJ19 and AEHPV22 are the paper's most dangerous citations *and* its most valuable, and the argument for including them is that a referee will find them anyway. Recommend including both, with the tightened guard.
3. **The briefed BPS84 title is wrong** (see the correction at the top). Any downstream note, abstract or reply that repeats *"Limitations on quantum mechanics from black holes"* will propagate a citation that does not exist. The real target is *Difficulties for the Evolution of Pure States Into Mixed States*, and the author order is Banks, Susskind, Peskin.
4. **'t Hooft's year and volume** — fetched record says Fundamental Theories of Physics 185, year 2006; the Springer volume of that title is 2016. Cite the arXiv (1405.1548) if in doubt; do not print a year the ledger has not verified.
5. **Ellis's page field** — "Stud. Hist. Phil. Sci. B 46 (2014) 5" may be an article number. Verify before it appears in a bibliography.
6. **Wheeler–DeWitt constrained quantization — [MEMORY], not verified here.** The canonical Hamiltonian treatment of general relativity defines dynamics only on the constraint surface, and "unitarity" there is notoriously sector-relative (the problem of time). If the paper wants the *sector* framing in the Hamiltonian-GR sense, that is the oldest precedent and it needs its own verified row; my INSPIRE query for DeWitt 1967 returned nothing usable, so this is a lead, not a fact.
7. **The Penrose row is a trap if used carelessly.** Penrose's account carries a rate (ħ/E_Δ) and a mechanism; §5.4 of the paper fences both off explicitly. Cite Pen96 only for the existence of a live non-unitary-collapse program, or a referee will ask why our unrestricted calculus has no rate while Penrose's does.
8. **Search coverage — the honest limit of this review.** arXiv's API rate-limited this session (HTTP 429) after roughly eight queries, so arXiv coverage is partial and was supplemented by INSPIRE-HEP and Crossref. Google Scholar, Web of Science, PhilPapers and all paywalled full texts were not consulted. **Every "actual claim" quoted above is from a fetched abstract, never from a paper body** — abstracts can understate the failing-region characterization in the papers themselves (AEHPV22 and CJ19 in particular are likely richer in full text, and richer is *worse* for the paper's novelty, not better). Non-English literature and conference proceedings are uncovered. The absence claims in "Direct answer" and "Novelty verdict" are therefore absence-of-fetched-evidence, not proven absence, and should be worded that way in the paper if they appear at all.
9. **One more thing worth a targeted look, not done here:** whether any *superselection*-rule or *algebraic-QFT* literature frames unitarity as sector-relative in the strict sense (unitary implementability within a superselection sector). A `fulltext` search for "sector-dependent unitarity" returned nothing **[FETCHED: empty result]**, which is weak positive evidence for the novelty claim; a specialist search of the AQFT literature would strengthen or kill it.
