class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]!=9:
            digits[-1]+=1
        else:
            k =len(digits)-1
            for i in range(k,-1,-1):
                if digits[i] + 1 == 10:
                    digits[i] =0
                else:
                    digits[i] =digits[i] +1
                    break
        if digits[0] == 0:
            return [1]+digits
        else:
            return digits
