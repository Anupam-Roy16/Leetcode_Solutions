class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack  = []
        j=0
        result = ""
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(s[i])
            else:
                stack.pop()
                if len(stack)==0:
                    result += s[j+1:i]
                    j = i+1
        return result
                    
                    
        