from typing import Optional

### Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(val = -5000, next = head)
        last_sorted = head
        current = head.next
        
        if head is None or head.next is None:
            return head
    
        while current is not None:
            if current.val >= last_sorted.val:
                last_sorted = last_sorted.next
            else:
                prev = dummy_head
                while prev.next.val <= current.val:
                    prev = prev.next
                last_sorted.next = current.next
                current.next = prev.next
                prev.next = current
            
            current = last_sorted.next
                
        return dummy_head.next

### Example usage:
if __name__ == "__main__":
    # Create a linked list for testing: 4 -> 2 -> 1 -> 3
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    
    # Sort the linked list
    solution = Solution()
    sorted_head = solution.insertionSortList(head)
    
    # Print the sorted linked list
    current = sorted_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
# Output: 1 -> 2 -> 3 -> 4 -> None
        