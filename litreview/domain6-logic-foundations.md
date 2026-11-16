# Domain 6 — Formal logic in physics foundations

*Literature scout report for `physical-iso/paper.md` (§2–§3 read first). Question: are there
prior attempts to map conservation laws as structural theorems of a substructural logic, and is
ours the first **mechanization** of these laws as grammar theorems?*

**Method and discipline.** Every bibliographic fact below is marked **[FETCHED]** (arXiv API /
abs page / e-print source, Crossref DOI, or a downloaded artifact whose path is given) or
**[MEMORY]** (my offline knowledge, needs a human check). I read the primary sources rather than
abstracts where the claim is about what a paper *says*: `cs/0404056` (Selinger–Valiron LaTeX
source), QWIRE's POPL'17 PDF and its Coq tree, `2005.08396` (Proto-Quipper-D tutorial source),
`1510.02198` (Ross thesis source), `2609.02661` (IULL source), `quant-ph/0402130`
(Abramsky–Coecke source), `0910.2401` (Abramsky, *No-Cloning in Categorical Quantum Mechanics*),
and the AFP entry `Isabelle_Marries_Dirac` (`No_Cloning.thy`).
Searches that returned nothing are reported as searches, not as proof of absence.

---

## Direct answer

**The READING is established; the MECHANIZED GRAMMAR THEOREMS are not.**

(a) *"No-cloning as a consequence of a linear type system"* — **YES, established**, and it is the
standard justification of the whole quantum-lambda-calculus / quantum-PL line. The strongest
logic-side statement is not in the PL papers at all but in Abramsky's categorical result: a
compact category *with* a natural cloning operation collapses (every endomorphism is a scalar
multiple of the identity) [Abr09] — a limitative theorem in the same genre as Joyal's lemma, and
the one citation a proof-theoretically literate referee will use against any claim that
no-cloning-as-structure is new. Note precisely what it is: a categorical incompatibility proof,
not a non-derivability theorem inside a calculus, unmechanized, and it treats cloning and deleting
*together* (a cartesian structure is "a monoidal structure plus natural diagonals and terminality,
i.e. plus cloning and deleting", `main.tex:227`) rather than as two laws with different strength.
In the programming-language line the reading is established as a **design rationale plus a typing
discipline**, not as a theorem: Selinger–Valiron motivate
their affine intuitionistic linear type system by no-cloning and enforce "unique referencing"
[SV06]; QWIRE says in as many words that "QWIRE uses linear types to enforce no-cloning" [PRZ17];
the Proto-Quipper-D tutorial states that "it is now well-known that they can be used to enforce
no-cloning … All well-typed programs in these languages satisfy the no-cloning property" [PQ20].
What none of them does is state or prove *"there is no derivation at the lone context `[C]`
concluding `C ⊗ C`"* as a theorem of the calculus; where QWIRE comes closest, it shows the cloner
fails to type-check and then `Abort`s the obligation (QWIRE `HOASExamples.v:495–497`) — a
demonstration on one term, not a non-derivability theorem.

(b) *A NO-VANISHING / unitarity analogue as a typing or grammar theorem* — **no precedent found
for the theorem we have.** The *program* of making unitarity a typing invariant exists and is
active: realizability in the unitary sphere [DGMV19], and — the closest single hit of this scout —
Intuitionistic Unitary Linear Logic, "a logic based on linear logic focusing on **conservation of
unitarity** for higher order terms", with coherence, completeness with regard to unitaries and
cut admissibility [ILV26]. But ILV26's conservation is a **denotational invariant** (every
derivable term denotes a unitary, by a semantics that *defines* the value sets as unitaries), not
a syntactic non-derivability statement, and it compares no restricted calculus against an
unrestricted one. In the quantum-PL languages, discarding a *quantum* wire is likewise forbidden
by typing (QWIRE `unused_qubit_fail`, `HOASExamples.v:488–493`; Proto-Quipper-D's discard gate is
`Bit -> Unit`, bits only [PQ20]) — again a discipline, demonstrated, never a theorem about which
derivations exist.

