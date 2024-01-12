# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur_node= ListNode()
        ans = cur_node
        while list1 and list2:
            if list1.val<list2.val:
                cur_node.next = list1
                list1,cur_node = list1.next,list1
            else:
                cur_node.next = list2
                list2, cur_node = list2.next,list2
        if list1:
            cur_node.next = list1
        if list2:
            cur_node.next = list2
        return ans.next
            
                
                
        
                
        