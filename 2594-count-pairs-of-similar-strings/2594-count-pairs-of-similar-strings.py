class Solution:
    def similarPairs(self, words: List[str]) -> int:
        for i in range(len(words)):
            s = set()
            for x in words[i]:
                s.add(x)
            s = list(s)
            s.sort()
            words[i] = "".join(s)
        words.sort()
        count = 0
        #print(words)
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if words[i] == words[j]:
                    count+=1
        return count

        