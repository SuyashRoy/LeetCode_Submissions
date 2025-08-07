# Leetcode Problem 119 - Pascal's Triangle II

---
## Problem Description

Given an integer `rowIndex`, return the `rowIndex`th (0-indexed) row of the Pascal's Triangle.

In Pascal's Triangle, each number is the sum of the two numbers directly above it.

### Example:

```
Input: rowIndex = 3
Output: [1,3,3,1]
```

### Constraints:

* `0 <= rowIndex <= 33`

## Approach

The problem requires generating only a specific row of Pascal's Triangle rather than the whole triangle. However, to compute the values of that specific row, we must generate all previous rows leading up to it.

The approach involves the following steps:

1. **Iterative Construction**:

   * Initialize an empty list to hold each row of the triangle.
   * Iterate from 0 to `rowIndex`, building one row at a time.

2. **Building a Row**:

   * Each row starts and ends with 1.
   * For elements in between, compute them as the sum of the two elements directly above from the previous row.
   * Specifically, for each element `j` in row `i`, the value is:

     ```
     row[j] = rows[i-1][j-1] + rows[i-1][j]
     ```

3. **Return Result**:

   * After building up to the desired row, return the final row.

This approach ensures correctness by leveraging the fundamental properties of Pascal's Triangle. While not optimized for space (as it constructs all rows up to the target), it is intuitive and suitable given the small constraint on `rowIndex`.

## Time and Space Complexity

* **Time Complexity**: `O(rowIndex^2)` — Each row has at most `rowIndex` elements, and we compute up to `rowIndex` rows.
* **Space Complexity**: `O(rowIndex^2)` — Due to storing all rows in memory until the target row is constructed.

---