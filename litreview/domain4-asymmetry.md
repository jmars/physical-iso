# Domain 4 — the no-cloning / unitarity asymmetry

Literature scout note for `physical-iso/paper.md` §3.3 and §5.5.
Sources: arXiv API (rate-limited, largely unavailable this session), INSPIRE-HEP API,
Crossref REST API, OpenAlex, zbMATH Open. Every bibliographic field below is
**[FETCHED]** (metadata read from one of those APIs, source named) unless marked
**[MEMORY]** (no reachable record of the claim itself — metadata only).

Target claim under test: *in a calculus where information loss is permitted
(the discard rule is present), duplication remains absolutely forbidden —
"lossy, not a breeder" — and this mirrors a physics asymmetry in which
no-cloning is more fundamental than unitarity.*

---

## Direct answer

**The physics content of the asymmetry is real and well established; the
"more fundamental than unitarity" framing is not stated anywhere I could reach;
and the logic-side structure is long known under a different name.**

Three separate findings, in order of how much they cost the paper:

**(1) "Cloning forbidden where information can be lost" is standard — it is the
scope of the no-cloning theorem, not a discovery.** The ban is proved for
arbitrary completely positive maps (Lin99), for broadcasting of non-commuting
*mixed* states by "no physical means" (BCJFS96), and — decisively — for
essentially *any* nonclassical finite-dimensional probabilistic model satisfying
a no-signaling criterion, with no dynamical assumption at all (BBLW07). So yes:
non-unitary, information-losing channels exist in abundance, and the cloning ban
survives all of them. The exact twin of "lossy, not a breeder" is in the
literature. **[FETCHED: abstracts of BCJFS96, BBLW07, HHSS05, Kit15 via INSPIRE;
Lin99 metadata via Crossref]**

**(2) Nobody frames it as a hierarchy claim.** I found no source arguing that
no-cloning is *more fundamental than* unitarity. The closest thing to the
opposite is the *unified-origin* framing: Horodecki–Horodecki–Sen(De)–Sen prove
that in any theory whose dynamics is linear with respect to stochastic mixing,
no-cloning **and** no-deleting both follow *if* conservation of information is
assumed — a common origin, not an asymmetry (HHSS05). And the black-hole
literature treats unitarity as one *assumption* among several, with no-cloning
conspicuously absent from the list (a complementarity paper enumerates
"unitarity, entropy-area formula, existence of an information observer,
semi-classical QFT for the asymptotic observer, GR for the infalling observer"
— arXiv:1210.6733 **[FETCHED]**). So the asymmetry is a *scope* asymmetry that
everyone uses and nobody argues for. A paper claiming to have discovered it
would be overclaiming; a paper claiming to have mechanized it would not.

**(3) The pure-logic half is a textbook distinction, and a referee from PL will
say so.** "Cloning forbidden even with discard present" is the difference between
**linear** types (used exactly once: no dropping *and* no copying) and **affine**
types (used at most once: dropping allowed, copying still impossible). That is
standard substructural type theory (Gir87, Wal04 **[FETCHED]**), and it has an
exact concurrency twin: affine session types may be discarded but never
duplicated (MosVas18 **[FETCHED]**). Abramsky goes further and proves no-cloning
itself as a *structural* incompatibility — a natural copying operation cannot
coexist with the structure that models entanglement — explicitly "the same genre
as Joyal's lemma" in categorical logic, and calls the result "a heretofore
unsuspected connection between limitative results in proof theory and no-go
theorems in quantum mechanics" (Abr09 **[FETCHED, abstract]**).

Net: the *asymmetry* is preceded in both registers. What is not preceded is the
particular mechanized artefact — see the verdict below.

One correction the paper should absorb: **the physics asymmetry is not an
asymmetry between two regimes.** In quantum mechanics lossy channels and
no-cloning coexist *inside one theory* (a CPTP map need not be unitary, and
cloning is still impossible). §5.5's "outside the kernel / inside the kernel"
division therefore has **no physics twin** — there is no regime where unitarity
globally fails while the rest of QM holds. The physics precedent supports the
*logical shape* (a ban that survives what the other ban cannot), not the
*cosmological staging*. This is the honest form of §5.5's claim, and it is
already close to what the paper's guard paragraph says.

---

## Closest precedents

Ordered by how close each comes to "lossy, not a breeder".

### 1. Lin99 — no-cloning for arbitrary completely positive maps (closest)
Lindblad, G. (1999). *A general no-cloning theorem.* Letters in Mathematical
Physics **47**, 189–196. DOI 10.1023/A:1007581027660. **[FETCHED: Crossref +
zbMATH zbl 0922.47065]**

