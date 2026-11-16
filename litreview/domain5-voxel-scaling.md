# Domain 5 — the (l_p²R)^{1/3} voxel scaling: provenance and experimental status

Scout memo for `physical-iso/paper.md` §6.1–§6.2. Evidence tags: **[FETCHED]** = metadata or
source text retrieved over the network this session (arXiv e-print, INSPIRE-HEP API, Crossref API);
**[MEMORY]** = recalled, not verified this session; **[NONE]** = searched, found nothing.
No identifier below is invented: every arXiv ID, DOI, volume and page came out of a fetch.

Network note: `export.arxiv.org/api` rate-limited (HTTP 429) for most of the session; `arxiv.org`
e-print tarballs and the INSPIRE-HEP and Crossref APIs stayed up, so primary-source reading was done
from **arXiv LaTeX sources**, which is stronger than abstracts. Two arXiv **API** searches only
("holographic quantum foam", "pixelation"/"spacetime", "voxel"/"holographic principle",
"cube root"/"holographic") succeeded; the rest were done through INSPIRE fulltext/metadata.

---

## Direct answer

### The provenance chain of the 1/3 exponent

The exponent has **one formula and two independent origins**, and the paper's specific route is the
*second* one.

1. **Károlyházy 1966** — the formula's first appearance. **Kar66** [FETCHED: INSPIRE record 50430;
Crossref DOI record]. He combined Heisenberg's uncertainty relation with the requirement that the
clock not be its own black hole and obtained, in the modern restatement, `Δs³ = l_p² s`
[FETCHED verbatim from Figurato–Bassi–Donadi 2024, eq. (1) and its footnote reproducing Károlyházy's
Eq. (3.1)] — i.e. `Δs = (l_p² s)^{1/3}`. Károlyházy's own abstract [FETCHED] says it exactly this
way: *"by combining Heisenberg's uncertainty relations with gravitation, quantitative limitations on
the sharpness of the structure of space-time are derived."* His purpose was wave-function reduction,
not holography.

2. **Ng & van Dam 1994** — the same relation, derived independently, and stated as a power law:
   *"The intrinsic uncertainty of a length is shown to be proportional to the one third power of the
   length itself"* [FETCHED, INSPIRE record 359304 abstract]. **NgdV94**. Their 2000 paper says of
   Károlyházy: *"Our derivation was completely independent of Karolyhazy's work. Besides, his
   interpretation of the result differs somewhat from ours."* [FETCHED verbatim, `gr-qc/9906003`
   source, `\bibitem{karol}`].

3. **The holographic counting route — this is the paper's move, and it is published.** Two places,
   in both directions of implication:

   - **Ng & van Dam 2000**, Found. Phys. 30, 795, §(v) **[FETCHED verbatim from `gr-qc/9906003`
     source]**: *"consider a region of space with linear dimension l. According to the conventional
     wisdom, the region can be partitioned into cubes as small as l_P³ ... But according to our
     spacetime foam picture, the smallest cubes inside that region have a linear dimension of order
     (l l_P²)^{1/3}. Accordingly, the number of degrees of freedom of the region is bounded by
     [l/(l l_P²)^{1/3}]³, i.e., the area of the region in Planck units, as stipulated by the
     holographic principle."* Direction here: foam ⇒ holography.

   - **Ng 2003**, Mod. Phys. Lett. A 18, 1073, §II **[FETCHED verbatim from `gr-qc/0305019` source]**:
     *"One can also derive the δl result by appealing to the holographic principle ... Consider a
     region of space measuring l × l × l, and imagine partitioning it into cubes as small as physical
     laws allow. With each small cube we associate one degree of freedom ... Thus the maximum number
     of degrees of freedom ... is (l/δl)³. It follows from the holographic principle that
     (l/δl)³ ≲ (l/l_P)², which yields precisely the same expression for spacetime fluctuation δl
     given by Eq. (nvd1)"*, where Eq. (nvd1) is `δl ≳ (l l_P²)^{1/3}`. Direction here: holography ⇒
     foam. **This is the paper's §6.1 argument, algebra for algebra, including the one-dof-per-cube
     premise.**

4. **The number is also published.** Ng 2003, same paper [FETCHED verbatim]: *"even on the size of
   the whole observable universe (~10¹⁰ light-years), Eq. (genfluct1) yields a fluctuation of only
   about 10⁻³³ cm, 10⁻¹³ cm, and 10⁻² cm for α = 1, 2/3 and 1/2 respectively."* The α = 2/3 entry —
   the holographic branch — is **10⁻¹³ cm = 10⁻¹⁵ m**, which is the paper's "nuclear-sized voxel",
   5×10⁻¹⁵ m, to the same order. Independently checkable: (l_p²R)^{1/3} with
   l_p = 1.616×10⁻³⁵ m, R = 4.4×10²⁶ m gives 4.8×10⁻¹⁵ m.

