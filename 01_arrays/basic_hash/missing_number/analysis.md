## Explanation of Thought Process

### Clarify the Problem
We are given `n` distinct integers taken from the range `[0, n]`.  
Exactly one number is missing.  
We need to find that number.

### Observations
- A complete sequence of `[0, n]` would have a known sum: `n * (n + 1) / 2`.
- The given list’s sum will be smaller by exactly the missing number.
- Thus, `missing = expected_sum - actual_sum`.

### Algorithm
1. Compute `n = len(nums)`.
2. Compute `expected_sum = n * (n + 1) // 2`.
3. Compute `actual_sum = sum(nums)`.
4. Return `expected_sum - actual_sum`.

### Complexity Analysis
- **Time Complexity:** O(n) — single pass for summation.
- **Space Complexity:** O(1) — constant auxiliary space.

### Alternative Approaches
- **Bitwise XOR:** XOR all indices and numbers; result is the missing one.
  - Advantage: avoids integer overflow, equally O(n), O(1).

### Notes
- If input is not sorted, sort it first (O(n log n)).
- Check boundaries: if first number > 0 or last number < n, include those missing ranges too.
