# Research Paper Replication Package

Replication package and empirical artifact evaluation harness for academic submission.

## Three-Tier Replication Runner

Run experimental evaluations via the standard three-tier script:
```bash
# 1. Fast smoke test (< 60s)
bash scripts/run_all.sh --dry-run

# 2. Sample dataset validation (< 15 min)
bash scripts/run_all.sh --sample

# 3. Full benchmark replication
bash scripts/run_all.sh --full
```

## Structure
- `manuscript/`: Typst / LaTeX source files.
- `experiments/`: Benchmark datasets, scripts, and evaluation pipelines.
- `results/`: Raw logs and generated plots/tables.

