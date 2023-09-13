class Solution:
    def jump(self, nums: List[int]) -> int:
        jump,current_furthest,current_end=0,0,0
        for i in range(len(nums)-1):
            current_furthest=max(current_furthest,i+nums[i])
            if i==current_end:
                jump+=1
                current_end=current_furthest
        return jump
        