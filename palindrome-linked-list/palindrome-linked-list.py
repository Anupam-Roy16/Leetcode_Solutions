# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        count = 0
        slow, fast ,prev= head,head,None
        while head:
            head = head.next
            count += 1
        print(count)
        while fast and fast.next and slow:
            temp = slow
            slow,fast  = slow.next, fast.next.next
            temp.next = prev
            prev = temp
        #print(slow.val,fast.val,prev.val)
        
      
        if count %2 !=0:
            slow = slow.next
            while prev:
                if prev.val != slow.val:
                    return False
                prev = prev.next
                slow = slow.next
            return True
        else:
            while prev:
                if prev.val != slow.val:
                    return False
                prev = prev.next
                slow = slow.next
            
            return True
            
        
        