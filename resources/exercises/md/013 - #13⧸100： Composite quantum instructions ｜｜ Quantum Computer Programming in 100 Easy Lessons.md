# Exercises

Let MySub(B) be a (qubit-manipulation) subroutine that operates on one qubit named B. (Everything in this problem works out just the same if MySub operates on more than 1 qubit, but let's just keep it simple.) Suppose the paths diagram for MySub is

or equivalently, its matrix representation is

```latex
\[
\begin{array}{c|cc}
 & |0\rangle & |1\rangle \\
\hline
|0\rangle & u & x \\
|1\rangle & v & y
\end{array}
\]
```

(a) Consider the operation on two qubits A,B called ControlledMySub(A,B) which does the thing its name suggests: like, “if A then MySub(B)”. Draw the paths diagram or matrix (your choice) for ControlledMySub(A,B).

(b) Consider the operation on two qubits A,B called NoOpAndMySub(A,B), which literally just does MySub on B and doesn't do anything to A. Draw the paths diagram or matrix (your choice) for NoOpAndMySub(A,B).

(c) Suppose there is another (qubit-manipulation) subroutine called OtherSub(A) operating on one qubit named A with the following matrix representation:

```latex
\[
\begin{array}{c|cc}
 & |0\rangle & |1\rangle \\
\hline
|0\rangle & \alpha & \delta \\
|1\rangle & \beta & \epsilon
\end{array}
\]
```

(Here $\alpha,\beta,\delta,\epsilon$ are still real numbers. I just decided to use Greek letters.) Using an amplitude tree, work out the final state after this code:

    (a) new qubit A,B
    (b) OtherSub(A)
    (c) MySub(B)

(d) Work out the final state after this code:

    (a) new qubit A,B
    (b) MySub(B)
    (c) OtherSub(A)

(e) Explain why for any initial superposition state of two qubits, doing OtherSub(A) then MySub(B) yields the same final state as doing MySub(B) then OtherSub(A).

Quantum Computer Programming in 100 Easy Lessons: Ryan O'Donnell
