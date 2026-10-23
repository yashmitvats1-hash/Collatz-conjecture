# Audit: Mod-4 Structural Forcing submission

Date: 2026-10-23  
Source: https://github.com/iamkhayyam/the-collatz-conjecture

## Verdict

This repository contains a potentially valid auxiliary theorem, E_empty, but does **not** contain a complete formal proof of the classical Collatz conjecture. Its own PROOF_STATUS.md explicitly lists the crucial bridge lemmas as not yet formalized and identifies gaps in the written arguments.

## What the formalized theorem says

The repository defines the simple map
\[
S(n)=\left\lfloor\frac{3n+1}{2}\right\rfloor
\]
and a set E of odd positive naturals whose every iterate under this auxiliary map remains odd. It formalizes E=∅ (the theorem E_empty), i.e. no positive integer has an infinite all-odd orbit under this simple map.

The key residue argument is understandable. For odd x, S(x) is odd exactly when x≡3 (mod 4). If a hypothetical n belongs to E, the submitted lemmas force n≡15 (mod 16). Writing n=16p+15 then propagates the all-odd property from n to a smaller p. A least-counterexample argument rules out E. This excludes one special kind of infinite parity pattern for S.

## Why that is not Collatz convergence

S is not the ordinary Collatz map on even inputs. Ordinary T sends an even x to x/2; S sends it to (3x+1)/2. Therefore after the first even S-iterate, continuing the S-orbit is no longer continuing the actual Collatz trajectory. The assertion that an S-orbit eventually becomes even does not by itself imply the ordinary Collatz orbit reaches a smaller value or reaches 1.

The repository's own PROOF_STATUS.md records:
- no_nontrivial_cycles: not fully formalized; the written argument confuses an orbit under the simple S-map with the accelerated odd-only map;
- no_divergent_orbits: not fully formalized; the ℓ≥2 case relies on "sufficiently large" plus finite checking but does not close both cases;
- collatz_convergence: pending those bridge lemmas.

Thus the strongest verified result should be cited narrowly as E_empty, not renamed as Collatz convergence.

## Useful exact observation

Suppose S^0(n), S^1(n), ..., S^m(n) are all odd. Then each application up to S^m uses the exact affine formula
\[
S^j(n)+1=\frac{3^j(n+1)}{2^j},\qquad 0\le j\le m.
\]
Since 3 is odd, oddness of S^m(n) forces n+1 to be divisible by 2^{m+1}; equivalently n≡−1 (mod 2^{m+1}). A fixed positive integer n cannot satisfy this for every m, which proves there is no infinite all-odd S-orbit. The divisibility statement concerns this special run of S-steps only; it does not provide a universal descent bound for T.

## Recommended next step

Retain E_empty as an auxiliary lemma, after independently rebuilding its Lean proof and checking its exact domain (especially whether zero is excluded). Do not use it as the foundation of a Collatz proof until a separate, fully rigorous bridge establishes universal descent or otherwise handles every possible orbit. The cycle and divergence cases must be proved independently, with no mutual circular dependence.

## Classification

- E_empty: **formalized auxiliary theorem claimed by the repository; scope limited to an all-odd orbit of S**.
- no_nontrivial_cycles / no_divergent_orbits / collatz_convergence: **incomplete in the repository's own status record**.
- Classical Collatz conjecture: **not proved by this submission as presented**.
