# LeetCode Problem 1: Two Sum

---
## Problem Description

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to the target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## Example

### Input:
```
nums = [2,7,11,15], target = 9
```

### Output:
```
[0,1]
```

### Explanation:
Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

## Approach

The approach to solving this problem is implemented in the `solution.py` file located in this folder. The logic involves using a two-pointer technique to find the two numbers that sum up to the target. The steps are as follows:

1. Sort a copy of the input array `nums` while keeping the original array intact.
2. Use two pointers, `i` starting at the beginning and `j` at the end of the sorted array.
3. Calculate the sum of the elements at the two pointers:
   - If the sum is less than the target, increment `i`.
   - If the sum is greater than the target, decrement `j`.
   - If the sum equals the target, store the two numbers 
4. Considering the case where duplicates are present in `nums`:
   - Compute the index of the smaller of the two numbers
   - In the case of identical numbers, only the first occurence index is obtained from `.index()` method
   - To tackle this, run a loop on `nums` in reverse and obtain the other index for the pair

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

## Notes

- Make sure to handle edge cases such as negative numbers and duplicate values in the array.
- The solution should aim for optimal time complexity.
- Test the solution with various inputs to ensure correctness.
- Refer to the `solution.py` file for the implementation details.

---