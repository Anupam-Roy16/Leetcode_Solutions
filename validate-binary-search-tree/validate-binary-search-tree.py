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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder_list = self.helper(root)
        for i in range(1,len(inorder_list)):
            if inorder_list[i] <= inorder_list[i-1]:
                return False
        return True