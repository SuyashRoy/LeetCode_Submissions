# LeetCode 283: Move Zeroes

---
## Problem Description

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements. Note that you must do this in-place without making a copy of the array.

### Example

#### Input:
```
nums = [0,1,0,3,12]
```

#### Output:
```
[1,3,12,0,0]
```

### Constraints:
- `1 <= nums.length <= 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

---

## Approach

The solution uses a two-pointer technique to efficiently rearrange the elements in-place. The key idea is to maintain a pointer for the position of the next non-zero element and iterate through the array to swap elements as needed.

### Steps:
1. Use a pointer (`nonZeroIndex`) to track the position where the next non-zero element should be placed.
2. Iterate through the array:
    - If the current element is non-zero, swap it with the element at `nonZeroIndex` and increment `nonZeroIndex`.
3. After the iteration, all non-zero elements will be at the beginning of the array, and the remaining positions will be filled with zeros.

Refer to the `solution.py` file in this folder for the detailed implementation.

---

## Complexity Analysis

- **Time Complexity**: O(n), where `n` is the length of the array. The array is traversed once.
- **Space Complexity**: O(1), as the operation is performed in-place without using extra space.

---