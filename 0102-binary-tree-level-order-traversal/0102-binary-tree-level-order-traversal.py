# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # first traverse all value in queue then update the queue by getting new child
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        queue = []
        queue.append(root)
        final_ans = []
        while queue:
            tmp_queue = queue
            ans = []
            next_queue = []
            while tmp_queue:
                root = tmp_queue.pop(0)
                ans.append(root.val)
                if root.left:
                    next_queue.append(root.left)
                if root.right:
                    next_queue.append(root.right)
            
            final_ans.append(ans)
            queue = next_queue
        return final_ans
            
        
        