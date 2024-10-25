# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dic = {}
        curr_node = head
        while curr_node != None:
            if curr_node in dic:
                return curr_node
            else:
                dic[curr_node] = 1
            curr_node = curr_node.next
        return None