class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1*stones[i]
            
        heapq.heapify(stones)
        while len(stones) > 1:
            
            temp1 = heapq.heappop(stones)
            temp2 = heapq.heappop(stones)
            if temp1 != temp2:
                heapq.heappush(stones,-1*abs(temp1 - temp2))
        if stones:
            return -1*stones[0]
        else:
            return 0