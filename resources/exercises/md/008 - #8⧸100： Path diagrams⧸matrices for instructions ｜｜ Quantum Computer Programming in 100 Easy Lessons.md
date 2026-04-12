# Exercises

Say we build a new classical reversible instruction as shown below:

```text
LeftCyclicShift(A,B,C):
 1 swap A B
 2 swap B C
```

Draw the path diagram for this operation `LeftCyclicShift`. You should be able to see that it is not its own “undo”; nevertheless, it is reversible. Write a program for its reverse (undo) operation, and also draw the associated path diagram.
