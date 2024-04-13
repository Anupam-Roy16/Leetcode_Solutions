# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def changeSign(self, head: ListNode):
        while ( head ):
            head.val *= -1
            head = head.next
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        self.changeSign(headA)
        
        while ( headB ):
            if headB.val < 0:break
            headB = headB.next
        
        self.changeSign(headA)
        return headB
    
    
# Time - O(n+m)
# Space - O(n)

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         first_set=set()
#         curr=headA
        
#         while curr:
#             first_set.add(curr)
#             curr=curr.next
        
#         curr = headB
#         while curr:
#             if curr in first_set:
#                 return curr
#             curr=curr.next

#         return None