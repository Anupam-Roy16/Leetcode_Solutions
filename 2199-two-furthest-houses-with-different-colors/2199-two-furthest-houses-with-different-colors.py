class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans1,ans2 = -1,-1
        size = len(colors)
        for i in range(size-1,0,-1):
            if colors[0] != colors[i]:
                ans1 = i
                break
        for i in range(size-1):
            if colors[size-1] != colors[i]:
                ans2 = size-1-i
                break
        return max(ans1,ans2)