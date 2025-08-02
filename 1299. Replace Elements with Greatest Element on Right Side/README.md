# Leetcode 1299: Replace Elements with Greatest Element on Right Side

---
## Problem Description

Given an array `arr`, replace every element in that array with the greatest element among the elements to its right, and replace the last element with `-1`.  
You are required to perform this operation in-place.

### Example:
**Input:**  
`arr = [17,18,5,4,6,1]`  
**Output:**  
`[18,6,6,6,1,-1]`

### Constraints:
- `1 <= arr.length <= 10^4`
- `1 <= arr[i] <= 10^5`

---

## Approach

The solution is implemented in the `solution.py` file. Below is a high-level explanation of the approach:

1. **Iterate from Right to Left:**  
    Start from the second-to-last element and move towards the beginning of the array. This allows us to keep track of the maximum element on the right side efficiently.

2. **Track the Maximum Element:**  
    Maintain a variable to store the maximum element encountered so far. Update this variable as you iterate through the array.

3. **In-Place Modification:**  
    Replace the current element with the maximum element on its right side. The last element is replaced with `-1`.

4. **Time Complexity:**  
    The solution runs in `O(n)` time, where `n` is the length of the array, as we traverse the array once.

5. **Space Complexity:**  
    The solution uses `O(1)` additional space since the modifications are done in-place.

---

## How to Run

1. Place the input array in the `solution.py` file.
2. Run the script to get the modified array as output.

For more details, refer to the implementation in `solution.py`.

---