(c) *Mechanization.* No-cloning **has** been mechanized in a proof assistant — but as the
Hilbert-space statement: AFP entry *Isabelle Marries Dirac*, theory `No_Cloning`,
`theorem (in quantum_machine) no_cloning` concludes `v = w ∨ ⟨v|w⟩ = 0` from a unitary cloning
hypothesis [BHL20]. Our paper must therefore never say "first mechanization of no-cloning"; the
defensible claim is **first mechanization of these laws as non-derivability theorems of a linear
grammar**. On that claim I found no precedent.

(d) Net verdict: **the dictionary is preceded, the theorems are novel.** Details in the
decomposition below. One finding *supports* the paper: SV06's system is deliberately **affine**
— "affine intuitionistic linear logic provides precisely the right type system"
[`conclusion.tex:17`, FETCHED] — i.e. it forbids contraction and permits weakening, which is
exactly the paper's *unrestricted* calculus. The mainstream quantum lambda calculus therefore
sits on the "cloning forbidden, discard allowed" side of §3.3's table, which the paper can cite
as a physics-respectable instance of that side.

---

## Closest precedents

**1. QWIRE — Paykin, Rand, Zdancewic, *QWIRE: a core language for quantum circuits*, POPL 2017**
[PRZ17]. The closest artifact overall, because it is both a statement and a Coq development.
*Exact claims [FETCHED, PDF text]:* "The 'no-cloning' theorem of quantum mechanics states that
quantum data cannot be cloned; in a programming environment, linear types ensure that quantum
programs do not try to violate this property" (introduction); "QWIRE uses linear types to enforce
no-cloning, but does not allow them to spill over into the host language" (related work).
*What is proved:* type safety/soundness of the circuit language, unitary denotation of circuits,
linearity of wires — the standard metatheory. *What is asserted, not proved:* that no-cloning is
enforced. *What is demonstrated:* in the Coq tree (`inQWIRE/QWIRE`, master, `HOASExamples.v`), the
cloner is declared at :495 and `clone_WT : Typed_Box clone` is discharged by `type_check` and then
**`Abort.`** at :496–497 — the file's own convention for "this does not type-check" (cf.
`absurd_fail`, `unmeasure_fail`, `unused_qubit_fail`). No general no-cloning lemma exists in the
development (`rg -i clon` over the whole tree: two hits, both this example).

**2. Selinger & Valiron, *A lambda calculus for quantum computation with classical control*,
MSCS 16(3):527–552, 2006** [SV06]. *Exact claims [FETCHED, arXiv source cs/0404056]:* "The reason
for this restriction is the well-known no-cloning property of quantum physics, which states that a
quantum bit cannot be duplicated … Syntactically, the requirement of unique referencing translates
into a linearity condition: a lambda abstraction λx.M is called linear if the variable x is used
**at most once**" (`term.tex:163–176`); the type system is "affine intuitionistic linear logic"
(`introduction.tex`, `conclusion.tex:17`). *Proved:* subject reduction and a type-inference
algorithm. *Not present:* any no-cloning theorem, any statement about which derivations are
impossible. This is the canonical statement of the reading, and — being affine — the canonical
worked instance of the *unrestricted* side of the asymmetry.

**3. Proto-Quipper-D — Fu, Kishida, Ross, Selinger, *A tutorial introduction to quantum circuit
programming in dependently typed Proto-Quipper*, LNCS 12227:153–168, 2020** [PQ20]. *Exact claims
[FETCHED, arXiv source 2005.08396, `scp-journal.tex:88–102`]:* "Linear types have been used for
resource aware programming [Girard 1987; Wadler 1990] and it is now well-known that they can be
used to enforce no-cloning [Selinger 2005]. A variety of programming languages use linear types
for quantum circuit programming, e.g., Proto-Quipper-S, Proto-Quipper-M, and QWire. **All
well-typed programs in these languages satisfy the no-cloning property.**" Also: the discard gate
is `Discard : Bit -> Unit` (:246) — discard exists only for classical bits — and garbage qubits
:630–640 "cannot be discarded since this would violate linearity". *Proved:* type safety of the
language. *Asserted:* the quoted sentence (as a community fact, not as a theorem of any of the
named systems).

