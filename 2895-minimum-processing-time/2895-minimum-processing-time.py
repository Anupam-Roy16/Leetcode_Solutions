class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse = True)
        p = processorTime
        p.sort()
        total_time = 0
        for i in range(len(p)):
            time_need = p[i] + tasks[4*i]
            total_time = max(time_need,total_time)
        return total_time
            
        