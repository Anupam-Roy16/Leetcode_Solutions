class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        max_count = 0
        for i in range(0,k):
            if (s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
                count += 1
        first_point = 0
        max_count = count
        for i in range(k,len(s)):
            if (s[first_point]=='a' or s[first_point]=='e' or s[first_point]=='i' or s[first_point]=='o' or s[first_point]=='u'):
                count -= 1
            if (s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
                count += 1
            max_count=max(max_count,count)
            first_point += 1
        return max_count
            
        