Claim: the no-cloning theorem is generalized from unitary operations to
completely positive maps — i.e., to channels that are neither invertible nor
trace-preserving. **Distance from our claim: essentially zero on the physics
side.** This *is* "duplication is forbidden in a strictly larger class of
processes than unitarity constrains".
*Caveat:* the abstract is paywalled and absent from Crossref, OpenAlex and
zbMATH (licence-restricted); the claim above is the paper's standing summary in
the field and is **[MEMORY]**, not fetched. The brief's guess of venue was
right in substance — it is *Lett. Math. Phys.*, not PRA.

### 2. BBLW07 — no-broadcasting holds with no dynamics at all
Barnum, H., Barrett, J., Leifer, M., & Wilce, A. (2007). *A generalized
no-broadcasting theorem.* Phys. Rev. Lett. **99**, 240501.
DOI 10.1103/PhysRevLett.99.240501; arXiv:0707.0620. **[FETCHED]**

Actual claim: generalized no-broadcasting "applicable to essentially *any*
nonclassical finite-dimensional probabilistic model satisfying a no-signaling
criterion, including ones with 'super-quantum' correlations". **Distance:** the
strongest single precedent — the ban is a property of the state/effect structure,
not of any dynamics, unitary or otherwise. If a referee wants to say "of course
the cloning ban does not need unitarity", this is the citation they will use.

### 3. BCJFS96 — the mixed-state form, stated over "physical means"
Barnum, H., Caves, C. M., Fuchs, C. A., Jozsa, R., & Schumacher, B. (1996).
*Noncommuting mixed states cannot be broadcast.* Phys. Rev. Lett. **76**,
2818–2821. DOI 10.1103/PhysRevLett.76.2818; arXiv:quant-ph/9511010.
**[FETCHED]**

Actual claim: "given a general mixed state ... there are no physical means for
*broadcasting* that state onto two separate quantum systems, even when the state
need only be reproduced marginally". **Distance:** close; the phrase "no physical
means" is what carries the non-unitary scope. The brief's PRL 76 guess is
correct (2818–2821, 1996).

### 4. Abr09 — no-cloning as a structural theorem, with the proof-theory link
Abramsky, S. (2009). *No-cloning in categorical quantum mechanics.* In
*Semantic Techniques in Quantum Computation* (S. Gay & I. Mackie, eds.),
Cambridge University Press, pp. 1–28. DOI 10.1017/CBO9781139193313.002;
arXiv:0910.2401. **[FETCHED]**

Actual claim: a novel version of no-cloning, "as an incompatibility between
having a 'natural' copying operation and the structural features required for
modeling quantum entanglement coexisting in the same category", "strikingly
similar to ... Joyal's lemma, which shows that a 'Boolean cartesian closed
category' trivializes". **Distance: this is the closest precedent on the LOGIC
side, and it is close enough to require a citation in the paper.** But note
precisely what it is and is not: it is a *categorical incompatibility* proof
(no natural copying vs compact structure), not a non-derivability theorem inside
a calculus, and it says nothing whatsoever about information conservation, the
discard rule, or an asymmetry between two laws. Our §3.3 claim is the pair; his
is one half, in a different formalism, with a different moral (cloning ↔
non-cartesianness).

### 5. HHSS05 — the rival framing, which the paper must answer
Horodecki, M., Horodecki, R., Sen(De), A., & Sen, U. (2005). *Common origin of
no-cloning and no-deleting principles: conservation of information.*
Foundations of Physics **35**, 2041–2049. DOI 10.1007/s10701-005-8661-4;
arXiv:quant-ph/0407038. **[FETCHED]**

Actual claim: "We consider theories for which dynamics is linear with respect to
stochastic mixing. We point out that the no-cloning and no-deleting principles
emerge in any such theory, if law of conservation of information is valid, and
two copies contain more information than one copy." **Distance: this is the
argument that most directly threatens the paper's framing** — it says the two
laws have one origin, not an asymmetric pair. The paper's answer is available and
sharp, and should be stated: HHSS05 must *assume* conservation as a
law of the theory; the calculus **derives the counterexample**
(`Dcare.no_vanishing_unrestricted_refuted`) — information loss is a *term*, not a
permitted model — while cloning survives in the same system. In other words, the
calculus supplies exactly the model HHSS05's antecedent excludes, and it is a
model with a derivation in it rather than a channel with a parameter in it.

### 6. Kit15 — the ban tracks noncommutativity, not invertibility
Kitajima, Y. (2015). *Imperfect cloning operations in algebraic quantum theory.*
Foundations of Physics **45**, 62. DOI 10.1007/s10701-014-9843-8; arXiv:1410.0074.
**[FETCHED]**

