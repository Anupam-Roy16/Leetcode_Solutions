class Solution:
    #first traverse the array , fix a position where new unique value sit and increase pos 1 when inserted value. maintain a variable val which hold last updated value . return pos
    def removeDuplicates(self, nums: List[int]) -> int:
        pos = 1
        val = nums[0]
        for i in range(1,len(nums)):
            if val != nums[i]:
                nums[pos] = nums[i]
                pos += 1
                val = nums[i]
        return pos
            
            
        