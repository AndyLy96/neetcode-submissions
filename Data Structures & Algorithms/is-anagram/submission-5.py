class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        coutS, coutT = {}, {}

        for i in range(len(s)):
            coutS[s[i]] = 1 + coutS.get(s[i], 0)
            coutT[t[i]] = 1 + coutT.get(t[i], 0)
        return coutS == coutT

