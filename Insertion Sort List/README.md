# Insertion Sort List

---
## Problem Description
The problem involves sorting a singly linked list using the **insertion sort** algorithm. The goal is to rearrange the nodes of the linked list such that they are in ascending order.

## Approach

The solution implements the insertion sort algorithm for a linked list. Here's a step-by-step breakdown of the approach:

1. **Initialization**:
    - Create a dummy node to act as the new head of the sorted portion of the list.
    - Use a pointer `current` to traverse the original list.

2. **Iterate Through the List**:
    - For each node in the original list, find the correct position in the sorted portion by comparing values.
    - Insert the node into the sorted portion by adjusting pointers.

3. **Insertion Logic**:
    - Use a pointer `prev` to traverse the sorted portion and find the correct position for the current node.
    - Insert the node by updating the `next` pointers of `prev` and the current node.

4. **Edge Cases**:
    - Handle cases where the list is empty or contains only one node.

5. **Time Complexity**:
    - The algorithm has a time complexity of \(O(n^2)\) in the worst case, where \(n\) is the number of nodes in the list.

## Example

Input:
```
4 -> 2 -> 1 -> 3
```

Output:
```
1 -> 2 -> 3 -> 4
```

---