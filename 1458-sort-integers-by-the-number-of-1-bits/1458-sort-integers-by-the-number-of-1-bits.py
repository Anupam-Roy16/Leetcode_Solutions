class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        ans = []
        tmp = {}
        for x in arr:
            count = 0
            n = x
            while n:
                if (n&1):
                    count+=1
                n = n>>1
            if count in tmp:
                tmp[count].append(x)
            else:
                tmp[count] = [x]
        for i in range(15):
            if i in tmp:
                tmp[i].sort()
                ans+=tmp[i]
        return ans


        