class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                temp_string = ""
                j = len(stack)-1
                #print(stack,j)
                while stack[-1] != '[':
                    temp_string += stack.pop(-1)
                    #print(s[j],"sfdfd")
                    #j -= 1
                    #print(j,stack[1])
                    
                stack.pop(-1)
                j -= 1
                print(temp_string)
                temp_string = temp_string[::-1]
                num = ""
                while stack and stack[-1]>='0' and stack[-1]<='9':
                    num += stack.pop(-1)
                num = num[::-1]
                num = int(num)
                temp_string = num*temp_string
                #print(temp_string)
                stack += temp_string
               # print(stack)
        res = ""
        res = res.join(stack)
        return res
                