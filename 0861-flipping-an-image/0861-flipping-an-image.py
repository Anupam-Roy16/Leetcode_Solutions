class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        ans = []
        for row in image:
            row = row[::-1]
            tmp_row = []
            for x in row:
                if x == 0:
                    tmp_row.append(1)
                else:
                    tmp_row.append(0)
            ans.append(tmp_row)
        return ans