## Problem
Given an array of integers, return indices of two numbers such that they add up to a target.

## Approach
Use a hash map to achieve O(n) lookup for complements.
Alternative (O(n²) brute force) was discarded for scalability reasons.

## Complexity
- **Time:** O(n)
- **Space:** O(n)

## Insights
- Classic example of trading space for time.
- Reinforces the power of precomputation in linear scans.
