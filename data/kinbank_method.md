# Kinbank spelling-based baseline — supplied analysis v2
Date archived: 2026-11-23
Status: **Researcher-supplied results, not independently reproduced or verified by this repository.**
Source repository: https://github.com/kinbank/kinbank
Source commit: `925cc0e702ae5481cfe0088aaa0e69c3991000f3` (reported 2026-08-03)
Source file: `cldf/forms.csv`

## Input and eligibility
- Total rows reported: **218,412**; languages with forms **1,287**.
- Eligible **183,550** rows, **1,255** languages, **69** named families, **21,219** distinct normalized forms.
- Missing/excluded: **34,862** rows: 34,437 contain letters outside a–z including non-Latin/IPA symbols; 407 nonalphabetic; 18 empty.
- Sum check: 183,550 + 34,862 = 218,412.
- Historic 2023 article figures 210,903 data points and 1,229 languages refer to a different release and should not be compared as if identical populations.

## Matching
Lowercase `Form`, normalize to Unicode NFD, strip combining marks, then split tokens on every non-[a-z] character. A row is eligible only when the whole normalized form consists exclusively of ASCII letter tokens separated by allowed delimiters. Whole-form means entire normalized form is one token exactly matching target. Substring means any token contains the target.

These are **orthographic/spelling comparisons, not IPA sound counts**. The `Segments` and `Graphemes` columns were reported empty for all 218,412 rows. IPA counts were **not computed** and remain missing.

## Parameter sets
- ALL: all kin terms.
- Parents: fF,fM,mF,mM.
- Mother: fM,mM (female/male ego's mother).
- Grandmothers: fFM,fMM,mFM,mMM; the first version of the CSV contained an incorrect shorthand label, corrected in v2.
- All grandparents: FF,FM,MF,MM.

## v1 → v2 correction
The tokenizer mistakenly retained characters including typographic apostrophes, spacing accents, breve and hyphen inside tokens, excluding 956 eligible rows. v1 eligible 182,594 / missing 35,818; v2 eligible 183,550 / missing 34,862. Whole-form target hits unchanged. Substring changes: `an` 28,629→28,672 forms and 916→919 languages; `ana` 7,282→7,284 forms, 474 languages unchanged; `anu`, `nana`, `ama` unchanged.

## Data files
- [kinbank_counts.csv](kinbank_counts.csv) — all 40 reported combinations across five parameter sets.
- [kinbank_vnv_control.csv](kinbank_vnv_control.csv) — all 18 vowel–nasal–vowel control trigrams, ranked by share of eligible languages with a substring.
- Exact-match / substring columns and percentages preserve the user's provided aggregation. Percentages were recomputed from integer counts to two decimal places in this repository transcription.

## Limitations
- Many writing systems and phonemic symbols are entirely excluded, not classified as nonmatches.
- Long forms disproportionately produce substring hits.
- Language forms are not independent observations; family grouping and borrowing matter.
- Orthographic conventions differ, including a/o/u, stress, and tone marking.
- Family is missing for some languages.
- This is **kinship vocabulary only**, not a denominator of sacred names and not a test of whether sacred names are enriched for these sound sequences.
- For independent verification, provide scripts and checksum/output artifacts, confirm source commit, rerun with language/kin-class stratification and family-aware analysis.
