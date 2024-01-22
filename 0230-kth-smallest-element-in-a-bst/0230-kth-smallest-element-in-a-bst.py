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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder_list = self.helper(root)
        return inorder_list[k-1]
        