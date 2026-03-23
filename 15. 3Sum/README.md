# LeetCode Problem 15: 3Sum

## Problem Description
The **3Sum** problem requires finding all unique triplets in the array that sum up to zero. The solution must not include duplicate triplets.

## Approach

### Algorithm
1. **Sorting**: The input array is first sorted to simplify the process of avoiding duplicates and to enable the two-pointer technique.
2. **Iterating**: Iterate through the array with a loop, treating each element as a potential first element of the triplet.
3. **Two-Pointer Technique**: For each iteration, use two pointers (one starting just after the current element and the other at the end of the array) to find pairs that sum up to the negative of the current element.
4. **Avoiding Duplicates**: Skip duplicate elements for both the first element and the two-pointer search to ensure unique triplets.
5. **Result Storage**: Store each valid triplet in a results list.

### Complexity
- **Time Complexity**: \(O(n^2)\), where \(n\) is the size of the input array. Sorting takes \(O(n \log n)\), and the two-pointer search runs in \(O(n)\) for each element.
- **Space Complexity**: \(O(1)\) additional space, excluding the space required for the output.

### Code
Refer to the `solution.py` file for the implementation.

## Example
**Input**: `nums = [-1, 0, 1, 2, -1, -4]`  
**Output**: `[[-1, -1, 2], [-1, 0, 1]]`

## Notes
- Ensure the input array is sorted before applying the two-pointer technique.
- Handle edge cases such as arrays with fewer than three elements or arrays with no valid triplets.

---