## 1 Clarifying the problem

The input is a list of integers.
The output should be a list containing all numbers that appear more than once.
Each duplicate should appear only once in the result, even if it occurs multiple times in the input.
Example:

[3, 5, 6, 7, 3, 5] → [3, 5]
[2, 2, 2, 2]       → [2]
[1, 2, 3]          → []


## 2 Initial idea
I need to keep track of numbers I’ve already seen.
If I see a number again, that means it’s a duplicate.

## 3 Data structure choice

If I use a list for seen, checking membership (num in seen) would take O(n) time.
For large inputs, this could degrade performance.
Instead, I’ll use a set, where membership checks are O(1) on average.
I’ll also use another set, duplicates, to ensure each duplicate is stored only once.

## 4 Algorithm
Loop through each number in the list.

If it’s not in seen, add it to seen.
If it’s already in seen, add it to duplicates.
At the end, return all items in duplicates as a list.

## 5 Complexity Analysis

Time Complexity: O(n), because each number is checked and inserted into a set once.
Space Complexity: O(n), in the worst case when all numbers are unique (stored in seen).

# !!! Set items are unordered, unchangeable, and do not allow duplicate values.