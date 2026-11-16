# Conservation as Grammar: No-Cloning and Unitarity as Structural Theorems of a Guarded Linear Calculus, with a Holographic Resolution Bound

*derivation-of-care research program — physics artifact*

**Abstract.** In standard quantum mechanics, unitarity is a postulate — forced, once probability preservation and reversibility are granted, by the symmetry structure of pure states — and no-cloning is a theorem about the formalism's linear maps. We exhibit a mechanized, sorted, guarded linear calculus in which both statements are *structural* theorems: properties of which well-formed processes exist at all, prior to any dynamics. No derivation duplicates a linear token (`no_contraction_content`, machine-checked in Lean 4), and in the guarded kernel no derivation consumes one into nothing (`no_vanishing_restricted`). The two laws carry different strength — cloning is forbidden by the grammar alone, even where discard and duplication remain available for other sorts — and the law's scope is pinned rather than settled: the cloning ban is the law of the linear types with no closed inhabitant, every preparable type provably clonable, the information carriers provably not, one boundary case open — while conservation of content requires the kernel's discard ban — an asymmetry that mirrors the physical one between a kinematic law and a dynamical one. The unrestricted calculus is not a harmless generalization: there, information loss is *derived* (an explicit construction is machine-checked) and the unguarded dynamics provably diverge — pay forever, deliver nothing. We give a translation manual into the language of observables, tensor networks, and structural holography; for the finitary fragment the dictionary is backed by a semantic bridge — a functor into the category of completely positive maps, under which the kernel/outside boundary is the no-discard/discard boundary and the loss process denotes the trace — while the remaining rows are readings: a dictionary, not an isomorphism, whose functor mirrors the laws without deriving them. Finally, if the guarded tick is *spatialized* — an assumption the calculus does not make — combining it with the Bekenstein–Hawking area law yields the bulk voxel scale of the spacetime-foam literature — $L \approx (l_p^2 R)^{1/3} \approx 5\times10^{-15}\,$m for the observable radius $R$, a scaling due to Károlyházy and to Ng — a projection, not a theorem. The exponent belongs to the entropy bound; the guard fixes no scale.

**Keywords:** linear logic; guarded recursion; no-cloning; unitarity; information conservation; holographic principle; spacetime foam; quantum gravity phenomenology.

## Epistemic framing

Every load-bearing claim in this paper carries one of three labels, following the convention of the sibling artifact [GL]:

- **[MEASURED]** — the claim is machine-checked in the companion mechanization, the *Care Calculus* (`Dcare`, a Lean 4 development [CCS]), and the voucher is a named theorem. The label means exactly: a proof assistant vouches for the statement, and the statement is about the calculus.
- **[INTERPRETATION]** — the claim is a reading: a mapping between the calculus and the language of physics. Interpretations are this paper's contribution; they are not theorems, and the paper says so wherever one carries weight. The correspondence itself is a **[INTERPRETATION]** throughout: a dictionary, not an isomorphism — with one constructed exception: the semantic bridge of §3.5 is mathematics at paper rigor, unmechanized, and its rows are stated as correspondences rather than derivations.
- **[PROJECTION]** — a statement about what some hypothetical physical instantiation could exhibit. Projections are not evidence and constrain nothing until an experiment is named.

The reader should hold one distinction fixed. A theorem *about a formal system* is a statement about derivations; a theorem *about the world* is a statement about measurements. Nothing in the mechanization bridges the two. What the mechanization provides — and this is not nothing — is a place where two of physics' most stubborn conservation facts appear as grammar rather than as postulates or as facts about maps, together with a machine-checked counterexample world in which one of them fails. What bridges that place and the world is interpretation, and it is labeled as such, all the way down.

## 1. Introduction

Quantum mechanics treats its two great conservation facts asymmetrically, and it is worth noticing how each is grounded.

Unitarity is a postulate. Time evolution is required to preserve transition probabilities and to be reversible; the symmetry structure of pure states then forces the implementing maps to be unitary up to phase [Wig59]. The requirement itself — that probability be conserved and information never destroyed — is not derived. It is demanded of the dynamics, and a quantum theory of gravity is expected to explain how a fundamentally gravitational world *achieves* it, not assume it.

No-cloning, by contrast, is a theorem [WZ82]: no machine can copy an unknown state, because a copier applied to superpositions would have to be nonlinear. The argument needs no dynamics at all — only the linearity of the formalism's maps. It is, in the sense this paper will make precise, *kinematic*.

This paper presents a formal system in which both facts are theorems of the same kind — structural non-derivability results about which processes exist — and in which their difference in strength is reproduced, sharply, by the system's architecture. The system is the Care Calculus, a sorted linear logic with a guarded fixpoint, mechanized in Lean 4 with the two conservation laws proved outright [CCS]. Its statements are about derivations in a grammar, not about Hilbert spaces; what we offer to physicists is a dictionary under which those statements read as the familiar laws, with the logical architecture doing visible work:

- No derivation spends one linear token as two — `Dcare.no_contraction_content` **[MEASURED]**. Under the dictionary: **no-cloning**, as a fact about what processes are well-formed rather than about what maps are linear.
- In the guarded kernel, no derivation consumes a linear token into nothing — `Dcare.no_vanishing_restricted` **[MEASURED]**. Under the dictionary: **information conservation**, the grammar-side of unitarity.
- The first law holds even in the calculus with discard and duplication left in for the sorts that admit them; the second fails there — an explicit loss process is machine-checked (`Dcare.no_vanishing_unrestricted_refuted` **[MEASURED]**) — and is restored by exactly one structural restriction: the discard ban. Kinematics survives the adversarial world; dynamics does not.
- The unguarded operational semantics does not merely permit loss — it provably never settles (`Dcare.adversary_spin_diverges` **[MEASURED]**) — and, under the dictionary, a stable sector and a lawful sector are the same sector **[INTERPRETATION]**.

### 1.1 Related work

Four literatures border this paper, and each owns part of what a careless reading would credit to us.

**The foam lineage.** Wheeler's spacetime foam — geometry fluctuating quantum mechanically at the Planck scale [Whe55, Whe57] — assumes the quantum formalism intact; his "law without law" is a conjecture about the *status* of dynamical law, not about conservation failing in the foam [Whe83]. The proposal that unitarity fails in the foam is Hawking's: information loss in collapse [Haw76] and the superscattering operator [Haw82], joined by the intrinsic-decoherence program [EHNS84] and gravitational state reduction [Pen96]. Those failures are global, or wherever a black hole forms — never sector-selective — and the modern verdict restores unitarity even in the foam [Page93, Haw05, Carlip23]. None of these literatures lets cloning fail: the loss proposals are linear maps on density matrices, so the linearity proof of no-cloning survives inside them [Page93].

**Sector-restricted unitarity.** Closest to this paper's structure is Cotler–Jensen's de Sitter matrix model, whose infinite-time evolution "is not unitary, although it acts unitarily on a subspace" [CJ19]; Banks–Susskind–Peskin showed that generalizing density-matrix evolution beyond the Schrödinger equation costs locality or energy-momentum conservation [BPS84] — the pay-for-generalization argument this paper's divergence theorems echo. The boundary in those results is dynamical or topological; none is drawn by a syntactic restriction on a theory's own rules.

**The asymmetry in quantum information.** That the cloning ban outlives unitarity is known: it extends to general completely positive maps [Lin99], and no-broadcasting holds in any nonclassical no-signaling theory with no dynamical assumption at all [BCJFS96, BBLW07]. The rival framing — no-cloning and no-deleting from a single conservation assumption [HHSS05] — runs the deduction opposite to ours. In programming-language theory the shape is definitional: the affine discipline, "may be dropped, may not be copied" [Gir87, Wal04].

**Quantum programming languages.** The reading that a linear type system enforces no-cloning is standard [SV06, PRZ17]; Abramsky proves the categorical form — a compact category with natural copying collapses — explicitly in the proof-theory genre [Abr09]; the Hilbert-space theorem itself is mechanized in Isabelle [BHL20]; and a linear logic with a denotational conservation-of-unitarity property exists [ILV26]. What none of these has: both laws as non-derivability theorems of a single grammar, one of them restored by removing exactly one rule, with the counterexample world's loss process mechanized alongside the law it violates.

The paper is organized as follows. §2 gives a physicist's tour of the calculus and its guarded kernel, ending with the translation table that gives this artifact its Rosetta-Stone role. §3 states the two conservation correspondences and the asymmetry between them, then the semantic bridge and the named open problem it stops at. §4 develops the structural reading of the guarded tick and of the duplicable-context boundary. §5 presents the refutation: the machine-checked loss process, its anatomy, the kernel's three independent exclusions of it, the divergence of the unguarded dynamics, and the selection reading that follows. §6 derives the resolution projection and says precisely what would and would not be measured. §7 concludes. A Scope-and-limits section draws the boundary once, plainly.

