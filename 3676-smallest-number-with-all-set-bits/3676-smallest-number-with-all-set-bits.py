class Solution:
    def smallestNumber(self, n: int) -> int:
        i = 1
        while 1:
            if n <= (1<<i)-1:
                return (1<<i)-1
            i+=1


        