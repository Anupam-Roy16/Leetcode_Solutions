class Solution:
    import math
    def hasAlternatingBits(self, n: int) -> bool:
        nn = 1
        flag = 0
        #n+1
     
        last = math.log(n+1) // math.log(2)
        last = int(last)
        last += 1
   
        print(last)
        flag = 1
        for i in range(last):
            
            if nn & n:
                if i ==0:
                    flag = 1
                    nn = nn<<1
                    continue
                if flag == 0:
                    flag = 1
                else:
                    return False
            else:
                print("0")
                if i == 0:
                    flag = 0
                    nn = nn<<1
                    continue
                if flag ==1:
                    flag = 0
                else:
                    return False
            nn = nn<<1
        return True
