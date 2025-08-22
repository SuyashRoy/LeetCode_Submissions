# LeetCode Problem 3: Longest Substring Without Repeating Characters

---
## Problem Description
Given a string `s`, find the length of the longest substring without repeating characters.

### Example
**Input:**  
`s = "abcabcbb"`  
**Output:**  
`3`  
**Explanation:** The answer is `"abc"`, with the length of `3`.

---

## Approach

The solution uses a sliding window technique to efficiently find the longest substring without repeating characters. Below is a step-by-step explanation of the approach:

### 1. Initialize Variables
- `substring`: A string to keep track of the current substring without repeating characters.
- `max_len`: An integer to store the maximum length of a substring found so far.

### 2. Iterate Through the Input String
- Loop through each character in the string `s` using `enumerate` to get both the index and the character.

### 3. Check for Repeating Characters
- If the current character is **not** in `substring`, append it to `substring`.
- If the current character **is** in `substring`:
    - Update `max_len` to the maximum of `max_len` and the length of `substring`.
    - Find the index of the first occurrence of the repeating character in `substring` using `substring.index(string)`.
    - Append the current character to `substring` and remove all characters up to and including the first occurrence of the repeating character.

### 4. Final Update
- After the loop, update `max_len` one last time to ensure the longest substring is accounted for.

### 5. Return the Result
- Return `max_len` as the length of the longest substring without repeating characters.

---

## Complexity Analysis
- **Time Complexity:**  
    The algorithm iterates through the string once, and operations like finding the index of a character in `substring` are linear in the worst case. Thus, the overall time complexity is **O(n²)**, where `n` is the length of the string.

- **Space Complexity:**  
    The space complexity is **O(n)** due to the storage of the `substring`.

---

## Key Insights
- The sliding window approach ensures that we only consider valid substrings without repeating characters.
- By dynamically adjusting the `substring` and keeping track of the maximum length, the solution avoids unnecessary recomputation.

---  