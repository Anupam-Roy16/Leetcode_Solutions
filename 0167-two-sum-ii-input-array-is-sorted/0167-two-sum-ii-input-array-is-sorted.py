class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first_pointer = 0
        last_pointer = len(numbers) -1
        while first_pointer < last_pointer:
            sum = numbers[first_pointer] + numbers[last_pointer]
            if sum == target:
                return [first_pointer+1, last_pointer+1]
            elif sum>target:
                last_pointer -= 1
            else:
                first_pointer += 1
                