class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #using linked list cycle concept, as striver video
        slow ,fast= nums[0] , nums[0]
        while 1:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
    