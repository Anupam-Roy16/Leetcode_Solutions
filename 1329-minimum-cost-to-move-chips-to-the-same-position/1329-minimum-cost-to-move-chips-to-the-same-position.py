class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        number_of_chip = len(position)
        min_count = 100000000000000000000
        for i in range(number_of_chip):
            count_step = 0
            for j in range(number_of_chip):
                if (abs(position[i] -position[j]) %2!=0):
                    count_step +=1
            if min_count > count_step:
                min_count = count_step
        return min_count

        