**4. Ross, *Algebraic and Logical Methods in Quantum Computation*, PhD thesis, Dalhousie 2015**
[Ross15]. *Exact claim [FETCHED, arXiv source 1510.02198, `background-lambda.tex:640–710`]:* the
section "Linearity" motivates linear logic by no-cloning, then derives strict linearity by
*removing implicit weakening and contraction*: "If contexts are removed from all nullary rules and
juxtaposed rather than merged in all binary rules, then we obtain a strictly linear system. In this
system, a variable occurs in the context of a valid typing judgement if and only if it appears
exactly once in the term being typed." This is the **closest verbal match** to our two laws as a
package (no contraction *and* no weakening), stated as a property of a type system, for a quantum
language, with no proof and no information-conservation reading.

**5. Lamiroy, Valiron, Vilmart, *Intuitionistic Unitary Linear Logic: A Proof-Theoretical Approach
to Purely Quantum Higher-Order*, arXiv:2609.02661 (2 Sep 2026; submitted to CSL 2027)** [ILV26].
The closest thing to a *unitarity-as-logic* theorem. *Exact claims [FETCHED, abs + source]:* "we
present Intuitionistic Unitary Linear Logic (IULL), a logic based on linear logic focusing on
conservation of unitarity for higher order terms. We prove the coherence of IULL, its completeness
with regard to unitaries, and the admissibility of its cut rules." Their interpretation
(`def:interp`) sets each value set to a set of unitaries (`sem{A ⊸ B} = {f ; f†f = Id, ff† = Id}`),
so conservation is a property of the *semantics*, and their corollary is "if π proves a sequent,
its denotation is a unitary". *Differences from ours, all material:* no syntactic
non-derivability theorem; no restricted-vs-unrestricted comparison (they instead delete the ⊕
rules that break unitarity, `article.tex:216`); no no-cloning discussion (`rg -i clon` returns
nothing); no guarded fixpoint or self-reference; the concern is non-causal higher-order processes
(quantum switch), not conservation of a linear token.

**6. Díaz-Caro, Guillermo, Miquel, Valiron, *Realizability in the Unitary Sphere*, LICS 2019,
pp. 1–13** [DGMV19]. Metadata verified; content not read this session — flagged as an adjacent
"well-typed ⇒ unitary" precedent that a referee could raise, and one the paper should be able to
name. It is the same *shape* of guarantee as ILV26 (typing restricts denotations to unitaries),
one decade earlier.

**7. Bordg, Lachnitt, He, *Certified Quantum Computation in Isabelle/HOL*, J. Automated Reasoning
65:691–709, 2020; AFP entry *Isabelle Marries Dirac*** [BHL20]. *Exact statement [FETCHED, AFP
tarball, `Isabelle_Marries_Dirac/No_Cloning.thy`]:*
`theorem (in quantum_machine) no_cloning` — assuming `U * (|v⟩ ⊗ |s⟩) = |v⟩ ⊗ |v⟩` and
`U * (|w⟩ ⊗ |s⟩) = |w⟩ ⊗ |w⟩` with `U` unitary and normalized `v`, `w`, concludes
`v = w ∨ ⟨v|w⟩ = 0`. This is the *physics* theorem about matrices, mechanized. It is the row that
forces the paper's novelty sentence to be scoped to *grammar*.

**8. Abramsky & Coecke, *A categorical semantics of quantum protocols*, LICS 2004** [AC04]
(already a ledger row). *Exact claim [FETCHED, arXiv source quant-ph/0402130]:* resource-sensitivity
appears once, as motivation — "compound systems to be described in a resource-sensitive fashion
(cf. the 'no cloning' and 'no deleting' theorems of quantum mechanics [Nielsen])"
(`arXivqcc.tex:159–161`). No theorem, no derivation. AC04 itself is therefore **not** a precedent
for conservation-as-grammar; the categorical precedent is Abramsky's later paper (item 9 below),
and it concerns cloning alone.

