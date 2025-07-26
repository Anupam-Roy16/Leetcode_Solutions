class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        sum_of_energy = sum(energy)
        ans = 0
        if sum_of_energy +1 > initialEnergy:
            ans += (sum_of_energy - initialEnergy+1) 
        current_experiance = initialExperience 
        print(ans)
        for x in experience:
            if x +1> current_experiance:
                tmp =( x+1- current_experiance)
                current_experiance +=tmp
                ans+=(tmp)
            current_experiance += x
        return ans
        