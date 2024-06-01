# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast  = head, head
        if head == None:
            return False
        while 1:
            slow=slow.next
            if fast and fast.next:
                fast = fast.next.next
            else:
                return False
            if slow == fast:
                return True
            
        
        