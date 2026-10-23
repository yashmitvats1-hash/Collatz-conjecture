#!/usr/bin/env python3
"""Check two explicit counterexamples to a claimed Collatz certificate.

The source axiom currently applies for n >= 2**71. The second test also
covers a hypothetical stronger lower cutoff n >= 2**109. This finite
regression supplements (but does not replace) the algebraic parity proof.
It does NOT disprove the Collatz conjecture.
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


def check_counterexample(label: str, n: int, cutoff: int) -> None:
    assert n >= cutoff
    assert n % 2 == 1
    assert n % 4 == 3

    for k in range(1, 201):
        odd = count_odd_iterates(k, n)
        even = k - odd
        # These inputs alternate parity through all 200 prefix terms.
        assert odd == (k + 1) // 2, (label, k, odd)
        assert even == k // 2, (label, k, even)
        assert not (odd <= 44 and even >= 71), (label, k, odd, even)

    print(f"{label}: n = {n}")
    print(f"  cutoff satisfied: n >= {cutoff}")
    print("  first 200 prefix terms alternate parity")
    print("  no k in [1, 200] has odd <= 44 and even >= 71")


def main() -> None:
    # This is already in the exact source axiom's n >= 2**71 domain.
    check_counterexample(
        "Original-domain counterexample",
        (1 << 102) - 1,
        1 << 71,
    )

    # This also defeats a hypothetical variant guarded by n >= 2**109.
    check_counterexample(
        "Higher-cutoff counterexample",
        (1 << 110) - 1,
        1 << 109,
    )

    print("PASS: both finite checks reject the claimed certificate.")
    print("The algebraic family proof establishes the claim for all prefixes.")
    print("These are counterexamples to the auxiliary axiom, not to Collatz.")


if __name__ == "__main__":
    main()