**9. Abramsky, *No-Cloning in Categorical Quantum Mechanics*, in *Semantic Techniques in Quantum
Computation*, CUP 2009, pp. 1–28** [Abr09]. *Exact claim [FETCHED, arXiv source 0910.2401]:* the
"Cloning Collapse Theorem" (`main.tex:799`) — "Let C be a compact category with cloning. Then every
endomorphism is a scalar multiple of the identity"; the paper presents it as "visibly in the same
genre as a well-known result by Joyal in categorical logic … showing that a 'Boolean cartesian
closed category' trivializes" (`main.tex:100`), and notes that products are "tensors with extra
structure: natural diagonals and projections, corresponding to cloning and deleting operations"
(`main.tex:267`). *What is proved:* a structural incompatibility theorem, non-constructive about
derivations, in a category. *What is not present:* a calculus, a mechanization, an unrestricted
counterexample, or the separation of the two laws. This is the strongest **logic-side** precedent
and the paper must cite it in §3.1; it is also the reason the novelty sentence has to be about
derivations, not about "seeing no-cloning as structure".

**10. Girard, *Linear logic*, TCS 50(1):1–101, 1987** [Gir87]; **Wadler, *Linear types can change
the world!*, 1990** [Wad90]; **Walker, *Substructural type systems*, in *Advanced Topics in Types
and Programming Languages*, MIT Press 2004, pp. 3–44** [Wal04]. The substructural basis: the
discipline that removes contraction (and weakening) and the resource reading of it. Girard's DOI
and Walker's DOI are verified; Wadler's pointer is **[MEMORY]**. Walker is the canonical
definitional reference for the exact distinction the paper's §5.5 turns on — linear = used exactly
once, affine = used at most once, so "may be dropped, may not be copied" is the *definition* of
the affine discipline. The quantum-PL literature cites Girard + Wadler for the reading ([PQ20]
above), which is the cleanest evidence that its ancestry is Girard + Wadler and not any physics
paper.

**11. Döring & Isham, *A topos foundation for theories of physics: I. Formal languages for
physics*, J. Math. Phys. 49 (2008)** [DI08]. *Exact claim [FETCHED, arXiv quant-ph/0703060
abstract]:* "constructing a theory of physics is equivalent to finding a representation in a topos
of a certain formal language that is attached to the system. Classical physics arises when the
topos is the category of sets…". This is the *other* logic-in-physics-foundations route: the logic
is the internal (intuitionistic) logic of a topos attached to a system's context, and its
impossibility results are about valuations/truth values. It is not a resource logic, makes no
conservation-as-grammar claim, and does not mechanize anything. Cite it (if at all) as the
structure-first contrast, not as a precedent.

---

## Novelty verdict — component by component

| component | verdict | evidence |
|---|---|---|
| **The reading**: linear types = no-cloning | **PRECEDED** (standard, explicitly stated) | SV06, PRZ17, PQ20, Ross15; ancestry Gir87/Wad90 |
| **The reading in limitative form**: no-cloning as a structural impossibility (cloning + compact structure collapse) | **PRECEDED** (categorical, unmechanized, bundles cloning with deleting) | Abr09 (Cloning Collapse Theorem; Joyal-lemma analogy) |
| **The reading, second half**: linear/affine typing forbids *discarding* quantum data, and that is what protects the resource | **PARTIALLY PRECEDED** — as a typing discipline, not as a conservation claim; "affine = may drop, may not copy" is definitional | QWIRE `unused_qubit_fail`; PQ20 `Discard : Bit -> Unit`; Ross15's strict linearity ("exactly once"); Wal04 |
| **Unitarity as a typing invariant** | **PARTIALLY PRECEDED / PRECEDED as a semantic guarantee** | ILV26 (conservation of unitarity, denotational); DGMV19 (realizability in the unitary sphere) |
| **Both laws as mechanized NON-DERIVABILITY theorems of one grammar** (`no_contraction_content`, `no_vanishing_restricted`) | **NOVEL as stated.** Closest mechanized artifact is QWIRE, whose no-cloning evidence is one aborted `type_check`; the only mechanized `no_cloning` theorem I found is the Hilbert-space one (BHL20); Abr09 proves one half structurally, in a category, with no calculus | PRZ17 Coq tree; BHL20 `No_Cloning.thy`; Abr09 |
| **The asymmetry**: contraction absolute in the unrestricted calculus, vanishing refuted there and restored by the discard ban | **NOVEL.** No precedent compares a *restricted* and an *unrestricted* version of the same calculus for these two laws; the quantum-PL systems are single-grain (SV06 affine; QWIRE/Proto-Quipper linear-and-no-discard) and assert both properties uniformly | SV06 (affine), PRZ17, PQ20 vs `Dcare.no_vanishing_unrestricted_refuted` |
| **The guarded-fixpoint component**: `▷` + `AllNonLinear Γ` making conservation compatible with self-reference/productivity, and the unrestricted fixpoint's divergence | **NOVEL, no analogue found.** No quantum-PL language in this survey has a guarded modality; the guarded-recursion literature (Nakano; Birkedal et al.) has no conservation reading; ILV26 has recursion only in the LICS'26 neighbours' sense, not a guarded fixpoint | absence across all sources read; flag in "what a human should check" |
| **"First mechanization of these laws"** (unqualified) | **WOULD BE FALSE** — no-cloning is mechanized in Isabelle/HOL | BHL20 |

