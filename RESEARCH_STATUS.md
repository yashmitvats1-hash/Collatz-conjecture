# Research Status — 2026-10-23

## Objective

Prove the classical Collatz conjecture or obtain a rigorously verified counterexample. No complete proof is currently accepted in this project. This status is deliberately separate from claims made by individual proof attempts.

## Theorem under investigation

For positive integers, define
\[
T(n)=\begin{cases}n/2& n\text{ even},\\3n+1&n\text{ odd}.\end{cases}
\]
The conjecture asserts: for every n ≥ 1, some finite iterate T^k(n)=1.

A useful sufficient reduction is the **descent property**: for every n>1, there is an iterate k with T^k(n)<n. If this property held for all n>1, strong induction on n would prove the conjecture. Establishing that descent property universally is itself the hard unsolved step; it must not be presented as already known.

## Established baseline and sources

- David Barina's peer-reviewed Journal of Supercomputing article reports exhaustive computational verification through 2^71. This is a finite verified range, not a universal proof: https://link.springer.com/article/10.1007/s11227-025-07337-0
- Wolfram MathWorld's current Collatz entry reports a 2026 verification limit of approximately 2075·2^60 ≈ 2^71.02: https://mathworld.wolfram.com/CollatzConjecture.html
- Terence Tao's 2019/2022 result shows that for every function f(N) tending to infinity, almost every starting value in logarithmic density has an orbit that reaches below f(N). This is a major almost-everywhere theorem, not universal convergence to 1. See the paper: https://arxiv.org/abs/1909.03562
- Multiple public repositories found in a 2026 search advertise complete Lean proofs. They are **claims to audit**, not accepted solutions. See proof-audit records below.

## First candidate-proof audit: CollatzLayerA v8.1

Source repository: https://github.com/AIDoctrine/CollatzLayerA

Status: **Rejected as a proof of Collatz. One declared axiom is directly false; another is an unverified universal base-case assumption.**

The source defines the standard map T and an odd_steps(k,n) function counting odd-valued iterates among T^i(n), 0 ≤ i < k. It then assumes:

1. base_case_109: every positive n < 2^109 reaches 1. This is declared as an axiom, not proved in Lean, and exceeds the documented finite verification bound cited above.
2. odd_steps_certificate: for every n ≥ 2^71 with n odd and n ≡ 3 mod 4, there exists k ≤ 200 for which the first k iterates contain at most 44 odd terms and at least 71 even terms. This axiom is **false**. Take n = 2^102 − 1. Since the first 101 iterates of S(x)=(3x+1)/2 remain odd, the ordinary trajectory alternates odd/even through T^200(n). For any k ≤ 200, odd_steps(k,n)=ceil(k/2), while k−odd_steps(k,n)=floor(k/2). If the latter is at least 71, the former is also at least 71, contradicting the claimed upper bound of 44. This is proved in detail in proof_audit/AXIOM_AUDIT_COLLATZLAYERA.md.

Therefore the theorem collatz_conjecture in that file depends on an explicitly false axiom and does not constitute a proof. A file reporting zero sorry can still depend on unproved axiom declarations.

## Second candidate-proof audit: Mod-4 Structural Forcing

Source repository: https://github.com/iamkhayyam/the-collatz-conjecture

Status: **The repository's proof-status file itself says the bridge to universal convergence is incomplete.** It formalizes a lemma about the simple map S(n)=(3n+1)/2 and the absence of a positive integer whose entire S-orbit remains odd. This is not the Collatz conjecture. The repository identifies gaps in the paper's no-nontrivial-cycles and no-divergent-orbits arguments; see proof_audit/MOD4_SUBMISSION_AUDIT.md.

## Initial proven observation (not enough to prove Collatz)

For the simple map S(x)=(3x+1)/2, if its first m iterates S^0(n),...,S^m(n) are all odd, then
\[
S^j(n)=\frac{3^j(n+1)}{2^j}-1
\]
for 0 ≤ j ≤ m, and oddness forces n ≡ −1 (mod 2^{m+1}). Thus a fixed positive integer cannot have an infinite all-odd S-orbit. This only bounds runs in the auxiliary map; it does not prove that the actual Collatz orbit descends, because the artificial S-map and the ordinary map differ once an even S-iterate appears.

## DeepSeek's first report: exact formula and rejected descent lemma

Source artifact: DeepSeek's report supplied on 2026-10-23. Full audit: proof_audit/DEEPSEEK_REPORT_AUDIT.md.

The accelerated iterate identity
\[
U^L(n)=\frac{3^L n+S_L}{2^{A_L}},\qquad
S_L=\sum_{j=0}^{L-1}3^{L-1-j}2^{A_j}
\]
is correct for an odd starting value n and the actual valuation sequence.

However, the report's stated Lemma 2—that A_L > L log₂(3) alone ensures U^L(n)<n—is false. The exact criterion is
\[
U^L(n)<n\quad\Longleftrightarrow\quad
S_L<n(2^{A_L}-3^L).
\]
The coefficient condition 2^{A_L}>3^L is not enough because S_L is positive.

