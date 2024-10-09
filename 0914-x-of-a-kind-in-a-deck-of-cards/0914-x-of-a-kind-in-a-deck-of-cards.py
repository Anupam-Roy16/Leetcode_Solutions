import math
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        dictionary = {}
        size = len(deck)
        count_num_type = 0
        min1 = 1000000
        for x in deck:
            if x in dictionary:
                dictionary[x] += 1
            else:
                dictionary[x] = 1
                count_num_type += 1
        count = 0
        for x in dictionary.values():
            if count == 0:
                e = math.gcd(x,x)
            else:
                e = math.gcd(e,x)
            count += 1
            
        if e>1:
            return True
        else:
            return False
        

                