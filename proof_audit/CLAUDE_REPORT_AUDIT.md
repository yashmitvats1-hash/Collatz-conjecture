# Claude Report Audit — direct source inspection

Date: 2026-10-23
Source report: Claude's audit of the Mod-4 Structural Forcing submission.
Repository audited directly: https://github.com/iamkhayyam/the-collatz-conjecture

## Overall verdict

Claude's principal conclusions check out, and direct inspection of `LeanProofs/Basic.lean` and `Collatz Conjecture v4/Wakil_Collatz_v4.tex` reveals an additional straightforward falsity in the stated cycle theorem: the Lean declaration `no_nontrivial_cycles` asserts an implication that is contradicted by the standard 1→4→2→1 cycle. It is marked `sorry`, so it is not proved; but its theorem statement is itself too strong.

The proposed Collatz proof is not valid. The auxiliary theorem `E_empty` is a true, narrowly scoped theorem about the simple auxiliary map, and does not imply classical Collatz convergence.

## 1. The exact statement of E_empty

In Basic.lean:
- `Smap (n : ℕ) := (3 * n + 1) / 2` is defined on all naturals using natural-number division.
- `inE n` means `Odd n ∧ ∀ k, Odd (Smap^[k] n)`.
- `E_empty` states `∀ n : ℕ, ¬ inE n`.

For odd x,
\[
S(x)+1=\frac{3(x+1)}2.
\]
While the successive S-values are odd, induction gives
\[
S^j(n)+1=\frac{3^j(n+1)}{2^j}.
\]
Let m=v₂(n+1). For every j<m, the right-hand side is even, so S^j(n) is odd. At j=m it is odd, so S^m(n) is even. Thus the number of consecutive odd terms starting with S⁰(n) is exactly v₂(n+1), a finite integer. This proves E=∅ directly.

In particular, n=2^r−1 has a run of length r. Hence there is no uniform upper bound on run length across all inputs. This elementary fact is fully consistent with the long-run counterexample found in our first axiom audit.

Direct source inspection confirms that E_empty and its dependencies occur before the later bridge theorems, which are each explicitly left as `sorry`. I did not run Lean locally or run `#print axioms E_empty`; a toolchain-level axiom report remains a reproducibility check.

## 2. Why E_empty does not imply Collatz

The auxiliary S-map agrees with two ordinary Collatz steps only when the input to S is odd:
\[
T^2(x)=S(x)\quad\text{for odd }x.
\]
Once S^j(n) first becomes even, subsequent S-iterations are not the ordinary Collatz orbit. The actual T-orbit instead halves the even value until it reaches the next odd value (or 1). It has not generally reached 1.

Example: n=7 gives S-values 7→11→17→26, where the first even value is 26. The ordinary orbit corresponds through this point to 7→22→11→34→17→52→26, then halves to 13. The property that S eventually becomes even gives no conclusion that the ordinary orbit has reached 1.

Therefore the paper's assertion that E=∅ is equivalent to the Collatz conjecture is false. Since E=∅ follows just from v₂(n+1)<∞ for each fixed n, using it as the main bridge to universal convergence would otherwise turn a simple valuation identity into a proof of the famous open problem.

## 3. The no-divergence argument: the ℓ≥2 descent claim fails

The paper chooses an odd minimum n* of the putative set F of odd starts whose ordinary T-orbits are unbounded. If the simple S-chain has exactly ℓ initial odd values, then
\[
n^*=2^\ell m-1,\qquad m\text{ odd},\qquad S^\ell(n^*)=3^\ell m-1.
\]
This final value is even. Let j=v₂(3^ℓm−1); after halving it, the next odd value is
\[
n'=(3^\ell m-1)/2^j.
\]

