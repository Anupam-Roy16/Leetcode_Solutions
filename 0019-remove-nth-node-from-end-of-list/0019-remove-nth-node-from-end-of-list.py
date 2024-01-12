# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        i = 0
        
        #count total node
        while cur:
            cur = cur.next
            i += 1
            
        #when first node is removed    
        cur = head
        n += 1
        if n>i:
            return head.next
        
        #while beyond first node is removed
        while cur:
            if i == n:
                cur.next = cur.next.next
                break
            cur = cur.next
            i -= 1
        return head