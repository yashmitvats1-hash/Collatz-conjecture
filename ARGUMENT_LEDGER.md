# Argument Ledger

Last updated: 2026-10-23

This ledger is a record of mathematical obligations, not a percentage-complete meter.

| ID | Claim / obligation | Status | Evidence / next action |
|---|---|---|---|
| L-001 | Every positive integer reaches the 1-4-2 cycle | **Open** | Classical Collatz conjecture; no proof in this project. |
| L-002 | Universal descent: every n>1 has some k with T^k(n)<n | **Open; sufficient for L-001** | Strong induction would prove L-001 if L-002 were established. Need prove the descent property, not assume it. |
| L-003 | CollatzLayerA v8.1 proves L-001 | **Refuted as submitted** | proof_audit/AXIOM_AUDIT_COLLATZLAYERA.md. Its odd_steps_certificate axiom fails for n=2^102−1. |
| L-004 | base_case_109 is justified by existing verification | **Unsupported** | Declared as an axiom for every 0<n<2^109. Published verification cited here is through 2^71. A finite-range axiom needs an independently reproducible certificate covering its claimed range. |
| L-005 | Mod-4 Structural Forcing proves L-001 | **Not established** | proof_audit/MOD4_SUBMISSION_AUDIT.md. Its own PROOF_STATUS.md leaves cycle/divergence bridge lemmas incomplete. |
| L-006 | No positive integer's entire S(n)=(3n+1)/2 orbit stays odd | **Auxiliary lemma; formalized in candidate repo** | Potentially useful residue descent for the artificial S-map; it does not alone imply descent under ordinary T. Rebuild/audit theorem and domain independently. |
| L-007 | Long all-odd runs under S force n≡−1 mod 2^(m+1) | **Proven elementary lemma** | If S^0(n),...,S^m(n) are odd, S^j(n)+1=3^j(n+1)/2^j and therefore 2^(m+1) divides n+1. This rules out an infinite such run for fixed n but gives no universal T-descent. |
| L-008 | Positive mean/logarithmic drift implies every deterministic orbit descends | **Invalid inference without additional proof** | Average-case distribution estimates do not automatically control every exceptional orbit. Need uniform deterministic bounds or a separate theorem excluding all exceptional orbits. |
| L-009 | DeepSeek Lemma 1: exact accelerated iterate formula | **Verified** | proof_audit/DEEPSEEK_REPORT_AUDIT.md. The affine recurrence and formula for S_L are correct. |
| L-010 | DeepSeek Lemma 2: A_L>L log₂(3) alone guarantees U^L(n)<n | **Refuted** | Counterexample n=165, L=17: A_17=27 and 2^27>3^17, but U^17(165)=167>165. The additive term matters; see the full audit. |
| L-011 | Arbitrarily long finite runs with v₂(3n+1)=1 are realizable | **Proven** | For any r≥1, n=2^(r+1)−1 has first r accelerated valuations equal to 1. This does not imply a single orbit has infinite such runs or disprove Collatz. |

## Required evidence before upgrading status

- Every theorem statement is copied exactly, including domain, quantifiers, map, and iteration convention.
- Every dependency is proven or independently cited with hypotheses checked.
- Every Lean file is checked for axioms, sorryAx, imported assumptions, and the exact target theorem.
- Computational claims specify executable source, exact limits, integer widths, overflow policy, validation strategy, and reproducibility.
- A different agent tries to break every candidate proof before it is accepted.
