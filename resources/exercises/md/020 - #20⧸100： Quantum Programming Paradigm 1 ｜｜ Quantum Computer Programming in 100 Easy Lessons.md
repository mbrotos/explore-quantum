# Exercises

This is a continuation of the Exercises from Episodes 5 and 7 (Part I and Part II of the problem).

Change your Probabilistic Computer Simulator so that it becomes a Quantum Computer Simulator. The input format should be almost the same as before, but instead of supporting the “RNG” instruction, you should support the “HAD” (=Hadamard) instruction (and of course, the variables now represent qubits, rather than bits). As for the output, two things will be required:

- Very similar to Part II, your code should first output the exact final amplitude on $|00\cdots 0\rangle$.
  As long as you output an easy-to-interpret representation of a number that exactly equals the final amplitude, I don’t mind the precise format; I suppose best would be something like
  “-(3/8)sqrt(2)” or “5/1024”.

- Second, somewhat similar to Part I, your code should additionally *simulate* (using the pseudo-random number generator built into the programming language you’re using) what would happen if the code ended with an “extract all” instruction. (So the output should look like one amplitude followed by one $n$-bit string; if you rerun the code with the same input, the amplitude should always be the same, but the $n$-bit string will probably change.)

Did you find "Part I" of this problem harder or easier to code than "Part I"
Why? What about versus this Quantum Part III? Could you have supported
n - 1000 in Parts II or III? Given a probabilistic program P, suppose you wanted to get a decent sense for the fraction of times it outputs each possible n-bit string. And suppose you'd be happy to have output like in Part I, but the language you're coding in has absolutely no support for (pseudo)randomness. Would you then be obliged to write your Part II code?
Conversely, suppose that given a quantum program Q, you don't care about the final amplitudes per se, you just want to get a decent sense for the fraction of times "extract al1" would output cach possible r-bit string. Are you obliged to write your Part III code? Might there be some kind of "simulation shortcut" as in Part I? What if your favorite programming language natively supported actual qubits?

*Quantum Computer Programming in 100 Easy Lessons: Ryan O’Donnell*
