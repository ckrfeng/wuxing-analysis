#!/usr/bin/env python3
"""Independent exact origin determinant/rank corroboration for A03.

Uses Python's standard library only. Run from any working directory:
    python3 /path/to/exact_origin_check.py

The sibling exact_origin_results.json is replaced with the deterministic
results. These finite checks corroborate, but do not replace, the universal
proofs in A03. No positive-state spectrum or nonlinear dynamics is computed.
"""

from collections import Counter
from fractions import Fraction
from itertools import permutations
import json
from pathlib import Path


def sparse_characteristic_terms(n):
    """Expand det(u I - c P) by Leibniz, P[i,j]=1 iff j=i-1 mod n.

    Monomials are represented by (u_degree, c_degree). The spectral formula
    is not used to generate the expansion.
    """
    terms = Counter()
    surviving_count = 0
    for perm in permutations(range(n)):
        diagonal_count = 0
        predecessor_count = 0
        for i, j in enumerate(perm):
            if j == i:
                diagonal_count += 1
            elif j == (i - 1) % n:
                predecessor_count += 1
            else:
                break
        else:
            inversions = sum(
                perm[i] > perm[j]
                for i in range(n)
                for j in range(i + 1, n)
            )
            sign = (-1) ** (inversions + predecessor_count)
            terms[(diagonal_count, predecessor_count)] += sign
            surviving_count += 1
    return terms, surviving_count


def rank_origin_at_a2_c1(n, g):
    """Exact row reduction of J=(2-g) I + P using rational arithmetic."""
    matrix = [
        [
            Fraction((2 - g) * (i == j) + ((i - 1) % n == j))
            for j in range(n)
        ]
        for i in range(n)
    ]
    rank = 0
    for column in range(n):
        pivot = next(
            (i for i in range(rank, n) if matrix[i][column]), None
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        divisor = matrix[rank][column]
        matrix[rank] = [value / divisor for value in matrix[rank]]
        for i in range(n):
            if i != rank and matrix[i][column]:
                multiplier = matrix[i][column]
                matrix[i] = [
                    value - multiplier * pivot_value
                    for value, pivot_value in zip(matrix[i], matrix[rank])
                ]
        rank += 1
    return rank


def require(condition, message):
    """Keep check failures active even if Python is invoked with -O."""
    if not condition:
        raise AssertionError(message)


def main():
    results = []
    for n in (5, 6, 8):
        terms, surviving_count = sparse_characteristic_terms(n)
        require(
            terms == {(n, 0): 1, (0, n): -1},
            f"Unexpected characteristic terms for n={n}: {terms}",
        )
        require(surviving_count == 2, f"Unexpected permutation count for n={n}")
        ranks = {str(g): rank_origin_at_a2_c1(n, g) for g in (1, 3)}
        require(ranks["3"] == n - 1, f"Incorrect boundary rank for n={n}")
        require(
            ranks["1"] == (n - 1 if n % 2 == 0 else n),
            f"Incorrect alternating/odd-control rank for n={n}",
        )
        results.append(
            {
                "n": n,
                "leibniz_terms": [
                    {"u_degree": u, "c_degree": c, "coefficient": coefficient}
                    for (u, c), coefficient in sorted(terms.items())
                ],
                "surviving_permutation_count": surviving_count,
                "rank_J_at_a2_c1_by_g": ranks,
            }
        )
    output = {
        "method": "Independent sparse Leibniz determinant and Fraction Gaussian elimination",
        "results": results,
    }
    serialized = json.dumps(output, indent=2) + "\n"
    destination = Path(__file__).resolve().with_name("exact_origin_results.json")
    destination.write_text(serialized, encoding="utf-8")
    print(serialized, end="")


if __name__ == "__main__":
    main()
