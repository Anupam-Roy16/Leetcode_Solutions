class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        length = len( points )
        if length == 1:
            return 1
        final_max = -1
        for i in range(length):
            freq = {}
            max = -1
            for j in range(length):
                if i==j:
                    continue
                if (points[j][0]-points[i][0])==0:
                    temp = 100000
                else:
                    temp = (points[j][1]-points[i][1])/(points[j][0]-points[i][0])
                if temp in freq:
                    freq[temp] += 1
                else:
                    freq[temp] = 1
                    
                if max<freq[temp]:
                    max = freq[temp]
            if max>final_max:
                final_max = max
        return final_max+1
        