# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        next_digit = 0
        result = ListNode(next_digit)
        current = None
        while l1 or l2:
            if current:
                current.next = ListNode(next_digit)
                current = current.next
            else:
                current = result
                
            if l1:
                current.val += l1.val
                l1 = l1.next
            if l2:
                current.val += l2.val
                l2 = l2.next
            next_digit, current.val = current.val // 10, current.val %10
        if next_digit != 0:
            current.next = ListNode(1)
        return result
                