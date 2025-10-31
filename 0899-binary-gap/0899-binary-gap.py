import math
class Solution:
    def binaryGap(self, n: int) -> int:
        
        if math.log(n) % math.log(2) == 0:
            number_of_bit = math.log(n) // math.log(2)
            number_of_bit = int(number_of_bit) +1
        else:
            number_of_bit = math.log(n) // math.log(2)
            number_of_bit = int(number_of_bit) +1
        flag = 1
        max_dist = -1000000
        last_set_pos = -1
        for i in range(number_of_bit):
            if (n & flag):
                #print("ad")
                if last_set_pos!=-1:
                    
                    tmp = abs(i-last_set_pos)
                    if tmp > max_dist:
                        max_dist = tmp
                last_set_pos = i
            flag = flag << 1
            #print(flag)
        if max_dist == -1000000:
            return 0
        else:
            return max_dist




        