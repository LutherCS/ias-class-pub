# Knapsack cryptosystem

Implement Hellman-Merkle knapsack cryptosystem and pass the provided tests to verify your implementation.

Here are some assumptions and implementation details:

1. The exact values of the superincreasing knapsack you generate are not important as long as the superincreasing property holds.
2. Calculate `n` as the smallest number greater than the sum of values in the superincreasing knapsack.
3. Calculate `m` as the largest number in the range [1, n) that is co-prime of `n`.
4. The output of the function `encrypt` is a list with a single integer value.
5. Pay additional attention to the cases where plaintext is shorter than 1 full character.

## References

* [Merkle–Hellman knapsack cryptosystem - Wikipedia](https://en.wikipedia.org/wiki/Merkle%E2%80%93Hellman_knapsack_cryptosystem)
* [Hiding information and signatures in trapdoor knapsacks - IEEE Journals & Magazine](https://ieeexplore.ieee.org/document/1055927)
* [Knapsack](http://www.cs.sjsu.edu/~stamp/CS265/SecurityEngineering/chapter5_SE/knapsack.html)
* [The Rise and Fall of Knapsack Cryptosystems](http://www.dtc.umn.edu/~odlyzko/doc/arch/knapsack.survey.pdf)
