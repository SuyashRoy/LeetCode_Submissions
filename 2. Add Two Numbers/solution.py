from typing import Optional

### Given -----> # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        solution = ListNode()
        temp = ListNode()
        solution = temp
        sol_list = []
        target = 0
        carry = 0
        while l1 is not None or l2 is not None:
            if l1 is not None and l2 is None:
                target = l1.val
                if carry == 1:
                    target+=1
                    carry = 0
                if target >=10:
                    target-=10
                    carry = 1
            elif l1 is None and l2 is not None:
                target = l2.val
                if carry == 1:
                    target+=1
                    carry = 0
                if target >=10:
                    target-=10
                    carry = 1
            elif (l1.val + l2.val) < 10:
                target = l1.val + l2.val
                if carry == 1:
                    target+=1
                    carry = 0
                if target >=10:
                    target-=10
                    carry = 1
            else:
                target = l1.val + l2.val - 10
                if carry == 1:
                    target += 1
                    carry = 0
                carry = 1
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            sol_list.append(target)
            if l1 is None and l2 is None:
                if carry == 1:
                    sol_list.append(1)
        # print(sol_list)

        for i in range(len(sol_list)):
            temp.val = sol_list[i]
            if i != len(sol_list) - 1:
                temp.next = ListNode()
                temp = temp.next
            else:
                break

        # print(solution)
        return solution

### Example usage:
solution = Solution()
result = solution.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))))
result_2 = solution.addTwoNumbers(ListNode(9, ListNode(9, ListNode(9))), ListNode(1))
result_3 = solution.addTwoNumbers(ListNode(0), ListNode(0))
result_4 = solution.addTwoNumbers(ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))), ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))

def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")
    
print_list(result)  # Output: 7 -> 0 -> 8 -> None
print_list(result_2)  # Output: 0 -> 0 -> 0 -> 1 -> None
print_list(result_3)  # Output: 0 -> None
print_list(result_4)  # Output: 8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1 -> None
            
        