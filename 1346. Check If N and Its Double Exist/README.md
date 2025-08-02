# LeetCode 1346: Check If N and Its Double Exist

---
## Problem Description

Given an array `arr` of integers, check if there exist two indices `i` and `j` such that:

- `i != j`
- `0 <= i, j < arr.length`
- `arr[i] == 2 * arr[j]`

Return `true` if such elements exist, otherwise return `false`.

## Example

### Example 1:
```
Input: arr = [10, 2, 5, 3]
Output: true
Explanation: For i = 2 and j = 1, arr[i] = 5 is double of arr[j] = 2.
```

### Example 2:
```
Input: arr = [7, 1, 14, 11]
Output: true
Explanation: For i = 2 and j = 0, arr[i] = 14 is double of arr[j] = 7.
```

### Example 3:
```
Input: arr = [3, 1, 7, 11]
Output: false
Explanation: There is no pair of indices that satisfies the conditions.
```

## Constraints

- `2 <= arr.length <= 500`
- `-10^3 <= arr[i] <= 10^3`

## Approach

The solution uses a hash set to efficiently check for the existence of `2 * arr[i]` or `arr[i] / 2` for each element in the array. The algorithm iterates through the array and performs the following steps:

1. For each element in the array, check if either `2 * arr[i]` or `arr[i] / 2` exists in the hash set.
2. If such a value exists, return `true`.
3. Otherwise, add the current element to the hash set and continue.
4. If no such pair is found after iterating through the array, return `false`.

This approach ensures an efficient solution with a time complexity of O(n).

Refer to the `solution.py` file in this folder for the implementation details.

---