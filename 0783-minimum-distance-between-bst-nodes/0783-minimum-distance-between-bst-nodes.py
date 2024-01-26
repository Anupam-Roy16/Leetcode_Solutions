# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root):
        if root == None:
            return []
        else:
            return self.helper(root.left) + [root.val] + self.helper(root.right)
        
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        current = self.helper(root)
        min = 100000000
        for i in range(len(current)-1):
            if min>current[i+1]-current[i]:
                min = current[i+1]-current[i]
        return min
        
        