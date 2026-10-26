# β-Caryophyllene across HepG2 and hypoxic UFH-001: a processed-effect comparison

> Generated evidence brief. Each statement is linked to a claim record; scientific interpretation still requires review.

**Research question:** Which metabolic and signaling responses to terpene exposure are reproducible, and which depend on cellular context or a specific target?

**Notebook:** `notebooks/terputer-human-bcp-context.ipynb` · SHA-256 `3a9ebec0cf57a3b2d06d932b475ce8385b4d7657a03fa2b4e11f51db2ea71672` · 1 executed code cells

## Abstract

**Source-reported:** The GSE276099 HepG2 and GSE125511 UFH-001 series expose human cell lines to the named compound β-caryophyllene, but differ in cell line, oxygen, dose, duration, vehicle, and processing. The UFH-001 vehicle controls are reused from GSE123856. (claim C01; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE276099), [2](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE125511))

**Observed in notebook:** The pinned source audits contribute 17,034 HepG2 and 60,603 UFH-001 feature rows. After joining numeric Entrez IDs, 16,772 IDs overlap; 294 symbol mismatches are excluded, leaving 16,478 strict shared IDs and 10,241 that meet each audit's expression filter. (claim C02; [3](https://github.com/Terpedia/terpedia-hepg2-bcp-rsem/tree/d575b95ae276283746cf3db8543c777d4a86d462), [4](https://github.com/Terpedia/terpedia-ufh001-bcp-fpkm/tree/258d36bad9bbd8df99e8141c3e140b2f85d04a00), [5](https://www.genenames.org/download/))

