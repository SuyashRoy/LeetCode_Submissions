# LeetCode Problem 2: Add Two Numbers

---
## Problem Description
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Example
### Input:
```
l1 = [2,4,3]
l2 = [5,6,4]
```

### Output:
```
[7,0,8]
```

### Explanation:
342 + 465 = 807.

## Approach
The solution involves the following steps:

1. **Initialization**: Use a dummy node to simplify the process of building the resulting linked list. Maintain a carry variable to handle sums greater than 9.

2. **Iterate Through Lists**: Traverse both linked lists simultaneously, adding corresponding digits along with the carry from the previous step.

3. **Handle Carry**: If the sum of two digits exceeds 9, compute the carry for the next iteration.

4. **Finalize the List**: After traversing both lists, if there is a remaining carry, append it as a new node.

5. **Return Result**: Return the linked list starting from the node next to the dummy node.

## Complexity Analysis
- **Time Complexity**: O(max(m, n)), where `m` and `n` are the lengths of the two linked lists. Each node is processed once.
- **Space Complexity**: O(max(m, n)), as the resulting linked list will have at most `max(m, n) + 1` nodes.

## Notes
- Ensure proper handling of edge cases, such as when one list is longer than the other or when both lists are empty.
- The solution avoids modifying the input lists and constructs a new linked list for the result.

## References
- [LeetCode Problem 2](https://leetcode.com/problems/add-two-numbers/)
- `solution.py` in this folder contains the implementation details.