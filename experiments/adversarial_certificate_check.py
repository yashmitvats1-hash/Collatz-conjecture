#!/usr/bin/env python3
"""Reproduce the counterexample to a claimed auxiliary certificate.

This does NOT disprove the Collatz conjecture. It checks a universally quantified
axiom used by the public repository AIDoctrine/CollatzLayerA.
"""

from __future__ import annotations


def collatz(n: int) -> int:
    """One step of the ordinary Collatz map."""
    return n // 2 if n % 2 == 0 else 3 * n + 1


def count_odd_iterates(k: int, n: int) -> int:
    """Count odd values among n, T(n), ..., T^(k-1)(n)."""
    count = 0
    x = n
    for _ in range(k):
        count += x % 2
        x = collatz(x)
    return count


def main() -> None:
    # The alleged axiom applies to every odd n >= 2**71 with n == 3 (mod 4).
    m = 102
    n = (1 << m) - 1
    assert n >= (1 << 71)
    assert n % 2 == 1
    assert n % 4 == 3

    for k in range(1, 201):
        odd = count_odd_iterates(k, n)
        even = k - odd
        # The ordinary orbit alternates odd/even for these first 200 steps.
        assert odd == (k + 1) // 2, (k, odd)
        assert even == k // 2, (k, even)
        # Hence no k can meet both requirements in odd_steps_certificate.
        assert not (odd <= 44 and even >= 71), (k, odd, even)

    print(f"n = 2^{m} - 1 = {n}")
    print("Input conditions for the alleged axiom: all satisfied.")
    print("First 200 iterates: 100 odd and 100 even.")
    print("No k in [1, 200] satisfies odd <= 44 and even >= 71.")
    print("PASS: counterexample to the auxiliary certificate found.")
    print("This is not a counterexample to the Collatz conjecture.")


if __name__ == "__main__":
    main()
