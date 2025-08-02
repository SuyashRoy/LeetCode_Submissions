# LeetCode 26: Remove Duplicates from Sorted Array

---
## Problem Description

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

Since it is impossible to change the length of the array in some languages, you must do this by modifying the input array in-place with O(1) extra memory.

### Example

**Input:**  
`nums = [1,1,2]`  
**Output:**  
`2, nums = [1,2,_]`  

**Input:**  
`nums = [0,0,1,1,1,2,2,3,3,4]`  
**Output:**  
`5, nums = [0,1,2,3,4,_,_,_,_,_]`  

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in non-decreasing order.

---

## Approach

The solution modifies the array in-place using a two-pointer technique:

1. Use one pointer (`i`) to track the position of the last unique element.
2. Iterate through the array with another pointer (`j`).
3. Whenever a new unique element is found, update the array at position `i + 1` and increment `i`.
4. Return `i + 1` as the count of unique elements.

This approach ensures O(n) time complexity and O(1) space complexity.

For the complete implementation, refer to the `solution.py` file in this folder.

---