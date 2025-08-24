class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastindex_dict = {}
        for i in range(len(s)):
            lastindex_dict[s[i]] = i
        
        seen = set()
        stack = []
        for i in range(len(s)):
            if s[i] in seen:
                continue
            while len(stack)!=0 and stack[-1] > s[i] and lastindex_dict[stack[-1]] > i:
                seen.remove(stack[-1]) 
                stack.pop(len(stack)-1)
            stack.append(s[i])
            seen.add(s[i])
        return "".join(stack)

        