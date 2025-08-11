# Leetcode Problem 747: Largest Number At Least Twice of Others

---
## Problem Description

You are given an integer array `nums` where the largest integer is at least twice as large as every other number in the array. Determine whether this condition is satisfied and return the index of the largest number. If the condition is not satisfied, return `-1`.

### Example

#### Input:
```
nums = [3, 6, 1, 0]
```

#### Output:
```
1
```

#### Explanation:
The largest number is `6`, and it is at least twice as large as every other number in the array. Its index is `1`.

---

## Approach

The solution follows these steps:

1. **Identify the Largest Number**:
    - Traverse the array to find the largest number and its index.

2. **Check the Twice Condition**:
    - Iterate through the array again to ensure that the largest number is at least twice as large as every other number. Skip the largest number itself during this check.

3. **Return the Result**:
    - If the condition is satisfied, return the index of the largest number. Otherwise, return `-1`.

This approach ensures an efficient solution with a time complexity of `O(n)` since the array is traversed twice.

---

## Complexity Analysis

- **Time Complexity**: `O(n)` where `n` is the length of the array.
- **Space Complexity**: `O(1)` as no additional space is used apart from variables.

---