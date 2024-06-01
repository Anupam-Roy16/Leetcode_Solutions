# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# prothome jeta choto seta ans liste add korbo. ai nodta save kore rakhbo. list1 and list2 taraverse korbo . jeta choto seta answere add korbo. ans list and jeta add korlam sei list samne shift korbo. kono akta list none hle loop break habe and oprta ans list a add hbe. 
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None or list2 == None:
            if list1 == None:
                return list2
            else:
                return list1
        if list1.val <= list2.val:
            ans = list1
            list1 = list1.next
        else:
            ans = list2
            list2 = list2.next
        head = ans
        while list1!=None and list2!= None:
            if list1.val <= list2.val:
                ans.next = list1
                list1 = list1.next
                ans = ans.next
            else:
                ans.next = list2
                list2  = list2.next
                ans = ans.next
        if list1 == None:
            ans.next = list2
        else:
            ans.next = list1
        return head
                
        