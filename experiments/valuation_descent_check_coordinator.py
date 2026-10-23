#!/usr/bin/env python3
"""Independent regression checks for Arena's explicit valuation-descent claims.

These checks do not prove the Collatz conjecture. They are finite tests of
specific algebraic lemmas and examples; see proofs/ARENA_001_VALUATION_DESCENT.md.
"""

from __future__ import annotations


def v2(x: int) -> int:
    if x <= 0:
        raise ValueError("v2 requires a positive integer")
    count = 0
    while x % 2 == 0:
        count += 1
        x //= 2
    return count


def accelerated_step(n: int) -> tuple[int, int]:
    if n <= 0 or n % 2 == 0:
        raise ValueError("accelerated_step expects a positive odd integer")
    x = 3 * n + 1
    a = v2(x)
    return x // (1 << a), a


def accelerated_iterate(n: int, length: int) -> tuple[int, list[int], list[int]]:
    """Return U^length(n), valuations, and cumulative A_j for j=0..length."""
    x = n
    valuations: list[int] = []
    cumulative = [0]
    for _ in range(length):
        x, a = accelerated_step(x)
        valuations.append(a)
        cumulative.append(cumulative[-1] + a)
    return x, valuations, cumulative


def verify_affine_formula(n: int, length: int) -> None:
    end, _alphas, A = accelerated_iterate(n, length)
    S = sum(3 ** (length - 1 - j) * (1 << A[j]) for j in range(length))
    numerator = 3**length * n + S
    denominator = 1 << A[length]
    assert numerator % denominator == 0
    assert numerator // denominator == end
    assert (end < n) == (S < n * (denominator - 3**length))


def verify_residue_classes(limit: int = 100_000) -> int:
    checked = 0
    for n in range(3, limit + 1, 2):
        depth = None
        if n % 4 == 1:
            depth = 1
        elif n % 16 == 3:
            depth = 2
        elif n % 32 == 23:
            depth = 3
        if depth is None:
            continue
        end, _, _ = accelerated_iterate(n, depth)
        assert end < n, (n, depth, end)
        checked += 1
    return checked


def verify_long_one_valuation_runs(max_m: int = 256) -> int:
    checked = 0
    for m in range(2, max_m + 1):
        start = (1 << m) - 1
        x = start
        for j in range(m - 1):
            x, a = accelerated_step(x)
            assert a == 1, (m, j, a)
            assert x == 3 ** (j + 1) * (1 << (m - j - 1)) - 1
            assert x > start, (m, j, start, x)
        checked += 1
    return checked


def main() -> None:
    # Verify the affine identity and exact endpoint criterion on many starts.
    formula_cases = 0
    for n in range(1, 1000, 2):
        for length in range(1, 15):
            verify_affine_formula(n, length)
            formula_cases += 1

    residue_cases = verify_residue_classes()
    run_cases = verify_long_one_valuation_runs()

    # DeepSeek counterexample: the multiplier condition holds, but U^17(165)>165.
    end, alpha, A = accelerated_iterate(165, 17)
    assert sum(alpha) == 27
    assert A[-1] == 27
    assert 2**27 > 3**17
    assert end == 167 > 165

    # Arena's local-contraction warning: final step contracts, but not below 7.
    start = 7
    vals = [start]
    x = start
    for _ in range(3):
        x, _ = accelerated_step(x)
        vals.append(x)
    assert vals == [7, 11, 17, 13]
    assert vals[-1] < vals[-2] and vals[-1] > start

    print(f"PASS: affine identity + endpoint criterion ({formula_cases} cases)")
    print(f"PASS: explicit residue-class descent ({residue_cases} starts <= 100000)")
    print(f"PASS: long valuation-one runs (m=2..{run_cases + 1})")
    print("PASS: n=165, L=17 defeats the multiplier-only descent condition")
    print("PASS: 7 -> 11 -> 17 -> 13 illustrates local contraction without global descent")
    print("These are finite regression tests, not a proof of universal convergence.")


if __name__ == "__main__":
    main()
