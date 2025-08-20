class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        arr = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ss =set()
        for s in words:
            tmp_str = ""
            for x in s:
                tmp_str += arr[ord(x)-ord('a')]
            ss.add(tmp_str)
        return len(ss)