5. **Independent re-derivations.** **Sas99** (Sasakura 1999, Prog. Theor. Phys. 102, 169) — cited by
   Ng & van Dam 2000 as "a very different way to obtain this result" [FETCHED, `\bibitem{karol}`].
   **DL89** (Diósi & Lukács 1989) and **AC94** (Amelino-Camelia 1994) are the *other* branch:
   Ng 2003 [FETCHED verbatim] says *"α = 1/2 corresponds to the random-walk model found in the
   literature [AC, dio89]"*. `√(l_p l)`, not `(l_p² l)^{1/3}`.

6. **The premise.** **tHooft93** (dimensional reduction) and **Suss95** (holography for any region)
   supply P1's area-bounded screen; both are already in the Ng 2025 review's reference list
   [FETCHED, INSPIRE record 3071893 reference field].

### Terminology: this is Ng's "holography model", α = 2/3

The whole family is parametrised by a single exponent: `δl ~ l_p^{1-α} l^α` with α = 1 (metric
fluctuation), **α = 2/3 (holographic counting — ours)**, α = 1/2 (random walk). Ng 2003 [FETCHED
verbatim]: *"The standard choice of α is α = 1; the choice of α = 2/3 discussed above appears to be
consistent with the holographic principle and black hole physics and will be called the holography
model."* The paper's §6.1 sentence — "the cleanest member of the 3D accumulation family" — is
correct, and the family has a name and an owner.

### Current experimental status

Six distinct channels; only one of them tests the α = 2/3 branch, and it tests it *angulary*, not by
timing.

| channel | observable | status for the α = 2/3 branch | key citation |
|---|---|---|---|
| **angular blurring** of distant point sources | foam accumulates in a wavefront over path R and widens the image; for α = 2/3 the effect is real but mild | **live and the only positive-leaning channel**: Steinbring 2023 finds GRB 221009A's angular-resolution data **consistent with** holographic (α = 2/3) blurring, with a limiting bound ~1°; earlier GRB and quasar work set limits | **Stein23**, **Stein15**, **NgStein25**, **SteinNg26** |
| **decoherence** (Károlyházy model) | gravity-induced loss of coherence | **the model has just been experimentally excluded in its generalized form** (2026) | **Fig24**, **Bort26** |
| **correlated interferometry** (Holometer) | transverse shear noise `√(l_pL)`, i.e. the α = 1/2 branch | **null**: the specific model excluded at 5.1σ (4.6σ with calibration), or normalisation < 44 % of prediction at 95 % CL — and the paper says the exclusion is *"only to the spectral shape of the particular model used here"* [FETCHED verbatim, `1512.01216` source] | **Hog12**, **Hol16** |
| **photon dispersion / arrival timing** | linear or quadratic Lorentz violation | **strongly constrained, but this is not our family** — see the correction below | **VPF13** |
| **UHECR / cosmic-ray** | same family, different messenger | limits only [MEMORY: no fetch] | — |
| **quasar/X-ray blurring** | same as row 1, other band | limits set | Ng, Christiansen & van Dam 2003 ApJ 591 L87 [FETCHED via Ng 2025 reference list] |

**The one thing the paper must not say.** `[VPF13]` in `citations.md` is *"Limits on spacetime
quantum 'foam' models from observations of GRB 090510"* — **no such paper exists** [NONE: Crossref
and INSPIRE both resolve the actual PRD 87, 122001 (2013) to a different title]. The real paper is
**Vasileiou et al. 2013, "Constraints on Lorentz invariance violation from Fermi-Large Area Telescope
observations of gamma-ray bursts", PRD 87, 122001, DOI 10.1103/PhysRevD.87.122001** [FETCHED,
Crossref DOI record]. It constrains **vacuum dispersion** (linear/quadratic LV), not voxel
accumulation. §6.2 currently uses it as the citation for "*Planck-scale accumulation models are
already constrained*" — that claim is not supported by that paper. (An independent scout in this tree
found the same thing for domain 1; two searches, same answer.)

---

## Closest precedents

Full citations, what each actually derived, and the exact route.

### Tier 1 — same formula, same route (the paper's own derivation is here)

