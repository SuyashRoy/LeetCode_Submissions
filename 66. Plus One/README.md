# LeetCode Problem 66: Plus One

---
## Problem Description
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer. The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit. You may assume the integer does not contain any leading zero, except the number 0 itself.

## Example
### Input:
```
digits = [1, 2, 3]
```
### Output:
```
[1, 2, 4]
```
### Explanation:
The array represents the integer 123. Incrementing by one gives 124, which is represented as [1, 2, 4].

## Approach
The solution iterates through the digits array from the least significant digit (rightmost) to the most significant digit (leftmost). It handles the following cases:
1. If the current digit is less than 9, increment it and return the result immediately.
2. If the current digit is 9, set it to 0 and continue to the next digit.
3. If all digits are processed and a carry remains, prepend `1` to the array.

This approach ensures an efficient solution with a time complexity of O(n), where `n` is the number of digits.

## References
- [LeetCode Problem 66](https://leetcode.com/problems/plus-one/)

---