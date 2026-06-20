class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for i in s:
            if i.isalnum():
                string += i
        if string.lower() == string[::-1].lower():
            return True
        return False
        