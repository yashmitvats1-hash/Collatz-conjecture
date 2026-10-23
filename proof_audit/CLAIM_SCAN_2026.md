# 2026 Claim Scan: What to audit, what not to assume

Updated: 2026-10-23. This is a triage document, not a claim that all mathematical work in these sources is invalid.

## 1. CollatzLayerA v8.1

Source: https://github.com/AIDoctrine/CollatzLayerA

Advertises a complete Lean 4 proof. The actual source declares two axioms feeding the theorem: base_case_109 and odd_steps_certificate. The second is directly false for n=2^102−1; see AXIOM_AUDIT_COLLATZLAYERA.md. Therefore the main theorem does not establish the conjecture as written, regardless of the reported zero sorry messages.

## 2. Mod-4 Structural Forcing

Source: https://github.com/iamkhayyam/the-collatz-conjecture

The repo's own PROOF_STATUS.md distinguishes its machine-checked E_empty theorem from the incomplete bridge to universal Collatz convergence. The theorem concerns the simple S-map and all-odd S-orbits. It does not prove the ordinary Collatz orbit converges. See MOD4_SUBMISSION_AUDIT.md.

## 3. "Huts and 2-adic classification classes" claimed proof — retracted

Source: https://www.cambridge.org/engage/coe/article-details/6a5a2316d1922e37d591413b

As of the current search, the page carries a retraction notice. It says the author requested retraction because the induction fails to establish that the dynamical map is well-defined on hut equivalence classes, and does not show that all representatives transition uniformly to a lower class. Consequently, the key implication was unjustified. This exemplifies why an induction needs a well-defined quotient dynamics and a rank decrease for every representative, not just selected representatives.

## 4. Established results that do not prove universal convergence

- Barina's peer-reviewed computation verifies every starting value through 2^71: https://link.springer.com/article/10.1007/s11227-025-07337-0
- Tao's theorem is a major almost-everywhere result; it does not assert that every orbit reaches 1: https://arxiv.org/abs/1909.03562
- A 2026 research snapshot explicitly continues to mark the full Collatz obligation as open: https://www.gero.uz/research/collatz-map/

## Audit policy

A title, abstract, preprint DOI, model consensus, compilation success, or a theorem proved under axioms is not enough. For each submission, extract the exact final theorem, inspect the complete assumption list, test all translation steps between maps, and prove that every induction or ranking argument works for every object in its domain. Save concrete counterexamples to bad intermediate lemmas even when the main conjecture remains open.
