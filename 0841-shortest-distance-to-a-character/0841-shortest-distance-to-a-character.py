class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = [1000000000 for i in range(len(s))]
        index_arr_c = []
        for i in range(len(s)):
            if c == s[i]:
                index_arr_c.append(i)
        for index in index_arr_c:
            tmp1 , tmp2 ,count1,count2= index,index,0,0
            while tmp1!=-1:
                if count1 <= ans[tmp1]:
                    ans[tmp1] = count1
                else:
                    break
                count1 += 1
                tmp1 -= 1
            while tmp2 != len(ans):
                if count2 <= ans[tmp2]:
                    ans[tmp2] = count2
                else:
                    break
                count2 += 1
                tmp2 += 1
        return ans
            




        