**Kar66** — Károlyházy, F. (1966). *Gravitation and quantum mechanics of macroscopic objects.*
Nuovo Cimento A **42**, 390. DOI 10.1007/BF02717926. [FETCHED]
Derived `Δs³ = l_p²s` from Heisenberg + the no-black-hole constraint on the clock's mass.
Route: **measurement gedanken experiment**. Not holographic; not a bulk discretisation.
Caveat worth knowing: the original Eq. (3.1) has a **known typo** — the power on `s` is printed 3/2
instead of 2/3 [FETCHED verbatim from Figurato–Bassi–Donadi 2024 footnote 1, which also says it does
not propagate]. Anyone quoting Károlyházy from the original should say so.

**NgdV94** — Ng, Y. J., & van Dam, H. (1994). *Limit to space-time measurement.* Mod. Phys. Lett. A
**9**, 335. DOI 10.1142/S0217732394000356. [FETCHED]
Same exponent, independent route (Salecker–Wigner clock + Schwarzschild), stated as "proportional to
the one third power of the length itself".

**NgdV00** — Ng, Y. J., & van Dam, H. (2000). *Measuring the foaminess of space-time with
gravity-wave interferometers.* Found. Phys. **30**, 795. DOI 10.1023/A:1003745212871;
arXiv:gr-qc/9906003. [FETCHED, source read]
Contains **both** the gedanken derivation (Eq. 2, `δl ≳ (l l_P²)^{1/3}`) **and** §(v)'s cube-counting
passage quoted above. `(l/δl)³ ≲ (l/l_P)²` appears here first, in the foam ⇒ holography direction.
The existing `citations.md` title for this row — *"Measuring the foaminess of space-time: foundation
and interpretation"* — **is not this paper's title**; the fetched title is *"...with gravity-wave
interferometers"*.

**Ng03** — Ng, Y. J. (2003). *Selected topics in Planck-scale physics.* Mod. Phys. Lett. A **18**,
1073. DOI 10.1142/S0217732303010934; arXiv:gr-qc/0305019. [FETCHED, source read]
**The closest precedent to §6.1 as written**: holography ⇒ partition into minimal cubes ⇒ one dof per
cube ⇒ `(l/δl)³ ≤ (l/l_P)²` ⇒ `δl ≳ (l l_P²)^{1/3}`, plus the α = 2/3 number 10⁻¹³ cm at the
observable-universe scale. It is a review, not a paper *about* the derivation — which is the only
space the paper has left.

**Sas99** — Sasakura, N. (1999). *An uncertainty relation of space-time.* Prog. Theor. Phys. **102**,
169–179. DOI 10.1143/PTP.102.169. [FETCHED] Independent route; cited as such by Ng & van Dam 2000.

### Tier 2 — the other exponent, and why the naming is a trap

**DL89** — Diósi, L., & Lukács, B. (1989). *On the minimum uncertainty of space-time geodesics.*
Phys. Lett. A **142**, 331. DOI 10.1016/0375-9601(89)90375-7. [FETCHED] `α = 1/2` branch.

**AC94** — Amelino-Camelia, G. (1994). *Limits on the measurability of space-time distances in (the
semiclassical approximation of) quantum gravity.* Mod. Phys. Lett. A **9**, 3415–3422.
DOI 10.1142/S0217732394003245. [FETCHED; Crossref abstract does not state the exponent — its
placement in the α = 1/2 branch is Ng 2003's classification, quoted above, not a reading of AC's own
text]

