class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        size = len(points)
        max_area = 0
        for i in range(size-2):
            for j in range(i+1,size-1):
                for k in range(j+1,size):
                    x1 , y1 = points[i]
                    x2 , y2 = points[j]
                    x3 , y3 = points[k]
                    area = abs((x1*(y2-y3)) - (x2*(y1-y3)) + (x3*(y1-y2)))/2
                    if area > max_area:
                               max_area = area
        return max_area