**Recommended wording for the paper** (three sentences, in §1 or the abstract, each of which the
literature above defends):
1. "Linear typing is the standard mechanism by which quantum programming languages enforce
   no-cloning [SV06, PRZ17, PQ20], and no-cloning is already a structural impossibility result in
   categorical quantum mechanics [Abr09]; this paper's contribution is not that reading but its
   mechanization as a non-derivability theorem."
2. "The no-cloning theorem itself has been mechanized in Isabelle/HOL as a statement about unitary
   matrices [BHL20]; what is mechanized here is the grammar-side statement, together with its
   counterpart for information conservation."
3. "The closest logical precedent for unitarity-as-typing is Intuitionistic Unitary Linear Logic
   [ILV26], which guarantees that every derivable term denotes a unitary; the present calculus
   instead proves the non-existence of a lossy derivation, and proves that the same law fails
   once the discard rule is restored."

Also worth one sentence in §3.3, with SV06 cited as corroboration: the mainstream quantum lambda
calculus is *affine* — no contraction, weakening present — i.e. it lives on the table's
"cloning forbidden, content not conserved" row, and its authors do not claim conservation. That
turns a novelty risk into evidence for the asymmetry.

---

## Proposed citation rows

Format as in `physical-iso/citations.md`. Existing keys WZ82, PB00, AC04, Nak00, AM13, Bir12,
CCS, GS, GL are **not** repeated; AC04's row should gain the sharper claim noted below.

