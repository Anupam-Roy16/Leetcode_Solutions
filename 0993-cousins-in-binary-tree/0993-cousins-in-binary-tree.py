# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = []
        queue.append(root)
        while queue:
            temp_queue = queue
            temp_list = []
            temp_list1 = []
            flag = 0
            while temp_queue:
                flag1 = 0
                front = temp_queue.pop(0)
                temp_list1.append(front.val)
                if front.left:
                    temp_list.append(front.left)
                    if flag == 0:
                        if front.left.val == x :
                            flag = 1
                            flag1 =1
                        if front.left.val == y:
                            flag = 2
                            flag1 = 1
                    elif flag == 1:
                        if front.left.val == y:
                            return True
                    else:
                        if front.left.val == x:
                            return True
                        
                if front.right:
                    temp_list.append(front.right)
                    if flag1 == 0:
                        if flag == 0:
                            if front.right.val == x: 
                                flag = 1
                            if front.right.val == y:
                                flag = 2
                        elif flag == 1:
                            if front.right.val == y:
                                return 1
                        else:
                            if front.right.val == x:
                                return 1
            queue +=temp_list
            #print(temp_list1)
        
        return False
                
        