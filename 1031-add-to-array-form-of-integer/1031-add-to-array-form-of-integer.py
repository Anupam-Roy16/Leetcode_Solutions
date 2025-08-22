class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans = []
        while k!=0:
            ans.append(k%10)
            k//=10
        ans = ans[::-1]
        final_ans= []
        if len(ans) < len(num):
            size = len(ans)
            j = len(num)-1
            carry = 0
            for i in range(size-1,-1,-1):
                if 10 > (ans[i] + num[j]+carry):
                    final_ans.append(carry+ans[i] +num[j])
                    carry = 0
                else:
                    final_ans.append((ans[i] + num[j]+carry)%10)
                    carry = 1
                j-=1
            if j == -1 and carry==1:
                final_ans.append(carry)
                return final_ans[::-1]
            for i in range(j,-1,-1):
                if 10 > (num[i] + carry):
                    final_ans.append(num[i] +carry)
                    carry = 0
                else:
                    final_ans.append((num[i]+carry)%10)
                    carry = 1
            if carry == 1:
                final_ans.append(1)
            return final_ans[::-1]
        else:
            size = len(num)
            j = len(ans)-1
            carry = 0
            for i in range(size-1,-1,-1):
                if 10 > (ans[j] + num[i]+carry):
                    final_ans.append(ans[j] +num[i]+carry)
                    carry = 0
                else:
                    final_ans.append((ans[j] + num[i]+carry)%10)
                    carry = 1
                j-=1
            print(final_ans)
            print(carry)
            if j == -1 and carry==1:
                final_ans.append(carry)
                print(final_ans)
                return final_ans[::-1]
            for i in range(j,-1,-1):
                if 10 > (ans[i] + carry):
                    final_ans.append(ans[i] +carry)
                    carry = 0
                else:
                    final_ans.append((ans[i]+carry)%10)
                    carry = 1
            if carry == 1:
                final_ans.append(1)
            return final_ans[::-1]





            

