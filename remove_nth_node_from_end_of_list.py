# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self,head,n):
        len = 0
        curr = head
        while curr:
            len += 1
            curr = curr.next

        if len == n:
            return head.next

        curr1 = head
        for _ in range(len-n-1):
            curr1 = curr1.next
        curr1.next = curr1.next.next
        return head
        
