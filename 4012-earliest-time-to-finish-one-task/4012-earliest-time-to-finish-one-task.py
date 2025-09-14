class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        minn_time = 10000000000000
        for time in tasks:
            time = time[0] + time[1]
            if minn_time > (time):
                minn_time = time
        return minn_time
        