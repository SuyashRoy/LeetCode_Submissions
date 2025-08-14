# LeetCode Problem 75: Sort Colors

---
## Problem Description
The problem **"Sort Colors"** is a classic algorithm problem that requires sorting an array containing only the integers `0`, `1`, and `2`. The goal is to sort the array in-place without using any library sorting functions.

### Constraints:
- The array contains only the integers `0`, `1`, and `2`.
- The solution must have a time complexity of O(n).
- The sorting must be done in-place.

For more details, visit the [LeetCode Problem Page](https://leetcode.com/problems/sort-colors/).

---

## Approach
The solution uses the **Dutch National Flag Algorithm**, which involves three pointers:
1. **Low Pointer**: Tracks the position for `0`s.
2. **High Pointer**: Tracks the position for `2`s.
3. **Current Pointer**: Iterates through the array.

The algorithm works by swapping elements to their correct positions as the `current` pointer traverses the array.

Refer to the `solution.py` file in this folder for the complete implementation and detailed explanation of the approach.

---

## Complexity Analysis
- **Time Complexity**: O(n), where `n` is the size of the array.
- **Space Complexity**: O(1), as the sorting is done in-place.

---

## Example
Input: `[2, 0, 2, 1, 1, 0]`  
Output: `[0, 0, 1, 1, 2, 2]`

---