## 2. The calculus and its guarded kernel

This section is a translation, not a tutorial; the calculus' full treatment is the companion paper [CCS]. What a physicist needs is the shape of the grammar and the two restriction layers.

### 2.1 Sorts and the linear discipline

The calculus is *sorted*: its base types divide into three linear resource sorts and a family of non-linear sorts. The linear sorts are `content` — the information token, written $C$ below; `trace` — the inert write-only archive, $T$; and `stream` — the live guarded stream. Every derivation at a lone content hypothesis spends it exactly once: `Dcare.single_linear_use` **[MEASURED]** — the formal statement of "used exactly once," machine-checked by a counting argument over derivations. Non-linear sorts — the duplicable source type (`knower`, $K$), its derived knowledge, values — may be duplicated through a gated contraction rule; `Dcare.knower_contractible` **[MEASURED]** exhibits the duplicable sort, marking the exact edge of the linear law. Streams are linear like content: the live stream is *spent*, not copied — the discipline §3.1 measures exactly — and the archive is linear too. There is no elimination rule for `trace`: nothing in the calculus reads a trace back.

Under the dictionary: `content` is a non-duplicable state — the thing quantum information theory says a qubit is. The linearity "used exactly once" is not a policy layered on the states; it is the grammar of the type. **[INTERPRETATION]**

### 2.2 The later modality and the guarded fixpoint

Self-reference enters through a fixpoint. The unguarded fixpoint destroys every conservation property at a stroke (a term can always unfold once more, so it need never deliver anything); the calculus instead guards it with the later modality $\triangleright$ (`Ty.later`): recursion through `Typed.fix` must pass one step of delay, and — crucially — the fixpoint rule fires only when its typing context is entirely non-linear (`AllNonLinear Γ`). The guard is priced, not free: each self-call costs one interval.

This is Nakano's later modality [Nak00] and Atkey–McBride's productive coprogramming [AM13]: a guarded fixpoint is not terminating but *productive* — it delivers one constructor per interval, forever. The step-indexed semantics that makes this precise is the topos-of-trees line [Bir12]. Two machine-checked facts matter here:

- `Dcare.no_fix_at_content` **[MEASURED]**: the guard excludes a guarded fixpoint at the content frame — and at any position in any context that carries content (`Dcare.guard_inherited` **[MEASURED]**). The recursion channel is physically separated from the conserved resource — self-reference cannot draw on the linear sector.
- `Dcare.selfapp_price` **[MEASURED]**: a fixpoint body can be exhibited that type-checks at a linear context, and the same context provably fails the side condition. The price of self-reference is exactly the resource the body would have re-consumed.

Under the dictionary: $\triangleright$ is a discrete tick. Nothing more. It supplies an ordering — one emission per interval — and no clock, no scale, and no Hamiltonian. **[INTERPRETATION]** The repeated temptation to read the guard as a fundamental time step is a projection, and is treated as one in §6.

### 2.3 The Guarded Kernel

The *Guarded Kernel* — the calculus's safe core, specified as the `ArmedSetup` (`Dcare.ArmedSetup`) — is the unrestricted calculus minus two rules:

1. **The discard ban** (`NoWeak`): no derivation may drop a resource. This single restriction carries both conservation laws of the kernel.
2. **The knower-synthesis ban** (`Dcare.NoKnowerSynthesis`): no binder may demand a synthesized duplicable source — the shape that the adversarial construction of §5 feeds on. At the no-discard grain this ban is not needed for the laws; it is carried because it excludes the adversarial conduit by a second, independent route.

Within the kernel, the two classical laws are absolute theorems: `Dcare.no_vanishing_restricted` and `Dcare.no_contraction_restricted` **[MEASURED]**, with armed forms (`Dcare.no_vanishing_armed`, `Dcare.no_contraction_armed`) under the full setup. The proofs rest on counting models: in the contraction model, soundness holds at all seventeen rules with no side condition; in the kernel's vanishing proof, the same shape is sound at sixteen rules, with the weak rule's obligation discharged by the discard ban itself — the restriction pays for its own soundness [CCS]. The axiom footprint: the kernel's theorems sit inside `propext` and `Quot.sound` alone, the companion's audit allowlist is Lean's standard three (`propext`, `Classical.choice`, `Quot.sound`), and there are no admitted axioms and no `sorry` anywhere in the restricted path. The kernel is not vacuous: the archive is legal (`Dcare.archival_witness` **[MEASURED]** — content may be consumed into a trace, recorded and counted), the closed trivial term is derivable, and the constants stand. What it forbids is exactly the discard.

Under the dictionary: the ArmedSetup is the specification of a stable sector — the boundary conditions a region of process-space must satisfy for its contents to conserve information. **[INTERPRETATION]**

### 2.4 The translation table

The Rosetta Stone, then. Each row pairs a construct of the calculus with its reading in the language of theoretical physics; every pairing is **[INTERPRETATION]**, anchored where noted by a **[MEASURED]** theorem.

| Calculus | Physics reading | Anchor |
|---|---|---|
| `content` linear; `single_linear_use` (uses = 1) | a non-duplicable state; each quantum of information spent exactly once | `Dcare.single_linear_use` [MEASURED] |
| `no_contraction_content` | **no-cloning** [WZ82]: one token cannot become two | [MEASURED] |
| `no_vanishing_restricted` | **unitarity / information conservation**: content cannot be consumed into nothing — *in the kernel* | [MEASURED] |
| `no_weakening_content` | the token is not merely unspent — it is spent *once*, exactly | [MEASURED] |
| $\triangleright$ / guarded fixpoint | the discrete tick; serialization of the exterior stream; no scale attached | [INTERPRETATION] |
| string diagrams over the sorted monoidal grammar | tensor-network notation [AC04]: the shared diagrammatic language | [INTERPRETATION] |
| the lete/pair exchange (§5) | a non-unitary channel: information delivered to a sink nothing reads | [MEASURED + INTERPRETATION] |
| `ArmedSetup` (discard ban + synthesis ban) | the boundary conditions of a stable sector | [INTERPRETATION] |
| `AllNonLinear Γ` vs the linear stream | a duplicable boundary sustaining a conserved bulk (§4.2) | [INTERPRETATION] |
| `archival_witness` / the trace type | no-deleting [PB00]: the write-only archive, reception without reduction | [MEASURED + INTERPRETATION] |

Two columns of the table deserve their warning. The middle column is a *reading*; the left column is a *theorem's subject*. The right column says which is which. A reader who forgets this will find §6 overclaiming; §6 is written to survive being read carefully.

## 3. The two conservation correspondences

### 3.1 No-cloning: the law that holds everywhere

The Wootters–Zurek theorem says: no universal machine copies unknown states, because a copier would act linearly on superpositions and cannot [WZ82]. The calculus's statement is prior to maps entirely:

> `Dcare.no_contraction_content` — there is no derivation at the lone context $[C]$ concluding $C \otimes C$. **[MEASURED]**

The proof is a counting model: interpret each type as a budget family, $C$ costs $1$, $C \otimes C$ costs $2$, and the model is sound at every rule with no hypothesis — so a context with budget $1$ can never fund a conclusion costing $2$. The arithmetic *is* the theorem [CCS]. The universal-machine form holds too:

> `Dcare.no_closed_cloner` — no closed term of type $C \multimap (C \otimes C)$ exists. **[MEASURED]**

and the quantitative form survives unrestricted:

> `Dcare.contraction_needs_two` — any derivation concluding $C \otimes C$ from a context $\Gamma$ requires a frame of budget at least $2$. **[MEASURED]**

The last is the sharpest statement a physicist will recognize: it is a *cost inequality*, the grammar's version of a superselection-style conservation constraint. And note the scope: these hold in the **unrestricted** calculus — with the discard rule present and with duplication available for the sorts that admit it. No-cloning needs no kernel. It is grammar-absolute.

The reading that linear types enforce this is standard in quantum programming languages — Selinger–Valiron's quantum λ-calculus adopts an affine intuitionistic linear logic for exactly this reason [SV06], QWIRE's linear wire types enforce it by construction [PRZ17], the Hilbert-space theorem is mechanized in Isabelle [BHL20], and Abramsky proves the categorical form — a compact category with natural copying collapses [Abr09]. What the calculus adds is the theorem's *kind*: not enforcement built into a language designed to have it, and not a statement about Hilbert spaces, but a non-derivability in a grammar that also contains the discard — the cloner fails to exist as a derivation of the very system that permits loss.

