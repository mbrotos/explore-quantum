**Exercise**

Suppose you have two paths diagrams called $X$ and $Y$, where $X$ has $m$ vertices on top and $n$ vertices on the bottom, and $Y$ has $n$ vertices on top and $p$ on the bottom (and all arrows labeled by real numbers). Hopefully, you have come to understand the following:

- $X$ is the same as an $n \times m$ matrix;
- $Y$ is the same as a $p \times n$ matrix;
- If you glue together the $n$ top nodes of $Y$ to the $n$ bottom nodes of $X$ and then you “compress” the result to a single paths diagram $Z$ (where the arrow from $s$ to $t$ in $Z$ is labeled by the sum of products-along-paths-from-$s$-to-$t$ in the glued diagram), then $Z$ is equivalent to the matrix $Y \cdot X$.

(a) Explain why a paths diagram with a single top node and $2^k$ bottom nodes (labeled by $k$-bit strings) is equivalent to a column vector, and why it can also be interpreted as a $k$-qubit quantum state.

(b) Given an arbitrary $k$-qubit superposition state $\varphi$, and a $k$-qubit-manipulation operation $Q$, explain how to answer the question “What quantum state results from starting with state $\varphi$ and applying $Q$?” using paths diagrams.

(c) Given any paths diagram $X$ with $m$ top vertices and $n$ bottom vertices (aka $n \times m$ matrix), let $X^\dagger$ (pronounced “$X$-dagger”) be the paths diagram/matrix formed by reversing all the arrows in $X$.¹ Explain how $X^\dagger$ looks as a matrix (vis-a-vis how $X$ looks as a matrix).

(d) Suppose $\varphi$ and $\psi$ are both paths diagrams with one vertex on top and $m$ vertices on bottom. In matrix terminology, what type of object is $\psi^\dagger$?

(e) Following up on the previous question, what well-known linear algebra concept arises when you glue $\psi^\dagger$ to the bottom of $\varphi$ and compress the result down to a $1 \times 1$ paths diagram?

(f) Following up some more, supposing $m = 2^k$, how could you use these ideas to know if $\varphi$ stands for a valid $k$-qubit quantum state?

¹ In case $X$’s entries have complex numbers, you should also do “complex-conjugate” on each of them when forming $X^\dagger$. Don’t worry about this, because we’re not going to use complex numbers, but I wanted to let you know.
