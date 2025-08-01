
---
# LeetCode Problem 876: Middle of the Linked List

## Problem Description
The problem requires finding the middle node of a given singly linked list. If the list has an even number of nodes, the second middle node should be returned.

## Approach: (Function finds the middle node of a given singly linked list using the two-pointer technique)
1. Utilize two pointers, `middleNode` (slow pointer) and `endNode` (fast pointer), to traverse the linked list
2. The `middleNode` pointer moves one step at a time, while the `endNode` pointer moves two steps at a time
3. By the time the `endNode` pointer reaches the end of the list (or becomes `None`), the `middleNode` pointer will be at the middle of the list
4. If the list has an even number of nodes, the second middle node is returned as per the problem's requirements

This approach ensures an efficient solution with a time complexity of **O(n)** and a space complexity of **O(1)**, as no additional data structures are used.

## Complexity Analysis
- **Time Complexity**: O(n), where `n` is the number of nodes in the linked list.
- **Space Complexity**: O(1), as the solution uses constant space.

This method is optimal and leverages the properties of linked lists effectively

---
