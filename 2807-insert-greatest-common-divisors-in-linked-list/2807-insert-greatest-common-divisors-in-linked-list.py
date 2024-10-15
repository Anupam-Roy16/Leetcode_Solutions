# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head.next
        while curr != None:
            temp_val = math.gcd(prev.val,curr.val)
            new_node = ListNode(temp_val)
            prev.next = new_node
            new_node.next = curr
            prev =curr
            curr = curr.next
        return head
            
            
        
        