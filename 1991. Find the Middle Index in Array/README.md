# LeetCode Problem 1991: Find the Middle Index in Array

---
## Problem Description

The problem requires finding the **middle index** of an array such that the sum of the elements to the left of the index is equal to the sum of the elements to the right of the index. If there is no such index, return `-1`. If there are multiple such indices, return the left-most one.

### Constraints:
- The array length is between `1` and `100`.
- Each element of the array is between `-1000` and `1000`.

For more details, visit the [LeetCode Problem Page](https://leetcode.com/problems/find-the-middle-index-in-array/).

---

## Approach

The solution is implemented in the `solution.py` file. Below is a high-level overview of the approach:

1. **Calculate Total Sum**: Compute the total sum of the array.
2. **Iterate Through the Array**: Use a single pass to maintain a running sum of elements to the left of the current index.
3. **Check Condition**: At each index, check if the left sum equals the total sum minus the left sum minus the current element.
4. **Return Result**: If the condition is satisfied, return the current index. If no such index is found, return `-1`.

---

## File Structure

- `solution.py`: Contains the implementation of the solution.

---

## Example

### Input:
```text
nums = [2, 3, -1, 8, 4]
```

### Output:
```text
3
```

### Explanation:
At index `3`, the left sum is `4` (2 + 3 - 1) and the right sum is also `4` (4). Hence, the middle index is `3`.

---