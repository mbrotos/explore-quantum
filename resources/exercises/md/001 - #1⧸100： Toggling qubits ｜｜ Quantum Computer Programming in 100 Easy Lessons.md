# Exercises

Say that you are allowed to use the following quantum instructions:

- `toggle ___`
- `if ___ then toggle ___`
- `if ( ___ AND ___ ) then toggle ___`

where the blanks `___` may be filled in by *distinct* qubit variable names (like `A,B,C`, etc.).

(a) Suppose you want to write a little subroutine that implements “if `(A OR B)` then toggle `C`”.  
&nbsp;&nbsp;&nbsp;&nbsp;Show how to do it using only the three allowed instructions.

**Note:** after this operation, `A` and `B` should be in their original states.

(b) Same question but for implementing “if `(NOT A)` then toggle `B`”. After this operation, `A` should be back to its original state.

(c) Same but for “`IncrMod4 A,B`”, which treats the two bits `A,B` as the binary encoding of a number from `{0,1,2,3}` (with `A` the most significant bit and `B` the least), and acts by incrementing this number by $1$, modulo $4$.

(d) Same for “`IncrMod8 A,B,C`”.

(e) Same for “`IncrMod3 A,B`”, which treats `A,B` as the binary encoding of a number from `{0,1,2}` and adds $1$ mod $3$ — and additionally just leaves the “invalid” case of `A,B = 11` as-is.

(f) Same but for “`SWAP A,B`” (which does what you think it does).

(g) Same but for “`LeftCyclicShift A,B,C`” which sets `A`'s new value to `B`'s old value, sets `B`'s new value to `C`'s old value, and sets `C`'s new value to `A`'s old value. You can call subroutines you’ve previously written, if you want.

(h) Same but for “`RightCyclicShift A,B,C`”.

(i) Go into python interactive mode and type:

```latex
(x,y) = (459,314)
x ^= y
y ^= x
x ^= y
(x,y)
```

What does it print out? Explain how/why this happened.
