## Explanation of Thought Process

### Clarify the Problem
We are given a sorted array of integers, possibly containing duplicates.  
We need to remove duplicates in-place** so that each unique element appears only once.  
The function should return the **new length** of the array containing only unique elements.

### Observations
- Since the array is sorted, **duplicates are consecutive**.
- We can use **two pointers**:
  - `slow`: points to the last unique element found.
  - `fast`: scans through the array to find new unique elements.
- When a new unique element is found, we increment `slow` and overwrite `nums[slow]` with it.

### Algorithm
1. If the array is empty, return `0`.
2. Initialize `slow = 0`.
3. Loop `fast` from `1` to `len(nums) - 1`.
4. If `nums[fast] != nums[slow]`:
   - Increment `slow` by 1.
   - Copy `nums[fast]` into `nums[slow]`.
5. Return `slow + 1` as the new length of unique elements.

### Complexity Analysis
- **Time Complexity:** O(n) — single traversal through the array.
- **Space Complexity:** O(1) — performed in-place, using only two pointers.

### Alternative Approaches
- **Using Python Sets:** Convert to `set(nums)` and sort.  
  - Simpler to code, but uses extra space and doesn’t meet in-place constraint.
- **Index tracking:** Count unique transitions instead of moving elements (useful for analytics, not mutation).

### Notes
- This approach only works for **sorted arrays**.  
  For unsorted arrays, you must first sort them or use a hash set.
- The array is modified in place, but only the first `k` elements (returned length) are valid unique values.
