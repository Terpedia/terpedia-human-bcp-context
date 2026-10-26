"""Descriptive cross-context comparison of two pinned β-caryophyllene audits."""

from __future__ import annotations

import csv
import hashlib
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "research/human-bcp-context"
DATA = PROJECT / "data"
RESULTS = PROJECT / "results"
EXPECTED = {
    "hepg2_descriptive_effects.tsv": "345e58b56a7b57ca43e4cde689424acbc363a88ee5adcb164ee678425c6d3373",
    "ufh001_descriptive_effects.tsv": "7eef7fe7c5f0b3bedd452308a6d250c553d7fe74a2cc09eb1731b291bff2d564",
    "hgnc_crosswalk.tsv": "d38e83b643c29cbb2ff7b20dc6aa8d57702f885ed8b8fcd3ae4af6d6369b998b",
}
MARKERS = ("HMGCR", "SCD", "SQLE", "FDFT1", "HMGCS1", "INSIG1", "STARD4", "SREBF2", "PGF", "NR4A1", "CSF1R", "ARTN", "CACNA1E")


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def records(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def ranks(values: list[float]) -> list[float]:
    order = sorted(range(len(values)), key=values.__getitem__)
    result = [0.0] * len(values)
    start = 0
    while start < len(order):
        end = start + 1
        while end < len(order) and values[order[end]] == values[order[start]]:
            end += 1
        rank = (start + end - 1) / 2 + 1
        for position in order[start:end]:
            result[position] = rank
        start = end
    return result


def sign(value: float) -> int:
    return (value > 0) - (value < 0)


def summarize(rows: list[dict], ufh_column: str, hep_column: str) -> dict:
    x = [float(row[ufh_column]) for row in rows]
    y = [float(row[hep_column]) for row in rows]
    comparable = [(a, b) for a, b in zip(x, y) if sign(a) and sign(b)]
    n = len(comparable)
    matches = sum(sign(a) == sign(b) for a, b in comparable)
    p_up_x = sum(a > 0 for a, _ in comparable) / n if n else 0
    p_up_y = sum(b > 0 for _, b in comparable) / n if n else 0
    baseline = p_up_x * p_up_y + (1 - p_up_x) * (1 - p_up_y)
    return {
        "overlap_rows": len(rows),
        "nonzero_in_both": n,
        "same_sign": matches,
        "different_sign": n - matches,
        "same_sign_fraction": matches / n if n else None,
        "sign_frequency_baseline_fraction": baseline if n else None,
        "same_sign_minus_baseline": matches / n - baseline if n else None,
        "ufh_positive_fraction": p_up_x if n else None,
        "hepg2_positive_fraction": p_up_y if n else None,
        "spearman_effect_rank_correlation": statistics.correlation(ranks(x), ranks(y)) if len(rows) > 1 else None,
    }


def main() -> None:
    for name, expected in EXPECTED.items():
        actual = digest(DATA / name)
        if actual != expected:
            raise ValueError(f"Pinned source hash changed: {name}: {actual}")
    crosswalk = records(DATA / "hgnc_crosswalk.tsv")
    official = {r["entrez_id"]: r for r in crosswalk}
    if len(official) != len(crosswalk):
        raise ValueError("HGNC crosswalk Entrez IDs are not unique")
    hep = records(DATA / "hepg2_descriptive_effects.tsv")
    ufh = records(DATA / "ufh001_descriptive_effects.tsv")
    hep_by_id = {r["gene_id"]: r for r in hep}
    mapped_ufh = [r for r in ufh if r["entrez_id"]]
    ufh_by_id = {r["entrez_id"]: r for r in mapped_ufh}
    if len(hep_by_id) != len(hep) or len(ufh_by_id) != len(mapped_ufh):
        raise ValueError("Source effect tables contain duplicate Entrez IDs")
    for row in mapped_ufh:
        official_row = official.get(row["entrez_id"])
        if official_row is None or any(row[key] != official_row[key] for key in ("ensembl_gene_id", "symbol", "hgnc_id")):
            raise ValueError(f"UFH-001 mapping differs from pinned HGNC: {row['entrez_id']}")
    matched = sorted(set(hep_by_id) & set(ufh_by_id), key=int)
    mismatch = [gene_id for gene_id in matched if hep_by_id[gene_id]["gene_symbol"] != ufh_by_id[gene_id]["symbol"]]
    mismatch_ids = set(mismatch)
    strict = [gene_id for gene_id in matched if gene_id not in mismatch_ids]
    rows = []
    for gene_id in strict:
        h, u = hep_by_id[gene_id], ufh_by_id[gene_id]
        vals = {
            "entrez_id": gene_id,
            "symbol": u["symbol"],
            "ensembl_gene_id": u["ensembl_gene_id"],
            "hepg2_mean_control_cpm": h["mean_control_cpm"],
            "hepg2_mean_treated_cpm": h["mean_treated_cpm"],
            "ufh_mean_vehicle_fpkm": u["mean_vehicle_fpkm"],
            "ufh_mean_bcp20_fpkm": u["mean_bcp20_fpkm"],
            "ufh_mean_bcp200_fpkm": u["mean_bcp200_fpkm"],
            "hepg2_expressed": h["included_max_mean_cpm_ge_1"],
            "ufh_expressed": u["included_max_arm_mean_fpkm_ge_1"],
            "hepg2_log2_pc_0_1": h["log2_ratio_pseudocount_0_1"],
            "hepg2_log2_pc_1": h["log2_ratio_pseudocount_1"],
            "ufh20_log2_pc_0_1": u["bcp20_log2_ratio_pc_0_1"],
            "ufh20_log2_pc_1": u["bcp20_log2_ratio_pc_1"],
            "ufh200_log2_pc_0_1": u["bcp200_log2_ratio_pc_0_1"],
            "ufh200_log2_pc_1": u["bcp200_log2_ratio_pc_1"],
        }
        for dose in (20, 200):
            vals[f"same_sign_{dose}_pc_0_1"] = int(sign(float(vals[f"ufh{dose}_log2_pc_0_1"])) == sign(float(vals["hepg2_log2_pc_0_1"])) and sign(float(vals["hepg2_log2_pc_0_1"])) != 0)
        rows.append(vals)
    both_expressed = [r for r in rows if r["hepg2_expressed"] == "True" and r["ufh_expressed"] == "True"]
    metrics = {}
    for dose in (20, 200):
        metrics[f"bcp{dose}"] = {
            "strict_overlap": summarize(rows, f"ufh{dose}_log2_pc_0_1", "hepg2_log2_pc_0_1"),
            "both_expressed_pc_0_1": summarize(both_expressed, f"ufh{dose}_log2_pc_0_1", "hepg2_log2_pc_0_1"),
            "both_expressed_pc_1": summarize(both_expressed, f"ufh{dose}_log2_pc_1", "hepg2_log2_pc_1"),
        }
    markers = [r for r in rows if r["symbol"] in MARKERS]
    present_markers = {r["symbol"] for r in markers}
    summary = {
        "source_projects": {"GSE276099": "d575b95ae276283746cf3db8543c777d4a86d462", "GSE125511": "258d36bad9bbd8df99e8141c3e140b2f85d04a00"},
        "input_sha256": EXPECTED,
        "hepg2_rows": len(hep),
        "ufh001_rows": len(ufh),
        "ufh001_mapped_entrez_rows": len(mapped_ufh),
        "shared_entrez_ids": len(matched),
        "shared_ids_with_symbol_mismatch_excluded": len(mismatch),
        "strict_shared_ids": len(rows),
        "strict_shared_ids_expressed_in_both": len(both_expressed),
        "dose_comparisons": metrics,
        "predeclared_marker_count": len(MARKERS),
        "predeclared_markers_present": len(present_markers),
        "predeclared_markers_missing": sorted(set(MARKERS) - present_markers),
        "limitations": [
            "Two processed bulk RNA-seq studies with different cell line, oxygen, dose, duration, vehicle, and quantification",
            "FPKM and CPM pseudocount ratios have different measurement scales; effect magnitudes are not directly comparable",
            "No new replicate-aware differential-expression model, p values, or context interaction",
            "GSE125511 dose contrasts share controls that are also reused from GSE123856",
            "Symbol mismatches are excluded from the primary join, which may remove valid renamed genes",
        ],
    }
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "analysis_summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n")
    write_tsv(RESULTS / "shared_gene_effects.tsv", rows, list(rows[0]))
    write_tsv(RESULTS / "marker_comparison.tsv", markers, list(rows[0]))
    write_tsv(RESULTS / "symbol_mismatches.tsv", [{"entrez_id": x, "hepg2_symbol": hep_by_id[x]["gene_symbol"], "ufh001_symbol": ufh_by_id[x]["symbol"]} for x in mismatch], ["entrez_id", "hepg2_symbol", "ufh001_symbol"])
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
