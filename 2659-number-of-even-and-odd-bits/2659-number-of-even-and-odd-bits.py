class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        i = 0
        even , odd = 0,0
        while n:
            if n&1 :
                if i%2==0:
                    even+=1
                else:
                    odd +=1
            n = n>>1
            i+=1
        return [even,odd]
        