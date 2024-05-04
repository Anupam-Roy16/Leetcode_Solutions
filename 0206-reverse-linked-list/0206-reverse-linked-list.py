# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # this is recursive same process as iterative. aware of return 
    def rec(self,node,prev):
        if node == None:
            return prev
        curr = node
        node = node.next
        curr.next = prev
        prev = curr
        return self.rec(node,prev)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None
        return self.rec(node,prev)
        