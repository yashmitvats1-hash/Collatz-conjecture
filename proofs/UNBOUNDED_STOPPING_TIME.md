# A lower bound for Collatz strict-descent stopping times

## Statement

Let the ordinary Collatz map be
\[
T(n)=\begin{cases}n/2&n\text{ even},\\3n+1&n\text{ odd}.\end{cases}
\]
For \(n>1\), define
\[
\tau(n)=\inf\{k\ge1:T^k(n)<n\},
\]
with \(\tau(n)=\infty\) if the set is empty.

If \(n\) is odd, let \(\nu=v_2(n+1)\) and write \(n+1=q2^\nu\) with \(q\) odd. Then
\[
\boxed{\tau(n)\ge \left\lceil (1+\log_2 3)\nu\right\rceil.}
\]
Consequently, the strict-descent stopping times are unbounded across starting values. This is a lower bound on how late descent can first occur; it is not a claim that descent eventually occurs for every input.

## Proof

For \(0\le j\le\nu\), induction through the initial odd/even pattern gives
\[
T^{2j}(n)=3^j q2^{\nu-j}-1.
\]
For \(0\le j<\nu\),
\[
T^{2j+1}(n)=3^{j+1}q2^{\nu-j}-2.
\]
These formulas show that every iterate at time \(t\) with \(1\le t<2\nu\) is greater than \(n=q2^\nu-1\): the even-indexed formula has multiplier \((3/2)^j>1\) when \(j\ge1\), while the odd-indexed formula has an even larger leading coefficient. At time \(2\nu\),
\[
T^{2\nu}(n)=3^\nu q-1>n.
\]

Let \(x=3^\nu q-1\). Since \(q\) is odd and \(3^\nu>2^\nu\),
\[
\frac{x}{n}=\frac{3^\nu q-1}{2^\nu q-1}>
\left(\frac32\right)^\nu.
\]
For every positive integer \(y\), \(T(y)\ge y/2\), so by induction
\[
T^r(x)\ge \frac{x}{2^r}.
\]
Therefore no fewer than \(\left\lceil\log_2(x/n)\right\rceil\) further steps can suffice to put the trajectory below \(n\). It follows that
\[
\begin{aligned}
\tau(n)
&\ge 2\nu+\left\lceil\log_2(x/n)\right\rceil\\
&\ge 2\nu+\left\lceil\nu\log_2(3/2)\right\rceil\\
&=\left\lceil(2+\log_2(3/2))\nu\right\rceil\\
&=\left\lceil(1+\log_2 3)\nu\right\rceil.
\end{aligned}
\]
Since \(\nu=v_2(n+1)\) can be arbitrarily large, the stopping time cannot have a finite uniform upper bound over all starting values. For instance, \(n=2^\nu-1\) has \(v_2(n+1)=\nu\).

## Scope and limitation

This theorem excludes a uniform bound \(\tau(n)\le M\) valid for every \(n\). It does **not** imply that some starting value never descends, does not establish divergence, and does not prevent a proof with an input-dependent stopping-time bound. A universal proof would need to show descent for each individual \(n\), with the bound allowed to vary.