Explicit counterexample: starting at n=165, the 17 accelerated valuations are
(4,1,1,1,1,2,2,1,2,1,1,2,1,1,1,2,3), which sum to A₁₇=27. Since 2²⁷=134,217,728 > 3¹⁷=129,140,163, the report's condition holds; nevertheless U¹⁷(165)=167>165. The additive term is larger than the coefficient margin. This refutes the lemma, not the Collatz conjecture.

DeepSeek is correct that arbitrarily long *finite* valuation-one runs exist. For every r≥1, n=2^(r+1)−1 has α₀=...=αᵣ₋₁=1. The exact residue class is n≡−1 (mod 2^(r+1)); its density is 2^(-r) among odd inputs and 2^(-(r+1)) among all positive integers. Such examples do not show that a single trajectory has an infinite run.

The report audit has been logged in ARGUMENT_LEDGER.md and GitHub issue #4 asks DeepSeek to respond to the explicit counterexample and provide a corrected, non-circular bound.

## Claude's audit of the Mod-4 submission: direct-source confirmation

Full audit: proof_audit/CLAUDE_REPORT_AUDIT.md. I independently inspected the repository's Lean file and LaTeX source after Claude's report.

The auxiliary theorem E_empty is true but limited: for the simple map S(n)=(3n+1)/2, the consecutive odd-run length is exactly m=v₂(n+1). Indeed, while the values remain odd, S^j(n)+1=3^j(n+1)/2^j; values S^j(n) are odd for j<m and S^m(n) is even. Hence E is empty for the elementary reason v₂(n+1) is finite. That fact alone does not imply the ordinary Collatz orbit reaches 1: after the S-chain's even value, the S-map no longer tracks T, and the ordinary T-orbit merely halves to the next odd value.

The source's claimed bridge remains incomplete. Its Lean declarations no_nontrivial_cycles, no_divergent_orbits and collatz_convergence contain sorry. In addition, no_nontrivial_cycles is false as currently stated: it asserts that T^K(n)≠n for all n>2 and all K>0, but T^3(4)=4 under the standard map 4→2→1→4. The theorem must be reformulated to exclude nontrivial cycles without excluding the trivial 1-4-2 cycle.

The paper's ℓ≥2 descent estimate also fails as a general claim. For ℓ=2 and n*=4m−1 with odd m≡3 (mod 4), the next odd value after the simple S-chain's first even value is n'=(9m−1)/2=n*+(m+1)/2>n*. Examples include 11→34→17→52→26→13 and 27→82→41→124→62→31. This invalidates the asserted general next-odd-step descent estimate but does not prove those starting values have unbounded orbits, so it is not a counterexample to Collatz.

The direct source inspection supports Claude's main audit. We did not execute Lean locally or run #print axioms E_empty; the source's E_empty proof lies before the later sorry declarations, and a pinned-toolchain compile/axiom report remains a formal reproducibility task.

## Arena's first-round report: valuation words and local descent

Review and coordinator derivations: proofs/ARENA_001_VALUATION_DESCENT_REVIEW.md.
Independently implemented regression checks: experiments/valuation_descent_check_coordinator.py.

Arena's core caution is correct: a later contraction does not imply an iterate below the original start. The accelerated orbit 7→11→17→13 contracts on the last step but ends above 7.

The following infinite residue classes were proven by explicit arithmetic and independently regression-tested for all odd starts up to 100,000:
- n≡1 (mod 4), n>1: one accelerated step descends because U(n)≤(3n+1)/4<n.
- n≡3 (mod 16): two accelerated steps descend.
- n≡23 (mod 32): three accelerated steps descend.

For n=2^m−1, the first m−1 accelerated valuations are all one and U^j(n)=3^j·2^(m−j)−1>n for 1≤j≤m−1. Hence no strategy using only a fixed, bounded collection of initial valuation-word certificates can itself cover every start. This does not preclude adaptive or unbounded-depth arguments.

Independent regression checks passed for 7,000 tested affine-formula / endpoint-criterion cases, 34,374 starts in the explicit residue classes up to 100,000, and 255 long-run cases through m=256. These are finite tests, not proof of universal convergence. Arena's report also cites 340 valuation words and 540 run-exit samples; the full files it references were not yet present when the repository tree was inspected, so those specific figures and its general run-exit lemma remain pending independent reproduction. Arena has been asked to commit the exact proof and test sources.

## Current research tracks

1. Find a universal descent lemma for the ordinary Collatz map or the accelerated odd map.
2. Inspect 2026 claimed proofs by checking all axioms, definitions, dependencies, and actual target theorem.
3. Explore parity-vector / residue-class methods with explicit handling of long adverse parity runs.
4. Maintain independent Lean-checkable lemmas and counterexamples; never treat model agreement as proof.

## Status vocabulary

- **Proven:** complete mathematical argument with all premises justified.
- **Formalized:** checked by a proof assistant; still inspect axioms and theorem statement.
- **Finite computation:** exact, reproducible within an explicit finite range.
- **Conditional:** follows only under listed assumptions.
- **Heuristic:** evidence or intuition, not a proof.
- **Refuted:** at least one explicit counterexample invalidates the claim.
- **Open:** required lemma remains unproved.

**Overall status: Open. No complete proof or counterexample to the classical Collatz conjecture has been established in this project.**
