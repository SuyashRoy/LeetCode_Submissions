from typing import Optional

### Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middleNode = head
        endNode = head
        while(endNode is not None and endNode.next is not None):
            middleNode = middleNode.next
            endNode = endNode.next.next
        return middleNode

### Example usage:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solution = Solution()
middle = solution.middleNode(head)
print(middle.val)  ### Output: 3

### Example with even number of nodes
head_even = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
solution_even = Solution()
middle_even = solution_even.middleNode(head_even)
print(middle_even.val)  ### Output: 4