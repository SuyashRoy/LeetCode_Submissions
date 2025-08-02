# LeetCode 1051: Height Checker

---
## Problem Description

The problem **Height Checker** requires determining how many students are not standing in the correct positions when compared to their expected order. The expected order is determined by sorting the heights in non-decreasing order.

You can find the full problem description on [LeetCode](https://leetcode.com/problems/height-checker/).

## Approach

The solution involves the following steps:

1. **Sort the Heights**: Create a sorted version of the input list of heights.
2. **Compare Positions**: Iterate through the original and sorted lists simultaneously, counting the number of positions where the heights differ.
3. **Return the Count**: The final count represents the number of students not in their correct positions.

The implementation of this approach can be found in the `solution.py` file in this folder.

## Complexity Analysis

- **Time Complexity**:  
    Sorting the list takes \(O(n \log n)\), and comparing the two lists takes \(O(n)\). Thus, the overall time complexity is \(O(n \log n)\).
    
- **Space Complexity**:  
    The space complexity is \(O(n)\) due to the creation of the sorted list.

## Usage

To understand the implementation details, refer to the `solution.py` file in this directory.

---