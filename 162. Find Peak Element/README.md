# LeetCode Problem 162: Find Peak Element

## Problem Description

A peak element is an element that is strictly greater than its neighbors. Given an input array `nums`, find a peak element and return its index. If the array contains multiple peaks, return the index of any of the peaks.

You may imagine `nums[-1] = nums[n] = -∞`.

### Constraints:
- `1 <= nums.length <= 1000`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `nums[i] != nums[i + 1]` for all valid `i`.

### Example:
#### Input:
```
nums = [1,2,3,1]
```
#### Output:
```
2
```
Explanation: 3 is a peak element and your function should return its index 2.

---

## Approach

The solution implemented in `solution.py` uses a **binary search** approach to efficiently find a peak element in `O(log n)` time complexity. This method leverages the properties of the array and avoids a brute-force search.

### Steps:
1. **Initialization**:
    - Define two pointers, `left` and `right`, to represent the search range. Initially, `left = 0` and `right = len(nums) - 1`.

2. **Binary Search**:
    - Calculate the middle index `mid` as `(left + right) // 2`.
    - Compare `nums[mid]` with `nums[mid + 1]`:
      - If `nums[mid] > nums[mid + 1]`, it means the peak lies on the left side (including `mid`). Update `right = mid`.
      - Otherwise, the peak lies on the right side. Update `left = mid + 1`.

3. **Termination**:
    - The loop continues until `left == right`, at which point `left` (or `right`) points to a peak element.

4. **Return**:
    - Return the index `left` as the peak element.

### Code:
```python
def findPeakElement(nums):
     left, right = 0, len(nums) - 1
     while left < right:
          mid = (left + right) // 2
          if nums[mid] > nums[mid + 1]:
                right = mid
          else:
                left = mid + 1
     return left
```

---

## Complexity Analysis

- **Time Complexity**: `O(log n)`  
  The binary search reduces the search space by half in each iteration.
  
- **Space Complexity**: `O(1)`  
  The solution uses constant space.

---

## Notes

- The binary search approach ensures optimal performance compared to a linear scan.
- The problem guarantees that a peak element always exists, so the solution is robust for all valid inputs.

---