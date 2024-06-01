# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        before  = None
        after = head
        if head == None:
            return head
        while after.next!=None:
            temp = after.next
            after.next = before
            before = after
            after = temp
        after.next = before
        return after
            
        
            