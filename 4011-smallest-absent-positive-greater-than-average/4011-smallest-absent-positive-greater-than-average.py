class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        average = sum(nums)//len(nums)
        if average < 0:
            check_number = 1
        else:
            check_number = average + 1
        nums = set(nums)
        while True:
            if check_number not in nums:
                return check_number
                break
            check_number+=1


        