# LeetCode Problem 3477: Fruits Into Baskets II

---
## Problem Description

You are given two arrays of integers, `fruits` and `baskets`, each of length `n`, where `fruits[i]` represents the quantity of the `i`th type of fruit, and `baskets[j]` represents the capacity of the `j`th basket.

From left to right, place the fruits according to these rules:

1. Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
2. Each basket can hold only one type of fruit.
3. If a fruit type cannot be placed in any basket, it remains unplaced.

Return the number of fruit types that remain unplaced after all possible allocations are made.

## Approach
Here's the high-level approach:

1. **Initialize the Variables**: Initialize a `num_placed` counter to count the fruits placed. Also initialize two arrays `placed` and `basket_placed` to denote the basket used for ith fruit and the fruit placed in the jth basket

2. **Iterate Through Fruits**: For each fruit type in the `fruits` array, attempt to place it in the leftmost available basket that can accommodate it.

3. **Track Unplaced Fruits**: If a suitable basket is found for a fruit type, increment the count of `num_placed` counter and track the fruit and basket placement with the two arrays

4. **Return the Result**: After processing all fruit types, return the count of unplaced fruits.

## Complexity Analysis

- **Time Complexity**: O($n^2$), where `n` is the length of the arrays, since we are looping over both the input arrays
- **Space Complexity**: O(n), as the algorithm uses a linear amount of extra space, (equal to length of arrays)

---