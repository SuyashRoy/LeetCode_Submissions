# LeetCode Problem 268: Missing Number

## Problem Description

The problem asks us to find the missing number in an array containing `n` distinct numbers taken from the range `[0, n]`. The array is guaranteed to have exactly one missing number.

## Approach

This solution leverages the **mathematical summation formula** to efficiently determine the missing number. The approach is based on the fact that the sum of the first `n` natural numbers can be calculated using the formula:

\[
\text{Sum} = \frac{n \times (n + 1)}{2}
\]

### Steps:

1. **Calculate the Expected Sum**: Using the formula above, compute the sum of numbers from `0` to `n`.
2. **Calculate the Actual Sum**: Compute the sum of all elements in the given array.
3. **Find the Missing Number**: Subtract the actual sum from the expected sum to get the missing number.

This approach ensures an **O(n)** time complexity and **O(1)** space complexity.

## Code

The solution is implemented in `solution.py` as follows:

```python
def missingNumber(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
```

### Explanation of the Code:

1. **Calculate `n`**: The length of the input array `nums` is used to determine the range `[0, n]`.
2. **Expected Sum**: The formula `n * (n + 1) // 2` is used to calculate the sum of the first `n` natural numbers.
3. **Actual Sum**: The `sum()` function computes the sum of all elements in the array.
4. **Missing Number**: The difference between the expected sum and the actual sum gives the missing number.

## Complexity Analysis

- **Time Complexity**: \(O(n)\), where \(n\) is the size of the input array. This is due to the single pass required to compute the sum of the array.
- **Space Complexity**: \(O(1)\), as no additional data structures are used.

## Example

### Input:
```python
nums = [3, 0, 1]
```

### Output:
```python
2
```

### Explanation:
- The expected sum for `n = 3` is \(3 \times (3 + 1) / 2 = 6\).
- The actual sum of the array is \(3 + 0 + 1 = 4\).
- The missing number is \(6 - 4 = 2\).

## Conclusion

This solution is optimal for the problem, utilizing a mathematical approach to achieve efficiency in both time and space. It is simple, elegant, and leverages the properties of arithmetic progression to solve the problem effectively.

---