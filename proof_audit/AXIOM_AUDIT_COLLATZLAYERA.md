# Adversarial audit: CollatzLayerA v8.1 certificate

Date: 2026-10-23  
Source: https://github.com/AIDoctrine/CollatzLayerA/blob/main/CollatzLayerA_v8_1_FINAL.lean

## Verdict

The repository does **not** establish the Collatz conjecture. Its purported main theorem depends on two axioms. More strongly, its axiom named odd_steps_certificate is false for an explicit input. This is a mathematical counterexample to a premise in that proposed proof, **not** a counterexample to the Collatz conjecture itself.

## The relevant formal definitions

The submitted Lean source defines the ordinary map
\[
T(n)=\begin{cases}n/2& n\text{ even},\\3n+1&n\text{ odd},\end{cases}
\]
and counts odd iterates by
\[
P(k,n)=\#\{i:0\le i<k,\ T^i(n)\text{ is odd}\}.
\]
Thus its definition satisfies P(k,n)=odd_steps(k,n), and the number of even terms among the first k iterates is k−P(k,n).

The declared axiom is:
\[
\forall n\ge 2^{71},\quad n\text{ odd},\quad n\equiv3\pmod4
\Rightarrow \exists k:\ 0<k\le200,\ P(k,n)\le44,\ k-P(k,n)\ge71.
\]
The README describes this as a deterministic universal trajectory certificate. The logical-framework document's probabilistic estimates do not prove such a statement for every integer.

## Explicit counterexample to the axiom

Take
\[
n=2^{102}-1.
\]
It satisfies all the axiom's input conditions:
- n ≥ 2^71;
- n is odd;
- n ≡ 3 (mod 4).

Define the auxiliary map S(x)=(3x+1)/2. As long as the iterates are odd, ordinary Collatz performs the two steps
\[
x\xrightarrow{T}3x+1\xrightarrow{T}(3x+1)/2=S(x).
\]
For this n, the exact formula for the auxiliary iterates is
\[
S^j(n)=3^j2^{102-j}-1.
\]
For every 0 ≤ j ≤ 101, the factor 2^{102-j} is even, so S^j(n) is odd. In particular, all the first 101 auxiliary iterates needed to cover the first 200 ordinary T iterates remain odd. Hence, for every 0 ≤ i < 200:
- T^i(n) is odd when i is even;
- T^i(n) is even when i is odd.

Consequently, for every k with 1 ≤ k ≤ 200,
\[
P(k,n)=\lceil k/2\rceil,\qquad k-P(k,n)=\lfloor k/2\rfloor.
\]
If the axiom's even-term requirement holds, then floor(k/2) ≥ 71, so k ≥ 142. It follows that
\[
P(k,n)=\lceil k/2\rceil\ge71>44,
\]
contradicting its required P(k,n) ≤ 44. If k < 142, the even-term requirement already fails. Thus **no permitted k exists** for n=2^102−1.

This refutes the universally quantified axiom directly, without needing any statement about the eventual fate of this orbit.

## Second axiom: base_case_109

The source also declares
\[
\forall n,\quad 0<n<2^{109}\Rightarrow \exists k,\ T^k(n)=1.
\]
This is an assumption, not a Lean theorem. The repository's comments cite verification through 2^68 and describe extension to 2^109 as consistent with known results; consistency with tested data is not a proof of this universal finite-range claim. The published Barina article reports verification up to 2^71: https://link.springer.com/article/10.1007/s11227-025-07337-0

Even if an independently verified computational certificate eventually discharged this finite-range axiom, the first axiom remains false.

## Why "zero sorry" does not save the claim

Lean's kernel checks theorems relative to declared axioms. Having zero uses of sorry is not equivalent to having no unproved assumptions. The source itself lists base_case_109 and odd_steps_certificate as axioms; collatz_conjecture follows only after accepting them. One is unsubstantiated and the other is contradicted by the exact input above.

## Reproducible check (illustrative only)

A small ordinary-Python check can calculate the first 200 parities of n=2**102-1 and observe 100 odd and 100 even values. That finite check is supplementary; the algebraic argument above is the proof that the purported axiom fails.

## Classification

- Claimed main theorem: **not a valid proof of Collatz**.
- odd_steps_certificate: **refuted** by n=2^102−1.
- base_case_109: **assumed, not proved** in this source.
- This audit: **complete for invalidating the submitted proof as written**; it does not resolve the classical conjecture.
