# LeetCode Problem 81: Search in Rotated Sorted Array II

## Problem Description

The problem requires determining if a given target value exists in a rotated sorted array that may contain duplicates. The array is sorted in ascending order, but it has been rotated at some pivot. The task is to return `true` if the target exists in the array, otherwise return `false`.

## Solution Explanation

The solution is implemented in `solution.py`. Below is a detailed explanation of the approach used:

### Approach

1. **Binary Search with Adjustments for Rotation**:
    - The solution uses a modified binary search algorithm to handle the rotation and duplicates in the array.
    - The key challenge is to determine which part of the array (left or right) is sorted, as the rotation disrupts the usual order.

2. **Handling Duplicates**:
    - Duplicates can make it difficult to determine the sorted portion of the array. To address this, the algorithm skips duplicate elements at the start and end of the current search range.

3. **Algorithm Steps**:
    - Initialize two pointers, `left` and `right`, to the start and end of the array.
    - While `left` is less than or equal to `right`:
      - Calculate the middle index, `mid`.
      - If the middle element matches the target, return `true`.
      - If duplicates are present at the boundaries (`nums[left] == nums[mid] == nums[right]`), increment `left` and decrement `right` to skip them.
      - Determine which side of the array is sorted:
         - If the left side is sorted (`nums[left] <= nums[mid]`):
            - Check if the target lies within this range. If yes, adjust `right` to `mid - 1`. Otherwise, adjust `left` to `mid + 1`.
         - If the right side is sorted:
            - Check if the target lies within this range. If yes, adjust `left` to `mid + 1`. Otherwise, adjust `right` to `mid - 1`.
    - If the loop ends without finding the target, return `false`.

### Complexity Analysis

- **Time Complexity**: O(n) in the worst case (due to duplicates), but typically O(log n) for most inputs.
- **Space Complexity**: O(1), as the solution uses constant extra space.

### Code

Refer to the `solution.py` file for the complete implementation.

## Example

### Input
```python
nums = [2, 5, 6, 0, 0, 1, 2]
target = 0
```

### Output
```python
True
```

### Explanation
The target `0` exists in the rotated array.

## Conclusion

This solution efficiently handles the challenges posed by rotation and duplicates in the array. By leveraging a modified binary search, it ensures optimal performance for most cases.

---