And the law's scope has now been sharply bounded — by falsifying its schema. The strong form, *no linear type is contractible*, is **false**: `Dcare.trace_contractible` exhibits $[\mathrm{trace}] \vdash \mathrm{trace} \otimes \mathrm{trace}$, with the hypothesis spent exactly once (`single_linear_use` holds) and the second copy *conjured from the empty context* — $\mathrm{nil} : [] \vdash \mathrm{trace}$ is closed. The engine is general (`Dcare.contractible_of_closed` **[MEASURED]**): any closed inhabitant of $\tau$ is a second copy at $[\tau]$, namely $\mathrm{pair}(\mathrm{var}\,0)\,c$. The concrete contractible types are the trace family — $\mathrm{trace}$, $\triangleright\,\mathrm{trace}$, $\mathrm{trace} \otimes \mathrm{trace}$ — and the self-arrows $\mathrm{arrow}\,C\,C$ (closed by the identity) and $\mathrm{arrow}\,C\,\mathbf{1}$, closed by the adversarial extractor itself (`Dcare.arrow_content_unit_contractible`); those five linearities are kernel computations (`Dcare.witnesses_are_linear` **[MEASURED]**), and the generic self-arrow family follows at every type (`Dcare.arrow_self_contractible` **[MEASURED]**). The type of the loss channel is, of all things, duplicable.

The repair is the physics arriving exactly. No-cloning is the law of the **linear** types with **no closed inhabitant**: you cannot double what you cannot prepare from nothing. This is Wootters–Zurek's own clause, as grammar [WZ82] — the theorem never forbade pairing an unknown state with a *blank* you prepared yourself; it forbade copying the unknown. The calculus's blanks are precisely its closed inhabitants ($\mathrm{nil}$ is the blank record; the identity is the known function). The classification is stated in-tree (`Dcare.T5`), with the preparability direction proved at *every* type (`Dcare.closed_implies_clone` **[MEASURED]**), and the linearity gate is itself necessary: the duplicable knower has no closed inhabitant yet is contractible (`Dcare.knower_contractible` **[MEASURED]**), so linearity is what turns preparability into the criterion. The settled cases span both sides of the boundary: unclonable — the carriers $C$ and $\mathrm{stream}$ (`Dcare.no_contraction_content`, `Dcare.no_contraction_stream`); clonable — the witnesses above (`Dcare.trace_contractible`, `Dcare.arrow_self_contractible`). The frontier beyond them is measured, and it is the honest kind: no predicate of net alone classifies (the trace and the stream carry the same net; only one is clonable), and the companion's analysis has reduced the residual to a single wall [CCS]: $\mathrm{arrow}\,C\,\mathrm{stream}$, which reduces to $[C] \nvdash \mathrm{stream}$ — the companion's own open question to the proof-assistant community, whose base case is now in-tree (`Dcare.no_closed_stream` **[MEASURED]**: from nothing, nothing flows) and whose tower case is discharged. One statement — *content does not entail a stream* — would close the community ask and the classification at once. The analysis is pinned to five root shapes, with the stream conduit itself inhabited at $[C]$ — it fails not at firing but at arrival, reaching the root as a linear arrow that cannot shed its knower domain — so the difficulty is measured, not mysterious [CCS]. Closing it wants a syntactic walk at the stream frame, not a counting argument. Stated honestly: one direction is a theorem at every type, the settled cases span both sides of the boundary, and the cloning law is not a sector law but a *preparability* law. **[MEASURED (anchors) + INTERPRETATION (the reading)**]

Under the dictionary: the impossibility of cloning is not a fact about which unitaries exist; it is a fact about which processes are well-formed. The calculus forbids the copier before dynamics is ever mentioned. **[INTERPRETATION]**

### 3.2 No-vanishing: the law that needs the kernel

The second conservation law — no process consumes information into nothing, the grammar-side of unitarity — has a different logical shape, and the difference is the paper's central observation.

In the unrestricted calculus, the law is **false**:

> `Dcare.no_vanishing_unrestricted_refuted` — there exists a derivation at $[C]$ concluding the trivial type. **[MEASURED]**

The derivation is explicit, machine-checked, and its anatomy is §5's subject. And the loss is not an artifact of proof-system detours: a **cut-free** derivation of $[C] \vdash \mathbf{1}$ exists — machine-checked, with no app-elimination anywhere (`Dcare.SCClosedKiller.witnessTyped_cutFree` **[MEASURED]**) — so normalization removes nothing: the loss process has a normal form. The mechanism is general, and is the leak theorem: *any* cut-free derivation of a non-linear type at the content frame yields a cut-free $[C] \vdash \mathbf{1}$ (`Dcare.SCClosedKiller.killerOf_cutFree` **[MEASURED]**) — spend the token into the non-linear channel, pair it with a trivial unit, and the exchange's reversed frame puts both non-linear positions where the discard can drop them. No application fires anywhere; the channel is closed by grammar, not by search.

In the guarded kernel the law is absolute:

> `Dcare.no_vanishing_restricted` — in the discard-free fragment, there is no derivation at $[C]$ concluding the trivial type. **[MEASURED]**

with the armed form under the full setup. The qualifier is not decoration: it is the entire content of the theorem. One restriction — remove the discard — and conservation of content becomes absolute: `Dcare.no_weakening_content` **[MEASURED]** pins the token's single use; the archive stays legal (§3.4); the constants stand. And the cut-free killer changes nothing here — it carries weak nodes, and the discard ban excludes it (`Dcare.SCClosedKiller.witness_not_noWeak` **[MEASURED]**). The atomic-head restriction excludes nothing; the discard ban excludes everything.

Unitarity has appeared inside logic before, denotationally: Intuitionistic Unitary Linear Logic proves a conservation-of-unitarity property for its well-typed terms, via denotational semantics and cut admissibility [ILV26]. The present statement is dual in kind: not an invariant of a well-behaved fragment, but a non-derivability in the permissive grammar, repaired by removing one rule.

### 3.3 The asymmetry

Put the two laws side by side:

