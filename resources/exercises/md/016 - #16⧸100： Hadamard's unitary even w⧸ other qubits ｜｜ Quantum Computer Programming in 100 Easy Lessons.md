# Exercise

Suppose $M$ is the $4 \times 4$ matrix representation of a quantum operation on 2 qubits. Given a matrix $M$, you’re probably used to calling the entries of the matrix $M_{ij}$. But since we think of the columns/rows of $M$ as being labeled by $|00\rangle, |01\rangle, |10\rangle, |11\rangle$, we will instead write $M[ab \to cd]$ for the entry in column $|ab\rangle$ and row $|cd\rangle$.

Next, suppose $N$ is the $4 \times 4$ matrix representation of another operation on 2 qubits; we again use notation like $N[ab \to cd]$ for its entries.

Now suppose we consider the composite operation on 2 qubits in which we first do (the operation represented by) $M$, and then we do (the operation represented by) $N$. Show that the matrix representation of this composite operation is $N \cdot M$, the matrix product.

(Note: Please remember that the only method you have at your disposal to analyze how quantum operations work is amplitude trees. Hint: consider gluing the paths diagram for $M$ to the paths diagram for $N$. . . Also, I suggest you try doing an example with numbers first, as practice.)
