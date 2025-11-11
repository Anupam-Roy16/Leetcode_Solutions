class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        even , odd = 0, 0
        for x in nums:
            if x%2==0:
                even+=1
            else:
                odd+=1
        if even >=2:
            return True
        else:
            return False


        