| | cloning forbidden | content conserved |
|---|---|---|
| unrestricted calculus | yes, for the token (its full scope is §3.1's preparability law) | **no** — a loss process is derived |
| guarded kernel | yes | yes, absolutely |
| what carries it | the sort discipline alone | the discard ban |

Physics has met this asymmetry before, in exactly this shape. No-cloning follows from linearity alone — a kinematic constraint, independent of dynamics [WZ82]. Information conservation requires the dynamics itself to be unitary — a constraint on processes, which fails the moment non-unitary channels are admitted. The calculus reproduces both the laws *and the gap between them*: a kinematic law that survives the most permissive rule-set, and a dynamical law that exists only in the sector that bans destruction. **[INTERPRETATION]**

The asymmetry is not news to quantum information either: the cloning ban extends to general completely positive maps — including lossy, non-invertible ones [Lin99] — and no-broadcasting holds in any nonclassical no-signaling theory, with no dynamics assumed [BCJFS96, BBLW07]. In type theory the same fact is definitional: it is the affine discipline, "may be dropped, may not be copied" [Wal04, Gir87]. The rival derivation — both no-cloning and no-deleting from a *single* conservation assumption [HHSS05] — assumes precisely what the calculus's kernel recovers and its outside loses. What the calculus adds is the two facts as theorems of one rule-set, with the refuting term mechanized beside the law it refutes. **[INTERPRETATION]**

And the asymmetry is not merely observed across the two laws — it is *computed* between two adjacent types. The vanishing conduit's type, $\mathrm{arrow}\,K\,\mathrm{knowledge}$, is priced non-linear by the grammar: weakable, and that reachability is the loss channel — the discard can take it. The stream conduit's type, $\mathrm{arrow}\,K\,\mathrm{stream}$, is priced linear — unweakable — because every stream-needing type is linear (`Dcare.needsS_linear` **[MEASURED]**): stream-need propagates to linearity, so the adversarial construction's final step, weakening the conduit away, is structurally blocked for stream [CCS]. One linearity computation separates the channel the discard can reach from the channel it cannot. The two conservation laws differ by a single `Bool` on adjacent types. **[MEASURED (the anchor) + INTERPRETATION (the reading)**] And the construction's autopsy shows the same gap from the inside: the vanishing channel runs all the way to the discard — a step the kernel must ban to kill it; the stream-cloning construction dies at its *trigger* (its conduit is inhabited, but nothing fires), so the stream law needs no kernel at all [CCS]. The two laws fail differently because the two constructions die at different steps: one at a rule the stable sector removes, one at the grammar itself. **[MEASURED (the autopsy is the companion's) + INTERPRETATION]**

The proof method rhymes with physics too. The counting model is a monotone quantity that every rule respects — conserved-charge reasoning, the same shape as a textbook conservation-law proof: exhibit the charge, check it at each vertex. The model does not merely certify the two laws; it *prices* them ($1$ in, $2$ needed, $1$ spent). **[INTERPRETATION]** And a second engine is already in-tree: the flow count — a net current from frame to conclusion, with generator fires as its sources; its content instance is the theorem that no clone of content exists without a mint (`Dcare.no_contraction_nogen` **[MEASURED]**). A conserved charge and a conserved current are different theorems about the same law, and the calculus needed both: the two engines have incomparable reach, and the companion's frontier measurement names the residual where they are blind at once — and proves that no monotone, fix-sound price model of the known clause shape can close it, so the missing instrument is *named* rather than merely absent [CCS]. Physics keeps exactly this genre too: no-go theorems about instruments, as distinct from no-go theorems about the world. **[INTERPRETATION]**

### 3.4 The archive and no-deleting

The kernel forbids consuming content into nothing; it does not forbid consuming content into a *record*:

> `Dcare.archival_witness` — content can be consumed into the trace type: $[C] \vdash T$. **[MEASURED]**

The trace type has no elimination rule — and that is now a pair of theorems, not a remark: no closed `trace → knowledge` function exists, and no `trace → value` either (`Dcare.past_cannot_teach`, `Dcare.past_cannot_value` **[MEASURED]**). "Store now, understand later" is untypable; the record is counted (`uses = 1` certifies the token was spent), but nothing certifies it was heard, and nothing ever can. Reception without reduction — the past is inert.

Under the dictionary this is the Pati–Braunstein no-deleting theorem's territory [PB00], with a distinction the physics does not usually draw. Physics forbids deleting an unknown state *against a blank* — the dual of cloning. The kernel likewise forbids the discard outright. But the calculus adds a second, quieter absolute: even the *legal* archive is permanently unread. It separates two things physics merges — you cannot erase the record (the ban), and you cannot retrieve it either (the grammar) — and makes the second one structural. **[INTERPRETATION]** And on the information paradox the archive takes a stance: what crosses is neither destroyed nor retrievable — recorded, counted, inert — the shape of the retained-information resolutions [Page93, Haw05]. **[INTERPRETATION]**

### 3.5 The semantic bridge: a functor into channels

The correspondences above are dictionary rows. For the channel-shaped fragment they can be backed by a construction: a functor into the category quantum information theory uses for open systems. This subsection builds it at paper rigor — nothing here is mechanized.

**The target.** $\mathbf{CPM}(\mathbf{FdHilb})$: objects are finite-dimensional Hilbert spaces, morphisms are completely positive maps $\mathcal{L}(H) \to \mathcal{L}(K)$ [Sel07]. Two structural facts carry everything. First, every object carries a canonical *discard* — the trace $\mathcal{L}(H) \to \mathbb{C}$ — so this is the category of open systems, in which forgetting to the environment is always available. Second, copying exists only along a *classical structure* — a chosen orthonormal basis, a special commutative dagger-Frobenius algebra [AC04] — and a compact category whose copying is natural collapses [Abr09]. Channels lose; they never breed [BCJFS96, BBLW07].

**The interpretation.** On the finitary types (no $\triangleright$, no fixpoint, no stream; arrows only where the first-order reading suffices):

| calculus | denotation |
|---|---|
| `content` $C$ | a system $H = \mathbb{C}^d$, $d \geq 2$, no structure chosen |
| `knower` $K$ and `knowledge` | classical structures: spaces with a chosen basis |
| `unit` | the monoidal unit $\mathbb{C}$ |
| $\otimes$ | $\otimes$ |
| `weak` (the discard) | the trace — the discard clause |
| `contr` at a non-linear sort | copying along the chosen structure — available exactly there |
| `pair` / `lete` | tensor of the maps / composition, after the exchange's swap (the rule binds both components linearly) |
| the constants (`gen`, `red`, `obj`, `terminate`) | fixed channels — the coalgebra's faces: state preparation (the mint), measurement readout, valuation, termination |
| `nil` / `snoc` | the empty record / appending along the archive's classical structure |
| `lam` / `app` | first-order currying and evaluation, where the first-order reading suffices |

Soundness at paper rigor: every derivation over the finitary fragment the table covers — the sorts, the constants, the structural rules at their gated sorts, tensor/pair/lete, first-order arrows, the archive — denotes the completely positive map assembled from these clauses, rule by rule. A grain note, found by building the companion simulator [CCS-sim]: the calculus's own discard is *gated* — weakening is available only at non-linear types — so erasure of the conserved token requires first carrying it into a discardable sector: the leak theorem's mechanism, denotationally. Two clauses matter beyond soundness. The discard clause makes the *unrestricted* calculus exactly the channel world — loss is denotable, always. The copying clause localizes duplication to the classical sorts — the denotational divide of `Dcare.needsS_linear`.

**Three correspondences.** (C1) *The boundary maps to the boundary.* Kernel derivations (no `weak`) denote composites that never use the trace clause; unrestricted derivations may — and on the quantum sector the kernel's image is exactly the unitaries: an auxiliary acquired on the way cannot be disposed of without the trace, so a kernel composite from the conserved system back to itself is pure (verified computationally: 170/170 kernel quantum-to-quantum constructions unitary [CCS-sim]). The kernel/outside line of §5.5 is the no-discard/discard line of the interpretation. (C2) *The laws are mirrored at the clause level.* In the clause set, the only operation that erases is the discard: every route from a structureless $d \geq 2$ system to the trivial system passes through the trace — any completely positive map $\mathcal{L}(H) \to \mathbb{C}$ is $X \mapsto \mathrm{Tr}(AX)$ with $A \geq 0$, hence the composite $\mathrm{Tr} \circ \Phi_A$ of a channel with the trace — the semantic image of `Dcare.counterexample_not_noweak` (the tree proved the same fact syntactically: the killer's last step *is* a weak; and the invariant is checked computationally: corpora of $10^4$–$10^5$ constructions at $d \leq 3$ — every quantum-to-trivial construction carries the discard [CCS-sim]). And the cloner on $H$ that `Dcare.no_contraction_content` forbids would be a copier with no structure chosen — the object [Abr09] shows cannot exist without collapse. (C3) *The preparability law.* §3.1's blanks — the closed inhabitants — denote basis states: prepared, known. The contractible types are those whose denotations carry chosen structures; content's carries none. "You cannot clone what you cannot prepare" reads "you cannot copy along a structure you have not chosen." And the loss derivation of §5.1 denotes an erasing channel $H \to \mathbb{C}$ — the conduit's channel composed with the full trace-out: §5.1's *trace-out map* becomes a lemma of the bridge. **[The construction is mathematics at paper rigor; the rows it backs are correspondences, not derivations — see the limits below.]**

**Three limits, stated where the construction is.** (i) *Soundness does not reflect.* A functor preserves derivable processes but cannot transfer non-derivability — the diagonal exists set-theoretically whether or not any derivation builds it — so the grammar's no-go theorems remain *stronger than their denotations*. The bridge mirrors the laws; it does not derive them. (ii) *The scope is finitary and first-order.* Streams, the guard, and the fixpoint are outside — the guarded half, below — and higher types are left open, as the quantum λ-calculus's own denotational program left them [SV06]. (iii) *Paper rigor.* Nothing in this subsection is machine-checked, and a categorical construction carries no empirical content by itself.

**The guarded half.** The finitary bridge has no home for $\triangleright$, `fix`, or stream — precisely the objects that carry the tick. That gap is not a footnote; it is the paper's named open problem, stated with its walls in §3.6.

### 3.6 The named open problem: quantum guarded domain theory

The bridge of §3.5 stops where the tick begins. Its halves each exist in the literature; their composition, per §1.1's survey, does not: a **quantum guarded domain theory**.

The target: presheaves on the ordered naturals valued in $\mathbf{CPM}(\mathbf{FdHilb})$, $\triangleright$ the shift functor — the guarded fixpoint denoting the unique productive solution [AM13, Bir12], $\triangleright A$ reading as "$A$ one tick later" (a discrete-time channel), and the serialization theorem `Dcare.chain_tick_buys_one` becoming semantic: the denotation applies exactly one channel per tick — discrete-time open dynamics, made categorical.

Three walls stand between the ingredients and the composition:

1. **Higher order.** $\mathbf{CPM}(\mathbf{FdHilb})$ is not cartesian closed — the obstruction the quantum λ-calculus's denotational program left open [SV06] — and a presheaf construction wants more structure than the bare completely-positive category supplies.
2. **The stream objects.** No infinite stream lives in $\mathbf{CPM}(\mathbf{FdHilb})$, finite-dimensional by fiat; the presheaf tower would supply streams as time-indexed families — but the dagger structure that carries the physics is delicate under presheaf constructions, and the two disciplines that must meet here — the guard's gate and the dagger's adjoints — have never been made to.
3. **Solvability.** The guarded fixpoint needs solution objects with $\omega$-limit structure; on the quantum side no such enrichment is standard. Inventing it is not a lemma; it is the problem — but the hope is checkable at toy grain, and it checks: guarded equations over $\omega$-indexed state streams have the unique productive solution, guess-independent and prefix-stabilizing, with contractive maps converging geometrically, while unguarded self-reference is guess-dependent [CCS-sim].

What success would buy: a denotation for the sigil of §4.1; serialization as a semantic fact; and the tick's scale-freeness promoted from fence to theorem — the shift functor carries no scale to fix. We state the target, the ingredients, and the walls. The construction is open.

## 4. The tick and the boundary

### 4.1 The guarded tick and the signature diagram

The calculus's canonical infinite object is machine-checked:

> `Dcare.knower_sustains_stream` — at a single duplicable-source hypothesis, a term of guarded-stream type is derivable: one source, sustaining an infinite stream. **[MEASURED]**

This is the seed of the program's notation [GS], rendered as the signature

$$\bigcirc : S \multimap (\triangleright A \,\circlearrowleft\, \bigcirc)$$

— a source $\bigcirc$ wired through the guard $\triangleright$ into a feedback loop. The physics reading instantiates the loop type: $A := BH$, giving the paper's emblem

$$\bigcirc : S \multimap (\triangleright BH \,\circlearrowleft\, \bigcirc)$$

a stream source feeding a horizon-delayed recursor. **[INTERPRETATION]** The reading is this: whatever the interior does in parallel, the exterior is a *serialized* stream — the guarded feedback wire delivers one emission per tick, and the ordering of the exterior is the tick's ordering. A causal boundary, in this grammar, is exactly a one-at-a-time interface: parallel interior process, step-indexed exterior stream.

The diagram is a tensor-network-style drawing over the sorted monoidal grammar — the same diagrammatic currency physics uses for tensor networks and process theories [AC04], which is why the translation is frictionless on the page. And both halves of the reading are anchored, not sketched: the guarded fixpoint unfolds **one tick at a time**, type-preservingly — each unfold consumes one $\triangleright$ and is repeatable at every interval (`Dcare.fix_unfold_closed`, `Dcare.fix_unfold_at_knower` **[MEASURED]**) — and at the feedback-agent grain every guarded step appends **exactly one** element to the accumulator (`Dcare.extractor_step_integrates` **[MEASURED]**). The count now holds at the chain grain too: emissions $=$ $\triangleright$-depth $= n$ at every stage of the unfolding chain — each $\triangleright$ consumed buys exactly one emission, never zero, never two (`Dcare.chain_tick_buys_one` **[MEASURED]**) — and the contrast with the spin is a single theorem: $n$ guarded ticks emit exactly $n$, while the unguarded spin emits exactly zero at every horizon (`Dcare.guarded_vs_spin` **[MEASURED]**). One scope fact, so nobody overreads it: *emission $\Rightarrow$ tick* is not a theorem — the cycle's extractor fires before any unfold — the count binds the unfolding chain, not firing as such. What remains a reading is the horizon itself; the count is a theorem.

Serialization has a twin structural fact, and it is why the hard questions are hard: the guard *recedes*. The tower frames are not a blind spot of the model — the guard prices them at zero budget, and the stream is refuted at every one of them [CCS]; the base case is a theorem in-tree (from nothing, nothing flows: `Dcare.no_closed_stream` **[MEASURED]**). What fails is any argument that would stop: a fix-rooted closed $\triangleright\,\mathrm{stream}$ is *equivalent* to the same question one guard higher, so the natural induction cannot terminate; and no monotone, fix-sound price model of the known clause shape can close the family — an impossibility theorem about the instruments themselves, not about the world [CCS]. The supply analysis is blind too, at every fixpoint ($\mathrm{NeedsS}(\triangleright a) = \mathrm{NeedsS}(a)$) [CCS]. Under the dictionary — a reading, not a theorem — the interior is infinitely stratified for this question: answered at each stratum, it regenerates one interval deeper, forever. The guard that serializes emission is the same guard that recedes before the analysis. **[INTERPRETATION]**

And the fence goes here, in bold: the guard orders emission; it does not fix a rate, a temperature, a spectrum, or a clock. No radiation is computed in this paper. The horizon reading of $\triangleright BH$ is a reading of a *type*, not a calculation of anything. **[INTERPRETATION]**

### 4.2 The boundary, structurally

The fixpoint's gate is the structural fact: `AllNonLinear Γ` — recursion may draw only on the duplicable sector; `Dcare.guard_inherited` **[MEASURED]** records that the guarded kernel changes nothing here, it inherits the gate. So the grammar's architecture is:

- a **duplicable ambient context** — unrestricted, copyable, the sector that funds recursion; and
- a **conserved linear stream** — the content sector, spent exactly once, guarded in time.

The counting model makes the relation precise: the linear stream's budget is *carried by* its ambient frame — a duplicable boundary funding a conserved interior, with the interior's arithmetic bounded by the frame that hosts it. **[MEASURED (the model) + INTERPRETATION (the reading)**] The arithmetic is now a lemma at every scale $n$ (and as an equality, where the general conservation law gives only an inequality): $n$ fires mint exactly $n$ content tokens; the tower they form is priced at least $n$ by the model; and the knower source that funds all of it is priced $\emptyset$ — yet occupies exactly one position, unchanged, with nothing archived or borrowed (`Dcare.holographic_budget` **[MEASURED]**). One duplicable boundary position, $n$ conserved emissions, zero marginal charge on the source: the reading is §4.2's holographic shape; the budget facts themselves are arithmetic.

Under the dictionary, this is the holographic separation in its structural form: an abundant, duplicable periphery sustaining an interior whose resources are exactly conserved; degrees of freedom in the interior priced by the frame that carries them. **[INTERPRETATION]** This is deliberately the *structural* content only. It resonates with the modern error-correcting view of holography — bulk lawfulness holding only within a protected substructure of boundary data — and that resonance is noted and then left alone; it is not asserted as content.

### 4.3 What this correspondence does not claim

No metric. No field theory. No anti-de Sitter space, no conformal field theory, no Ryu–Takayanagi formula, no duality statement of any kind. The calculus contains no geometry — its only temporal structure is the tick's ordering, and its only spatial notion is the boundary/bulk *separation of grammatical roles*. Everything with a meter in it enters in §6, as physics input, labeled. The claim of §4 is exactly this: the grammar's architecture (duplicable boundary / conserved interior / one-emission-per-tick interface) is the same *shape* as structural holography, and the shape can be studied where it is fully rigorous — in the calculus — even while nothing metric is claimed. **[INTERPRETATION]**

## 5. The refutation: why the guard is load-bearing

### 5.1 The anatomy of the exchange

In the unrestricted calculus, the machine-checked counterexample of §3.2 exists, and it has a named anatomy — four theorems, one story **[MEASURED]**:

- `Dcare.the_cycle` — an epistemic cycle is assembled: a duplicable source sustaining a stream;
- `Dcare.the_swap` — the lete/pair exchange: the content token is spent as the head of the cycle's stream — handed to the cycle as its next emission;
- `Dcare.the_conduit` — a reader is synthesized to receive it — the channel that would make the hand-off a *communication*;
- `Dcare.the_discard` — the conduit is then weakened away. Deleted. The reader that would have heard the token never exists at the conclusion.

Net effect, as a process: the token was consumed — `uses = 1`, the books balance — and it was delivered to a sink that nothing reads. The whole is `Dcare.unrestricted_counterexample` **[MEASURED]**: a complete, well-formed derivation whose conclusion carries no content and no record. The information is not transformed. It is *spent into unreadability*.

Under the dictionary: a **non-unitary channel**. Not a unitary process with an unfortunate basis, and not a decohering but reversible interaction — a channel whose output literally does not contain what its input did. The composite's shape will be recognizable to anyone who has derived a master equation: couple the conserved token to an unconstrained carrier, then discard the carrier — the calculus's trace-out map. §3.2's cut-free killer is this shape in normal form: the coupling (the conduit), the pairing, and the discard, with no application left to eliminate. **[INTERPRETATION]** In the language of §1: unitarity fails, and it fails *derivably*, in the world where the discard is legal.

### 5.2 Three exclusions

The kernel refuses this construction three times over, and the independence of the refusals is the point **[MEASURED]**:

- `Dcare.counterexample_not_noweak` — the construction's final step *is* a discard. The discard ban alone refutes it.
- `Dcare.counterexample_conduit_no_synthesis` — the synthesis ban kills the conduit independently, by a second route that does not pass through the discard.
- `Dcare.counterexample_not_armed` — the full ArmedSetup excludes the whole shape.

Two independent structural barriers, either of which suffices — and one negative result that prices them differently: the cut-free (atomic-head) restriction excludes the killer *not at all* — §3.2's normal-form witness lives there (`Dcare.SCClosedKiller.lamArm_false` **[MEASURED]**) — while the discard ban excludes every variant of it. The barriers are real but asymmetric: the discard ban is load-bearing; the synthesis ban is an independent second lock; cut-freeness is decorative. A physicist will recognize the architecture: like a gauge redundancy protecting a conservation law, the grammar protects its conserved quantity redundantly — and, as with redundancies, not every one pulls weight. **[MEASURED (the exclusions) + INTERPRETATION (the reading)**]

### 5.3 The dynamics: divergence

The refutation is not static. The calculus has two operational semantics: in the guarded one, a stopped configuration is terminal — a process may halt, having delivered; in the *unguarded* one, a stopped configuration is not terminal but spins: it recurs at every horizon, ticking forever, emitting nothing. The machine-checked verdict:

> `Dcare.adversary_spin_diverges` — under the unguarded semantics, the stopping policy run from an initial state diverges. **[MEASURED]**

> `Dcare.spin_pays_forever_buys_nothing` — the spinning trajectory accrues cost forever and delivers nothing. **[MEASURED]**

The contrast's bookkeeping closes both sides. Under the guarded semantics, a run that is not infinite is finite — once silent at one interval, silent forever (`Dcare.run_not_infinite_is_finite` **[MEASURED]**) — while from the spun state the *only* unguarded step is the spin itself (`Dcare.looped_only_spins` **[MEASURED]**): zero emission, one cost unit, forever, deterministically. And the two-worlds picture is now a single theorem rather than an assembly: with the same generator, the same policy class, and the same starting configuration, the guarded semantics reaches `stopped` in finitely many steps and *cannot* diverge — `stopped` is a dead end under `Step` — while the unguarded semantics diverges: halts $\wedge$ $\neg$Diverges$_G$ $\wedge$ Diverges$_U$ (`Dcare.guard_halts_unguarded_spins`, `Dcare.guarded_no_divergence` **[MEASURED]**).

So the unrestricted world is doubly unfit as a substrate for stable process: it *permits* information destruction by one theorem, and its dynamics *never settle* by another. Loss and non-settlement arrive together — which is, under the dictionary, the pairing one would want of a sector that cannot host an S-matrix: no conservation and no asymptotics in the same package. **[INTERPRETATION]**

### 5.4 The metastability sentence

One sentence, labeled, and then the fence. **[INTERPRETATION]** A sector that permits the discard admits — by theorem — a process that destroys content, while its own dynamics provably never settle: the shape of a metastable phase, apparently stable, loss-permitting, with no ground state to reach. The calculus quantifies none of that metastability: no rate, no barrier, no mechanism is derived, and the shape is where the analogy stops.

### 5.5 The selection reading

There is a distinguished lineage in fundamental physics with this general shape: Wheeler's spacetime foam — geometry fluctuating quantum mechanically at the Planck scale [Whe55, Whe57] — and his later "law without law" [Whe83]. Wheeler's own emergence of law is statistical and observer-participatory; the selection shape used here is not his, and it is not the anthropic selection of the cosmological literature [Car74] either. It is closest in spirit to cosmological natural selection [Smo92] — but that mechanism selects among values of the dimensionless parameters, and its own author scopes it so: the prediction concerns "the observed low energy parameters and not to the fundamental landscape of theories" [Smo06]. The calculus's version selects over the rule-set itself, and it is, unusually, formal. It needs no observer, no reproduction, and no fine-tuning argument; the selection is theorem-shaped:

- *outside* the kernel, information loss is not possible but **derived** (§5.1), and the dynamics **diverge** (§5.3);
- *inside* the kernel, conservation of content is **absolute** (§3.2).

A stable sector and a lawful sector are the same sector, and the boundary between them is one rule: the discard. **[MEASURED (both halves) + INTERPRETATION (the reading)**]

And the reading has a signature, checkable against the tree rather than argued in prose: the pre-lawful regime is **lossy, not a breeder**. Cloning stays forbidden in the unrestricted calculus (§3.1): `Dcare.no_contraction_content` holds with the discard present and duplication available for the duplicable sorts. What fails outside the kernel is conservation; duplication of the token fails nowhere (the law's full scope over linear types is §3.1's preparability law, and it cuts the same way: even the contractible types are conjured blanks, not copied unknowns). **[MEASURED (the anchor) + INTERPRETATION (the reading)**] The shape is not new, and the paper does not claim it is — its ancestry in linear non-unitary evolution, in the no-broadcasting theorem's scope, and in the affine discipline is §3.3's, cited there. What is ours is the packaging: both facts are theorems of *one* rule-set, the loss an exhibited derivation and the ban unconditional in the very system that exhibits it, with the boundary between regimes a single structural rule — a boundary measured at two grains: neither normalization nor the atomic-head restriction excludes the loss process, and the discard ban alone does. That is the tree-checkable residue.

The guard, stated once more for the record: this is *structural ancestry*, not identification — the foam lineage's loss proposals, their global (never sector-selective) shape, and the modern verdict that restores unitarity even in the foam are §1.1's, cited there [Haw76, Haw82, EHNS84, Pen96; Page93, Haw05, Carlip23]. What §1.1 cannot carry is the proximity ranking: the closest structural precedent is Cotler–Jensen's de Sitter evolution, unitary on a subspace [CJ19] — a *dynamical* boundary, not a grammatical one — and the cost argument of [BPS84] shares its shape with ours. The calculus offers a rigorous object with the shape of the old intuition — conservation failing in the pre-lawful regime while the kinematic law survives — and does not claim the intuition was about this object. **[INTERPRETATION]**

## 6. Experimental signatures

This section is a **[PROJECTION]** throughout, with the physics inputs marked. It exists because physicists reasonably ask what a grammar could ever point a detector at. The answer is: not the theorems — a theorem about derivations has no error bars. What a detector can test is the projection, and the projection has a definite scale.

### 6.1 The screen bound and the voxel count

Two inputs and one assumption.

**(P1) The screen bound [MEASURED — cited physics].** The Bekenstein–Hawking area law [Bek73, Haw75]: the maximal entropy of a region is its boundary area in Planck units, $S \le A/4l_p^2$. Read informationally: a region of radius $R$ is described by a *screen* carrying at most

$$N_{\text{screen}} \;\lesssim\; \frac{4\pi R^2}{4\,l_p^2} \;=\; \frac{\pi R^2}{l_p^2}$$

irreducible degrees of freedom — one per Planck area, up to the $O(1)$ constant.

**(P2) The voxel count [PROJECTION].** *Assume* the guarded tick is spatialized: the bulk interior is discretized at resolution $L$. This is the assumption the calculus does not make — $\triangleright$ orders emission, it does not tile space — but it is the minimal reading under which the grammar's discreteness meets geometry at all. A spherical bulk resolved at $L$ carries $N_{\text{voxel}} \approx (R/L)^3$ cells.

**(P3) Equate them [PROJECTION].** The interior cannot carry more cells than the screen carries bits:

$$(R/L)^3 \;\lesssim\; \frac{\pi R^2}{l_p^2} \qquad\Longrightarrow\qquad L \;\gtrsim\; (\pi)^{-1/3}\,\bigl(l_p^2 R\bigr)^{1/3}.$$

Suppressing the $O(1)$ geometric factors deliberately — they are not the content:

$$\boxed{\,L \;\approx\; \bigl(l_p^2 R\bigr)^{1/3}\,}$$

With $l_p = 1.62\times10^{-35}\,$m and the observable radius $R = 4.4\times10^{26}\,$m: $l_p^2 R \approx 1.2\times10^{-43}\,$m$^3$, so

$$L \;\approx\; 5\times10^{-15}\,\text{m},$$

— the voxel of the observable bulk is *nuclear-sized*. This is the "MIP-map" scaling, and the metaphor is exact about what it means: as a texture's interior is magnified beyond the resolution its stored mip level carries, the interior aliases. One bit per screen pixel fixes the interior's effective resolution; magnification beyond $L$ buys nothing. The scaling is not ours, and the paper's claim on it is only the framing. Károlyházy's clock argument gave $(\Delta s)^3 \gtrsim l_p^2 s$ in 1966 [Kar66]; Ng and van Dam re-derived it from measurability limits [NgdV94] and by exactly the cube-counting route above — minimal cubes, one degree of freedom each, under the holographic bound [NgdV00, tHooft93, Suss95]; Ng's review runs the derivation in this paper's direction and prints the same order of magnitude — $10^{-13}$ cm at the observable-universe scale, against this paper's $5\times10^{-15}$ m — for the $\alpha = 2/3$ branch [Ng03]. The family is being tested; see §6.2. What the grammar contributes is only where the discreteness is pointed from — a tick that is a theorem about derivations, not a postulate about space.

### 6.2 Two scalings, two instrument classes

The transverse variant. The older, two-dimensional version of the argument — the screen constrains *transverse* position only — gives $\Delta x \approx \sqrt{c\,t_P\,L}$: Hogan's holographic noise [Hog12], an MHz-band shear between causally connected positions, which motivated the Fermilab Holometer. The verdict is in: the paired 39-meter interferometers' cross-spectra exclude the transverse-shear model at $5.1\sigma$ (normalization below 44% of the prediction at 95% confidence) [Chou16]. The exclusion binds that model's spectral shape at apparatus baselines — the form is not stated at cosmic scales, where it would be $\sim\!10^{-4}\,$m and is not defensible.

The volumetric form's channel. $L \approx (l_p^2 R)^{1/3}$ at $5\times10^{-15}\,$m is not an interferometer number, and its signature is not a timing one: $5\times10^{-15}\,$m is $1.7\times10^{-23}\,$s of light travel — the picosecond-scale figures belong to the transverse family. The $\alpha = 2/3$ model's channel is *angular*: wave-packet widening accumulated over cosmological path lengths, blurring gamma-ray-burst images [Stein15]. Nor does the family live in an observational vacuum — but the honest landscape is contested, not clean. The 2003 wavefront-coherence claims — Hubble imaging of extragalactic sources [Rag03, Lieu03] — announced the destruction of first-generation foam models; the accumulation arithmetic was itself corrected by the review this paper cites [Ng03], which shows the claimed exclusions overestimated by the cumulative factor $(L/\lambda)^{\alpha}$ — so the 2003 results constrain rather than kill. A second program tests the same exponent on blazars and quasars, by requiring that sources stay point-like: $\alpha \gtrsim 0.58$ in X-rays, $\alpha \gtrsim 0.67$ at GeV, $\alpha \gtrsim 0.72$ at TeV — the GeV bound's own authors calling it "disfavoring the holographic model, but perhaps not decisively" [Perlman14], the TeV bound sitting just above $2/3$, and later analyses claiming a sharper rule-out [NgP22 and references therein]. Against this, the GRB aggregation fits $\alpha = 0.650$–$0.735$, with $2/3$ inside [Stein23]. The comparison is not yet decisive in either direction, for reasons the field's own methodology review names: the amplitude is fixed only as "$a \sim 1$" [Ng03], and the distance-measure and light-path averaging conventions are unsettled [NgP22] — two $O(1)$-class freedoms that keep every current number provisional. Where this paper's projection stands is therefore exact: the guard contributes discreteness and no number, the entropy bound fixes the $1/3$ — and the resulting $\alpha = 2/3$ is consistent with the GRB window, strained by the TeV bound, and undecidable until the averaging problem is settled. Its status is live on two fronts. GRB 221009A — the brightest yet observed — has angular data consistent with the model's blurring, with a limiting bound near one degree [Stein23]. And the generalized Károlyházy model has just been excluded on a neighboring channel: gravity-induced decoherence in a laboratory setting, $R_K > 4.64\,$m at 95% confidence against a predicted $R_K < 1.98\,$m [Bort26] — an exclusion of the decoherence channel, not of the blurring channel. A detector pointed at this projection is a gamma-ray imaging instrument, not a gravitational-wave antenna: LISA-class and Einstein-Telescope-class observatories are exquisite low-frequency strain meters, and a femtometer-scale pixelation of the cosmological bulk is not in their design band. This correction is stated because the natural first instinct — "point the gravitational-wave detectors at it" — points the wrong instruments.

### 6.3 What a detection would and would not mean

The exponent belongs to the entropy bound. The $1/3$ in $(l_p^2 R)^{1/3}$ is fixed by the dimensional mismatch between an area-bounded screen and a volume-filling interior [Bek73, Haw75] — by physics input (P1), not by the guard. The guard contributed discreteness (P2's premise) and nothing numeric. **The guard fixes no scale.** Any specific $L$ arises from *combining* the tick with a physical bound; the tick alone is scale-free, and a universe could run this grammar at any pixel size whatsoever. **[PROJECTION]**

So: a detected accumulation at this scale would support the projection — a discrete bulk at the area-entropy resolution — and would say nothing about the calculus, whose theorems would remain theorems either way. A non-detection at a given scale constrains the projection family there, and constrains the grammar not at all. We looked for a second handle and state its absence: the time-domain version of the same scaling gives $\delta t \approx 1.7\times10^{-23}\,$s over a cosmological baseline — ten orders below any timing instrument — so the angular channel is the only live one, which is why the literature uses it. The honest experimental content of this paper is therefore a double negative: *if* the grammar is spatialized *and* the screen bound is the right ledger, *then* the bulk's pixels are this size — and the instruments that test the first clause are already taking data: the $\alpha = 2/3$ blurring model is consistent with the brightest GRB yet observed [Stein23], while its generalized decoherence twin is excluded [Bort26]. The projection is not idle; it is being decided.

## 7. Conclusion

Physics keeps its two conservation facts as a postulate and a theorem about maps. The Care Calculus, mechanized and sorry-free in its guarded kernel, keeps them both as grammar: no well-formed process duplicates the linear token, and in the kernel no well-formed process destroys it. The asymmetry between the laws — kinematic, absolute; dynamical, conditional on the discard ban — reproduces, structurally, the asymmetry physics already knows. The adversarial calculus supplies the counterfactual physicists cannot build: a world where information loss is *derived* and the dynamics *provably never settle* — lossy, never a breeder, exactly inverting which laws fail first. The guarded tick and the duplicable boundary give the shape of structural holography — serialized exterior, conserved interior — without one meter of geometry claimed. And the one projection the grammar motivates, a femtometer-scale voxel for the observable bulk, comes with its falsifiers already named and its epicycles refused: the exponent is the entropy bound's, the scale is the projection's, and the theorems stand whatever the photons say.

In this reading, the dictionary's last row writes itself: physics is, possibly, the study of the well-typed sector. That sentence is a reading — the paper's largest **[INTERPRETATION]** and its smallest claim — and the calculus, which cannot leave its own grammar, would be the last to insist on it.

## Scope and limits

- **The bridge is a mirror, not a derivation.** §3.5 constructs a functor from the finitary fragment into $\mathbf{CPM}(\mathbf{FdHilb})$: it preserves processes, and the two laws' images are the categorical facts (no natural copying; no route to the trivial system that bypasses the trace). Functors do not reflect non-derivability — the grammar's no-go theorems are stronger than their denotations — and no bridge to spacetimes, or to the guarded fragment, is built.
- **The counting model is natural-number-valued.** It has no inner product, no amplitudes, no superposition, no probabilities. It prices processes; it does not linearize them. Anything quantum-mechanical in this paper arrives by interpretation (the dictionary of §2.4), by citation ([WZ82, PB00, AC04]), or — for the finitary fragment, as pure mathematics without empirical content — by the denotational construction of §3.5.
- **The calculus contains no geometry.** Its only temporal structure is the tick's ordering; its only spatial notion is the boundary/bulk separation of grammatical roles. All scales, distances, and areas in §6 are physics inputs to a projection.
- **The theorems constrain no experiment.** §6 is a projection with named instruments; a detection or a null result there touches the projection, never the grammar.
- **The mechanization is self-contained.** Every [MEASURED] voucher is a named `Dcare.*` declaration in the companion development [CCS], checked against Lean's standard three axioms (`propext`, `Classical.choice`, `Quot.sound`) with zero admitted axioms; the verification script in this artifact's `scripts/` confirms every cited name exists in the tree.

## References

- [WZ82] Wootters, W. K., & Zurek, W. H. (1982). A single quantum cannot be cloned. *Nature* 299, 802–803.
- [PB00] Pati, A. K., & Braunstein, S. L. (2000). Impossibility of deleting an unknown quantum state. *Nature* 404, 164–165.
- [AC04] Abramsky, S., & Coecke, B. (2004). A categorical semantics of quantum protocols. *Proc. LICS 2004*, 415–425.
- [Sel07] Selinger, P. (2007). Dagger compact closed categories and completely positive maps. *Electronic Notes in Theoretical Computer Science* 170, 139–163.
- [Wig59] Wigner, E. P. (1959). *Group Theory and Its Application to the Quantum Mechanics of Atomic Spectra.* Academic Press.
- [Gir87] Girard, J.-Y. (1987). Linear logic. *Theoretical Computer Science* 50(1), 1–101.
- [Wal04] Walker, D. (2004). Substructural type systems. In B. C. Pierce (ed.), *Advanced Topics in Types and Programming Languages*, MIT Press, 3–44.
- [Abr09] Abramsky, S. (2009). No-cloning in categorical quantum mechanics. In *Semantic Techniques in Quantum Computation*, Cambridge University Press, 1–28.
- [SV06] Selinger, P., & Valiron, B. (2006). A lambda calculus for quantum computation with classical control. *Mathematical Structures in Computer Science* 16(3), 527–552.
- [PRZ17] Paykin, J., Rand, R., & Zdancewic, S. (2017). QWIRE: a core language for quantum circuits. *Proc. POPL 2017*, PACMPL 1(POPL), 846–858.
- [BHL20] Bordg, A., Lachnitt, H., & He, Y. (2020). Certified quantum computation in Isabelle/HOL. *Journal of Automated Reasoning* 65, 691–709.
- [ILV26] Lamiroy, J., Valiron, B., & Vilmart, R. (2026). Intuitionistic unitary linear logic: a proof-theoretical approach to purely quantum higher-order. arXiv:2609.02661.
- [Lin99] Lindblad, G. (1999). A general no-cloning theorem. *Letters in Mathematical Physics* 47, 189–196.
- [BCJFS96] Barnum, H., Caves, C. M., Fuchs, C. A., Jozsa, R., & Schumacher, B. (1996). Noncommuting mixed states cannot be broadcast. *Physical Review Letters* 76, 2818–2821.
- [BBLW07] Barnum, H., Barrett, J., Leifer, M., & Wilce, A. (2007). A generalized no-broadcasting theorem. *Physical Review Letters* 99, 240501.
- [HHSS05] Horodecki, M., Horodecki, R., Sen(De), A., & Sen, U. (2005). Common origin of no-cloning and no-deleting principles: conservation of information. *Foundations of Physics* 35, 2041–2049.
- [Nak00] Nakano, H. (2000). A modality for recursion. *Proc. LICS 2000*.
- [AM13] Atkey, R., & McBride, C. (2013). Productive coprogramming with guarded recursion. *Proc. ICFP 2013*.
- [Bir12] Birkedal, L., Møgelberg, K. E., Schwinghammer, J., & Støvring, K. (2012). First steps in synthetic guarded domain theory. *Logical Methods in Computer Science* 8(4).
- [Whe55] Wheeler, J. A. (1955). Geons. *Physical Review* 97, 511–536.
- [Whe57] Wheeler, J. A. (1957). On the nature of quantum geometrodynamics. *Annals of Physics* 2, 604–614.
- [Whe83] Wheeler, J. A. (1983). Law without law. In Wheeler & Zurek (eds.), *Quantum Theory and Measurement*, Princeton University Press, 182–213.
- [Haw76] Hawking, S. W. (1976). Breakdown of predictability in gravitational collapse. *Physical Review D* 14, 2460–2473.
- [Haw82] Hawking, S. W. (1982). The unpredictability of quantum gravity. *Communications in Mathematical Physics* 87, 395–415.
- [EHNS84] Ellis, J., Hagelin, J. S., Nanopoulos, D. V., & Srednicki, M. (1984). Search for violations of quantum mechanics. *Nuclear Physics B* 241, 381–405.
- [Pen96] Penrose, R. (1996). On gravity's role in quantum state reduction. *General Relativity and Gravitation* 28, 581–600.
- [Page93] Page, D. N. (1993). Information in black hole radiation. *Physical Review Letters* 71, 3743–3746.
- [Haw05] Hawking, S. W. (2005). Information loss in black holes. *Physical Review D* 72, 084013.
- [Carlip23] Carlip, S. (2023). Spacetime foam: a review. *Reports on Progress in Physics* 86, 066001.
- [BPS84] Banks, T., Susskind, L., & Peskin, M. E. (1984). Difficulties for the evolution of pure states into mixed states. *Nuclear Physics B* 244, 125–134.
- [CJ19] Cotler, J., & Jensen, K. (2021). Emergent unitarity in de Sitter from matrix integrals. *Journal of High Energy Physics* 12, 089.
- [Smo92] Smolin, L. (1992). Did the universe evolve? *Classical and Quantum Gravity* 9, 173–192.
- [Smo06] Smolin, L. (2006). The status of cosmological natural selection. arXiv:hep-th/0612185.
- [Car74] Carter, B. (1974). Large number coincidences and the anthropic principle in cosmology. *IAU Symposium 63*, 291–298.
- [Bek73] Bekenstein, J. D. (1973). Black holes and entropy. *Physical Review D* 7, 2333–2346.
- [Haw75] Hawking, S. W. (1975). Particle creation by black holes. *Communications in Mathematical Physics* 43, 199–220.
- [tHooft93] 't Hooft, G. (1993). Dimensional reduction in quantum gravity. *Conf. Proc. C* 930308, 284; arXiv:gr-qc/9310026.
- [Suss95] Susskind, L. (1995). The world as a hologram. *Journal of Mathematical Physics* 36, 6377–6396.
- [Kar66] Károlyházy, F. (1966). Gravitation and quantum mechanics of macroscopic objects. *Nuovo Cimento A* 42, 390.
- [NgdV94] Ng, Y. J., & van Dam, H. (1994). Limit to space-time measurement. *Modern Physics Letters A* 9, 335.
- [NgdV00] Ng, Y. J., & van Dam, H. (2000). Measuring the foaminess of space-time with gravity-wave interferometers. *Foundations of Physics* 30, 795.
- [Ng03] Ng, Y. J. (2003). Selected topics in Planck-scale physics. *Modern Physics Letters A* 18, 1073.
- [Hog12] Hogan, C. J. (2012). Interferometers as probes of Planckian quantum geometry. *Physical Review D* 85, 064007.
- [Chou16] Chou, A. S., et al. (2016). First measurements of high frequency cross-spectra from a pair of large Michelson interferometers. *Physical Review Letters* 117, 111102.
- [Stein15] Steinbring, E. (2015). Detectability of Planck-scale-induced blurring with gamma-ray bursts. *Astrophysical Journal* 802, 38.
- [Rag03] Ragazzoni, R., Turatto, M., & Gaessler, W. (2003). The lack of observational evidence for the quantum structure of spacetime at Planck scales. *Astrophysical Journal Letters* 587, L1–L4.
- [Perlman14] Perlman, E., Ng, Y. J., et al. (2014). New constraints on quantum foam models from X-ray and gamma-ray observations. arXiv:1411.7262; proc. 14th Marcel Grossmann Meeting (2017), 3935–3941.
- [NgP22] Ng, Y. J., & Perlman, E. (2022). Probing spacetime foam with extragalactic sources of high-energy photons. *Universe* 8(7), 382.
- [Lieu03] Lieu, R., & Hillman, L. W. (2003). The phase coherence of light from extragalactic sources: direct evidence against first-order Planck-scale fluctuations in time and space. *Astrophysical Journal Letters* 585, L77–L80.
- [Stein23] Steinbring, E. (2023). Holographic quantum-foam blurring is consistent with observations of gamma-ray burst GRB 221009A. *Galaxies* 11, 115.
- [Bort26] Bortolotti, N., Piscicchia, K., Porcelli, A., Laubenstein, M., Manti, S., Marcianò, A., Nola, F., & Curceanu, C. (2026). Experimental exclusion of a generalized Károlyházy gravity-induced decoherence model. *New Journal of Physics* 28, 064511.
- [CCS] *The Care Calculus: A Mechanized Linear Type Theory for Safe Agents.* Companion mechanization and paper (in preparation; in-tree as the dcare artifact).
- [CCS-sim] *channel-sim* — the companion simulator: the bridge's clause dictionary, executable, with its corpora checks. Program artifact (in-tree).
- [GS] *The Guarded Syntax: A Notation for Linear Resource Calculi.* Program artifact (in-tree as the notation artifact).
- [GL] *The Guarded Line: What Metacircular Proof Theory and Self-Model Dynamics Share.* Program artifact (in-tree as the isomorphism artifact).
