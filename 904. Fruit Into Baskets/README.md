# LeetCode Problem 904: Fruit Into Baskets

---
## Problem Description

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array `fruits` where `fruits[i]` is the type of fruit the `i-th` tree produces.

You want to collect as much fruit as possible, but you are only allowed to use **two baskets**. Each basket can only hold a single type of fruit, and there is no limit on the amount of fruit each basket can hold. Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the starting tree) while moving to the right. The goal is to maximize the total number of fruits you can collect.

### Constraints:
- `1 <= fruits.length <= 10^5`
- `0 <= fruits[i] < fruits.length`

## Approach

The solution uses the **sliding window technique** to efficiently solve the problem. Below is a high-level explanation of the approach:

1. **Sliding Window Initialization**:
    - Use two pointers to represent the current window of trees being considered.
    - Maintain a dictionary to track the count of each fruit type in the current window.

2. **Expand the Window**:
    - Iterate through the array, adding fruits to the window while ensuring that the number of distinct fruit types does not exceed two.

3. **Shrink the Window**:
    - If the number of distinct fruit types exceeds two, shrink the window from the left until the condition is satisfied.

4. **Track the Maximum**:
    - During each iteration, calculate the size of the current window and update the maximum size if the current window is larger.

5. **Output the Result**:
    - Return the maximum size of the window as the result.

## File Structure

- `solution.py`: Contains the implementation of the sliding window approach to solve the problem.

## Complexity Analysis

- **Time Complexity**: `O(n)`, where `n` is the length of the `fruits` array. Each element is processed at most twice (once when expanding the window and once when shrinking it).
- **Space Complexity**: `O(1)`, as the dictionary will store at most two distinct fruit types at any time.

## Example

Input:
```
fruits = [1, 2, 1]
```

Output:
```
3
```

Explanation:
- You can collect all fruits since there are only two types of fruits.

For more details, refer to the implementation in `solution.py`.

---