# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = []
        queue.append(root)
        ans = root.val
        while queue:
            temp_queue = queue
            temp_list = []
            while temp_queue:
                front = temp_queue.pop(0)
                if front.left:
                    temp_list.append(front.left)
                if front.right:
                    temp_list.append(front.right)
            if len(temp_list) != 0:
                ans = temp_list[0].val
            queue += temp_list
        return ans
            
        