
This project implements the Hill Climbing algorithm to solve the Knapsack Problem, comparing three different neighbor generation strategies:

- **OneBit Flip**: Flips the inclusion of one item.
- **Swap Two Items**: Swaps the inclusion statuses of two items.
- **KBit Flip**: Flips `k=2` random items simultaneously.

The effectiveness of these strategies was evaluated based on their accuracy in finding the optimal solution across 1,000, 10,000, and 100,000 runs. A brute force method was used to determine the optimal solution for comparison. The accuracy was measured as the percentage of times the algorithm found the optimal solution.

### Test Results Comparison Table

| **Neighbor Generation Method** | **Accuracy Test (1,000 Runs)** | **Accuracy Test (10,000 Runs)** | **Accuracy Test (100,000 Runs)** | **Time Complexity (Neighbor Generation)** | **Notes** |
|--------------------------------|--------------------------------|---------------------------------|----------------------------------|-------------------------------------------|-----------|
| OneBit Flip                    | 32.4%                          | 30.91%                          | 31.04%                           | O(n)                                      | Small changes, efficient but prone to local optima. |
| Swap Two Items                 | 25.2%                          | 24.55%                          | 24.97%                           | O(n²)                                     | Larger changes but randomness reduces effectiveness. |
| KBit Flip                      | 38.6%                          | 35.50%                          | 36.48%                           | O(k * n)                                  | Best performance, larger exploration with reasonable computation cost. |

### Analysis and Findings

- **KBit Flip** consistently outperformed the other methods in terms of accuracy, with the highest rates across all run sizes. This strategy's ability to flip two items simultaneously allowed for broader exploration of the search space, helping the algorithm escape local optima more effectively.
- **OneBit Flip** showed moderate accuracy but performed consistently across different test sizes. Its smaller, incremental changes allowed for steady exploration but limited its ability to find the global optimum in complex problem spaces.
- **Swap Two Items** had the lowest accuracy in all test cases. Despite generating a larger number of neighbors, the randomness introduced did not consistently lead to better solutions. Its increased computational complexity did not result in higher performance.

### Time Complexity Analysis

- **OneBit Flip** was the most efficient, with a time complexity of O(n), making it suitable for scenarios where computation time is limited.
- **Swap Two Items** had the highest time complexity (O(n²)), but this did not translate into better performance, suggesting that generating a large number of neighbors is not always beneficial.
- **KBit Flip** offered a balance between exploration and computational cost, with a complexity of O(k * n). This combination of larger moves and manageable computational cost led to the best results overall.

### Conclusion

The Hill Climbing algorithm with **K Bit Flip** neighbor generation proved to be the most effective strategy for solving the Knapsack Problem, achieving the highest accuracy across all run sizes. While **OneBit Flip** was computationally efficient and delivered consistent results, it struggled to escape local optima in more complex scenarios. **Swap Two Items** showed the weakest performance, indicating that large, random changes do not necessarily improve the search process.

### Future Improvements

Implementing a restarting mechanism within the Hill Climbing algorithm can ensure a 100% success rate in finding the optimal solution. This involves regenerating the current solution randomly whenever the algorithm gets stuck in a local optimum, allowing exploration of different parts of the solution space.

### Source Code

The source code for this implementation is included in the project folder for review and testing.


