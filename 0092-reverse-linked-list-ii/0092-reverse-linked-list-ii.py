# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right:
            return head
        from_left_to_right =[]
        i = 1
        fake_head = head
        
        #This loop cut the data from left to right and paste in a list
        while fake_head:
            if i>=left and i<=right:
                from_left_to_right.append(fake_head.val)
            fake_head = fake_head.next
            i += 1
            
            
        from_left_to_right.reverse()
        fake_head = head
        i=1
        cur = ListNode()
        ans = cur
        flag = 0
        j=0
        
        
        #This loop travese the original linked list and crete a new linked list
        while fake_head:
            if i>=left and i<=right:
                if flag == 0:
                    cur.val = from_left_to_right[j]
                else:
                    cur.next = ListNode()
                    cur = cur.next
                    cur.val = from_left_to_right[j]
                j+=1   
            else:
                if flag == 0:
                    cur.val = fake_head.val
                else:
                    cur.next = ListNode()
                    cur = cur.next
                    cur.val = fake_head.val
            
            fake_head = fake_head.next
            i += 1
            flag += 1 
            
            
        return ans
            