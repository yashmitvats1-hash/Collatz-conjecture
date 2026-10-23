# A lower bound for Collatz strict-descent stopping times

## Statement

Let
`T(n)=n/2` for even `n`, and `T(n)=3n+1` for odd `n`. For `n>1), define
[
\tau(n)=\inf\{k\ge1:T^k(n)<n\},
]
with `τ(n)=∞` if the set is empty.

If `n` is odd, let `ν=v₂(n+1)` and write `n+1=q2^ν` with `q` odd. Then
[
\boxed{\tau(n)\ge \left\lceil (1+\log_2 3)\nu\right\rceil.}
]
Consequently, the strict-descent stopping times are unbounded across starting values. This is a lower bound on how late descent can first occur; it is not a claim that descent eventually occurs for every input.

## Proof

For `0≤j≤ν`, induction through the initial odd/even pattern gives
[
T^{2j}(n)=3^j q2^{\nu-j}-1.
]
For `0≤j<ν`,
[
T^{2j+1}(n)=3^{j+1}q2^{\nu-j}-2.
]
These formulas show that each iterate at time `t` with `1≤t<2ν` is greater than `n=q2^ν−1`: the even-indexed formula has multiplier `(3/2)^j>1` when `j≥1`, while the odd-indexed formula has an even larger leading coefficient. At time `2ν`,
[
T^{2\nu}(n)=3^\nu q-1>n.
]

Let `x=3^νq−1`. Since `q` is odd and `3^ν>2^ν`,
[
\frac{x}{n}=\frac{3^\nu q-1}{2^\nu q-1}>
\left(\frac32\right)^\nu.
]
For every positive integer `y`, `T(y)≥y/2`, so by induction
[
T^r(x)\ge \frac{x}{2^r}.
]
Therefore, no fewer than `ceil(log₂(x/n))` further steps can suffice to put the trajectory below `n`. It follows that
[
\begin{aligned}
\tau(n)
&\ge 2\nu+\left\lceil\log_2(x/n)\right\rceil\\
&\ge 2\nu+\left\lceil\nu\log_2(3/2)\right\rceil\\
&=\left\lceil(2+\log_2(3/2))\nu\right\rceil\\
&=\left\lceil(1+\log_2 3)\nu\right\rceil.
\end{aligned}
]
Since `ν=v₂(n+1)` can be arbitrarily large, the stopping time cannot have a finite uniform upper bound over all starting values. For instance, `n=2^ν−1` has `v₂(n+1)=ν`.

## Scope and limitation

This theorem excludes a uniform bound `τ(n)≤M` valid for every `n`. It does **not** imply that some starting value never descends, does not establish divergence, and does not prevent a proof with an input-dependent stopping-time bound. A universal proof would need to show descent for each individual `n`, with the bound allowed to vary.
