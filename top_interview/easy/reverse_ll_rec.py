
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        '''
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
        '''
        
        start, _= self.reverseListRec(head)
        return start
 
    def reverseListRec(self, head): 
        if not head or not head.next:
            return head, head
        
        start, end = self.reverseListRec(head.next)
        
        head.next = None
        
        end.next = head
        end = head
        
        return start, end
