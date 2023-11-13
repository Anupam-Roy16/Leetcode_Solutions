class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        List = []
        if len(nums) == 0:
            return List
        num = nums[0]
        first = nums[0]
        for i in range( len( nums ) ):
            if nums[i] == num:
                num += 1
                if i == len(nums)-1:
                    if first !=nums[i]:
                        var=str(first) + "->" +str(nums[i])
                    else:
                        var=str(first)
                    List.append(var)
                    
            else:
                if first !=nums[i-1]:
                    var=str(first) + "->" +str(nums[i-1])
                else:
                    var=str(first)
                List.append(var)
                first = nums[i]
                num = nums[i]+1
                if i == len(nums)-1:
                    var=str(first)
                    List.append(var)
        return List
                
            
        