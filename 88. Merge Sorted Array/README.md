# LeetCode Problem 88: Merge Sorted Array

---
## Problem Description

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively. 

Merge `nums2` into `nums1` as one sorted array. The final sorted array should not be returned by the function but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements to be merged, and the last `n` elements are set to `0` and should be ignored.

### Constraints:
- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

---

## Approach

The solution uses a **two-pointer technique** to merge the arrays in-place, starting from the end of both arrays. This approach ensures that the larger elements are placed in their correct positions in `nums1` without overwriting any existing values.

### Steps:
1. Initialize two pointers, one for the last element of the initialized part of `nums1` (`m-1`) and one for the last element of `nums2` (`n-1`).
2. Use a third pointer starting from the end of `nums1` (`m + n - 1`) to place the largest elements in their correct positions.
3. Compare the elements pointed to by the two pointers and place the larger one at the position of the third pointer.
4. Decrement the respective pointers and repeat until all elements are merged.
5. If any elements remain in `nums2`, copy them into `nums1`.

This approach ensures an efficient in-place merge with a time complexity of **O(m + n)** and a space complexity of **O(1)**.

---

## Example

### Input:
```plaintext
nums1 = [1, 2, 3, 0, 0, 0], m = 3
nums2 = [2, 5, 6], n = 3
```

### Output:
```plaintext
nums1 = [1, 2, 2, 3, 5, 6]
```

---