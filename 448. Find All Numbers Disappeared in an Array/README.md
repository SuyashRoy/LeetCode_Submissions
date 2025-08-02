# LeetCode 448: Find All Numbers Disappeared in an Array

---
## Problem Description

Given an array `nums` of size `n` where `nums` contains integers in the range `[1, n]`, some elements appear twice, and others appear once. Find all the integers in the range `[1, n]` that do not appear in `nums`.

You must write an algorithm that runs in `O(n)` time and uses constant extra space.

**Example:**
```
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
```

## Approach

The solution leverages the input array itself to track the presence of numbers. The key idea is to mark the indices corresponding to the numbers in the array as visited by negating the values at those indices. This allows us to identify the missing numbers in a single pass.

### Steps:
1. Iterate through the array and for each number, calculate its corresponding index.
2. Mark the value at that index as negative to indicate the presence of the number.
3. After processing the array, iterate through it again to find indices with positive values. These indices correspond to the missing numbers.
4. Return the missing numbers as the result.

This approach ensures `O(n)` time complexity and uses constant extra space since the input array is modified in place.

## File Structure

- `solution.py`: Contains the implementation of the algorithm to solve the problem.

## Complexity Analysis

- **Time Complexity:** `O(n)` - The array is traversed twice.
- **Space Complexity:** `O(1)` - No additional data structures are used; the input array is modified in place.

---