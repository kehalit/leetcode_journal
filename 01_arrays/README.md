#  Two-Pointer Pattern

## What It Is

The two-pointer technique uses two indices (pointers) that move through a data structure (usually an array or string) 
to perform comparisons or reorganize elements efficiently.  
It often replaces a brute-force `O(n²)` nested loop with a clean, linear `O(n)` scan.

Instead of examining every possible pair, we exploit the structure or ordering of the input to guide how the pointers move.

---

## When to Use

Use the two-pointer pattern when:
- The data is sorted or can be logically ordered.  
- The problem involves pair relationships, boundary traversal, or in-place modification.
- You need to avoid extra memory (e.g., deduplicating, rearranging).
- You want to find something like:
  - A pair that meets a sum condition.
  - A subarray meeting certain constraints.
  - Unique elements in a sorted array.
  - A reversed or mirrored arrangement.

## more details on
- https://neetcode.io/roadmap
- https://seanprashad.com/leetcode-patterns/ — curated roadmap of problems by technique.
- https://www.geeksforgeeks.org/dsa/two-pointers-technique/  — clear description with examples and visualizations.

