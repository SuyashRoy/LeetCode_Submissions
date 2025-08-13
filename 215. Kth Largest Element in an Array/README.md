# 215. Kth Largest Element in an Array

---
## Problem Description
Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array. Note that it is the `k`th largest element in sorted order, not the `k`th distinct element.

### Example:
**Input:** `nums = [3,2,1,5,6,4], k = 2`  
**Output:** `5`

**Input:** `nums = [3,2,3,1,2,4,5,5,6], k = 4`  
**Output:** `4`

### Constraints:
- `1 <= k <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`

---

## Approach

The solution uses the following approach:

1. **Heap Data Structure**:  
    A min-heap is utilized to efficiently find the `k`th largest element. By maintaining a heap of size `k`, we can ensure that the smallest element in the heap is the `k`th largest element in the array.

2. **Algorithm Steps**:
    - Iterate through the array and add elements to the heap.
    - If the heap size exceeds `k`, remove the smallest element (heap root).
    - After processing all elements, the root of the heap will be the `k`th largest element.

3. **Time Complexity**:  
    - Building and maintaining the heap takes `O(n log k)` time, where `n` is the number of elements in the array.
    - This is efficient for large arrays with a small `k`.

4. **Space Complexity**:  
    - The space complexity is `O(k)` due to the heap storage.

---