# Leetcode 941: Valid Mountain Array

---
## Problem Description

Given an array of integers `arr`, return `true` if and only if it is a valid mountain array.

A mountain array must satisfy the following conditions:
1. `arr.length >= 3`
2. There exists some index `i` (0 < i < arr.length - 1) such that:
    - `arr[0] < arr[1] < ... < arr[i]`
    - `arr[i] > arr[i+1] > ... > arr[arr.length - 1]`

For more details, visit the [Leetcode Problem Page](https://leetcode.com/problems/valid-mountain-array/).

---

## Approach

The solution involves the following steps:

1. **Edge Case Check**: If the length of the array is less than 3, return `false` immediately.
2. **Climbing Up**: Traverse the array from the start, ensuring that each element is strictly increasing until the peak is reached.
3. **Peak Validation**: Ensure that the peak is not the first or last element of the array.
4. **Descending Down**: Continue traversing the array, ensuring that each element is strictly decreasing after the peak.
5. **Final Check**: If the traversal ends at the last element and all conditions are satisfied, return `true`. Otherwise, return `false`.

The implementation of this approach can be found in the `solution.py` file in this folder.

---

## Complexity Analysis

- **Time Complexity**: O(n), where `n` is the length of the array. The array is traversed at most twice.
- **Space Complexity**: O(1), as no additional space is used apart from variables.

---

## Example

### Input
```plaintext
arr = [0, 3, 2, 1]
```

### Output
```plaintext
true
```

### Explanation
The array satisfies the mountain array conditions:
- It strictly increases from 0 to 3.
- It strictly decreases from 3 to 1.

---