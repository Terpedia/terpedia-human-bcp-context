# Terpedia human β-caryophyllene context comparison

This forkable project compares the pinned processed-effect tables from [HepG2 GSE276099](https://github.com/Terpedia/terpedia-hepg2-bcp-rsem/tree/d575b95ae276283746cf3db8543c777d4a86d462) and [hypoxic UFH-001 GSE125511](https://github.com/Terpedia/terpedia-ufh001-bcp-fpkm/tree/258d36bad9bbd8df99e8141c3e140b2f85d04a00). It includes an [executed Jupyter notebook](notebooks/terputer-human-bcp-context.ipynb), [generated report](research/human-bcp-context/generated/white-paper.md), [claim ledger](research/human-bcp-context/generated/claim-ledger.tsv), [results](research/human-bcp-context/results), and [execution receipt](research/execution-receipts/terputer-human-bcp-context.json).

The strict join retains 16,478 shared Entrez IDs after excluding 294 symbol mismatches; 10,241 pass each upstream audit's expression filter. For those rows, effect direction agrees for 48.85% at UFH-001 20 µM and 48.88% at 200 µM against the HepG2 contrast, close to sign-frequency baselines of 49.44% and 49.90%. This is a descriptive comparison of processed **bulk** RNA-seq summaries. The studies differ in cell line, oxygen, dose, exposure duration, vehicle, and quantification. There is no matched context interaction, cross-study DEG replication claim, or target-specific Perturb-seq inference.

## Count-based follow-up status

The [HepG2 raw-read white paper](https://github.com/Terpedia/terpedia-hepg2-bcp-rsem/blob/f0e0a56ae1b510fa622a11e218fe6b3b8d2f8d54/research/hepg2-bcp-raw-counts/generated/white-paper.md) now reports a separate, receipt-pinned count-model contrast. It does not replace the processed-effect values used in this frozen comparison. The [UFH-001 raw-count notebook](https://github.com/Terpedia/terpedia-ufh001-bcp-fpkm/blob/main/notebooks/terputer-ufh001-bcp-raw-counts.ipynb) and [cross-context comparison notebook](https://github.com/Terpedia/terpedia-ufh001-bcp-fpkm/blob/main/notebooks/terputer-bcp-cross-context.ipynb) are method artifacts until their execution receipts and results are published. Count-based directional comparison will be reported separately; no updated cross-context result is asserted here.

## Reproduce

Use Python 3.10 or newer and Node.js:

```sh
python -m pip install -r requirements.txt
python restore-inputs.py research/human-bcp-context/report-spec.json
python notebook-runner.py notebooks/terputer-human-bcp-context.ipynb . 120 '["research/human-bcp-context/results/analysis_summary.json","research/human-bcp-context/results/shared_gene_effects.tsv","research/human-bcp-context/results/marker_comparison.tsv","research/human-bcp-context/results/symbol_mismatches.tsv"]' '["research/human-bcp-context/analysis.py","research/human-bcp-context/data/hepg2_descriptive_effects.tsv","research/human-bcp-context/data/ufh001_descriptive_effects.tsv","research/human-bcp-context/data/hgnc_crosswalk.tsv"]'
node report-generator.mjs research/human-bcp-context/report-spec.json
```

Input URLs point to immutable source-repository commits and are checksum pinned. The original GEO matrices, upstream methods, and sample-level QC reside in the two source projects. The comparison notebook verifies the one-to-one HGNC map, joins numeric Entrez IDs, excludes symbol mismatches, calculates effect-sign agreement and sign-frequency baselines, and reports predeclared marker directions. The [methods note](research/human-bcp-context/README.md) explains the interpretation boundary.

To attach a fork to a `terpedia-report` workspace, use the `add_research_project_submodule` tool with slug `human-bcp-context`; its path is `projects/human-bcp-context`.
