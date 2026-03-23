# LeetCode Problem 53: Maximum Subarray

## Problem Description
The problem requires finding the contiguous subarray (containing at least one number) which has the largest sum and returning its sum.

## Approach

### Algorithm
The solution implemented in `solution.py` uses **Kadane's Algorithm**, which is an efficient way to solve the problem in linear time.

1. Initialize two variables:
    - `current_sum` to track the sum of the current subarray.
    - `max_sum` to store the maximum sum encountered so far.

2. Iterate through the array:
    - For each element, decide whether to add it to the current subarray or start a new subarray with the current element.
    - Update `current_sum` to the maximum of the current element or `current_sum + current element`.
    - Update `max_sum` to the maximum of `max_sum` and `current_sum`.

3. Return `max_sum` as the result.

### Complexity
- **Time Complexity**: O(n), where n is the number of elements in the array.
- **Space Complexity**: O(1), as no additional data structures are used.

### Example
Input: `nums = [-2,1,-3,4,-1,2,1,-5,4]`  
Output: `6`  
Explanation: The subarray `[4,-1,2,1]` has the largest sum = 6.

This approach ensures optimal performance and simplicity.

## File Structure
- `solution.py`: Contains the Python implementation of the solution.
- `README.md`: Documentation of the problem and approach.

## References
- [LeetCode Problem 53](https://leetcode.com/problems/maximum-subarray/)
- Kadane's Algorithm
- Python Standard Library

---