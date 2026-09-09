class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        lists, listt = {}, {}

        for i in range(len(s)):
            lists[s[i]] = 1 + lists.get(s[i],0)
            listt[t[i]] = 1 + listt.get(t[i],0)

        return lists == listt

        