**Hog12** — Hogan, C. J. (2012). *Interferometers as probes of Planckian quantum geometry.*
Phys. Rev. D **85**, 064007. DOI 10.1103/PhysRevD.85.064007; arXiv:1002.4880. [FETCHED, source read]
Predicts *transverse* holographic noise `Δx ≈ √(ct_P L)` [FETCHED verbatim: *"Transverse positions of
trajectories separated by distance L appear to fluctuate by amount Δx ≈ √(ct_PL)"*], from a
**noncommuting-position** theory, explicitly *not* a fluctuating metric [FETCHED: *"not describable
as fluctuations of a quantized metric, or as any kind of fluctuation, dispersion or propagation effect
in quantum fields"*].
**Two corrections to the existing rows.** (i) There is no CQG **29**, 195012 by Hogan [NONE: fetched
CQG v29 2012 listings show 195012 not present in the holographic-noise family; the real record is PRD
85, 064007]. (ii) The paper's framing — "the screen constrains *transverse* position only ... Hogan's
holographic-noise scaling" — puts Hogan in the α = 1/2 slot that Ng's review calls the **random-walk**
model. Both are defensible (Hogan's own word is "holographic"), but the paper is using the same
adjective for two different exponents, and a referee in this field will notice.

**Hol16** — Chou, A. S., Gustafson, R., Hogan, C., Kamai, B., Kwon, O., Lanza, R., McCuller, L.,
Meyer, S. S., Richardson, J., Stoughton, C., Tomlin, R., Waldman, S., & Weiss, R. (2016). *First
measurements of high frequency cross-spectra from a pair of large Michelson interferometers.*
Phys. Rev. Lett. **117**, 111102. DOI 10.1103/PhysRevLett.117.111102; arXiv:1512.01216. [FETCHED,
source read] The null result §6.2 leans on: *"The model of Eq. (E:holo_model) is thus excluded with
5.1σ statistical significance, reduced by the 10 % calibration uncertainty to 4.6σ. Alternatively ...
a constraint on the normalization of this model to be less than 44 % of the predicted value at 95 %
confidence level."* Instrument paper (not the null result): Chou et al., Class. Quantum Grav. **34**,
065005 (2017), DOI 10.1088/1361-6382/aa5e5c [FETCHED].

### Tier 3 — the holographic premise and the review of record

**tHooft93** — 't Hooft, G. (1993). *Dimensional reduction in quantum gravity.* Conf. Proc. C **930308**,
284. arXiv:gr-qc/9310026. [FETCHED]
**Suss95** — Susskind, L. (1995). *The world as a hologram.* J. Math. Phys. **36**, 6377–6396.
DOI 10.1063/1.531249. [FETCHED]
**Bek73** — Bekenstein, J. D. (1973). *Black holes and entropy.* Phys. Rev. D **7**, 2333–2346.
DOI 10.1103/PhysRevD.7.2333. [FETCHED, Crossref DOI record]
**Haw75** — Hawking, S. W. (1975). *Particle creation by black holes.* Commun. Math. Phys. **43**,
199–220. DOI 10.1007/BF02345020. [FETCHED, Crossref DOI record]
These are the paper's P1. They are correct as cited; only their status label (`needs-human`) is stale.

**NgStein25** — Ng, Y. J., & Steinbring, E. (2025). *Holographic quantum foam: from theory to
observations.* Int. J. Mod. Phys. D **34**, 2544018. DOI 10.1142/S0218271825440183. [FETCHED]
This is the **review of record** for the whole program, and its abstract states the program's own
summary: *"distance uncertainty scaling as the cube root of distances, consistent with the holographic
principle — hence the name 'Holographic Quantum Foam'."* Its 49-entry reference list is the cleanest
single provenance source I found, and I used it as a cross-check on every Tier-1 row above.

### Tier 4 — the GRB constraint line the brief was reaching for

**Stein15** — Steinbring, E. (2015). *Detectability of Planck-scale-induced blurring with gamma-ray
bursts.* Astrophys. J. **802**, 38. DOI 10.1088/0004-637X/802/1/38; arXiv:1502.03745. [FETCHED]
**Stein23** — Steinbring, E. (2023). *Holographic quantum-foam blurring is consistent with
observations of gamma-ray burst GRB221009A.* Galaxies **11**, 115. DOI 10.3390/galaxies11060115.
[FETCHED] Its abstract [FETCHED]: *"it fits all GRB angular-resolution data of 10 MeV or any lesser
peak energy and can still be consistent with the highest-energy localization of GRB221009A: a limiting
bound of about 1 degree is in agreement with a holographic QG-favored formulation."* Its model
parameter is explicit [FETCHED, `2311.10168` source]: *"α specifying the quantum gravity (QG) model,
1/2 implies a random walk and 2/3 is consistent with the holographic principle"* — i.e. **the paper's
own α = 2/3 scaling, constrained against real GRB data.**
**SteinNg26** — Steinbring, E., & Ng, Y. J. (2026). *Holographic quantum foam: theoretical
underpinnings and observational evidence.* PoS CORFU2025, 205. DOI 10.22323/1.509.0205;
arXiv:2603.18277. [FETCHED] Latest status; presents the HQF-widened PSF for real telescopes.

**Fig24** — Figurato, L., Bassi, A., & Donadi, S. (2024). *On the testability of the Károlyházy
model.* New J. Phys. **26**, 013001. DOI 10.1088/1367-2630/ad1499; arXiv:2306.10094. [FETCHED,
source read] Restates `Δs³ = l_p²s` and works out what a test would require.
**Bort26** — Bortolotti, N., Piscicchia, K., Porcelli, A., Laubenstein, M., Manti, S., Marcianò, A.,
Nola, F., & Curceanu, C. (2026). *Experimental exclusion of a generalized Károlyházy gravity-induced
decoherence model.* New J. Phys. **28**, 064511. DOI 10.1088/1367-2630/ae774c; arXiv:2601.00651.
[FETCHED] Abstract [FETCHED]: *"We obtain a bound R_K > 4.64 m (95 % C.L.) ... When combined with the
theoretical upper bound R_K < 1.98 m derived from macroscopic localization requirements, our result
excludes the generalized Károlyházy model."* **This is the sharpest current experimental statement
against the α = 2/3 formula's original home.** It excludes a *generalized* parameterisation via the
decoherence channel; it is not a statement about cosmological wavefront accumulation, and the paper
should not over- or under-read it.

### Searched, not found

- **"Palmer & Branziero" / "Palmer Branziero holographic"** — the brief's lead (3). **Nothing**
  [NONE: Crossref `query.bibliographic=Branziero` → 0 rows; Crossref and INSPIRE for
  Palmer + holographic foam → only Ng's own papers and Steinbring 2023]. I believe the lead is a
  conflation, and that the paper actually being recalled is **Stein23** (Steinbring 2023, GRB221009A,
  α = 2/3 holographic blurring) or **SteinNg26**. Flagged for a human, not silently substituted.
- **"voxel" + "holographic principle"** in any arXiv abstract — **0 hits** [FETCHED].
- **"pixelation" + "spacetime"** — 15 hits, all black-hole imaging / radiative-transfer / EHT / ML
  [FETCHED]; nothing on foam discretisation.
- **"MIP-map"** + holographic — **0 hits** [FETCHED, INSPIRE fulltext].
- Someone deriving the *bulk lattice spacing* from the Bekenstein bound **earlier than Ng & van Dam
  2000** — not found. Károlyházy 1966's route is a measurement gedanken, not a counting argument, so
  on present evidence the counting route starts with **NgdV00 §(v)**.

---

## Novelty verdict

**PRECEDED.**

For the *physics* the paper states — "the interior cannot carry more cells than the screen carries
bits, so `(R/L)³ ≲ πR²/l_p²` and `L ≳ (l_p²R)^{1/3}`" — this is the **same derivation, with the same
premise and the same algebra, published twice**: Ng & van Dam 2000 §(v) [FETCHED verbatim] and Ng 2003
§II [FETCHED verbatim]. The number that comes out (10⁻¹³ cm ≈ 10⁻¹⁵ m at the observable-universe
scale) is also published [Ng 2003, FETCHED verbatim]. The formula itself is older than either
(Károlyházy 1966; Ng & van Dam 1994).

What is **not** preceded, and is the paper's actual contribution:

1. **The framing.** Nowhere in the foam literature is this the *projection of a discrete tick of a
   grammar*. Ng's α = 2/3 is a statement about metric fluctuations; the paper's is a statement about
   what a spatialised tick would have to look like if it met a Bekenstein screen. That is a claim
   about the calculus, not about the vacuum, and no physics paper makes it.
2. **The vocabulary.** "voxel", "MIP-map", "one bit per screen pixel" appear nowhere in this
   literature [NONE: three independent searches]. It is a genuinely clearer metaphor than "small
   cubes as small as physical laws allow" — but it is a metaphor, and the paper's own §6.3 already
   says the honest thing about it.
3. **The negative half.** The paper's §6.3 claim — *the exponent belongs to the entropy bound; the
   guard fixes no scale* — is **stronger and more careful than anything in the precedent**. Ng 2003
   says "the holographic principle has its origin in the quantum fluctuations of spacetime", i.e. he
   reads the coincidence as evidence *for* the foam picture. The paper reads it as a constraint on
   what a grammar can be made to say. That is the one sentence here with no ancestor.

**What this means for the manuscript.** §6.1's existing hedge — "The scaling is not new to this
paper — it is the cleanest member of the 3D accumulation family" — is **correct and confirmed**. The
fix is not to weaken the hedge; it is to **name the family**: it is Ng's holography model, α = 2/3,
and the derivation route is Ng & van Dam 2000 / Ng 2003. As written, the paper cites `[NdV03]` for
this and `[NdV03]` is the wrong paper title (see the table). A referee who works in this area will
recognise the derivation in one reading; citing it costs one sentence and converts a vulnerability
into a credential.

---

## Proposed citation rows

Format is `citations.md`'s own: key | used in | claim it carries | full citation | status.
Statuses use the ledger's existing vocabulary; everything below is Crossref/INSPIRE-verified, so
`verified (INSPIRE/Crossref, 2026-11-16)` is proposed as an available status value.

| key | used in | claim it carries | full citation | status |
|---|---|---|---|---|
| Kar66 | §6.1 | The cube-root distance uncertainty from Heisenberg + the clock's Schwarzschild bound: `Δs³ = l_p² s`; the formula's first appearance | Károlyházy, F. (1966). *Gravitation and quantum mechanics of macroscopic objects.* Nuovo Cimento A **42**, 390. DOI 10.1007/BF02717926 | verified (INSPIRE 50430 + Crossref); note the printed 3/2 power in his Eq. (3.1) is a typo for 2/3 |
| NgdV94 | §6.1 | Independent derivation (Salecker–Wigner clock) that the length uncertainty is "proportional to the one third power of the length itself" | Ng, Y. J., & van Dam, H. (1994). *Limit to space-time measurement.* Mod. Phys. Lett. A **9**, 335. DOI 10.1142/S0217732394000356 | verified (INSPIRE 359304 + Crossref) |
| NgdV00 | §6.1 | The cube-counting route: partition a region into minimal cubes, one dof each, `(l/δl)³ ≲ (l/l_P)²`, and read it as the holographic bound's origin in spacetime fluctuations | Ng, Y. J., & van Dam, H. (2000). *Measuring the foaminess of space-time with gravity-wave interferometers.* Found. Phys. **30**, 795. DOI 10.1023/A:1003745212871; arXiv:gr-qc/9906003 | verified (source read, `\bibitem{karol}` chain confirmed) — REPLACES the existing NdV03 row, whose title is wrong |
| Ng03 | §6.1, §6.3 | The derivation in the paper's own direction (holography ⇒ minimal cubes ⇒ `δl ≳ (l l_P²)^{1/3}`), and the α = 2/3 number 10⁻¹³ cm at the observable-universe scale | Ng, Y. J. (2003). *Selected topics in Planck-scale physics.* Mod. Phys. Lett. A **18**, 1073. DOI 10.1142/S0217732303010934; arXiv:gr-qc/0305019 | verified (source read; both passages quoted verbatim above) |
| Sas99 | §6.1 | An independent derivation of a cube-root space-time uncertainty relation | Sasakura, N. (1999). *An uncertainty relation of space-time.* Prog. Theor. Phys. **102**, 169–179. DOI 10.1143/PTP.102.169 | verified (Crossref DOI record) |
| tHooft93 | §6.1 | The holographic/dimensional-reduction premise: bulk degrees of freedom encoded on the boundary | 't Hooft, G. (1993). *Dimensional reduction in quantum gravity.* Conf. Proc. C **930308**, 284. arXiv:gr-qc/9310026 | verified (INSPIRE 36137) |
| Suss95 | §6.1 | The area bound generalised from horizons to arbitrary regions | Susskind, L. (1995). *The world as a hologram.* J. Math. Phys. **36**, 6377–6396. DOI 10.1063/1.531249 | verified (Crossref DOI record) |
| DL89 | §6.2 | The α = 1/2 random-walk branch of the same family (as classified by Ng 2003) | Diósi, L., & Lukács, B. (1989). *On the minimum uncertainty of space-time geodesics.* Phys. Lett. A **142**, 331. DOI 10.1016/0375-9601(89)90375-7 | verified (INSPIRE 283181) |
| AC94 | §6.2 | The other α = 1/2 reference in Ng's classification of the family | Amelino-Camelia, G. (1994). *Limits on the measurability of space-time distances in (the semiclassical approximation of) quantum gravity.* Mod. Phys. Lett. A **9**, 3415–3422. DOI 10.1142/S0217732394003245 | verified (Crossref DOI record); the exponent is NOT in its abstract — the α = 1/2 assignment is Ng 2003's |
| Hog12 | §6.2 | Transverse holographic noise `Δx ≈ √(ct_P L)` from noncommuting position — predicts MHz-band shear, and is the α = 1/2 branch in Ng's classification | Hogan, C. J. (2012). *Interferometers as probes of Planckian quantum geometry.* Phys. Rev. D **85**, 064007. DOI 10.1103/PhysRevD.85.064007; arXiv:1002.4880 | verified (source read) — CORRECTS the existing Hog12 row: no CQG 29, 195012 exists; title and journal are both wrong |
| Hol16 | §6.2 | The Holometer null: the Hogan transverse-shear model excluded at 5.1σ (4.6σ with calibration), equivalently normalisation < 44 % of prediction at 95 % CL; applies only to that model's spectral shape | Chou, A. S., Gustafson, R., Hogan, C., Kamai, B., Kwon, O., Lanza, R., McCuller, L., Meyer, S. S., Richardson, J., Stoughton, C., Tomlin, R., Waldman, S., & Weiss, R. (2016). *First measurements of high frequency cross-spectra from a pair of large Michelson interferometers.* Phys. Rev. Lett. **117**, 111102. DOI 10.1103/PhysRevLett.117.111102; arXiv:1512.01216 | verified (source read) — REPLACES the existing Hol16 row (no author list, no journal, no year, claim vague) |
| Chou17 | §6.2 | The instrument paper: pair of 39 m Michelson interferometers, 3.8 MHz light-crossing | Chou, A., Glass, H., Gustafson, H. R., Hogan, C., Kamai, B. L., Kwon, O., Lanza, R., McCuller, L., Meyer, S. S., Richardson, J., Stoughton, C., Tomlin, R., & Weiss, R. (2017). *The Holometer: an instrument to probe Planckian quantum geometry.* Class. Quantum Grav. **34**, 065005. DOI 10.1088/1361-6382/aa5e5c; arXiv:1611.08265 | verified (INSPIRE 1500264) |
| Stein15 | §6.2 | GRB image blurring as the observational channel for α = 2/3 foam, and what it would take to detect | Steinbring, E. (2015). *Detectability of Planck-scale-induced blurring with gamma-ray bursts.* Astrophys. J. **802**, 38. DOI 10.1088/0004-637X/802/1/38; arXiv:1502.03745 | verified (INSPIRE 1344191) |
| Stein23 | §6.2, §6.3 | GRB 221009A angular data are CONSISTENT with holographic (α = 2/3) foam blurring; limiting bound ~1° | Steinbring, E. (2023). *Holographic quantum-foam blurring is consistent with observations of gamma-ray burst GRB221009A.* Galaxies **11**, 115. DOI 10.3390/galaxies11060115 | verified (abstract + source read) |
| NgStein25 | §6.2 | The program's own review: distance uncertainty scales as the cube root of distance, consistently with the holographic principle | Ng, Y. J., & Steinbring, E. (2025). *Holographic quantum foam: from theory to observations.* Int. J. Mod. Phys. D **34**, 2544018. DOI 10.1142/S0218271825440183 | verified (INSPIRE 3071893; 49-ref list read) |
| SteinNg26 | §6.2 | Current status: the HQF-widened PSF computed for real instruments, consistent with GRB 221009A | Steinbring, E., & Ng, Y. J. (2026). *Holographic quantum foam: theoretical underpinnings and observational evidence.* PoS CORFU2025, 205. DOI 10.22323/1.509.0205; arXiv:2603.18277 | verified (INSPIRE 3131558) |
| Fig24 | §6.2, §6.3 | Testability of the Károlyházy model via gravity-induced decoherence; restates `Δs³ = l_p²s` | Figurato, L., Bassi, A., & Donadi, S. (2024). *On the testability of the Károlyházy model.* New J. Phys. **26**, 013001. DOI 10.1088/1367-2630/ad1499; arXiv:2306.10094 | verified (source read) |
| Bort26 | §6.2, §6.3 | Experimental EXCLUSION of the generalized Károlyházy model: `R_K > 4.64 m` (95 % CL) against the theoretical `R_K < 1.98 m` | Bortolotti, N., Piscicchia, K., Porcelli, A., Laubenstein, M., Manti, S., Marcianò, A., Nola, F., & Curceanu, C. (2026). *Experimental exclusion of a generalized Károlyházy gravity-induced decoherence model.* New J. Phys. **28**, 064511. DOI 10.1088/1367-2630/ae774c; arXiv:2601.00651 | verified (INSPIRE 3096950) |
| VPF13 | §6.2 | **CORRECTED CLAIM**: constrains Lorentz invariance violation (linear and quadratic vacuum dispersion) from Fermi-LAT GRB observations — it does NOT constrain the `(l_p²R)^{1/3}` voxel family | Vasileiou, V., Jacholkowska, A., Piron, F., Bolmont, J., Couturier, C., Granot, J., Stecker, F. W., Cohen-Tanugi, J., & Longo, F. (2013). *Constraints on Lorentz invariance violation from Fermi-Large Area Telescope observations of gamma-ray bursts.* Phys. Rev. D **87**, 122001. DOI 10.1103/PhysRevD.87.122001 | verified (Crossref DOI record) — the existing row's TITLE DOES NOT EXIST and its claim is not supported |
| Bek73 | §6.1 | The area law `S = A/4l_p²` — the screen bound of P1 | Bekenstein, J. D. (1973). *Black holes and entropy.* Phys. Rev. D **7**, 2333–2346. DOI 10.1103/PhysRevD.7.2333 | verified (Crossref DOI record) — upgrades the existing row from needs-human |
| Haw75 | §6.1 | The same area law from black-body radiation — the screen bound of P1 | Hawking, S. W. (1975). *Particle creation by black holes.* Commun. Math. Phys. **43**, 199–220. DOI 10.1007/BF02345020 | verified (Crossref DOI record) — upgrades the existing row from needs-human |
| NCvD03 | §6.2 | Extragalactic point sources as the α = 2/3 probe; first observational limits in this program | Ng, Y. J., Christiansen, W. A., & van Dam, H. (2003). *Probing Planck-scale physics with extragalactic sources?* Astrophys. J. **591**, L87. | verified as a citation (present in Ng & Steinbring 2025's reference list, INSPIRE 3071893) — DOI and page range not fetched; needs-human for the DOI |

Keys **retired**: `NdV03` (title does not exist; split into `NgdV94` + `NgdV00`). Keys **re-keyed**:
`Hog12` and `Hol16` keep their keys but need the corrected data. No `Pal26` row: that paper could not
be found.

---

## What a human should still check

1. **Read Károlyházy 1966 in the original** (Nuovo Cim. A 42, 390 — paywalled; I have only the
   abstract and the two modern restatements). Confirm that the relation printed there is `Δs³ ∝ l_p²s`
   and that the 3/2-vs-2/3 discrepancy really is a typo and not a different relation. Figurato et al.
   say it is a typo, which is why the second-order source is trustworthy, but "trustworthy secondary"
   is not "read it".
2. **Decide the attribution sentence.** The recommendation is Ng 2003 + Ng & van Dam 2000 as the
   route, Károlyházy 1966 and Ng & van Dam 1994 as the formula's origins, and the α = 2/3 name
   ("the holography model") as the family's. If the human prefers a lighter touch, the minimum is one
   clause naming Ng — but §6.1 must not read as if the counting argument is the paper's.
3. **Decide whether to keep "Hogan's holographic-noise" for the `√(l_pR)` branch.** It is Hogan's own
   word, but Ng calls the same exponent the *random-walk* model, and the paper calls `(l_p²R)^{1/3}`
   "holographic" too. One adjective, two exponents, one footnote would fix it.
4. **The `[VPF13]` correction is a claim-level change, not a citation-data change.** §6.2's sentence
   "exactly the channel in which Planck-scale accumulation models are already constrained [VPF13,
   NdV03]" is not supportable with that reference. Either replace it with **Stein15/Stein23** (the
   real accumulation-channel constraints) or drop the claim. This has to be the human's call because
   it edits an argument, not a row.
5. **`Bort26` cuts the other way and someone should read the whole paper before it is cited.** A 2026
   *experimental exclusion* of the generalized Károlyházy model sits awkwardly next to a paper that
   leans on the same formula. It is excluded in its decoherence parameterisation, not in the
   wavefront-accumulation parameterisation (which is what `Stein23` tests) — but that distinction has
   to be stated in the paper, not assumed, and the full text was not read here (abstract only).
6. **Independent arithmetic (mine, reproducible, out of my brief's scope but it bears on §6.2).**
   §6.2 assigns "picosecond-scale timing structure" to the volumetric scaling. Measured: `L/c` with
   `L = 5×10⁻¹⁵ m` is **1.7×10⁻²³ s** — eleven orders below a picosecond. The picosecond figure is
   what the *transverse* scaling gives: `√(l_pR) = 8.4×10⁻⁵ m`, `/c = 2.8×10⁻¹³ s ≈ 0.3 ps`; and
   Ng 2003 independently writes `(R_H l_p)^{1/2} ~ 10⁻¹⁴ s` for the α = 1/2 branch's bit-flip time
   [FETCHED]. So the two §6.2 paragraphs contradict each other, and the ps number belongs to the
   paragraph above. (The domain-1 scout in this tree found the same arithmetic independently.)
7. **`NCvD03`'s DOI was not fetched.** One Crossref call settles it.

---

*Scope: this memo is literature only. I wrote exactly one file
(`/workspace/physical-iso/litreview/domain5-voxel-scaling.md`); `paper.md`, `citations.md`,
`PROGRESS.md` and `scripts/` were not touched, and no gate was run — the patches above are
ready-to-paste, not applied.*
