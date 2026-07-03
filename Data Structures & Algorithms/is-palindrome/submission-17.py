class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        w = s.lower()
        while l < r:
            if not w[l].isalnum():
                l += 1
                continue
            if not w[r].isalnum():
                r -= 1
                continue

            if w[l] == w[r]:
                l += 1
                r -= 1
            else:
                return False

        return True
