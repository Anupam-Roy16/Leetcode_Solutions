class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends = set(friends)
        ans = []
        for x in order:
            if x in friends:
                ans.append(x)
        return ans
        
        