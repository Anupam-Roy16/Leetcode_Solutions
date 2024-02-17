class Solution:
    def decodeString(self, s: str) -> str:
        'using one stack problem is solved . lement pushed in stack untill got ]  . when get ] traverse back to stack and pop and string is got multiplied by the prior number and then pushed on stack '
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                temp_string = ""
                while stack[-1] != '[':
                    temp_string += stack.pop(-1)
                stack.pop(-1)
                temp_string = temp_string[::-1]
                num = ""
                while stack and stack[-1]>='0' and stack[-1]<='9':
                    num += stack.pop(-1)
                num = num[::-1]
                num = int(num)
                temp_string = num*temp_string
                stack += temp_string
        res = ""
        res = res.join(stack)
        return res
                