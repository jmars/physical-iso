# Data landscape for the §6 test: what existing data can sharpen the α = 2/3 blurring bound

Scout: data-landscape (2026-11-16). Network live: arXiv export API, Crossref, FSSC,
**e-print sources downloaded and read** (LaTeX `.tex`, not abstracts) for Ng03,
Stein15, Stein23, Perlman14, and Ng–Perlman22. Every number below marked
**[FETCHED]** was read out of a file or API answer I pulled this session; **[MEMORY]**
is recalled, unverified, and must not ship in the paper without a human check.

Search scope warning: the arXiv API searches **metadata only** (title + abstract).
Eight distinct query formulations were run (§2 lists them). A paper that tests the
same physics without saying "blurring", "PSF", "foam" or "GRB" in its abstract would
be invisible to this method. Crossref and FSSC were used for the rest.

---

## 1. The Steinbring program's actual coverage

**Stein15 (arXiv:1502.03745, ApJ 802, 38)** [FETCHED — full `.tex` read].

- **Sample:** not a stacking of all GRBs, and not a single event. It analyses the
  Fermi LAT **GRB catalog of 27 bursts, of which 10 have z ≥ 0.5**, spanning
  **0.5 ≤ z ≤ 4.3** [ms.tex:99, :119]. The abstract's "10 highest-redshift GRB
  detections reported for the Fermi satellite" is that subsample. The paper says so
  plainly: "Newly detected z > 0.5 GRBs … greater statistics could be used to
  disentangle these from systematic uncertainty in source position" [ms.tex:115] —
  i.e. 2015 explicitly asks for the larger sample.
- **Energy range / statistic:** peak energy per burst (up to >10 GeV), converted to a
  single wavelength by 1/(2πcℏ) [ms.tex:99]; the observable is the **positional
  accuracy** of each burst — the 90 %-confidence point-source localization radius —
  normalised by redshift and by peak energy, compared against the in-flight LAT PSF
  from Ackermann 2013c, parameterised as a power law with slope ρ = 0.70 and scale
  R = 1.9×10⁸, i.e. **68 % containment 5° at 30 MeV → 1.5′ at 60 GeV** [ms.tex:101].
