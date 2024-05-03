class Solution:
    #first duplicate number and its index saved in hash then iterate over list and if duplicate number index difference is less or equal then k then true otherwise False  
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_table = {}
        for i in range(len(nums)):
            if nums[i] in hash_table:
                if i - hash_table[nums[i]]<=k:
                    return True
                else:
                    hash_table[nums[i]] = i
            else:
                hash_table[nums[i]] = i
        return False
            