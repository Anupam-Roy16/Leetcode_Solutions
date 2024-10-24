class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        ans = set()
        for x in nums1:
            dic[x] = 1
        for y in nums2:
            if y in dic:
                ans.add(y)
        return list(ans)
        