**Observed in notebook:** Among 10,241 strict shared IDs above both expression filters, UFH-001 20 µM versus HepG2 effect signs agree for 5,003 (48.85%); the sign-frequency baseline is 49.44%, and Spearman rank correlation is -0.026. The UFH-001 200 µM comparison agrees for 5,006 (48.88%) versus a 49.90% baseline, with rank correlation -0.048. (claim C03; [3](https://github.com/Terpedia/terpedia-hepg2-bcp-rsem/tree/d575b95ae276283746cf3db8543c777d4a86d462), [4](https://github.com/Terpedia/terpedia-ufh001-bcp-fpkm/tree/258d36bad9bbd8df99e8141c3e140b2f85d04a00))

## Background

**Source-reported:** The GSE276099 HepG2 and GSE125511 UFH-001 series expose human cell lines to the named compound β-caryophyllene, but differ in cell line, oxygen, dose, duration, vehicle, and processing. The UFH-001 vehicle controls are reused from GSE123856. (claim C01; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE276099), [2](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE125511))

## Methods

**Observed in notebook:** The pinned source audits contribute 17,034 HepG2 and 60,603 UFH-001 feature rows. After joining numeric Entrez IDs, 16,772 IDs overlap; 294 symbol mismatches are excluded, leaving 16,478 strict shared IDs and 10,241 that meet each audit's expression filter. (claim C02; [3](https://github.com/Terpedia/terpedia-hepg2-bcp-rsem/tree/d575b95ae276283746cf3db8543c777d4a86d462), [4](https://github.com/Terpedia/terpedia-ufh001-bcp-fpkm/tree/258d36bad9bbd8df99e8141c3e140b2f85d04a00), [5](https://www.genenames.org/download/)) Artifacts: [research/human-bcp-context/results/analysis_summary.json](../results/analysis_summary.json), [research/human-bcp-context/results/symbol_mismatches.tsv](../results/symbol_mismatches.tsv), [research/human-bcp-context/results/shared_gene_effects.tsv](../results/shared_gene_effects.tsv).

**Observed in notebook:** Among 10,241 strict shared IDs above both expression filters, UFH-001 20 µM versus HepG2 effect signs agree for 5,003 (48.85%); the sign-frequency baseline is 49.44%, and Spearman rank correlation is -0.026. The UFH-001 200 µM comparison agrees for 5,006 (48.88%) versus a 49.90% baseline, with rank correlation -0.048. (claim C03; [3](https://github.com/Terpedia/terpedia-hepg2-bcp-rsem/tree/d575b95ae276283746cf3db8543c777d4a86d462), [4](https://github.com/Terpedia/terpedia-ufh001-bcp-fpkm/tree/258d36bad9bbd8df99e8141c3e140b2f85d04a00)) Artifacts: [research/human-bcp-context/results/analysis_summary.json](../results/analysis_summary.json), [research/human-bcp-context/results/shared_gene_effects.tsv](../results/shared_gene_effects.tsv).

## Results

**Observed in notebook:** The pinned source audits contribute 17,034 HepG2 and 60,603 UFH-001 feature rows. After joining numeric Entrez IDs, 16,772 IDs overlap; 294 symbol mismatches are excluded, leaving 16,478 strict shared IDs and 10,241 that meet each audit's expression filter. (claim C02; [3](https://github.com/Terpedia/terpedia-hepg2-bcp-rsem/tree/d575b95ae276283746cf3db8543c777d4a86d462), [4](https://github.com/Terpedia/terpedia-ufh001-bcp-fpkm/tree/258d36bad9bbd8df99e8141c3e140b2f85d04a00), [5](https://www.genenames.org/download/)) Artifacts: [research/human-bcp-context/results/analysis_summary.json](../results/analysis_summary.json), [research/human-bcp-context/results/symbol_mismatches.tsv](../results/symbol_mismatches.tsv), [research/human-bcp-context/results/shared_gene_effects.tsv](../results/shared_gene_effects.tsv). **Limitation:** The source filters use different units (CPM and FPKM). Excluding symbol mismatches may remove valid renamed genes; no orthology problem exists, but annotation harmonization remains version-dependent.

**Observed in notebook:** Among 10,241 strict shared IDs above both expression filters, UFH-001 20 µM versus HepG2 effect signs agree for 5,003 (48.85%); the sign-frequency baseline is 49.44%, and Spearman rank correlation is -0.026. The UFH-001 200 µM comparison agrees for 5,006 (48.88%) versus a 49.90% baseline, with rank correlation -0.048. (claim C03; [3](https://github.com/Terpedia/terpedia-hepg2-bcp-rsem/tree/d575b95ae276283746cf3db8543c777d4a86d462), [4](https://github.com/Terpedia/terpedia-ufh001-bcp-fpkm/tree/258d36bad9bbd8df99e8141c3e140b2f85d04a00)) Artifacts: [research/human-bcp-context/results/analysis_summary.json](../results/analysis_summary.json), [research/human-bcp-context/results/shared_gene_effects.tsv](../results/shared_gene_effects.tsv). **Limitation:** These are descriptive signs and ranks of processed group means, not independent tested treatment effects. Baseline is calculated from observed sign frequencies, not a biological null model or p-value.

**Observed in notebook:** HMGCR has a descriptive log2 ratio of +1.525 at 200 µM in UFH-001 and -0.017 in HepG2; FDFT1, SQLE, and INSIG1 similarly rise in high-dose UFH-001 but are near-flat or slightly lower in HepG2. Both source tables show negative PGF ratios, but UFH-001 PGF is below its predeclared expression filter. (claim C04; [3](https://github.com/Terpedia/terpedia-hepg2-bcp-rsem/tree/d575b95ae276283746cf3db8543c777d4a86d462), [4](https://github.com/Terpedia/terpedia-ufh001-bcp-fpkm/tree/258d36bad9bbd8df99e8141c3e140b2f85d04a00)) Artifacts: [research/human-bcp-context/results/marker_comparison.tsv](../results/marker_comparison.tsv). **Limitation:** CPM and FPKM effects and pseudocounts are not magnitude-comparable. A shared PGF sign at low UFH-001 abundance does not establish replication, and marker differences cannot be assigned to cell type alone.

## Interpretation

**Observed in notebook:** Among 10,241 strict shared IDs above both expression filters, UFH-001 20 µM versus HepG2 effect signs agree for 5,003 (48.85%); the sign-frequency baseline is 49.44%, and Spearman rank correlation is -0.026. The UFH-001 200 µM comparison agrees for 5,006 (48.88%) versus a 49.90% baseline, with rank correlation -0.048. (claim C03; [3](https://github.com/Terpedia/terpedia-hepg2-bcp-rsem/tree/d575b95ae276283746cf3db8543c777d4a86d462), [4](https://github.com/Terpedia/terpedia-ufh001-bcp-fpkm/tree/258d36bad9bbd8df99e8141c3e140b2f85d04a00)) Artifacts: [research/human-bcp-context/results/analysis_summary.json](../results/analysis_summary.json), [research/human-bcp-context/results/shared_gene_effects.tsv](../results/shared_gene_effects.tsv). **Limitation:** These are descriptive signs and ranks of processed group means, not independent tested treatment effects. Baseline is calculated from observed sign frequencies, not a biological null model or p-value.

**Observed in notebook:** HMGCR has a descriptive log2 ratio of +1.525 at 200 µM in UFH-001 and -0.017 in HepG2; FDFT1, SQLE, and INSIG1 similarly rise in high-dose UFH-001 but are near-flat or slightly lower in HepG2. Both source tables show negative PGF ratios, but UFH-001 PGF is below its predeclared expression filter. (claim C04; [3](https://github.com/Terpedia/terpedia-hepg2-bcp-rsem/tree/d575b95ae276283746cf3db8543c777d4a86d462), [4](https://github.com/Terpedia/terpedia-ufh001-bcp-fpkm/tree/258d36bad9bbd8df99e8141c3e140b2f85d04a00)) Artifacts: [research/human-bcp-context/results/marker_comparison.tsv](../results/marker_comparison.tsv). **Limitation:** CPM and FPKM effects and pseudocounts are not magnitude-comparable. A shared PGF sign at low UFH-001 abundance does not establish replication, and marker differences cannot be assigned to cell type alone.

## Limitations

**Claim C01 (source-reported):** The GSE276099 HepG2 and GSE125511 UFH-001 series expose human cell lines to the named compound β-caryophyllene, but differ in cell line, oxygen, dose, duration, vehicle, and processing. The UFH-001 vehicle controls are reused from GSE123856. **Limitation:** Chemical stereochemistry and purity were not harmonized; this is neither a matched context experiment nor independent replication of one exposure protocol. ([1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE276099), [2](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE125511))

**Claim C02 (observed):** The pinned source audits contribute 17,034 HepG2 and 60,603 UFH-001 feature rows. After joining numeric Entrez IDs, 16,772 IDs overlap; 294 symbol mismatches are excluded, leaving 16,478 strict shared IDs and 10,241 that meet each audit's expression filter. **Limitation:** The source filters use different units (CPM and FPKM). Excluding symbol mismatches may remove valid renamed genes; no orthology problem exists, but annotation harmonization remains version-dependent. ([3](https://github.com/Terpedia/terpedia-hepg2-bcp-rsem/tree/d575b95ae276283746cf3db8543c777d4a86d462), [4](https://github.com/Terpedia/terpedia-ufh001-bcp-fpkm/tree/258d36bad9bbd8df99e8141c3e140b2f85d04a00), [5](https://www.genenames.org/download/))

**Claim C03 (observed):** Among 10,241 strict shared IDs above both expression filters, UFH-001 20 µM versus HepG2 effect signs agree for 5,003 (48.85%); the sign-frequency baseline is 49.44%, and Spearman rank correlation is -0.026. The UFH-001 200 µM comparison agrees for 5,006 (48.88%) versus a 49.90% baseline, with rank correlation -0.048. **Limitation:** These are descriptive signs and ranks of processed group means, not independent tested treatment effects. Baseline is calculated from observed sign frequencies, not a biological null model or p-value. ([3](https://github.com/Terpedia/terpedia-hepg2-bcp-rsem/tree/d575b95ae276283746cf3db8543c777d4a86d462), [4](https://github.com/Terpedia/terpedia-ufh001-bcp-fpkm/tree/258d36bad9bbd8df99e8141c3e140b2f85d04a00))

**Claim C04 (observed):** HMGCR has a descriptive log2 ratio of +1.525 at 200 µM in UFH-001 and -0.017 in HepG2; FDFT1, SQLE, and INSIG1 similarly rise in high-dose UFH-001 but are near-flat or slightly lower in HepG2. Both source tables show negative PGF ratios, but UFH-001 PGF is below its predeclared expression filter. **Limitation:** CPM and FPKM effects and pseudocounts are not magnitude-comparable. A shared PGF sign at low UFH-001 abundance does not establish replication, and marker differences cannot be assigned to cell type alone. ([3](https://github.com/Terpedia/terpedia-hepg2-bcp-rsem/tree/d575b95ae276283746cf3db8543c777d4a86d462), [4](https://github.com/Terpedia/terpedia-ufh001-bcp-fpkm/tree/258d36bad9bbd8df99e8141c3e140b2f85d04a00))

## Next research steps

**Proposed:** Use a matched factorial design crossing HepG2 and UFH-001 with common vehicle, oxygen, β-caryophyllene doses and timepoints, biological replicates, and a dose-by-cell interaction model. Add HMGCR or PGF perturbation with viability and target-engagement controls to test dependency. (claim C05; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE276099), [2](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE125511), [3](https://github.com/Terpedia/terpedia-hepg2-bcp-rsem/tree/d575b95ae276283746cf3db8543c777d4a86d462), [4](https://github.com/Terpedia/terpedia-ufh001-bcp-fpkm/tree/258d36bad9bbd8df99e8141c3e140b2f85d04a00))

**Proposed:** Reprocess both studies from raw reads against one pinned human annotation and fit within-study replicate-aware models before applying a predeclared pathway-level replication rule. (claim C06; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE276099), [2](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE125511))

## Data and code availability

The source specification is `research/human-bcp-context/report-spec.json` (SHA-256 `31a16bbac71ccb1695ef605cd63045accff3217e2bbac1e3127ae536e32f76d1`). The claim ledger and generation receipt accompany this report. File hashes identify the report files and cited result artifacts. 3 externally sourced input files have a source URL and hash listed below. The [notebook execution receipt](../../execution-receipts/terputer-human-bcp-context.json) matches the saved notebook and records hashes for result files written during its fresh-kernel run. It also pins 4 declared local input files by SHA-256. It records the Python version and installed package versions. Notebook execution does not independently validate scientific interpretation.

### External data files

The following download locations and file hashes match inputs pinned by the notebook execution receipt. The generator does not download these files or verify that the URLs remain live.

| Input | Download | SHA-256 |
| --- | --- | --- |
| `research/human-bcp-context/data/hepg2_descriptive_effects.tsv` | [Source file](https://raw.githubusercontent.com/Terpedia/terpedia-hepg2-bcp-rsem/d575b95ae276283746cf3db8543c777d4a86d462/research/hepg2-bcp-rsem/results/descriptive_effects.tsv) | `345e58b56a7b57ca43e4cde689424acbc363a88ee5adcb164ee678425c6d3373` |
| `research/human-bcp-context/data/ufh001_descriptive_effects.tsv` | [Source file](https://raw.githubusercontent.com/Terpedia/terpedia-ufh001-bcp-fpkm/258d36bad9bbd8df99e8141c3e140b2f85d04a00/research/ufh001-bcp-fpkm/results/descriptive_effects.tsv) | `7eef7fe7c5f0b3bedd452308a6d250c553d7fe74a2cc09eb1731b291bff2d564` |
| `research/human-bcp-context/data/hgnc_crosswalk.tsv` | [Source file](https://raw.githubusercontent.com/Terpedia/terpedia-ufh001-bcp-fpkm/258d36bad9bbd8df99e8141c3e140b2f85d04a00/research/ufh001-bcp-fpkm/hgnc_crosswalk.tsv) | `d38e83b643c29cbb2ff7b20dc6aa8d57702f885ed8b8fcd3ae4af6d6369b998b` |

## References

[1] GEO GSE276099 HepG2 series. https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE276099
[2] GEO GSE125511 UFH-001 series. https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE125511
[3] Pinned executed HepG2 audit. https://github.com/Terpedia/terpedia-hepg2-bcp-rsem/tree/d575b95ae276283746cf3db8543c777d4a86d462
[4] Pinned executed UFH-001 audit. https://github.com/Terpedia/terpedia-ufh001-bcp-fpkm/tree/258d36bad9bbd8df99e8141c3e140b2f85d04a00
[5] HGNC official human gene nomenclature. https://www.genenames.org/download/
