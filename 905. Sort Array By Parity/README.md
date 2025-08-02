# LeetCode 905: Sort Array By Parity

---
## Problem Description

Given an integer array `nums`, move all the even integers at the beginning of the array followed by all the odd integers. Return **any array** that satisfies this condition.

### Constraints:
- `1 <= nums.length <= 5000`
- `0 <= nums[i] <= 5000`

## Approach

The solution involves iterating through the array and separating the even and odd numbers. The even numbers are collected first, followed by the odd numbers. This ensures that the resulting array satisfies the required condition.

### Steps:
1. Traverse the array and identify even numbers.
2. Append all even numbers to the result list.
3. Append all odd numbers to the result list.
4. Return the combined list.

The implementation of this approach can be found in the `solution.py` file in this folder.

## Complexity Analysis

- **Time Complexity**: O(n), where `n` is the length of the array. This is because we traverse the array once.
- **Space Complexity**: O(n), as we use an additional list to store the result.

## Example

Input:
```
nums = [3, 1, 2, 4]
```

Output:
```
[2, 4, 3, 1]
```

(Note: Other valid outputs include `[4, 2, 3, 1]` or any permutation where even numbers precede odd numbers.)

---