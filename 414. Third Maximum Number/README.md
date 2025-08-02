# LeetCode 414: Third Maximum Number

---
## Problem Description

Given an integer array `nums`, return the **third distinct maximum** number in this array. If the third maximum does not exist, return the **maximum** number.

You can find the full problem description on [LeetCode](https://leetcode.com/problems/third-maximum-number/).

---

## Approach

The solution implemented in `solution.py` follows these steps:

1. **Remove Duplicates**: Use a set to eliminate duplicate numbers from the array.
2. **Sort the Numbers**: Sort the unique numbers in descending order.
3. **Check for Third Maximum**:
    - If there are at least three distinct numbers, return the third maximum.
    - Otherwise, return the maximum number.

This approach ensures that the solution is both efficient and easy to understand.

---

## Complexity Analysis

- **Time Complexity**: 
  - Removing duplicates and sorting the array takes \(O(n \log n)\), where \(n\) is the size of the input array.
- **Space Complexity**: 
  - The space used for storing the unique numbers is \(O(n)\).

---

## File Structure

- `solution.py`: Contains the implementation of the solution.

---

## Example

Input:
```
nums = [3, 2, 1]
```

Output:
```
1
```

Explanation: The third maximum number is `1`.

---