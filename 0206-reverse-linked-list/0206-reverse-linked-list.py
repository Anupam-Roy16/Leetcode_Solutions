# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        node = head
        while node!= None:
            current = node
            node = node.next
            current.next = prev
            prev = current
        return prev
            
        