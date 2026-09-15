class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(filter(str.isalnum, s))

        return cleaned.lower() == cleaned[::-1].lower()