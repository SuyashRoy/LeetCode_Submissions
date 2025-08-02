# LeetCode Problem 27: Remove Element

---
## Problem Description

The problem requires modifying an array in-place to remove all instances of a specified value and return the new length of the array. The order of elements can be changed, and it doesn't matter what values are left beyond the new length.

For more details, visit the [LeetCode Problem Page](https://leetcode.com/problems/remove-element/).

---

## Approach

The solution uses a two-pointer technique to efficiently remove the specified value from the array. Here's a high-level overview of the approach:

1. **Two Pointers**: Use one pointer to iterate through the array (`i`) and another pointer (`k`) to track the position of the next valid element.
2. **Element Check**: For each element in the array, check if it matches the value to be removed.
3. **Update Array**: If the current element does not match the value, assign it to the position tracked by `k` and increment `k`.
4. **Return Result**: After processing all elements, `k` will represent the new length of the array.

This approach ensures that the array is modified in-place with O(1) extra space and O(n) time complexity.

---

## File Structure

- `solution.py`: Contains the implementation of the solution.

---

## Example

Given the input:
```plaintext
nums = [3, 2, 2, 3]
val = 3
```

After calling the function, the array will be modified to:
```plaintext
nums = [2, 2, _, _]
```
And the function will return:
```plaintext
new_length = 2
```

---

## Complexity Analysis

- **Time Complexity**: O(n), where `n` is the number of elements in the array.
- **Space Complexity**: O(1), as the solution modifies the array in-place without using extra space.

---