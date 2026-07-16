class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s):
            return 0

        l, maxlength = 0, 0
        chars = set()

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            
            chars.add(s[r])
            curr = r - l + 1
            maxlength = max(maxlength, curr)
        
        return maxlength
