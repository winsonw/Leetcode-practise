# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nth = self.dive(head, n)
        print(nth)
        if nth == n:
            if nth == 1:
                head = None
            else:
                head=head.next
        return head
    
    def dive(self, head, n):
        if not head.next:
            return 1
        nth = self.dive(head.next, n) 
        if nth == n:
            head.next = head.next.next
        return nth + 1
        