# LeetCode Problem 229: Majority Element II

## Problem Description

The problem asks us to find all elements in an array that appear more than `n/3` times, where `n` is the size of the array. The solution must run in linear time and use constant extra space.

For more details, visit the [LeetCode Problem Page](https://leetcode.com/problems/majority-element-ii/).

---

## Solution Explanation

The solution is implemented in the `solution.py` file. It uses the **Boyer-Moore Voting Algorithm** to efficiently find the majority elements. Here's a breakdown of the approach:

### Key Steps:

1. **Candidate Selection**:
    - Maintain two potential candidates (`candidate1` and `candidate2`) and their respective counts (`count1` and `count2`).
    - Traverse the array and update the candidates based on the following rules:
      - If the current number matches `candidate1` or `candidate2`, increment their respective counts.
      - If `count1` or `count2` is zero, assign the current number as the new candidate and set its count to 1.
      - Otherwise, decrement both counts.

2. **Candidate Validation**:
    - After the first pass, `candidate1` and `candidate2` are potential majority elements.
    - Perform a second pass to count their occurrences and verify if they appear more than `n/3` times.

3. **Output**:
    - Return the verified majority elements as the result.

### Complexity Analysis:
- **Time Complexity**: `O(n)` for two passes through the array.
- **Space Complexity**: `O(1)` as only a constant amount of extra space is used.

---

## Code

Refer to the `solution.py` file for the complete implementation.

---

## Example

### Input:
```python
nums = [3, 2, 3]
```

### Output:
```python
[3]
```

### Explanation:
- The number `3` appears more than `n/3` times in the array.

---

## Notes

This solution is optimal for the given constraints and adheres to the requirements of linear time complexity and constant space usage.  