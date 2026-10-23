# Audit of Gemini's Collatz report

Date: 2026-10-23  
Subject: Axiom audit, affine contraction bound, and bounded-horizon obstruction

## Executive verdict

Gemini's central conclusion is right: the submitted CollatzLayerA proof depends on a false universally quantified trajectory-certificate axiom and an unproved base-case axiom. Its high-threshold counterexample is valid. The report also contains (i) a threshold inconsistency that does not apply to the exact source, (ii) an incorrect claimed affine-drift bound, and (iii) a broad no-go phrasing that should be restricted to fixed uniform horizons / prefix-count certificates.

This invalidates the submitted proof, not the Collatz conjecture.

## 1. Exact source statement and the threshold issue

I fetched and inspected `AIDoctrine/CollatzLayerA/CollatzLayerA_v8_1_FINAL.lean`. Its exact declaration is:

```lean
axiom odd_steps_certificate : ∀ n : ℕ, n ≥ 2 ^ 71 → n % 2 = 1 → n % 4 = 3 →
    ∃ k : ℕ, k > 0 ∧ k ≤ 200 ∧ odd_steps k n ≤ 44 ∧
      k - odd_steps k n ≥ 71
```

Therefore Gemini's concern that `n = 2^102 - 1` might fall outside the certificate's domain because it is below `2^109` does **not** apply to this source: the certificate axiom starts at `2^71`. The separate `base_case_109` axiom covers positive `n < 2^109`; it does not restrict the domain of `odd_steps_certificate`.

Nevertheless, Gemini's lifted example `n = 2^110 - 1` is also valid and has the benefit of exceeding `2^109`. Thus the certificate fails even for a hypothetical modified declaration with an additional `n ≥ 2^109` premise.

For either input, let `k0` be the exponent in `n = 2^k0 - 1`. Through at least the first 200 terms when `k0 ≥ 101`, the ordinary trajectory has alternating parity. Consequently, for each `1 ≤ K ≤ 200`,
`odd_steps(K,n) = ceil(K/2)` and `K - odd_steps(K,n) = floor(K/2)`. If the even-count lower bound is at least 71, then the odd count is also at least 71, contradicting the required odd count at most 44. This directly refutes `odd_steps_certificate`.

The second declared assumption, `base_case_109`, asserts convergence for every positive `n < 2^109`. It is an axiom in the source, not a theorem proved there. Evidence verifying a smaller finite range cannot discharge the larger range.

## 2. The multiplicative / additive contraction bridge

Gemini is correct that a valid prefix with `u ≤ 44`, `d ≥ 71`, and `n ≥ 2^71` would force descent. In particular,
`3^44 < 2^70`, so the multiplicative term is below `n/2`.

However, the report gives this bound as though it were universally valid:
`T^K(n) ≤ (3^u n + 3^u - 2^u)/2^d`.
That specific additive correction is false; the additive term depends on the placement of even steps within the parity word.

Counterexample: `n=11`, `K=6`:
`11 → 34 → 17 → 52 → 26 → 13 → 40`.
The first six terms contain `u=3` odd and `d=3` even values. The proposed right side is
`(3^3·11 + 3^3 − 2^3)/2^3 = 316/8 = 39.5`,
but `T^6(11)=40`. So the claimed upper bound fails.

A sufficient correct bound is
`T^K(n) ≤ (3^u/2^d)n + (3^u−1)/2`.
To see this, expand the trajectory as a composition of affine steps: an odd step has slope 3 and adds 1; an even step has slope 1/2 and adds 0. Each of the `u` additive contributions is multiplied by a suffix containing some number `r` of factors 3 and some factors 1/2, hence is at most `3^r`. The values of `r` across odd steps are `0,...,u−1`, so the total additive contribution is at most `1+3+...+3^(u−1)=(3^u−1)/2`.

With `u≤44` and `d≥71`,
`3^u/2^d ≤ 3^44/2^71 < 1/2`,
and
`(3^u−1)/2 < 2^69 ≤ n/4` for `n≥2^71`.
Therefore `T^K(n) < 3n/4 < n`. The affine bridge is sound under this valid bound; the false certificate premise is already fatal to the submitted proof.

## 3. Bounded-horizon obstruction: correct scope

The core construction is valid. For odd `n), write `n+1=q·2^ν` where `q` is odd and `ν=v₂(n+1)`. Direct induction gives
`T^(2j)(n)=3^j q·2^(ν−j)−1` for `0≤j≤ν`,
and for `j<ν` the odd-indexed values are
`T^(2j+1)(n)=3^(j+1)q·2^(ν−j)−2`.
The trajectory stays above the initial `n` through time `2ν`, reaching `T^(2ν)(n)=3^νq−1`. Also `T(x)≥x/2` for every positive integer, and
`(3^νq−1)/(2^νq−1) > (3/2)^ν`.
It follows that the strict-descent stopping time
`τ(n)=inf{k≥1:T^k(n)<n}`
satisfies
`τ(n) ≥ ceil((1+log₂3)ν)`
(with `τ(n)=∞` if no strict descent occurs). In particular, `τ(2^ν−1)` is unbounded as `ν` grows.

Thus **no single finite M can bound the strict-descent stopping time for every starting value**. Likewise, no prefix-count certificate scheme that requires a contracting-count witness within one fixed horizon M can cover every input.

This does **not** rule out a proof whose descent horizon depends on the input, an adaptive residue analysis, or a proof using a different invariant. The classical conjecture does not assert a uniform bound on the first time an iterate falls below its start. Calling the result an impossibility theorem for all finite-depth residue-class methods would be too broad. The explicit valuation argument is sufficient; invoking Hensel lifting is unnecessary for this specific claim.

A standalone proof of the stopping-time lower bound is recorded in `proofs/UNBOUNDED_STOPPING_TIME.md`.

## 4. Research consequence

A fixed horizon such as `K≤200` cannot be assumed to provide enough even terms to force contraction for every odd start. Any viable route must allow the horizon to grow with a parameter such as `v₂(n+1)`, or use a global argument that controls the entire trajectory. But long initial growth, and even eventual local contraction, still does not imply an iterate below the original start. The variable-horizon argument must explicitly control the trajectory after the forced initial run.

## Classification

- `odd_steps_certificate`: **Refuted** by an explicit parity-word family.
- `base_case_109`: **Assumed, not proved** in the submitted Lean source.
- Contraction bridge from a genuinely existing certificate: **Valid**, using a correct additive bound.
- Exact correction `(3^u−2^u)/2^d`: **Refuted as a universal bound**.
- Unbounded strict-descent stopping times: **Proven** by the `v₂(n+1)` argument.
- Universal Collatz convergence: **Still open**.
