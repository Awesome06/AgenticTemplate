# Research Paper Replication Package

Replication package and empirical artifact evaluation harness for academic submission (CORE A*/A venues: ISSTA, FSE, ASE, MSR, EDM).

---

## Three-Tier Replication Runner

Run experimental evaluations via the three-tier execution harness:

```bash
# 1. Fast smoke test (< 60s) on toy dataset
bash scripts/run_all.sh --dry-run
# Or cross-platform:
python scripts/run_all.py --dry-run

# 2. Representative sample validation (< 15 min)
bash scripts/run_all.sh --sample
# Or cross-platform:
python scripts/run_all.py --sample

# 3. Full benchmark replication across all subjects
bash scripts/run_all.sh --full
# Or cross-platform:
python scripts/run_all.py --full
```

---

## Non-Parametric Statistics Engine

Compute empirical software engineering metrics with zero external dependencies:

```bash
# Compute Vargha-Delaney A12 effect size
python scripts/stats_calculator.py a12 --treatment 15 18 19 22 --control 8 9 11 12

# Compute Cliff's delta
python scripts/stats_calculator.py cliff --treatment 15 18 19 22 --control 8 9 11 12

# Compute 95% Wilson score confidence interval
python scripts/stats_calculator.py wilson --successes 85 --total 100

# Apply Benjamini-Hochberg False Discovery Rate (FDR) control
python scripts/stats_calculator.py fdr --p-values 0.001 0.023 0.048 0.12 0.35
```

---

## Directory Structure

- `scripts/`: Replication runners (`run_all.sh`, `run_all.py`) and empirical statistics engine (`stats_calculator.py`).
- `docs/`: 4-quadrant threats to validity documentation (`THREATS_TO_VALIDITY_TEMPLATE.md`).
- `manuscript/`: Typst or LaTeX manuscript source documents.
- `experiments/`: Benchmark datasets, subject projects, and evaluation pipelines.
- `results/`: Raw evaluation log outputs and statistical summary tables.
