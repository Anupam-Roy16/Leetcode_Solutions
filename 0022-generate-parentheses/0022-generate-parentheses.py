class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(close_count,start_count,s):
            if close_count == n == start_count:
                res.append(s)
                return 
            
            if start_count < n:
                dfs(close_count,start_count+1 , s+"(")
                
            if close_count < start_count:
                dfs(close_count+1, start_count,s+")")
        dfs(0,0,"")
        return res
                
        
        