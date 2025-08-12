# LeetCode Problem 1200: Minimum Absolute Difference

---
## Problem Description

Given an array of distinct integers `arr`, find all pairs of elements with the minimum absolute difference of any two elements. Each pair `[a, b]` should be listed in ascending order (i.e., `a < b`), and the pairs should be returned in ascending order of `a`.

### Constraints:
- `2 <= arr.length <= 10^5`
- `-10^6 <= arr[i] <= 10^6`

## Approach

The solution involves the following steps:

1. **Sort the Array**: Sorting the array ensures that the absolute difference between consecutive elements is minimized.
2. **Find the Minimum Difference**: Iterate through the sorted array to calculate the absolute differences between consecutive elements and determine the minimum difference.
3. **Collect Pairs**: Iterate through the sorted array again to collect all pairs of elements whose absolute difference equals the minimum difference.
4. **Return the Result**: Return the list of pairs sorted in ascending order.

This approach ensures an efficient solution with a time complexity of \(O(n \log n)\) due to the sorting step, followed by a linear pass to find the minimum difference and collect the pairs.

## Example

### Input:
```plaintext
arr = [4, 2, 1, 3]
```

### Output:
```plaintext
[[1, 2], [2, 3], [3, 4]]
```

### Explanation:
After sorting the array, the minimum absolute difference is `1`, and the pairs with this difference are `[1, 2]`, `[2, 3]`, and `[3, 4]`.

---