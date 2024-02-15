class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() #sort according to first number in sublist .if first number is equal ,sort by second number in sublist
        start = intervals[0][0]
        end = intervals[0][1]
        res_list = []
        for j in range(1 , len(intervals)):
            if intervals[j][0] <= end:
                end = max(intervals[j][1] , end)
            else:
                temp_list = [start,end]
                res_list.append(temp_list)
                start = intervals[j][0]
                end = intervals[j][1]
                
        res_list.append([start , end])
        return res_list
            
                
        