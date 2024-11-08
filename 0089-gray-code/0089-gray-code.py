class Solution:
    def grey_str_generate(self,n):
        if n == 1:
            return ["0","1"]
        else:
            temp = self.grey_str_generate(n-1)
            ans = []
            for x in temp:
                ans.append("0"+x)
            for i in range(len(temp)-1,-1,-1):
                ans.append("1"+temp[i])
            return ans
        
        
    def dec_generator(self,temp):
        ans = []
        for x in temp:
            d = len(x)-1
            temp_ans =0
            #print(x)
            for i in range(len(x)):
                temp_ans += (int(x[i])*(1<<d))
                d -=1
            #print(temp_ans)
            ans.append(temp_ans)
        return ans
            
        
    def grayCode(self, n: int) -> List[int]:
        temp = self.grey_str_generate(n)
        return self.dec_generator(temp)
        
        