class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ans = 0
        for x in fruits:
            flag = 0
            for i in range(len(baskets)):
                if x <= baskets[i]:
                    baskets[i] = 0
                    flag = 1
                    break
            if flag ==0:
                ans +=1

        return ans
        