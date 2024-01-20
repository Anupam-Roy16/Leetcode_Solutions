# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root):
        if root == None:
            return [-1000000]
        elif root.left==None and root.right==None:
            return [root.val]
        else:
            return [root.val] + self.inorder(root.left) + self.inorder(root.right)
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if self.inorder(p) == self.inorder(q):
            print(self.inorder(p),self.inorder(q))
            return 1
        else:
            return 0