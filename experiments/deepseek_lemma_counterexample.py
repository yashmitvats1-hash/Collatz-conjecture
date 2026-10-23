#!/usr/bin/env python3
"""Counterexample to the claim A_L > L log_2(3) implies U^L(n) < n.

This script verifies arithmetic in DeepSeek's proposed sufficient condition.
It does not disprove the Collatz conjecture.
"""

from __future__ import annotations

from math import log2


def accelerated_step(n: int) -> tuple[int, int]:
    """Return U(n)=(3n+1)/2^v2(3n+1) and the exact 2-adic valuation."""
    if n <= 0 or n % 2 == 0:
        raise ValueError("accelerated_step expects a positive odd integer")
    x = 3 * n + 1
    valuation = 0
    while x % 2 == 0:
        x //= 2
        valuation += 1
    return x, valuation


def main() -> None:
    n0 = 165
    n = n0
    cumulative_valuation = 0
    valuations: list[int] = []

    for _ in range(17):
        n, alpha = accelerated_step(n)
        valuations.append(alpha)
        cumulative_valuation += alpha

    assert valuations == [4, 1, 1, 1, 1, 2, 2, 1, 2, 1, 1, 2, 1, 1, 1, 2, 3]
    assert cumulative_valuation == 27
    assert 2**27 > 3**17
    assert cumulative_valuation > 17 * log2(3)
    assert n == 167
    assert n > n0

    gap = 2**cumulative_valuation - 3**17
    additive_term = 2**cumulative_valuation * n - 3**17 * n0
    assert additive_term == 1_106_233_681
    assert gap * n0 == 837_798_225
    assert additive_term > gap * n0

    print(f"start n = {n0}, L = 17")
    print(f"valuations = {valuations}")
    print(f"A_L = {cumulative_valuation}, L*log2(3) = {17 * log2(3):.12f}")
    print(f"2^A_L = {2**cumulative_valuation}, 3^L = {3**17}")
    print(f"U^L(n) = {n} (so the orbit increased by {n - n0})")
    print(f"S_L = {additive_term}")
    print(f"n*(2^A_L - 3^L) = {gap * n0}")
    print("PASS: counterexample to the proposed sufficient condition found.")
    print("This is not a counterexample to the Collatz conjecture.")


if __name__ == "__main__":
    main()