| key | used in | claim it carries | full citation | status |
|---|---|---|---|---|
| SV06 | §3.1, §3.3 | Quantum lambda calculus on **affine** intuitionistic linear logic: linearity (at most once) is the syntactic form of no-cloning; subject reduction + type inference are the proved results, no no-cloning theorem | Selinger, P., & Valiron, B. (2006). *A lambda calculus for quantum computation with classical control.* Mathematical Structures in Computer Science 16(3), 527–552. DOI 10.1017/S0960129506005238 | FETCHED (Crossref DOI; arXiv cs/0404056 source quoted) |
| SV09 | §3.1 | The survey in which the QPL community's "linear types enforce no-cloning" statement is standardly cited | Selinger, P., & Valiron, B. (2009). *Quantum Lambda Calculus.* In S. Gay & I. Mackie (eds.), Semantic Techniques in Quantum Computation, Cambridge University Press, 135–172. DOI 10.1017/CBO9781139193313.005 | FETCHED (Crossref metadata only; content unread — see check list) |
| PRZ17 | §3.1, §3.3 | QWIRE uses linear wire types to enforce no-cloning; the cloner's typing obligation is demonstrated to fail and aborted, no general non-derivability theorem is stated | Paykin, J., Rand, R., & Zdancewic, S. (2017). *QWIRE: a core language for quantum circuits.* POPL 2017, PACMPL 1(POPL), 846–858. DOI 10.1145/3009837.3009894 | FETCHED (Crossref; PDF text; Coq tree `HOASExamples.v:495–497`) |
| PQ20 | §3.1, §3.3 | "All well-typed programs in these languages satisfy the no-cloning property"; discard is typed only for classical bits | Fu, P., Kishida, K., Ross, N. J., & Selinger, P. (2020). *A tutorial introduction to quantum circuit programming in dependently typed Proto-Quipper.* LNCS 12227, 153–168. arXiv:2005.08396 | FETCHED (arXiv abs + source) |
| Ross15 | §3.1 | Strict linearity removes implicit weakening *and* contraction, so a variable occurs in a valid judgement iff used exactly once; motivated by no-cloning | Ross, N. J. (2015). *Algebraic and Logical Methods in Quantum Computation.* PhD thesis, Dalhousie University. arXiv:1510.02198 | FETCHED (arXiv abs + source) |
| ILV26 | §3.2, §3.3 | Closest precedent for unitarity-as-logic: a linear logic whose derivable terms denote unitaries ("conservation of unitarity"), with coherence, completeness w.r.t. unitaries, cut admissibility — a denotational guarantee, not a non-derivability theorem | Lamiroy, J., Valiron, B., & Vilmart, R. (2026). *Intuitionistic Unitary Linear Logic: A Proof-Theoretical Approach to Purely Quantum Higher-Order.* arXiv:2609.02661 (submitted to CSL 2027) | FETCHED (arXiv abs + source) |
| DGMV19 | §3.2 | Realizability semantics in the unitary sphere: well-typed terms realize unitaries — the earlier "unitarity as typing" precedent | Díaz-Caro, A., Guillermo, M., Miquel, A., & Valiron, B. (2019). *Realizability in the Unitary Sphere.* LICS 2019, 1–13. DOI 10.1109/LICS.2019.8785834 | FETCHED (Crossref metadata; content unread) |
| BHL20 | §1, §3.1 | The no-cloning theorem mechanized as a Hilbert-space statement: a unitary cloning two non-orthogonal states forces them equal or orthogonal | Bordg, A., Lachnitt, H., & He, Y. (2020). *Certified Quantum Computation in Isabelle/HOL.* Journal of Automated Reasoning 65, 691–709. DOI 10.1007/s10817-020-09584-7; artifact: AFP entry *Isabelle Marries Dirac*, theory `No_Cloning` | FETCHED (Crossref; AFP tarball, theorem `no_cloning` read) |
| Abr09 | §3.1 | No-cloning as a structural impossibility: a compact category with a natural cloning operation collapses (every endomorphism scalar); presented as the Joyal-lemma genre, with cloning and deleting bundled in "cartesian structure" | Abramsky, S. (2009). *No-Cloning in Categorical Quantum Mechanics.* In S. Gay & I. Mackie (eds.), Semantic Techniques in Quantum Computation, Cambridge University Press, 1–28. DOI 10.1017/CBO9781139193313.002; arXiv:0910.2401 | FETCHED (Crossref; arXiv source, `main.tex:100,227,267,799`) |
| Gir87 | §2.1, §3.1 | The substructural discipline (no contraction, no weakening) whose resource reading underwrites the whole correspondence | Girard, J.-Y. (1987). *Linear logic.* Theoretical Computer Science 50(1), 1–101. DOI 10.1016/0304-3975(87)90045-4 | FETCHED (Crossref) |
| Wal04 | §5.5 | Definitional reference for the linear/affine distinction: linear = exactly once, affine = at most once ("may be dropped, may not be copied") — the PL name for the unrestricted calculus | Walker, D. (2004). *Substructural type systems.* In B. C. Pierce (ed.), Advanced Topics in Types and Programming Languages, MIT Press, 3–44. DOI 10.7551/mitpress/1104.003.0003 | FETCHED (Crossref) |
| Wad90 | §2.1 | The resource reading of linear types, cited by the QPL literature alongside Girard | Wadler, P. (1990). *Linear types can change the world!* In M. Broy & C. B. Jones (eds.), Programming Concepts and Methods (IFIP TC 2), North-Holland, 347–359 | MEMORY — needs-human (pages/venue) |
| DI08 | §1 or §4 (contrast only) | The structure-first alternative: a physical theory is a representation of a formal language in a topos; the logic is the topos's internal one, not a resource logic | Döring, A., & Isham, C. J. (2008). *A topos foundation for theories of physics: I. Formal languages for physics.* Journal of Mathematical Physics 49. DOI 10.1063/1.2883740 | FETCHED (Crossref; arXiv quant-ph/0703060 abstract quoted) |

