class Solution:
    def isValid(self, s: str) -> bool:
        ll = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                ll.append(s[i])
            else:
                if len(ll) == 0:
                    print("1")
                    return False
                else:
                    if (s[i]==')' and ll[-1]=='(') or (s[i]=='}' and ll[-1]=='{') or (s[i]==']' and ll[-1]=='['):
                        ll.pop()
                    else:
                        print("2")
                        return False
                        print("2")
        if len(ll) == 0:
            return True
        else:
            print("3")
            return False

            
        