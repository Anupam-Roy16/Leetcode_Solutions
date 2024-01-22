# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,left,right):
        if left==None or right==None:
            return left==right
        elif left.val != right.val:
            return False
        else:
            return self.helper(left.left,right.right) and self.helper(left.right,right.left)
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root.left,root.right)
        
        