Actual claim: a universal ε-imperfect cloning operation exists if and only if
the system's algebra of observables is abelian. **Distance:** supportive; it
locates the ban in the algebraic structure rather than in any dynamical
restriction. Useful as a one-line second citation if a referee presses on
"linearity" vs "noncommutativity".

### 7. The logic-side precedents (the paper must cite at least one)
Girard, J.-Y. (1987). *Linear logic.* Theoretical Computer Science **50**, 1–101.
DOI 10.1016/0304-3975(87)90045-4. **[FETCHED]**

Walker, D. (2004). *Substructural type systems.* In *Advanced Topics in Types and
Programming Languages* (B. C. Pierce, ed.), MIT Press, pp. 3–44.
DOI 10.7551/mitpress/1104.003.0003. **[FETCHED]**

Mostrous, D., & Vasconcelos, V. T. (2018). *Affine sessions.* Logical Methods in
Computer Science **14**(4:14). DOI 10.23638/LMCS-14(4:14)2018. **[FETCHED]**

Actual claims: structural rules (weakening, contraction) are where resource
discipline lives, with the exponentials as the controlled exception (Gir87);
linear = used exactly once, affine = used at most once, so "may be dropped, may
not be copied" is the *definition* of the affine discipline (Wal04); affine
session types are typable precisely when a channel may be abandoned but not
duplicated (MosVas18). **Distance:** the asymmetry, stripped of physics, is this
distinction. Given the paper's own §5.5 fingerprint is *literally* the affine
discipline, the paper must say so and cite it, or a PL referee will read the
document as unaware of the field it is borrowing from.

### 8. Adjacent, weaker
Jozsa, R. (2002). *A stronger no-cloning theorem.* arXiv:quant-ph/0204153.
**[FETCHED: arXiv id via INSPIRE; no journal record]** — quantitative
strengthening: the supplementary information needed to clone a pure state "must
always be as large as it can possibly be". Optional.

Dieks, D. (1982). *Communication by EPR devices.* Physics Letters A **92**,
271–272. DOI 10.1016/0375-9601(82)90084-6. **[FETCHED]** — independent discovery;
the paper currently cites only Wootters–Zurek, and a referee will notice.

Vagenas, E. C., Farag Ali, A., & Alshal, H. (2019). *GUP and the no-cloning
theorem.* European Physical Journal C **79**. arXiv:1811.06614. **[FETCHED:
INSPIRE; article number not fetched]** — the Planck-scale variant the brief asked
about; it takes the ban as input to compute a modified Page time rather than
testing its survival. Reported so the brief's lead is closed, not as a
recommended row.

---

## Novelty verdict

**PARTIALLY-NOVEL.** Not "novel", and the paper should not use that word.

**What is preceded, flatly:**

- the asymmetry as a *scope fact* in quantum information — Lin99, BCJFS96,
  BBLW07 establish that cloning bans hold for non-unitary, information-losing
  processes. Anyone in quantum information will regard "cloning is more
  fundamental than unitarity" as obvious once stated.
- the asymmetry as a *structural/logical* fact — Abramsky's categorical
  no-cloning with its explicit Joyal-lemma analogy (Abr09) is the sharpest prior
  statement that a cloning ban is a limitative *proof-theoretic*-shaped result.
- the specific pair "may be dropped, may not be copied" — that is the definition
  of affine typing (Wal04), with a concurrency instance (MosVas18). The paper's
  §5.5 fingerprint is, in PL terms, the observation that the unrestricted
  calculus is affine. This is the single most likely referee kill, and it is
  cheap to defuse: cite the lineage and claim the mechanization, not the insight.

**What is not preceded, as far as I can reach:**

A *single* machine-checked calculus in which all three of these hold at once:
(a) no-cloning is a theorem in the *permissive* system (discard present,
duplication available for duplicable sorts); (b) **the conservation law is
refuted by an explicit derivation term** in that same system, not by a model or a
parameter; (c) restoring conservation costs exactly one rule, and the resulting
theorem is absolute. Abramsky has (a) in a category, not a calculus, and no (b) or
(c). Horodecki et al. have the pair as *assumptions*, not as a refutation. The
linear/affine literature has the discipline but never the refutation of the
*other* law as a derivable counterexample.

The mechanized *counterexample* is the distinctive artefact. `no_vanishing`
being **false** with a named, inspected proof term — rather than merely
unprovable — is what lets the paper say "the lossy world is not a hypothetical
model, it is this term", and that is a claim about derivations that no physics
paper in this area can make.