AC04's existing row claim can be sharpened: resource-sensitivity is *motivation* in that paper
("cf. the 'no cloning' and 'no deleting' theorems"), not a theorem — so citing AC04 for
diagrammatic language is safe, citing it for no-cloning-as-structure is not.

---

## What a human should still check

1. **SV09's actual sentence.** I verified only its metadata; the claim "linear types enforce
   no-cloning" is attributed to it *by* [PQ20]. Read ch. 4 of *Semantic Techniques in Quantum
   Computation* before the row ships as a content claim, or demote the row to "metadata only".
2. **DGMV19 content.** Same status: metadata verified, semantics-of-the-paper not read. If it
   proves "well-typed ⇒ unitary" for a first-order quantum language, [ILV26] is not even the first
   such result and §3.2's novelty sentence must narrow to the *non-derivability* form.
3. **The 2026 LICS cluster**, which I have only second-hand from [ILV26]'s bibliography and could
   not verify in Crossref: Barsse, Péchoux & Perdrix, *Quantum Control and General Recursion
   Beyond the Unitary Case*, LICS 2026 (LIPIcs 380, 14:1–14:26); Hirata & Tsukada, *Causality in
   Pure Quantum Computation with Quantum Control*, LICS 2026 (LIPIcs 380, 57:1–57:28). If either
   states a conservation theorem, it belongs in the novelty paragraph. Verify before citing.
4. **The absence claim.** I searched arXiv (API + HTML: `"no-cloning" AND "linear logic"`,
   `ti:"no-cloning"`, `"unitarity" AND "linear types"`, `"conservation" AND "linear logic" AND
   quantum`, `"no-vanishing"`, `"no-cloning" AND {Coq, Isabelle, Agda, Lean}`), Crossref, OpenAlex
   and the AFP. arXiv's relevance ranking is keyword-OR and no single query is exhaustive; a
   Google Scholar / DBLP pass on "conservation as grammar", "no derivation" + "unit type", and
   "non-derivability" + "no-cloning" is still worth one hour before submission. Absence was not
   proven, only unrefuted by targeted search.
5. **Wadler 1990's pages** ([MEMORY], above).
6. **ILV26's title** has a `%TODO` in its own source at `article.tex:18`; arXiv lists it as
   ending "Higher-Order". Cite the arXiv id, not a proceedings page, until CSL 2027 publishes.
7. **QWIRE-adjacent question worth one grep before a referee asks it:** whether Proto-Quipper's or
   QWIRE's metatheory *proves* no-duplication/no-discard as a lemma (rather than demonstrating a
   failing `type_check`). I checked QWIRE's whole Coq tree: no such lemma. Proto-Quipper's Coq
   development was not downloaded.
8. **The paper's own wording.** §3.3 currently claims the asymmetry as an observation about this
   calculus — safe. If any sentence is added saying the *reading* is new, it is false [SV06,
   PRZ17, PQ20, Abr09] and a referee will say so in one line. Likewise §5.5's "lossy not a
   breeder" fingerprint is, in PL terms, the affine discipline [Wal04]: cite it and claim the
   mechanization, not the insight.
9. **Scope overlap with the sibling reports.** The physics-side precedents for the asymmetry
   (non-broadcasting, common-origin-of-no-cloning-and-no-deleting, no-signalling-style
   derivations) are domain 4's subject and are covered in `litreview/domain4-asymmetry.md`; this
   report deliberately covers only the logic/type-theory side. The two files should be read
   together before `citations.md` is updated, so that no sibling row is contradicted (in
   particular: "the asymmetry is preceded in the physics register" and "the *mechanized pair* is
   not" are compatible statements, and the paper needs both).
