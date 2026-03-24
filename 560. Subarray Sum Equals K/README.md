# Leetcode Problem 560: Subarray Sum Equals K

## Problem Description

Given an array of integers `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals to `k`.

### Example:
```
Input: nums = [1,1,1], k = 2
Output: 2
```

## Solution Explanation

The solution provided in `solution.py` uses an efficient approach with a **HashMap (dictionary)** to keep track of cumulative sums and their frequencies. This reduces the time complexity compared to a brute-force approach.

### Key Steps in the Solution:

1. **Initialize Variables**:
    - `count` to store the number of subarrays that sum to `k`.
    - `current_sum` to maintain the cumulative sum while iterating through the array.
    - `prefix_sums` as a dictionary to store the frequency of cumulative sums. It is initialized with `{0: 1}` to handle cases where a subarray starting from the beginning equals `k`.

2. **Iterate Through the Array**:
    - For each element in `nums`, add it to `current_sum`.
    - Check if `current_sum - k` exists in `prefix_sums`. If it does, it means there is a subarray ending at the current index that sums to `k`. Add the frequency of `current_sum - k` to `count`.
    - Update `prefix_sums` with the current cumulative sum.

3. **Return the Result**:
    - After iterating through the array, `count` contains the total number of subarrays whose sum equals `k`.

### Complexity Analysis:
- **Time Complexity**: O(n), where `n` is the length of the array. Each element is processed once.
- **Space Complexity**: O(n), for storing the cumulative sums in the dictionary.

### Code:
Refer to the `solution.py` file for the complete implementation.

## How to Run:
1. Place the `solution.py` file in the same directory as this README.
2. Run the script with your desired input to test the solution.

## Conclusion:
This solution efficiently solves the problem using a HashMap to track cumulative sums, making it suitable for large input sizes.