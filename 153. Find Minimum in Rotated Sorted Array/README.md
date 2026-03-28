# LeetCode Problem 153: Find Minimum in Rotated Sorted Array

## Problem Description

The problem requires finding the minimum element in a rotated sorted array. The array is sorted in ascending order but has been rotated at some pivot. You must solve the problem in O(log n) time complexity.

**Example:**
```
Input: nums = [3,4,5,1,2]
Output: 1
```

## Approach

The solution uses a **binary search** approach to achieve the required O(log n) time complexity. Here's a detailed explanation of the implementation:

### Steps:

1. **Initialization:**
    - Define two pointers, `left` and `right`, to represent the bounds of the search space.
    - `left` starts at the beginning of the array, and `right` starts at the end.

2. **Binary Search:**
    - While `left` is less than `right`:
      - Calculate the middle index: `mid = left + (right - left) // 2`.
      - Compare `nums[mid]` with `nums[right]`:
         - If `nums[mid] > nums[right]`, the minimum must be in the right half. Update `left = mid + 1`.
         - Otherwise, the minimum is in the left half or at `mid`. Update `right = mid`.

3. **Result:**
    - When the loop ends, `left` and `right` converge to the index of the minimum element. Return `nums[left]`.

### Code

```python
def findMin(nums):
     left, right = 0, len(nums) - 1
     while left < right:
          mid = left + (right - left) // 2
          if nums[mid] > nums[right]:
                left = mid + 1
          else:
                right = mid
     return nums[left]
```

### Complexity Analysis

- **Time Complexity:** O(log n) due to binary search.
- **Space Complexity:** O(1) as no additional space is used.

## Conclusion

This approach efficiently finds the minimum element in a rotated sorted array using binary search. The key insight is leveraging the properties of the rotated array to reduce the search space in each iteration.

---