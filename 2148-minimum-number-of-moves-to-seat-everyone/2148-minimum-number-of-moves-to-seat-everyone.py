class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        size = len(students)
        ans = 0
        for i in range(size):
            ans += abs(seats[i]-students[i])
        return ans
        