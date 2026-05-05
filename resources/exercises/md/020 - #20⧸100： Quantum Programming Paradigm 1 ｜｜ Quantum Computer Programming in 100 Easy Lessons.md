# Exercises

This is a continuation of the Exercises from Episodes 5 and 7 (Part I and Part II of the problem).

Change your Probabilistic Computer Simulator so that it becomes a Quantum Computer Simulator. The input format should be almost the same as before, but instead of supporting the “RNG” instruction, you should support the “HAD” (=Hadamard) instruction (and of course, the variables now represent qubits, rather than bits). As for the output, two things will be required:

- Very similar to Part II, your code should first output the exact final amplitude on $|00\cdots 0\rangle$.
  As long as you output an easy-to-interpret representation of a number that exactly equals the final amplitude, I don’t mind the precise format; I suppose best would be something like
  “-(3/8)sqrt(2)” or “5/1024”.

- Second, somewhat similar to Part I, your code should additionally *simulate* (using the pseudo-random number generator built into the programming language you’re using) what would happen if the code ended with an “extract all” instruction. (So the output should look like one amplitude followed by one $n$-bit string; if you rerun the code with the same input, the amplitude should always be the same, but the $n$-bit string will probably change.)

Did you find “Part II” of this problem harder or easier to code than “Part I”?  
What about this tutorial’s Quantum Computer Simulator? Part III? Given a probabilistic program, $P$, supports you wanted to get a sense for the fraction of times it outputs each possible $n$-bit string. And suppose you’d like to have a probabilistic program, $P$, to get a sense for (pseudo)randomness. Would you then be obliged to write your Part II code? Conversely, suppose that given a quantum program $Q$, you don’t care about the final amplitudes per se; you just want to get a decent sense for “function of 1 bit” from $Q$. Might the code be simply simulate the effects of an “extract all” operation? Could it be as in Part I? What if your favorite programming language natively supported actual qubits?

*Quantum Computer Programming in 100 Easy Lessons: Ryan O’Donnell*
