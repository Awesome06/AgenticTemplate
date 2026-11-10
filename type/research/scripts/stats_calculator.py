#!/usr/bin/env python3
"""
scripts/stats_calculator.py - Non-Parametric Empirical Software Engineering Statistics Calculator.

Implements required empirical SE statistics with zero external dependencies:
1. Vargha-Delaney A12 effect size (with standard SE magnitude thresholds).
2. Cliff's delta effect size.
3. Wilson score confidence intervals for binomial proportions.
4. Benjamini-Hochberg False Discovery Rate (FDR) adjustment for multiple comparisons.
"""

import argparse
import math
import sys
from typing import List, Tuple, Dict, Any


def vargha_delaney_a12(treatment: List[float], control: List[float]) -> Tuple[float, str]:
    """
    Computes Vargha-Delaney A12 non-parametric effect size.
    A12 measures the probability that a randomly chosen observation from the treatment
    group is greater than a randomly chosen observation from the control group.
    """
    m = len(treatment)
    n = len(control)
    if m == 0 or n == 0:
        raise ValueError("Treatment and control groups must both contain at least 1 observation.")

    # Pairwise comparison
    greater = 0.0
    equal = 0.0
    for x in treatment:
        for y in control:
            if x > y:
                greater += 1.0
            elif x == y:
                equal += 1.0

    a12 = (greater + 0.5 * equal) / (m * n)

    # Magnitude interpretation (Vargha & Delaney, 2000)
    diff = abs(a12 - 0.5)
    if diff < 0.06:
        magnitude = "negligible"
    elif diff < 0.14:
        magnitude = "small"
    elif diff < 0.21:
        magnitude = "medium"
    else:
        magnitude = "large"

    return a12, magnitude


def cliffs_delta(treatment: List[float], control: List[float]) -> Tuple[float, str]:
    """
    Computes Cliff's delta effect size.
    delta = 2 * A12 - 1. Ranges from -1.0 to +1.0.
    """
    a12, _ = vargha_delaney_a12(treatment, control)
    delta = 2.0 * a12 - 1.0

    abs_d = abs(delta)
    if abs_d < 0.147:
        magnitude = "negligible"
    elif abs_d < 0.33:
        magnitude = "small"
    elif abs_d < 0.474:
        magnitude = "medium"
    else:
        magnitude = "large"

    return delta, magnitude


def wilson_score_interval(successes: int, total: int, confidence: float = 0.95) -> Tuple[float, float, float]:
    """
    Computes Wilson score confidence interval for binomial proportions.
    Returns (observed_proportion, lower_bound, upper_bound).
    """
    if total <= 0:
        raise ValueError("Total trials must be positive.")
    if successes < 0 or successes > total:
        raise ValueError("Successes must be between 0 and total.")

    # z value approximation for confidence
    z_table = {
        0.90: 1.644853,
        0.95: 1.959964,
        0.99: 2.575829,
    }
    z = z_table.get(confidence, 1.959964)

    p = successes / total
    denom = 1.0 + (z**2) / total
    center = (p + (z**2) / (2.0 * total)) / denom
    spread = (z * math.sqrt((p * (1.0 - p) + (z**2) / (4.0 * total)) / total)) / denom

    lower = max(0.0, center - spread)
    upper = min(1.0, center + spread)

    return p, lower, upper


def benjamini_hochberg(p_values: List[float], alpha: float = 0.05) -> List[Tuple[float, float, bool]]:
    """
    Applies Benjamini-Hochberg False Discovery Rate (FDR) procedure.
    Returns list of (original_p, adjusted_p, is_significant).
    """
    m = len(p_values)
    if m == 0:
        return []

    # Sort p-values with original indices
    indexed = sorted(enumerate(p_values), key=lambda x: x[1])
    adjusted = [0.0] * m

    # Calculate adjusted p-values from largest to smallest
    min_adj = 1.0
    for rank_minus_1, (orig_idx, p_val) in reversed(list(enumerate(indexed))):
        rank = rank_minus_1 + 1
        adj_p = min(1.0, (p_val * m) / rank)
        min_adj = min(min_adj, adj_p)
        adjusted[orig_idx] = min_adj

    results = []
    for p_val, adj_p in zip(p_values, adjusted):
        results.append((p_val, adj_p, adj_p <= alpha))

    return results


def main():
    parser = argparse.ArgumentParser(description="Empirical SE Non-Parametric Statistics Calculator.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # a12 parser
    p_a12 = subparsers.add_parser("a12", help="Compute Vargha-Delaney A12 effect size")
    p_a12.add_argument("--treatment", "-t", nargs="+", type=float, required=True, help="Treatment values")
    p_a12.add_argument("--control", "-c", nargs="+", type=float, required=True, help="Control values")

    # cliff parser
    p_cliff = subparsers.add_parser("cliff", help="Compute Cliff's delta")
    p_cliff.add_argument("--treatment", "-t", nargs="+", type=float, required=True, help="Treatment values")
    p_cliff.add_argument("--control", "-c", nargs="+", type=float, required=True, help="Control values")

    # wilson parser
    p_wilson = subparsers.add_parser("wilson", help="Compute Wilson score confidence interval")
    p_wilson.add_argument("--successes", "-s", type=int, required=True, help="Number of successes")
    p_wilson.add_argument("--total", "-n", type=int, required=True, help="Total trials")
    p_wilson.add_argument("--confidence", type=float, default=0.95, help="Confidence level (0.90, 0.95, 0.99)")

    # fdr parser
    p_fdr = subparsers.add_parser("fdr", help="Apply Benjamini-Hochberg FDR correction")
    p_fdr.add_argument("--p-values", "-p", nargs="+", type=float, required=True, help="List of raw p-values")
    p_fdr.add_argument("--alpha", type=float, default=0.05, help="Significance threshold (default: 0.05)")

    args = parser.parse_args()

    if args.command == "a12":
        val, mag = vargha_delaney_a12(args.treatment, args.control)
        print(f"Vargha-Delaney A12: {val:.4f} (magnitude: {mag})")

    elif args.command == "cliff":
        val, mag = cliffs_delta(args.treatment, args.control)
        print(f"Cliff's delta: {val:.4f} (magnitude: {mag})")

    elif args.command == "wilson":
        prop, low, high = wilson_score_interval(args.successes, args.total, args.confidence)
        print(f"Proportion: {prop:.4f} [{low:.4f}, {high:.4f}] ({int(args.confidence*100)}% Wilson CI)")

    elif args.command == "fdr":
        res = benjamini_hochberg(args.p_values, args.alpha)
        print(f"Benjamini-Hochberg FDR (alpha={args.alpha}):")
        for i, (orig, adj, sig) in enumerate(res):
            status = "SIGNIFICANT" if sig else "NOT significant"
            print(f"  Test {i+1}: p_raw = {orig:.4e}, p_adj = {adj:.4e} -> {status}")


if __name__ == "__main__":
    main()

