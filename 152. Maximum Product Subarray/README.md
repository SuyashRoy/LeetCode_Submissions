# LeetCode Problem 152: Maximum Product Subarray

## Problem Description

The problem requires finding the contiguous subarray within an array (containing at least one number) which has the largest product. The goal is to return the maximum product of such a subarray.

## Approach

This solution uses a dynamic programming approach to efficiently compute the maximum product subarray. The key idea is to maintain two variables at each step:

1. **`max_product`**: The maximum product ending at the current index.
2. **`min_product`**: The minimum product ending at the current index (to handle negative numbers).

### Steps:

1. **Initialization**:
    - Start with the first element of the array as the initial `max_product`, `min_product`, and `result`.

2. **Iterate through the array**:
    - For each element, calculate the potential maximum and minimum products by considering:
      - The current element itself.
      - The product of the current element with the previous `max_product`.
      - The product of the current element with the previous `min_product`.
    - Update `max_product` and `min_product` accordingly.

3. **Update the result**:
    - At each step, update the `result` with the maximum value of `max_product`.

4. **Return the result**:
    - The `result` holds the maximum product of any contiguous subarray.

This approach ensures that the solution is computed in **O(n)** time complexity with **O(1)** space complexity.

## Code

The implementation can be found in the `solution.py` file. Below is a brief explanation of the code:

```python
class Solution:
     def maxProduct(self, nums: List[int]) -> int:
          # Initialize variables
          max_product = nums[0]
          min_product = nums[0]
          result = nums[0]
          
          # Iterate through the array
          for i in range(1, len(nums)):
                num = nums[i]
                
                # Compute temporary max and min
                temp_max = max(num, max_product * num, min_product * num)
                min_product = min(num, max_product * num, min_product * num)
                max_product = temp_max
                
                # Update the result
                result = max(result, max_product)
          
          return result
```

## Complexity Analysis

- **Time Complexity**: O(n), where n is the length of the input array. We traverse the array once.
- **Space Complexity**: O(1), as we use only a constant amount of extra space.

## Edge Cases

- Single-element arrays.
- Arrays with all negative numbers.
- Arrays containing zeros.

## Conclusion

This solution efficiently computes the maximum product subarray using a dynamic programming approach. By maintaining the maximum and minimum products at each step, it handles negative numbers and zeros effectively.

---