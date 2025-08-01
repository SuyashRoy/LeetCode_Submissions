# 1342. Number of Steps to Reduce a Number to Zero

## Problem Description
Given an integer `num`, the task is to return the number of steps to reduce it to zero. In one step, you can either:
1. Subtract `1` from it if the number is odd.
2. Divide it by `2` if the number is even.

## Example
### Example 1:
```
Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7.  
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3.  
Step 4) 3 is odd; subtract 1 and obtain 2.  
Step 5) 2 is even; divide by 2 and obtain 1.  
Step 6) 1 is odd; subtract 1 and obtain 0.
```

### Example 2:
```
Input: num = 8
Output: 4
Explanation: 
Step 1) 8 is even; divide by 2 and obtain 4.  
Step 2) 4 is even; divide by 2 and obtain 2.  
Step 3) 2 is even; divide by 2 and obtain 1.  
Step 4) 1 is odd; subtract 1 and obtain 0.
```

### Example 3:
```
Input: num = 123
Output: 12
```

## Constraints
- `0 <= num <= 10^6`

## Approach
1. Initialize a counter to track the number of steps.
2. Use a loop to repeatedly apply the rules:
    - If the number is even, divide it by 2.
    - If the number is odd, subtract 1.
3. Increment the counter for each operation.
4. Stop when the number becomes 0 and return the counter.

## Complexity
- **Time Complexity:** O(log(num)) - Each division by 2 reduces the number significantly.
- **Space Complexity:** O(1) - No additional space is used.

## Links
- [LeetCode Problem](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/)