# Mathematical Target 001: Universal Descent

## Target lemma

For every integer n>1, there exists k≥1 such that T^k(n)<n, where T is the ordinary Collatz map.

This lemma would imply the conjecture by strong induction: assume all positive m<n eventually reach 1. Choose k with T^k(n)=m<n. If m≥1, the induction hypothesis gives j with T^j(m)=1, so T^{k+j}(n)=1. (If an iterate reaches 0 this would need separate handling, but T maps positive integers to positive integers, so it does not.)

The target is not an easier equivalent reformulation unless we find an independent reason to establish it. The open obligation is precisely to prove descent for every n>1.

## Auxiliary map and exact affine formula

For odd x, define S(x)=(3x+1)/2. While all values S^0(n),...,S^m(n) remain odd, each step agrees with two ordinary Collatz steps:
\[
T^2(x)=S(x)\quad\text{for odd }x.
\]
Under that all-odd hypothesis, induction gives
\[
S^j(n)+1=\frac{3^j(n+1)}{2^j},\qquad 0\le j\le m.
\]
Since 3 is invertible modulo every power of 2, oddness of S^m(n) implies 2^(m+1) divides n+1, hence n≡−1 mod 2^(m+1).

Consequences:
1. A fixed positive n cannot have S^j(n) odd for every j.
2. This does **not** produce a uniform bound independent of n: examples n=2^r−1 realize long all-odd runs.
3. It does **not** imply universal descent. Before the auxiliary S-orbit first becomes even, the values can rise. After that point, S is not the ordinary Collatz map on the even input.

## Why residue covers are not automatically proofs

For a fixed finite parity word, an iterate of T has an affine form whose leading coefficient is a power of 3 divided by a power of 2. A word with a contracting coefficient gives descent for sufficiently large starts in its residue class, but a complete proof must cover every start, all noncontracting words, and every threshold without a gap. Showing that most residue words contract is not enough: the uncovered exceptional words must be ruled out, not assumed statistically negligible.

## Next deliverable

Each agent should either:
- prove an explicit new lemma implying descent, with every quantifier covered; or
- identify a precise obstruction to a proposed route and deliver a smaller surviving theorem.

Do not relabel the target lemma as proven until its full universal quantifier has a complete proof.