**And the mapping weakens the claim further, in a way the paper should state
itself before a referee does:** the physics twin compares *channels* to
*derivations*. A CP map is an object in a category of processes; a non-derivation
is the absence of a proof. The correspondence is between "the ban that does not
need the extra assumption" and "the theorem that does not need the extra rule" —
an analogy of *logical dependency structure*, not an isomorphism of objects. The
paper's existing scope note covers "isomorphism"; it should be extended to cover
this specific substitution.

Recommended wording for §3.3's physics paragraph: the asymmetry is **known in
quantum information as the scope of the no-cloning theorem** (Lin99, BCJFS96,
BBLW07) and **known in proof theory as the linear/affine distinction** (Wal04),
and what this paper adds is that both halves are *theorems of one calculus*, with
the failure of the second proved by an exhibited term.

---

## Proposed citation rows

Table format is the one `citations.md` already uses. Status values follow its
convention: `verified` / `needs-human` / `program-artifact` / `unused`.

| key | used in | claim it carries | full citation | status |
|---|---|---|---|---|
| Lin99 | §3.3 | The cloning ban does not depend on unitarity: it extends to arbitrary completely positive maps, including non-invertible, information-losing ones | Lindblad, G. (1999). *A general no-cloning theorem.* Letters in Mathematical Physics 47, 189–196. DOI 10.1023/A:1007581027660 | needs-human (Crossref/zbMATH metadata verified this session; abstract paywalled, claim from memory) |
| BCJFS96 | §3.3 | Broadcasting non-commuting mixed states is impossible by "no physical means" — the ban is on processes, not on unitaries | Barnum, H., Caves, C. M., Fuchs, C. A., Jozsa, R., & Schumacher, B. (1996). *Noncommuting mixed states cannot be broadcast.* Phys. Rev. Lett. 76, 2818–2821. DOI 10.1103/PhysRevLett.76.2818 | verified (INSPIRE + Crossref, 2026-11-16) |
| BBLW07 | §3.3 | The ban is a property of the state/effect structure: generalized no-broadcasting holds in essentially any nonclassical probabilistic model satisfying no-signaling, with no dynamical assumption | Barnum, H., Barrett, J., Leifer, M., & Wilce, A. (2007). *A generalized no-broadcasting theorem.* Phys. Rev. Lett. 99, 240501. DOI 10.1103/PhysRevLett.99.240501 | verified (INSPIRE, 2026-11-16) |
| Abr09 | §3.3 (position note; optional §2.1) | No-cloning as a structural incompatibility between natural copying and the structure modeling entanglement, explicitly the same genre as Joyal's lemma — "a heretofore unsuspected connection between limitative results in proof theory and no-go theorems in quantum mechanics" | Abramsky, S. (2009). *No-cloning in categorical quantum mechanics.* In *Semantic Techniques in Quantum Computation*, Cambridge University Press, pp. 1–28. DOI 10.1017/CBO9781139193313.002; arXiv:0910.2401 | verified (Crossref + INSPIRE abstract, 2026-11-16) |
| HHSS05 | §3.3 or §5.5 (the rival framing the paper answers) | No-cloning and no-deleting both follow in any theory with linear dynamics *if* information conservation is assumed — a common origin rather than an asymmetry | Horodecki, M., Horodecki, R., Sen(De), A., & Sen, U. (2005). *Common origin of no-cloning and no-deleting principles: conservation of information.* Foundations of Physics 35, 2041–2049. DOI 10.1007/s10701-005-8661-4 | verified (Crossref + INSPIRE abstract, 2026-11-16) |
| Wal04 | §3.3 or §5.5 | Linear = used exactly once (no dropping); affine = at most once (dropping allowed, copying impossible) — the type-theoretic form of the asymmetry, and the name for §5.5's fingerprint | Walker, D. (2004). *Substructural type systems.* In *Advanced Topics in Types and Programming Languages* (B. C. Pierce, ed.), MIT Press, pp. 3–44. DOI 10.7551/mitpress/1104.003.0003 | verified (Crossref, 2026-11-16) |
| Gir87 | §2.1 or §3.3 | Structural rules are where resource discipline lives; the exponentials are the controlled exception permitting weakening and contraction | Girard, J.-Y. (1987). *Linear logic.* Theoretical Computer Science 50, 1–101. DOI 10.1016/0304-3975(87)90045-4 | verified (Crossref, 2026-11-16) |
| MosVas18 | §5.5 (optional) | Affine session types: a channel may be abandoned but never duplicated — the concurrency-side twin of "lossy, not a breeder" | Mostrous, D., & Vasconcelos, V. T. (2018). *Affine sessions.* Logical Methods in Computer Science 14(4:14). DOI 10.23638/LMCS-14(4:14)2018 | verified (Crossref, 2026-11-16) |
| Die82 | §3.1 | Independent discovery of the no-cloning theorem | Dieks, D. (1982). *Communication by EPR devices.* Physics Letters A 92, 271–272. DOI 10.1016/0375-9601(82)90084-6 | verified (Crossref, 2026-11-16) |
| Kit15 | §3.3 (optional second citation) | A universal imperfect cloner exists iff the algebra of observables is abelian — the ban tracks noncommutativity, not invertibility | Kitajima, Y. (2015). *Imperfect cloning operations in algebraic quantum theory.* Foundations of Physics 45, 62. DOI 10.1007/s10701-014-9843-8 | verified (INSPIRE abstract, 2026-11-16) |
| Joz02 | §3.1 (optional) | Quantitative strengthening: the supplementary information needed to clone a pure state must be maximal | Jozsa, R. (2002). *A stronger no-cloning theorem.* arXiv:quant-ph/0204153 | needs-human (no journal record found) |
| Vage19 | §6 or §5.5 (only if the Planck-scale paragraph survives) | No-cloning examined under a generalized uncertainty principle; used as input to a modified Page time | Vagenas, E. C., Farag Ali, A., & Alshal, H. (2019). *GUP and the no-cloning theorem.* European Physical Journal C 79. arXiv:1811.06614 | needs-human (INSPIRE: journal + year only; article number not fetched) |

