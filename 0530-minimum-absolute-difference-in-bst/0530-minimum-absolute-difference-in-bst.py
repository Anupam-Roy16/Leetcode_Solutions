# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    #return inorder_list which is sorted in asceding order
    
    def helper(self,root):
        if root == None:
            return []
        else:
            return self.helper(root.left) + [root.val] + self.helper(root.right)
        
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        inorder_list = self.helper(root)
        
        # founded minimum differece
        min = 10000000000
        for i in range(len(inorder_list)-1):
            if min > (inorder_list[i+1] - inorder_list[i]):
                min = inorder_list[i+1] - inorder_list[i]
        return min
                        