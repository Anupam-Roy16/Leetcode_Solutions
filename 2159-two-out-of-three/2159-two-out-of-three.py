class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ans = set()
        for x in nums1:
            if x in nums2 or x in nums3:
                ans.add(x)
        
        for x in nums2:
            if x in nums1 or x in nums3:
                ans.add(x)
        return list(ans)
        

        