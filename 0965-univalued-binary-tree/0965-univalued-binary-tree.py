# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # preorder traverse and check the equality
    
    def helper(self,root,k):
        if root == None:
            return 1
        else:
            return root.val == k and self.helper(root.left,k) and self.helper(root.right,k)
    
    
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root,root.val)
            
        