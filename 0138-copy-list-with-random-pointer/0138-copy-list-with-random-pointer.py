"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        flag = 0
        real_head = head
        real_head2=head
        if head==None:
            return head
        
        #this loop creates a list without random connection
        while head:
            if flag==0:
                new_node=Node(head.val)
                ans_node = new_node
            else:
                new_node.next = Node(head.val)
                new_node = new_node.next
            head = head.next
            flag +=1
            
            
        
        #this loop saves random connection index in a dictionary
        temp_dict = dict()
        i=0
        while real_head:
            real_head1 = real_head2
            j = 0
            flag = 0
            while real_head1:
                if real_head.random == real_head1:
                    temp_dict[i] = j
                    flag = 1
                    break
                real_head1 = real_head1.next
                j+=1
            if flag==0:
                temp_dict[i]=-1
            real_head = real_head.next
            i+=1
         
        
        
        #This loops creates random connection according to dictionary
        temp = ans_node
        i=0
        while temp:
            j = temp_dict[i]
            k = 0
            temp1 = ans_node
            while temp1:
                if k == j:
                    temp.random = temp1
                  
                    break
                k+=1
                temp1 = temp1.next
            temp = temp.next
            i += 1
            
        return ans_node