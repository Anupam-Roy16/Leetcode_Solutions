# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        curr = head
        prev = None
        i = 0
        while curr!=None and curr.next!=None:
            temp1 = curr
            temp2 = curr.next
            temp3 = curr.next.next
            temp2.next = temp1
            temp1.next = temp3
            
            if  i == 0:
                res = temp2
            else:
                prev.next = temp2
            
            curr = temp3
            prev = temp1
            
            i+=1
        return res
            
        