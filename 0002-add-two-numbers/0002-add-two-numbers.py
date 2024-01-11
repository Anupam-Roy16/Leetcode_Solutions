# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_list = ListNode()
        ans = result_list
        extra_val = 0
        flag = 0
        while l1 or l2:
            if l1 and l2:
                digit_sum = l1.val + l2.val
            elif l1!=None and l2==None:
                digit_sum = l1.val
            elif l1==None and l2!=None:
                digit_sum = l2.val
            
            if (digit_sum + extra_val) <10:
                if flag == 0:  
                    result_list.val = digit_sum + extra_val
                    extra_val = 0
                else:
                    result_list.next = ListNode()
                    result_list.next.val = digit_sum + extra_val
                    extra_val = 0
                    result_list = result_list.next
            else:
                if flag==0:
                    result_list.val = (digit_sum + extra_val)%10
                    extra_val = 1
                else:
                    result_list.next = ListNode()
                    result_list.next.val = (digit_sum + extra_val)%10
                    extra_val = 1
                    result_list = result_list.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
            flag += 1
        if extra_val:
            result_list.next = ListNode()
            result_list.next.val = 1
            
        return ans
                
            
        