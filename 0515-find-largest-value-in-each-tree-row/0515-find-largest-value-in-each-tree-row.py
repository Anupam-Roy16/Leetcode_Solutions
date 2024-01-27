# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        queue = []
        queue.append(root)
        ans = [root.val]
        
        while queue:
            temp_queue = queue
            temp_list = []
            maxx = -10000000000000
            while temp_queue:
                front = temp_queue.pop(0)
                if front.left:
                    temp_list.append(front.left)
                    if front.left.val>maxx:
                        maxx = front.left.val
                if front.right:
                    temp_list.append(front.right)
                    if front.right.val>maxx:
                        maxx=front.right.val
           
            if len(temp_list) != 0:
                ans.append(maxx)
            queue += temp_list
        return ans
        