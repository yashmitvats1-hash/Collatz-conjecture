# Collatz Conjecture Research

A collaborative, proof-oriented investigation of the Collatz conjecture. The goal is a correct proof or a rigorously verified counterexample—not merely a plausible argument, numerical evidence, or agreement among AI systems.

## Exact statement

Define
\[
T(n)=\begin{cases}
n/2,&n\equiv 0\pmod 2,\\
3n+1,&n\equiv 1\pmod 2.
\end{cases}
\]
The conjecture says that for every integer \(n\ge 1\), there exists \(k\ge 0\) such that \(T^k(n)=1\).

The familiar cycle \(1\to4\to2\to1\) is allowed. A proof must cover **every** positive integer.

## Working principles

1. **Proof over persuasion.** A claimed proof is a draft until every inference and hypothesis has been checked.
2. **State the quantifiers.** Distinguish all starting values from almost all, density-one, bounded ranges, or values satisfying extra assumptions.
3. **Expose the bridge.** Probabilistic drift, average-case behavior, simulations, and finite searches do not by themselves prove universal termination.
4. **Track dependencies.** Every lemma must be proved or linked to a precise, accepted theorem with hypotheses verified.
5. **Try to break every candidate.** A reviewer should actively search for a counterexample, hidden circularity, unjustified interchange of limits, missing residue classes, and unhandled boundary cases.
6. **Reproducibility.** Code, test ranges, compiler versions, seeds, and machine-checkable certificates must be recorded. Computation supports a finite claim only within its verified scope.
7. **No false status claims.** Label outputs as idea, conjecture, heuristic, computational observation, conditional theorem, checked lemma, formalized lemma, or complete proof.

## Initial research tracks

- **Track A — accelerated odd map / residue covers:** Study \(S(n)=(3n+1)/2^{v_2(3n+1)}\) on odd positive integers, valuation sequences, modular partitions, and finite certificates for descent.
- **Track B — descent and induction:** Investigate sufficient conditions such as proving that every \(n>1\) has an iterate below \(n\); make every equivalence and threshold exact.
- **Track C — analytical / dynamical approaches:** Examine known drift, stopping-time, density, and distribution results; isolate the precise obstacle to upgrading an almost-everywhere result to a universal theorem.
- **Track D — formal verification and red-team review:** Design machine-checkable representations and adversarially audit every candidate proof.

## Status at project start

**Overall conjecture: OPEN in this research record. No proof or counterexample has been established here.**

Computational verification through a large finite bound is valuable evidence but is not a proof of the universal statement. See `RESEARCH_STATUS.md` and `AGENT_ASSIGNMENTS.md`.

## What qualifies as a proof submission?

A submission must contain: (i) an exact theorem statement; (ii) definitions and all assumptions; (iii) numbered lemmas and complete proofs; (iv) a dependency/reference list; (v) an explicit explanation of how the lemmas imply the universal claim; (vi) independent red-team review; and, where feasible, a Lean 4 formalization. Any remaining unproved statement must be labeled as a gap, not silently treated as true.
