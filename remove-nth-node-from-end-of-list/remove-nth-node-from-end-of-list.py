# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total_node = 0
        head1,temp = head,head
        while temp!=None:
            total_node += 1
            temp = temp.next
        pos = total_node-n
        flag = 1
        if pos == 0:
            return head.next
        while flag < pos:
            head = head.next
            flag += 1
        print(head.val)
        head.next = head.next.next
        return head1
        
        