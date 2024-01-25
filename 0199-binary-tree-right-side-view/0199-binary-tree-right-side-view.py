# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #frist traverse all value in queue and save the last value and then update the queue by the child form traversing all value. thus repeate
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        queue.append(root)
        res = []
        if root == None:
            return root
        while queue:
            temp_queue = queue
            temp_list = []
            while temp_queue:
                front = temp_queue.pop(0)
                ans = front.val
                if front.left:
                    temp_list.append(front.left)
                if front.right:
                    temp_list.append(front.right)
            res.append(ans)
            queue += temp_list
        return res