For ℓ=2, take any odd m≡3 (mod 4). Then 9m−1≡2 (mod 4), so j=1, and
\[
n^*=4m-1,\qquad n'=(9m-1)/2.
\]
But
\[
n'-n^* = (m+1)/2>0.
\]
Therefore there are infinitely many such n* (equivalently n*≡11 mod 16) for which the next odd value after the first even S-iterate is *larger*, not smaller. Examples are 11→34→17→52→26→13 and 27→82→41→124→62→31 in ordinary T, where the next odd values 13>11 and 31>27.

This refutes the paper's general assertion that for all sufficiently large n* the next odd value must be below n*, as derived from the displayed coefficient estimate. In the LaTeX, the factor is
\[
\frac{3^\ell}{2^{\ell+1}}=\frac12(3/2)^\ell.
\]
It increases with ℓ, rather than decreasing; it equals 9/8 at ℓ=2 and is greater than 1 for every ℓ≥2. The claimed coefficient-based descent estimate cannot work.

Qualification: these examples refute the asserted universal next-odd-step descent statement; by themselves they do **not** prove these n* have unbounded orbits, so they are not counterexamples to the Collatz conjecture or a direct refutation of the conditional minimal-element claim restricted to F. They show that the paper has not established its required inequality for every input.

The paper's subsequent remark tries to replace this gap by an argument that refers back to E_empty and no_nontrivial_cycles. That does not repair the proof: E_empty only proves a finite S-run, and no_nontrivial_cycles is itself unproved and has an overstrong statement (next section).

## 4. The cycle theorem declaration is itself false as stated

Basic.lean declares:
`no_nontrivial_cycles (n) (hn : n > 2) (K) (hK : K > 0) : collatz^[K] n ≠ n`.

But `collatz` is the ordinary Collatz map, for which
\[
4\to2\to1\to4.
\]
Thus `collatz^[3] 4 = 4`, with 4>2 and 3>0. The declared proposition would imply this is unequal to 4, which is false. The declaration is filled by `sorry` and therefore the file has not proved it. The paper's wording that the only cycle containing 1 is 1→2→1 is likewise inconsistent with its own ordinary-map definition; the standard cycle is 1→4→2→1.

A valid theorem would need to exclude cycles disjoint from the known trivial cycle, with an exact statement ensuring it does not accidentally exclude the 1–4–2 cycle. That corrected theorem would still need proof.

## 5. Other source-scope checks

- The actual Lean source does have `sorry` in `no_nontrivial_cycles`, `no_divergent_orbits`, and `collatz_convergence`, as Claude reported from PROOF_STATUS.md.
- `no_divergent_orbits` is stated as boundedness of every T-orbit. The crucial ℓ≥2 argument in the paper is not established by the written threshold argument, the finite verification range, or the subsequent circularly connected remark.
- The assertion about density is correct with the convention made explicit: the class n≡−1 mod 2^(r+1) has density 2^−(r+1) among all positive integers, or 2^−r conditional on odd starts.
- I have not independently compiled the repository or run `#print axioms E_empty`. The narrow mathematical identity above independently verifies the theorem's content, but Lean/kernel provenance should be recorded separately.

## Status ledger

| Claim | Status |
|---|---|
| E_empty: no infinite all-odd S-chain | True elementary auxiliary theorem; source gives a Lean proof before the bridge `sorry`s |
| E_empty implies classical Collatz | False |
| No nontrivial cycles as declared in Lean | False theorem statement; contradicted by n=4, K=3 |
| No divergence, ℓ=1 case | Valid local descent calculation |
| No divergence, ℓ≥2 general descent | Invalid as stated; explicit infinite family of increases |
| collatz_convergence | Not proved in this submission |
| Overall paper's complete-proof claim | Not established |

## Next actions

1. Keep the source theorem E_empty, but state it narrowly and preferably also present the direct valuation proof.
2. Mark `no_nontrivial_cycles` as false as currently quantified (not merely missing a proof).
3. Ask Claude to confirm the n=4, K=3 falsification and the infinite ℓ=2 family, and whether any additional source-level defect remains.
4. Continue the universal-descent proof search independently of this paper.
