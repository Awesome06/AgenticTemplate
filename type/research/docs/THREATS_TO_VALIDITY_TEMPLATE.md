# Threats to Validity

To ensure empirical rigor in academic review (CORE A*/A venues: ISSTA, FSE, ASE, MSR, EDM), every paper manuscript and replication package must address all four validity quadrants:

---

## 1. Internal Validity
*Internal validity concerns the extent to which the observed empirical effects are truly caused by the evaluated system rather than confounding variables or experimental artifacts.*

- **Confounding Factors:** Did system performance vary due to differing LLM temperature settings, hardware differences, or varying context window limits?
- **Dataset Contamination:** Were benchmark evaluation repositories or test problems present in the pre-training corpus of the evaluated foundation models?
- **Prompt Engineering & Leakage:** Were prompts systematically standardized across baseline and treatment conditions to prevent accidental prompt-leakage of reference solutions?

---

## 2. External Validity
*External validity addresses the generalizability of the findings across diverse real-world software engineering environments.*

- **Subject Diversity:** Are the evaluated benchmark subjects drawn from multiple programming languages (e.g. Go, Rust, Python, TypeScript) and multiple application domains (systems, full-stack, data engineering)?
- **Project Scale:** Does the benchmark reflect realistic repository scales (multi-file architectures, complex dependency trees) rather than isolated synthetic toy functions?
- **Task Variety:** Were evaluation tasks sampled across defect remediation, feature authoring, API migration, and security patching?

---

## 3. Construct Validity
*Construct validity evaluates whether the metrics and evaluation instruments accurately capture the theoretical engineering phenomena under study.*

- **Metric Fidelity:** Does Pass@1 or AST match score truly reflect semantic correctness, or can superficial stylistic changes bias the metric?
- **Human vs Automated Evaluation:** If using automated LLM evaluators ("LLM-as-a-judge"), were judgements calibrated against blind human expert annotations?
- **Runtime Flakiness:** Were execution-based benchmarks rerun across multiple seeds or trials to eliminate transient test flakiness?

---

## 4. Conclusion Validity
*Conclusion validity concerns whether the statistical analyses, sample sizes, and empirical relationships drawn are statistically sound.*

- **Non-Parametric Analysis:** Were non-parametric effect sizes (Vargha-Delaney A12 or Cliff's delta) computed, avoiding erroneous assumptions of normal distribution?
- **Confidence Intervals:** Are proportion metrics reported with Wilson score intervals rather than standard Wald intervals?
- **Multiple Comparisons:** Was the False Discovery Rate (FDR) controlled using the Benjamini-Hochberg procedure across all family-wise statistical tests?

