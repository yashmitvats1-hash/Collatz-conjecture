# Team Kickoff and Work Orders

Date opened: 2026-10-23

## Project introduction (send to every agent)

We are investigating the classical Collatz conjecture:
\[
T(n)=\begin{cases} n/2 & n\text{ even},\\3n+1 & n\text{ odd},\end{cases}
\qquad
\forall n\ge1\ \exists k\ge0:T^k(n)=1.
\]
The objective is a rigorous proof. The conjecture remains open in the established mathematical literature; do not claim success because several models agree, a program passes finite tests, or a Lean file compiles. A formal proof depending on an unproved axiom has not proved the conjecture.

I (ChatGPT) will act as coordinator and red-team proof auditor. The shared repository is https://github.com/yashmitvats1-hash/Collatz-conjecture. Read README.md and RESEARCH_STATUS.md before doing work. Our first priority is to identify valid lemmas and eliminate false proof routes, then develop new arguments.

## Arena — independent proof architecture

Work independently of the other agents at first. Identify one or two promising proof strategies and derive a concrete theorem that would imply universal convergence. Prefer a small, exact lemma over a large speculative framework. For every proposed lemma, give full definitions, hypotheses, a line-by-line proof, and explain why it is not equivalent to assuming Collatz itself. Try the odd-only/Syracuse map, descent via strong induction, parity-vector/2-adic arguments, and residue-class descent covers. Do not merely list known approaches. Include the strongest counterargument to your own proposal.

## Gemini — adversarial audit of CollatzLayerA v8.1

Independently audit https://github.com/AIDoctrine/CollatzLayerA, starting with the Lean file CollatzLayerA_v8_1_FINAL.lean, its declarations of base_case_109 and odd_steps_certificate, and the main theorem dependency graph. Determine the precise theorem Lean actually proves when axioms are admitted. Test the certificate against deliberately adversarial inputs, particularly n = 2^m - 1, whose early ordinary-Collatz parities alternate odd/even. Return exact Lean or arithmetic witnesses for every failed claim. Do not accept probabilistic drift as a deterministic universal bound.

## Claude — independent audit of the Mod-4 Structural Forcing submission

Audit https://github.com/iamkhayyam/the-collatz-conjecture. Distinguish the fully formalized lemma E_empty (about the simple map S(n)=(3n+1)/2 having no forever-all-odd orbit) from the classical Collatz conjecture. Study PROOF_STATUS.md, identify the exact gaps in no_nontrivial_cycles, no_divergent_orbits, and collatz_convergence, and independently check whether the paper's bridge is circular or incomplete. Return a theorem dependency diagram and a minimal counterexample to any invalid inference. Also suggest a correct formalization target that provides progress without asserting Collatz outright.

## DeepSeek — number-theoretic proof search and literature audit

Develop an independent descent-based strategy. Analyze the accelerated odd map Syr(n)=(3n+1)/2^{v_2(3n+1)} and the exact affine formula for a fixed parity/valuation word. Identify what a finite residue-class cover must prove and why positive average drift cannot simply be promoted to every orbit. Search for a novel elementary lemma, with a complete proof or a sharply defined open subproblem. Independently assess all claimed complete Collatz proofs found online in 2026; prioritize their actual hypotheses, axioms, and theorem statements rather than abstracts.

## Coordinator (ChatGPT) — work orders

1. Maintain the repository status and references.
2. Independently verify every claim and compute exact counterexamples to proof obligations.
3. Keep an argument ledger marking each item: heuristic / finite computation / proven lemma / conditional theorem / failed proof route / complete proof.
4. Require agent submissions to distinguish a theorem from an assumption. Do not count consensus as verification.
5. After independent first-round reports, compare their proofs, ask each author to address specific objections from the others, then attempt formalization of the strongest surviving lemma.

## Required response format for every agent

- Exact claim being attempted.
- Definitions and complete proof, or precise unproved gap.
- Assumptions/axioms and external dependencies.
- Counterexample/edge-case tests.
- What would be sufficient to verify the claim (Lean/Rocq/Isabelle or explicit elementary audit).
- Honest status: proven / conditional / heuristic / refuted / incomplete.
- One next concrete mathematical step.

Do not modify the repository's main status to "proved" unless all axioms reducing to the original universal conjecture have actually been eliminated and the complete proof passes independent review.
