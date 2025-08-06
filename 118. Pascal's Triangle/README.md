# 118. Pascal's Triangle

---
## Problem Description

Given an integer `numRows`, return the first `numRows` of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

```
    1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
```

## Constraints

- `1 <= numRows <= 30`

## Approach

The solution generates Pascal's Triangle row by row. Each row is constructed based on the previous row:

1. Start with the first row `[1]`.
2. For each subsequent row:
   - Begin with `[1]`.
   - Compute the intermediate values by summing adjacent elements from the previous row.
   - End the row with `[1]`.
3. Repeat until the desired number of rows (`numRows`) is generated.

This approach ensures that each row is built iteratively, leveraging the properties of Pascal's Triangle.

## Complexity

- **Time Complexity**: `O(numRows^2)`  
  Each row computation involves iterating through the previous row, and there are `numRows` rows.

- **Space Complexity**: `O(numRows^2)`  
  The space is used to store all rows of the triangle.

## Usage

Refer to the `solution.py` file in this folder for the implementation of the above approach.

---