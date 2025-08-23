# Longest Palindromic Substring

---

## Problem Description

Given a string `s`, return the longest palindromic substring in `s`.

A **palindrome** is a string that reads the same backward as forward.

### Example 1:
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

### Example 2:
```
Input: s = "cbbd"
Output: "bb"
```

### Constraints:
- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters.

---

## Approach

The solution uses a brute-force approach to find the longest palindromic substring:

1. Iterate through the string `s` and build substrings starting from each character.
2. For each substring, check if it is a palindrome by comparing it with its reverse.
3. Keep track of the longest palindrome found so far.
4. Return the longest palindromic substring.

### Key Points:
- The algorithm uses nested loops to generate substrings and checks for palindromic properties.
- The time complexity is **O(n³)** due to the substring generation and palindrome check.
- This approach is simple but not optimal for larger inputs.

---

## Notes

- This solution is not optimized for performance. For better efficiency, consider dynamic programming or expanding around the center techniques.
- The provided implementation is a good starting point for understanding the problem and brute-force solutions.

---  