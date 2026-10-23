# Arena Report Review: Valuation Words and Universal Descent

Date: 2026-10-23
Source: Arena's first-round report relayed by the project owner.
Coordinator review: core explicit residue-class claims checked algebraically and by independent finite regression tests.

## Verdict

Arena correctly keeps its universal conclusion open and identifies a central difficulty: a later contraction relative to the current iterate need not bring the orbit below the original starting value. The example
\[
7\to11\to17\to13
\]
under the accelerated odd map illustrates this.

The explicit descent claims for the residue classes n≡1 (mod 4), n≡3 (mod 16), and n≡23 (mod 32) are correct, with the domain n>1 and the accelerated map
\[
U(n)=\frac{3n+1}{2^{v_2(3n+1)}}\quad (n\text{ positive odd}).
\]

Arena's report refers to two repository deliverables, `proofs/ARENA_001_VALUATION_DESCENT.md` and `experiments/valuation_descent_check.py`, but these files were not present in the repository tree when checked. The report summary did not include the full valuation-word proof or precise general run-exit lemma. Thus the explicit claims below have been checked, but Arena's stated 340-word regression run and general run-exit lemma have not yet been independently reproduced. Arena is asked to commit the full source so these can be audited.

## 1. Exact accelerated valuation-word formula

Let n₀=n be positive odd. Set
\[
\alpha_i=v_2(3n_i+1),\qquad n_{i+1}=U(n_i),\qquad
A_j=\sum_{i=0}^{j-1}\alpha_i,\quad A_0=0.
\]
For every actual trajectory segment of length L≥1,
\[
U^L(n)=\frac{3^L n+S_L}{2^{A_L}},\qquad
S_L=\sum_{j=0}^{L-1}3^{L-1-j}2^{A_j}.
\]
This follows by iterating the affine recurrence 2^{α_i}n_{i+1}=3n_i+1. Equivalently, the numerator correction satisfies S₁=1 and S_{L+1}=3S_L+2^{A_L}.

For a fixed exact accelerated valuation word (α₀,…,α_{L−1}), its realizations among odd integers form one residue class modulo 2^{A_L+1}. In particular, that class has density 2^{-A_L} conditional on an odd input, and 2^{-(A_L+1)} among all positive integers. This is a congruence-cylinder fact; in the word length L, the modulus is determined by the total valuation A_L, not simply by 2^L. The report's missing full proof should still be supplied so this claim can be formalized and independently checked.

The exact necessary-and-sufficient endpoint condition is
\[
U^L(n)<n
\iff S_L<n(2^{A_L}-3^L).
\]
Consequently, the weaker condition 2^{A_L}>3^L alone is not sufficient; a direct counterexample appears in proof_audit/DEEPSEEK_REPORT_AUDIT.md.

## 2. Explicit residue-class descent lemmas

### Lemma A: n≡1 (mod 4), n>1

Write n=4k+1, where k≥1. Then 4 divides 3n+1, so
\[
U(n)\le\frac{3n+1}{4}<n
\]
because n>1. Thus every n>1 in this residue class descends in one accelerated step.

The exception n=1 must be excluded because U(1)=1.

### Lemma B: n≡3 (mod 16)

Write n=16k+3 with k≥0. Since v₂(3n+1)=1,
\[
U(n)=24k+5.
\]
The next accelerated image is
\[
U^2(n)=\frac{9k+2}{2^{v_2(9k+2)}}.
\]
Since 0< U²(n)≤9k+2<16k+3=n, every such n descends in at most two accelerated steps.

### Lemma C: n≡23 (mod 32)

Write n=32k+23 with k≥0. The first two valuations equal one, giving
\[
U(n)=48k+35,\qquad U^2(n)=72k+53.
\]
Then
\[
U^3(n)=\frac{27k+20}{2^{v_2(27k+20)}}.
\]
Since
\[
0<U^3(n)\le27k+20<32k+23=n,
\]
every such n descends in at most three accelerated steps.

These are exact infinite families. They are useful local lemmas but do not cover all odd starting values.

## 3. Finite-depth obstruction via n=2^m−1

For m≥2, let n=2^m−1. For 0≤j≤m−1 while the formulas apply,
\[
U^j(n)=3^j2^{m-j}-1.
\]
For each j<m−1, this value is 3 modulo 4, so the next valuation is one. Therefore the first m−1 accelerated valuations are all one, and
\[
U^j(n)>n\qquad(1\le j\le m-1),
\]
since (3/2)^j>1.

Given any fixed certificate depth D, choosing m>D prevents this starting value from descending within D initial accelerated steps. Thus a finite-depth strategy that only checks a bounded collection of initial-word certificates cannot on its own prove universal descent for every odd input. This is not a claim that one orbit has an infinite all-ones valuation word; m varies with the starting value.

## 4. Independent regression results

The coordinator independently checked the explicit residue-class statements for all odd starts up to 100,000. No failure was found. Also independently checked:
- n=165 has the DeepSeek counterexample U¹⁷(165)=167 with A₁₇=27;
- n=7 follows U: 7→11→17→13, so the last contraction does not give descent below the original start;
- n=2^m−1 has an initial run of valuation-one steps for the tested values of m.

These are finite regression checks accompanying the algebraic proofs above, not proof of universal convergence and not an independent replication of Arena's stated 340 valuation-word tests, 540 run-exit samples, or moduli-through-4096 check.

## 5. What is still missing

1. Arena should commit the full report and scripts it names so every statement, test count, and exact run-exit hypothesis is available.
2. The general run-exit lemma must state its full congruence conditions and exact inequality, then be proved from the valuation-word formula.
3. The unproved global bridge remains: even if every long all-ones run eventually exits, later contraction still must outweigh all earlier growth to put the iterate below the original start.
4. The complete descent theorem must cover every positive odd integer, not a finite collection of residue classes or only average/typical words.

## Status

- Exact iterate formula: **correct**.
- Residue classes 1 mod 4 (n>1), 3 mod 16, and 23 mod 32 descend: **proven by the explicit arguments here**.
- Arbitrarily long finite initial valuation-one runs: **proven**.
- Arena's broad run-exit lemma and stated 340/540 test suite: **awaiting the full committed source for independent audit**.
- Universal descent and the Collatz conjecture: **open**.
