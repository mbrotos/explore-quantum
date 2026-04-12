# Exercises

Suppose you have a directed bipartite graph with $m$ vertices on the top and $n$ vertices on the bottom, where all the directed edges go from the top to the bottom. For clarity, call it the “amber”-colored graph, and let $A$ be the $n\times m$ grid of numbers where in the $i$th column $(1\le i\le m)$ and $j$th row $(1\le j\le n)$ we have the number of ways (i.e., number of directed edges) from top vertex $i$ to bottom vertex $j$. For example, in the above diagram (ignoring the blue lower half) we have $m=4$, $n=3$ and

```latex
A=\begin{pmatrix}
3 & 1 & 0 & 0\\
0 & 1 & 2 & 0\\
1 & 0 & 1 & 1
\end{pmatrix}
```

Suppose we have another such bipartite graph, the “blue”-colored graph, with $n$ vertices on the top, $p$ vertices on the bottom, and associated $p\times n$ grid of numbers $B$. The lower half of the above diagram gives an example, with $p=2$.

(a) Write $B$ out for the specific blue graph shown in the diagram.

(b) Suppose we glue the $n$ vertices at the bottom of the amber graph to the $n$ vertices at the top of the blue graph, as in the diagram. Now let $C$ be the $p\times m$ grid of numbers where in the $i$th column $(1\le i\le m)$ and $k$th row $(1\le k\le p)$ we have the number of ways (i.e., number of directed paths) from top vertex $i$ all the way down to bottom vertex $k$. Write $C$ out for the specific amber/blue combo graph shown in the diagram.

(c) In general, explain why $C$ is derived from $A$ and $B$ from the rule for matrix multiplication,

```latex
C=BA.
```
