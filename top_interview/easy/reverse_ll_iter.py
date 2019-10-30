# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        #Base case when head is NULL
        if not head:
            return head
        
        #General case
        prev = head
        curr  = head.next
        head.next = None
        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        
        return prev
