# DeepSeek Report Audit — 2026-10-23

Source: DeepSeek report supplied for Sprint 001.

## Executive result

**Lemma 1 (exact accelerated iterate formula): valid.**

**Lemma 2 (valuation-dominated descent as stated): false, including for a start n>1.** A concrete counterexample is n=165 after L=17 accelerated steps. This report is useful because it isolates the multiplicative drift and the exact affine correction; however, the additive term S_L cannot be discarded.

The classical Collatz conjecture remains open in this project.

## 1. Exact formula: checked

For odd n_0=n, let n_{i+1}=U(n_i)=(3n_i+1)/2^{α_i}, where α_i=v_2(3n_i+1)≥1, and A_j=Σ_{i<j} α_i with A_0=0. Iterating the affine recurrence gives

U^L(n) = (3^L n + S_L)/2^{A_L},

where S_L=Σ_{j=0}^{L-1} 3^{L-1-j} 2^{A_j}.

This is correct. The equivalent recurrence S_{L+1}=3S_L+2^{A_L}, S_1=1, verifies the formula by induction. It gives an exact handle on the additive correction.

## 2. Lemma 2 is false as written

DeepSeek claims that A_L > L log₂(3), equivalently 2^{A_L}>3^L, is by itself sufficient to conclude U^L(n)<n. The correct rearrangement is

U^L(n)<n
iff 3^L n+S_L < 2^{A_L}n
iff S_L < n(2^{A_L}-3^L).

Thus 2^{A_L}>3^L only makes the coefficient of n negative in the difference. It does **not** ensure that the positive additive term S_L is smaller than the available margin.

### Explicit counterexample (n=165, L=17)

The accelerated trajectory and valuations are:

| i | n_i | α_i = v₂(3n_i+1) | n_{i+1} |
|---:|---:|---:|---:|
| 0 | 165 | 4 | 31 |
| 1 | 31 | 1 | 47 |
| 2 | 47 | 1 | 71 |
| 3 | 71 | 1 | 107 |
| 4 | 107 | 1 | 161 |
| 5 | 161 | 2 | 121 |
| 6 | 121 | 2 | 91 |
| 7 | 91 | 1 | 137 |
| 8 | 137 | 2 | 103 |
| 9 | 103 | 1 | 155 |
| 10 | 155 | 1 | 233 |
| 11 | 233 | 2 | 175 |
| 12 | 175 | 1 | 263 |
| 13 | 263 | 1 | 395 |
| 14 | 395 | 1 | 593 |
| 15 | 593 | 2 | 445 |
| 16 | 445 | 3 | 167 |

The valuations sum to A₁₇=27. Numerically,

- 2²⁷ = 134,217,728;
- 3¹⁷ = 129,140,163;
- therefore 2²⁷ > 3¹⁷ and 27 > 17 log₂(3);
- nevertheless U¹⁷(165)=167>165.

The exact identity has S₁₇ = 1,106,233,681, while
165(2²⁷−3¹⁷)=837,798,225. The required inequality S₁₇ < 165(2²⁷−3¹⁷) fails. This refutes Lemma 2 as stated, without contradicting the Collatz conjecture.

## 3. Correct usable statement

For a fixed actual accelerated trajectory segment of length L, the exact criterion is

U^L(n)<n iff S_L < n(2^{A_L}−3^L).

In particular, the condition A_L > L log₂(3) is necessary for descent in this affine expression but is not sufficient. A sufficient condition is the strict inequality above (or an independently proved upper bound for S_L that implies it). The latter must not simply be renamed as already proven.

This also corrects the report's concluding reduction: proving that A_L crosses the line L log₂(3) at least once is not enough. The proof must control the additive correction S_L as well, or establish a stronger margin that dominates it.

## 4. Long runs of valuation-one steps: checked, with precision note

The report's underlying point is correct: arbitrarily long finite strings α_i=1 are realizable. A precise construction is n=2^{r+1}−1 (and more generally n≡−1 mod 2^{r+1}). For j≤r, as long as the first j valuations are one,

U^j(n)=3^j(n+1)/2^j−1.

For j<r, the term 3^j(n+1)/2^j is divisible by 4, so U^j(n)≡3 mod 4 and the next valuation is 1. Thus α_0=…=α_{r−1}=1. During this segment A_r=r and U^r(n)=2·3^r−1 for the minimal representative.

Density convention: this is one residue class modulo 2^{r+1}. It has natural density 2^{-(r+1)} among all positive integers, or density 2^{-r} conditional on n being odd. The report should specify which density it means. Its mention of a modulus 2^r for this exact condition appears to be off by one: the direct congruence is n≡−1 mod 2^{r+1}.

This construction proves that long upward segments exist; it does not prove that any single trajectory has arbitrarily long such segments, nor that a trajectory fails to descend.

## 5. Additional wording that needs refinement

- A “unique residue class modulo 2^L” is correct for a specified ordinary parity word of length L under the usual parity-vector formulation. For a prescribed accelerated valuation word (α_0,…,α_{L−1}), the relevant modulus is tied to the total valuation A_L, not generally just 2^L. Keep ordinary parity words and accelerated valuation words distinct.
- Average valuation E[α_i]=2 under a geometric/uniform model is an average-model statement. It cannot be applied as a deterministic guarantee on every trajectory without a separate proof.
- Tao's result is an almost-everywhere result about orbit minima approaching arbitrarily slowly growing bounds; it is not universal convergence for every start.
- The report's note that Lean had a kernel soundness issue in 2026 is factually supported by the Lean developers' 1 August 2026 postmortem: an AI-assisted sorry-free apparent Collatz disproof exploited a kernel bug, which was fixed. This is a reason for toolchain hygiene, not evidence against sound Lean proofs built and rechecked with the fixed toolchain.
- The report refers to a “Universal Drift Invariant” retraction without a source name or citation in the provided text. That particular claim should stay unverified until the exact document/retraction is identified.

## 6. What we should ask DeepSeek next

1. Acknowledge or refute the explicit n=165, L=17 counterexample.
2. Replace Lemma 2 with the exact inequality S_L < n(2^{A_L}−3^L), and provide a genuinely non-circular bound on S_L that can imply it.
3. State whether its “prescribed-parity residue class” discussion refers to ordinary parity words or accelerated valuation words, and give the exact modulus and density in each case.
4. Propose a run-control theorem that applies to every individual starting value, not merely typical values or all finite patterns collectively.

## Status

- Lemma 1: **verified correct**.
- Lemma 2 as written: **refuted by n=165, L=17**.
- Long finite runs α_i=1: **proved realizable for arbitrary lengths**.
- Universal descent/convergence: **still open**.
