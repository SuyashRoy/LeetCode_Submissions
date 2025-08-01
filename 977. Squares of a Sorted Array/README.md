# 977. Squares of a Sorted Array

---
## Problem Description
Given an integer array `nums` sorted in **non-decreasing order**, return an array of the **squares of each number** sorted in **non-decreasing order**.

## Example
### Input:
```
nums = [-4, -1, 0, 3, 10]
```
### Output:
```
[0, 1, 9, 16, 100]
```

### Input:
```
nums = [-7, -3, 2, 3, 11]
```
### Output:
```
[4, 9, 9, 49, 121]
```

## Constraints
- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in **non-decreasing order**.

## Approach
The problem can be solved efficiently using a two-pointer technique. By comparing the absolute values of the numbers at the start and end of the array, we can determine the largest square and place it in the correct position in the result array.

---