- **Bound:** no hard number in degrees; the paper's result is a *consistency* claim
  ("none of the GRB sources has a reported apparent angular size much smaller than
  Φ, even for energies higher than 10 GeV" [ms.tex:109]) plus the falsifiable
  statement that sources blurred beyond Φ "must be lost to the background"
  [ms.tex:121]. The bound quantity is the **model amplitude**, and the model has two
  free parameters — see §4.

**Stein23 (arXiv:2311.10168, Galaxies 11, 115)** [FETCHED — full `.tex` read].

- **Event:** GRB 221009A (the BOAT), z = 0.151, used as the anchor point — but the
  analysis is **not single-event**. It overlays "**all** the *Fermi* LAT and GBM
  localizations" and draws "the 5 %, 10 %, 50 % and 90 % containment of all the LAT
  plus GBM roll-angle and error-radii data, which now have both their peaks and
  averages in a **combined sample**" [Galaxies tex:298]. So 2023 *is* a
  population-level (catalog-contour) aggregation, with the one bright event pinned
  against the highest-energy localizations.
- **The bound:** a characteristic angle **Θ = 1°** is introduced and used as the mean
  foam blurring; the fit quotes **α = 0.650** for the X-ray comparison [tex:284] and
  **α = 0.735** as the "weakest possible Φ_Θ" at the highest LAT energies
  [tex:311]. So the published statement is a *range*, **α ≈ 0.65–0.74, with 2/3
  inside it**, not a one-sided upper bound. The abstract's "limiting bound of about
  1 degree is in agreement with a holographic QG-favored formulation" is that.
- **PSF statistic:** the model PSF width is Φ = R(λ/D)^ρ + ∫₀^θ Δφ σ(Δφ) d(Δφ), a
  four-regime "wedding cake" between the instrument resolution and the FoV
  [tex:269–272]; the LAT PSF itself is taken from **in-flight measurements on AGNs**,
  Appendix A [tex:396].
- **Data source, stated in the paper:** the public **HEASARC** archive, "accessed on
  1 November 2022" [tex:199–200].

**The two reviews** [FETCHED metadata + abstracts via Crossref/arXiv]:

- **Ng & Steinbring, IJMPD 34, 2544018 (2025)**, "Holographic quantum foam: From
  theory to observations", DOI 10.1142/S0218271825440183 — **metadata only; the text
  was not obtained** (World Scientific; no abstract in Crossref either). Do not cite
  its content from this memo.
- **Steinbring & Ng, PoS(CORFU2025) 205**, DOI 10.22323/1.509.0205 [FETCHED via
  Crossref], **= arXiv:2603.18277** (same title, authors and abstract) [FETCHED].
  Watch the identification: the arXiv preprint carries the *CORFU* title, **not** the
  IJMPD title — they are two different documents.
- What they say the frontier is [abstract, FETCHED]: the whole spectrum of GRB
  221009A "all consistent with blurring by HQF", and the deliverable is "a
  calculation of the HQF-widened point-spread function (PSF) **for real telescopes
  viewing a GRB**". The next dataset is not named; the direction is per-telescope PSF
  modelling of the same one event.

## 2. Has anyone else stacked multi-event PSF/blurring tests?

**Answer: nobody else does the GRB PSF channel, but a *different* multi-source
program already tests the same α on quasars and blazars — and it disfavours 2/3.**

Queries run against arXiv (metadata, max 20–40 hits each): `all:"holographic noise"`;
`all:Steinbring AND all:"gamma-ray"` (20 newest); `all:"gamma-ray burst" AND
all:"spacetime foam"`; `all:"point spread function" AND all:"quantum foam"`;
`all:"spacetime foam" AND all:blurring`; `all:"holographic" AND all:"gamma-ray burst"
AND all:blurring`; `all:"image blurring" AND all:"gamma-ray burst"` (0 hits);
`all:"holographic noise" AND all:stack` (0 hits); `all:"spacetime foam" AND
all:quasar` (40 newest). Findings:

- The **PSF/image-blurring** channel returns exactly one research group: Steinbring
  (with Ng). No second group, no competitor stacking analysis. [FETCHED — every
  query result set]
- The **quasar/AGN image** channel is a second, older program:
  **Christiansen, Ng & van Dam 2005 (gr-qc/0508121)** propose core-halo structure in
  distant quasar images [FETCHED abstract]; **Perlman et al. 2014 (arXiv:1411.7262)**
  and **Perlman et al. 2016 (arXiv:1607.08551)** carry it out. Perlman14
  [FETCHED full `.tex`] quotes, in Table 1 terms:
  **α ≳ 0.58 (Chandra X-rays), α ≳ 0.67 (Fermi GeV), α ≳ 0.72 (TeV Cherenkov)**, and
  says of the GeV number: "sets a constraint of α > 0.67 on spacetime foam models,
  *i.e.*, **disfavoring the holographic model, but perhaps not decisively**"
  [spfoam_blur_verO.tex:750]. Perlman16's abstract is blunter: "rule out several
  models of spacetime foam, including the interesting random-walk and **holographic**
  models" [FETCHED].
- **But the mechanism is not image stacking.** The GeV α > 0.67 constraint comes from
  the *existence of a large number of unresolved GeV blazars* (population/observability
  argument, [.tex:744–750]), and the X-ray one from a sample of six Chandra quasar
  images [.tex:652]. It tests the exponent by requiring that sources stay point-like,
  not by measuring a stacked PSF width.
- **The field's own methodology review** — **Ng & Perlman 2022 (arXiv:2205.12852)**
  [FETCHED full `.tex`] — states the open methodological problem: "we discuss the
  appropriate distance measure for calculating the expected angular broadening …
  all these methods ultimately depend on the availability of ways (if any) to carry
  out **proper averaging** of contributions from different light paths from the
  source to the telescope" [abstract, and review §on averaging]. That is the
  technical reason no consensus number exists.
- **Hostile precedent on the channel itself:** **Coule 2003 (astro-ph/0302333)**
  argues that for wavefront-division interference/diffraction the initial transverse
  coherence is produced by propagation (van Cittert–Zernike), so the effect is
  "strongly immune to quantum gravity influences that could tend to reduce phase
  coherence" [FETCHED abstract]; and the Lieu–Hillman claims that "ruled out" the
  family were answered by Ng on the cumulative-factor error (§4) — Ng03 [FETCHED]:
  Lieu–Hillman "neglected to take into account the correction factor … overestimate
  … by a factor (L/λ)^α"; "Ragazzoni et al. contains the same error"
  [gr-qc/0305019 tex:828–838]. **Any new stacked analysis must state which side of
  this coherence argument it sits on.**
- The only "stacking" in Stein23 is of a *different* effect: pair-production haloes
  around low-z blazars, "looked for, without success … by stacking together the data
  of many sources" [tex:196] — not the foam channel.

## 3. Data availability mechanics

- **Fermi data are public with no proprietary period.** FSSC Data Policy, fetched
  verbatim [FETCHED — https://fermi.gsfc.nasa.gov/ssc/data/policy/]: "Since the
  beginning of the second year of operations, all LAT science data has been released
  as early as possible, **typically within a day or two of acquisition**"; and "GBM
  data were not proprietary at any time during the mission and are released as early
  as possible during science operations."
- **How many GRBs have LAT detections at all:** **186** in the first ten years
  (2008 Aug 4 – 2018 Aug 4), of which 91 show 30–100 MeV emission and 169 are
  detected above 100 MeV; the LAT independently triggered on only **4**
  [**Axelsson et al. 2019, arXiv:1906.11403**, "A decade of GRBs observed by
  Fermi-LAT: The 2nd GRB catalog", FETCHED abstract]. Order of magnitude: **~10² LAT
  bursts**, vs **~10³ GBM bursts**. Stein23 states the union as "over 3390 GRBs
  (median-z 1.41; highest-z 4.61)" found by LAT+GBM [tex:199, FETCHED] — quote it
  with the caveat that this is the joint GBM-dominated count.
- **High-level products per burst already exist:** the 2nd LAT GRB catalog presents,
  for all 186 bursts, "onset, duration and temporal properties … as well as spectral
  characteristics in the 100 MeV–100 GeV energy range", with particular attention to
  the highest-energy photons [FETCHED abstract]; the LAT PSF needed to interpret them
  is published from in-flight AGN measurements (Stein23 Appendix A); GBM peak
  energies and error radii per burst are in the GBM catalog. Stein15 assumes exactly
  this stack of products, and cites the LAT resolution as 90 %-containment
  [ms.tex:101].
- **Practical consequence:** a re-analysis needs no proprietary data and no new
  observations — only the FSSC/LAT tools (PSF IRFs, `gtpsf`/`gtsrcprob`-class
  likelihood) plus the catalogs. The irreducible limitation is the LAT PSF itself
  (5° at 30 MeV): the foam signal is only visible where the instrumental PSF is
  sharp, i.e. **above ~10 GeV**, where the photon counts per burst are tiny.

## 4. The normalization question — **the decisive one**

**The α-family carries a free O(1) amplitude. Only the scaling shape is fixed.**

- **Ng 2003 (arXiv:gr-qc/0305019, MLPA 18, 1073)** [FETCHED full `.tex`]: the whole
  family is
  δℓ ~ l_P (L/l_P)^{1−α}, cumulative factor **𝒞_α = (L/λ)^{1−α}** — explicitly
  𝒞_{1/2} = (L/λ)^{1/2}, **𝒞_{2/3} = (L/λ)^{1/3}**, 𝒞₁ = 1 [tex:478–489]. The
  phase is then δφ ~ 2πa·𝒞_α, and the amplitude is **fixed only as "we expect
  a ~ 1"** [tex:812–816, verbatim: "Since we expect $a \sim 1$"]. There is no
  derivation of a; α itself is also a free choice of model.
- **So the phenomenology has two free parameters** — (a, α) — and the sharp content is
  the exponent. Stein15 makes this explicit in its own machinery: it writes
  **a₀ ~ 1** [ms.tex:41] and a normalization A = 1/log[(1+z)a₀(L/l_P)^{1−α}],
  "0.021 at z=4 for a₀=1 and α=0.67" [ms.tex:70] — i.e. it *sets* a₀ = 1 and varies α.
  Stein23 does the same: Δφ_max ∝ **a₀** with "a₀ ~ 1" [Galaxies tex:191, 265].
- **Therefore:** a stacked analysis tests **shape (α)** and, at fixed a₀ = 1, an
  implied amplitude. It cannot test the amplitude independently, and the a₀ = 1
  convention is where an O(1) systematic enters. This is exactly why the two camps can
  disagree at Δα ≈ 0.003 (α ≳ 0.67 vs α ≈ 0.650–0.735).
- **Second, independent O(1)-class freedom:** the *distance measure and light-path
  averaging* (Ng–Perlman 2022's own caveat, §2). Two analyses of the same α can differ
  by the choice of L(z) and of what is averaged. Any stacked analysis must state both
  conventions, or it is not comparable to Perlman's α > 0.67.

## 5. Adjacent existing-data channels (one line each)

- **Polarization coherence of distant sources — partially ruled out as a channel.**
  Tamburini et al. 2011 (A&A 533, A71, DOI 10.1051/0004-6361/201015808), "No quantum
  gravity signature from the farthest quasars": a null [FETCHED Crossref; content
  [MEMORY]]. GRB afterglow polarimetry sets |η| < 2×10⁻⁷ on Gambini–Pullin
  birefringence — **Fan, Wei & Xu 2007 (astro-ph/0702006)** [FETCHED abstract]; that
  is *birefringence*, not the foam-blurring amplitude, and Coule 2003 notes the phase
  ambiguity "could reduce any underlying polarization" [FETCHED].
- **AGN/blazar PSF stability vs redshift — the best-populated existing channel.**
  Perlman et al. 2014/2016: α ≳ 0.58 / 0.67 / 0.72 (X / GeV / TeV), "disfavoring the
  holographic model, but perhaps not decisively"; **this channel is where the strongest
  existing α-bound lives, and it is not a GRB analysis** [FETCHED full `.tex`].
- **Distant-galaxy image sizes — a clean null.** Ragazzoni, Turatto & Gaessler 2003,
  ApJL 587, L1, "The Lack of Observational Evidence for the Quantum Structure of
  Spacetime at Planck Scales" [FETCHED Crossref]; Ng03 argues its α = 2/3 exclusion
  used the wrong cumulative factor [FETCHED tex:835–838].
- **Narrow-emission-line spectroscopy of quasars — a quoted one-line alternative** in
  Stein23 (Cooke 2020, key from the paper's bibliography, **not** independently
  resolved this session: a Crossref search returned a *different* 2026 PRD paper
  "Spectroscopy as a probe of spacetime foam" (Kim, Nugent & Wang, DOI
  10.1103/j7z8-kbvr) [FETCHED], which is a distinct object). Treat "Cooke 2020" as
  **[MEMORY] — needs-human** before citing.
- **CMB-based bounds — nothing found.** arXiv metadata: `all:"quantum foam" AND
  all:CMB` (one irrelevant hit, physics/0209013), `all:"spacetime foam" AND
  all:"power spectrum"` (0 hits), `all:"spacetime foam" AND all:"cosmic microwave
  background"` (0 hits) [FETCHED]. Note the scope: metadata-only search, so this is
  "nothing found", not "nothing exists". The HQF framework's *cosmological* claim (a
  predicted dark sector, arXiv:2603.18277 abstract [FETCHED]) is not a blurring bound
  and cannot be counted here.
- **GRB photon-dispersion (stochastic LIV) — the same events, a different statistic.**
  Vasileiou et al. 2015, Nature Physics 11, 344 (DOI 10.1038/nphys3270) [FETCHED
  Crossref]; Stein23 quotes the current dispersion limit as 1.2 E_P (Liu 2022)
  [tex:195, FETCHED]. Orthogonal to blurring: it measures arrival-time spread, not
  image width.

---

## Verdict

**(a) largely done, in a coarse form; (b) a sharper version is open and feasible; but
(c) the amplitude question caps what any of it can prove.** Steinbring 2023 already is
a multi-event analysis — it overlays all LAT and GBM localizations and their 5/50/90 %
containment contours, with GRB 221009A as the high-energy anchor, and quotes
α ≈ 0.650–0.735. What is *not* done by anyone is a proper burst-by-burst **likelihood
stacking** of LAT photon probabilities against a foam-widened PSF: the existing work
uses catalog-level containment radii and LAT roll angles, which are the coarsest
possible statistic, and the 2nd LAT GRB catalog (186 bursts, per-burst spectra,
public immediately) makes the finer analysis feasible today on public data with no new
observations. Two structural blockers bound its payoff. First, the α-family's amplitude
is fixed only to O(1) — Ng writes "we expect a ~ 1" — so a stack sharpens the
**exponent**, and can at best convert "consistent with 2/3" into a tighter α interval;
it cannot measure the amplitude that §6's derivation would actually predict. Second,
the same exponent is already constrained harder by a *different* dataset — Perlman et
al.'s GeV blazar population gives α > 0.67, "disfavoring the holographic model, but
perhaps not decisively" — and the two results disagree at Δα ≈ 0.003, which is inside
the distance-measure/averaging systematic that Ng & Perlman themselves flag as
unresolved. So a stacked GRB analysis is worth doing as an **independent, same-α,
different-systematic cross-check** (it would be the first one not reliant on quasar
image sizes), and the paper should present it that way — not as a measurement of the
projection's amplitude. The §6 test remains a shape test.

---

### Out-of-brief observation (not written into paper.md — flagged for the orchestrator)

`paper.md` §6.2's "live status" paragraph cites Stein23 (consistent, ~1°) and Bort26
(decoherence channel excluded) but **does not mention Perlman et al. 2014/2016's
α > 0.67 GeV-blazar bound, which is the strongest existing α constraint and points the
other way**. A referee in this field will know that number. If §6 is revised, that
disagreement — not just Bort26's different channel — is what the "live status" sentence
should name.

### What this scout did NOT verify

- Ng & Steinbring's IJMPD 34, 2544018 **content** (metadata only).
- Any full text behind a paywall; no Google Scholar, no full-text index, no ADS API
  (ADS abstract pages were not queried — no token; INSPIRE was not needed).
- The Cooke 2020 identification (§5).
- Numerical claims I did not read out of a fetched file are absent from this memo on
  purpose.
