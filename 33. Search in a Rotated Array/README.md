# LeetCode Problem 33: Search in Rotated Sorted Array

## Problem Description

You are given an integer array `nums` sorted in ascending order (with distinct values), and an integer `target`. The array is rotated at an unknown pivot index such that the array becomes `[nums[p], nums[p+1], ..., nums[n-1], nums[0], nums[1], ..., nums[p-1]]` (0-indexed). For example, `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`.

Given the array `nums` after the rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

## Solution Explanation

The solution is implemented in the `solution.py` file. Below is a detailed explanation of the approach:

### Approach

1. **Binary Search with Rotation Handling**:
    - The problem requires `O(log n)` complexity, which suggests using binary search.
    - The array is rotated, so we need to determine which part of the array is sorted during each step of the binary search.

2. **Steps**:
    - Initialize two pointers, `left` and `right`, to the start and end of the array.
    - While `left <= right`:
      - Calculate the middle index `mid`.
      - Check if `nums[mid]` is equal to the `target`. If yes, return `mid`.
      - Determine which half of the array is sorted:
         - If `nums[left] <= nums[mid]`, the left half is sorted:
            - Check if the `target` lies within the range `[nums[left], nums[mid]]`. If yes, adjust `right` to `mid - 1`. Otherwise, adjust `left` to `mid + 1`.
         - Otherwise, the right half is sorted:
            - Check if the `target` lies within the range `[nums[mid], nums[right]]`. If yes, adjust `left` to `mid + 1`. Otherwise, adjust `right` to `mid - 1`.
    - If the loop ends without finding the `target`, return `-1`.

3. **Edge Cases**:
    - Empty array: Return `-1`.
    - Single element array: Check if the element matches the `target`.

### Code

```python
def search(nums, target):
     left, right = 0, len(nums) - 1

     while left <= right:
          mid = (left + right) // 2

          if nums[mid] == target:
                return mid

          # Determine which side is sorted
          if nums[left] <= nums[mid]:  # Left side is sorted
                if nums[left] <= target < nums[mid]:
                     right = mid - 1
                else:
                     left = mid + 1
          else:  # Right side is sorted
                if nums[mid] < target <= nums[right]:
                     left = mid + 1
                else:
                     right = mid - 1

     return -1
```

### Complexity Analysis

- **Time Complexity**: `O(log n)` due to binary search.
- **Space Complexity**: `O(1)` as no additional space is used.

## Example

### Input
```plaintext
nums = [4,5,6,7,0,1,2]
target = 0
```

### Output
```plaintext
4
```

### Explanation
- The target `0` is found at index `4`.

## Conclusion

This solution efficiently handles the rotated sorted array using binary search, ensuring `O(log n)` runtime complexity. It leverages the properties of sorted subarrays to narrow down the search space.

---