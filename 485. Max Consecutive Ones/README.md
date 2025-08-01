# 485. Max Consecutive Ones

---
## Problem Description
Given a binary array `nums`, return the maximum number of consecutive `1`s in the array.

### Example:
**Input:** `nums = [1,1,0,1,1,1]`  
**Output:** `3`  
**Explanation:** The first two `1`s and the last three `1`s form two groups of consecutive `1`s. The maximum number of consecutive `1`s is `3`.

### Constraints:
- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.

---

## Approach

### Algorithm:
1. Initialize a counter `counter` to track the current streak of `1`s and a variable `window` to store the maximum streak.
2. Iterate through the array:
    - If the current element is `1`, increment `counter`.
    - If the current element is `0`, update `window` with the maximum of `window` and `counter`, then reset `counter` to `0`.
3. After the loop, update `window` one last time to account for a streak ending at the last element.
4. Return `window`.

---

## Complexity Analysis
- **Time Complexity:** `O(n)` - We traverse the array once.
- **Space Complexity:** `O(1)` - No additional space is used.

---