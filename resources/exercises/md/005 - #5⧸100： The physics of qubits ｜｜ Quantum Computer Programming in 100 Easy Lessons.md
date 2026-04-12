I’m transcribing the visible text exactly as shown, including the partially obscured ending.
Exercises

Write a “Probabilistic Computer Simulator” in your favorite programming language. This will be like the “Quantum Computer Simulator” I demoed in Scratch, but for probabilistic computing rather than quantum computing. In particular, all the variables will be of data type “bit” rather than “qubit”.

For simplicity, rather having variable allocation via commands like “new bit A”, let’s assume that the first input to your program will be a nonnegative integer $n$, and this indicates that the program will use $n$ bit-valued variables, which will just be numbered $1, 2, ..., n$, rather than named. (As usual, assume all bits are initialized to the value $0$.) You should ensure that there’s absolutely no trouble at all in having, say, $n = 100, 000$ (or larger). The point of this problem, which will become clear in its future Parts II and III, is to see that this task is easily doable for very large values of $n$ (assuming your computer can actually generate random bits).

Regarding output, for simplicity, rather than requiring an explicit instruction like “extract all”, your program should just automatically print out all the final bit values at the end. Thus after receiving “n” as input, the remaining input will be some code consisting of a list of bit-manipulation instructions.

The bit-manipulation instructions supported will be the same ones we saw in our first Lec-
ture 1 quantum code example (except that they will operate on bits, rather than qubits) . . . plus the one special probabilistic instruction “RNG” that produces randomness. For your parsing simplicity, we will use the short instruction names used in quantum computing rather than my pseudocode versions; namely:

```text
NOT     i                        (this means “toggle bit i”)
CNOT    i j                      (this means “if bit i then toggle bit j”)
CCNOT   i j k                    (this means “if (bit i AND bit j) then toggle bit k”)
RNG     i                        (this command should set bit i to 0 or 1 with probability 1/2 each)
```

In the above, $i, j, k$ stand for distinct bit numbers between $1$ and $n$. Your program may assume that the input code is properly formatted.

Given the input “n” value and subsequent code (say, from a text file, although you can use a reasonable alternative system if that’s convenient for you) your program should use (pseudo)randomness as built into your programming language of choice to simulate one run of the code, prin
