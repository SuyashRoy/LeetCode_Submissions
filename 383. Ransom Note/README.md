# LeetCode Problem 383: Ransom Note

---
## Problem Description
Given two strings `ransomNote` and `magazine`, determine if you can construct the `ransomNote` using the letters from `magazine`. Each letter in `magazine` can only be used once in `ransomNote`.

## Approach

To solve this problem, we can use the following approach:

1. **Initial Check**:  
    If the length of `ransomNote` is greater than the length of `magazine`, it is impossible to construct the `ransomNote`. Return `False` in this case.

2. **Frequency Count**:  
    Use a dictionary to count the frequency of each character in `magazine`. This will help us track how many times each letter is available for use.

3. **Validation**:  
    Iterate through each character in `ransomNote` and check if it exists in the dictionary with a non-zero count:
    - If the character is not available or its count is zero, return `False`.
    - Otherwise, decrement the count of the character in the dictionary.

4. **Final Result**:  
    If all characters in `ransomNote` can be matched with available characters in `magazine`, return `True`.

## Example Usage

```python
# Example 1
Input: ransomNote = "a", magazine = "b"
Output: False

# Example 2
Input: ransomNote = "aa", magazine = "ab"
Output: False

# Example 3
Input: ransomNote = "aa", magazine = "aab"
Output: True
```

This approach ensures that we efficiently check the feasibility of constructing the `ransomNote` using the `magazine` while maintaining a time complexity of O(n + m), where `n` is the length of `ransomNote` and `m` is the length of `magazine`.

---