WZ82 already has a row and is verified; no new row is needed, but note it is now
double-checked against Crossref (Nature 299, 802–803, DOI 10.1038/299802a0).

---

## What a human should still check

1. **Lin99's actual wording.** The paper's whole §3.3 physics paragraph may lean
   on it, and I could not read a single sentence of it: no abstract in Crossref,
   OpenAlex (null), zbMATH (licence-restricted) or Semantic Scholar (elided by
   the publisher), and it is not on arXiv. Someone with journal access must
   confirm (a) that the generalization is to arbitrary CP maps, (b) whether
   non-trace-preserving maps are explicitly included, (c) whether approximate
   cloning is bounded in the same paper. **If (a) is wrong, the paragraph loses
   its closest precedent** — BCJFS96 and BBLW07 would then have to carry it
   alone, which they can, but the sentence must change.
2. **Occurrences of the asymmetry stated as a thesis.** I searched INSPIRE titles
   and abstracts, Crossref, OpenAlex and zbMATH; I did **not** do a systematic
   full-text search, and Google Scholar / Semantic Scholar full text were
   unavailable. A human should check Peres's *Quantum Theory: Concepts and
   Methods*, Nielsen–Chuang §12.1.1, and the Wootters–Zurek *Physics Today* 62
   (2009) retrospective, which are the standard places such a framing sentence
   would appear in textbook form.
3. **The proof-theory side is under-searched, and it is where the risk is.**
   I confirmed Girard/Walker/Abramsky, but I did not read the quantum-λ-calculus
   or linear-logic no-cloning literatures: e.g. *Linear Lambda-Calculus is
   Linear* (FSCD 2022, LIPIcs — **seen in OpenAlex, not read**), Selinger–Valiron
   *A Lambda Calculus for Quantum Computation* (SIAM J. Comput. 33, 2004
   **[FETCHED: DOI only]**), Altenkirch–Grattage's QML line, and the
   *two kinds of linearity* literature. Any of these could contain a
   non-derivability statement of no-cloning in a typed calculus — which would
   move the verdict from PARTIALLY-NOVEL toward PRECEDED on the mechanization
   claim too. This is the check I would most want done before submission.
4. **Horodecki et al. is a genuine objection, not a citation.** Decide how §3.3
   answers it. My recommendation is the one above — their antecedent (assume
   conservation) is exactly what the calculus refutes — but the authors should
   read the full paper, since the abstract alone does not say whether they claim
   an *equivalence* (in which case the paper's asymmetry is a claim about
   *dependency direction* and must be phrased that way very carefully).
5. **Whether §5.5 wants a physics citation at all.** On the evidence here, the
   physics does not support a two-regime reading: there is no regime where
   unitarity fails while the rest of quantum mechanics stands. If §5.5 keeps
   Wheeler and Carter, it should say in one sentence that the physics precedent
   is an asymmetry *within* one theory, and that the two-regime reading is the
   calculus's own — labeled, not borrowed.
6. **Nothing here is a claim about the tree.** I did not read a line of
   `/workspace/dcare/lean` this session and did not run either gate script. Every
   statement about `Dcare.*` names in this note is quoted from `paper.md` §3, not
   measured.
