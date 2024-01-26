# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #run bfs on tree and simultaneously save the val in list and check needy vallue is in list or not 
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        queue = []
        current = []
        queue.append(root)
        while queue:
            front = queue.pop(0)
            if (k - front.val) in current:
                return 1
            current.append(front.val)
            if front.left:
                queue.append(front.left)
            if front.right:
                queue.append(front.right)
        return False
        
            
        