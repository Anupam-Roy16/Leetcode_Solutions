class Solution:
    def minimumMoves(self, s: str) -> int:
        size = len(s)
        count_move,i = 0 ,0
        while i<size:
            flag = 0
            for j in range(i,size):
                if s[j] == 'X':
                    flag = 1
                    count_move +=1
                    i = j+3
                    break
            if flag == 0:
                break
        return count_move


        