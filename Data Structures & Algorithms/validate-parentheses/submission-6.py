class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {"(":")", "{":"}", "[":"]"}
        close = [")","}","]"]

        if len(s) % 2 != 0:
            return False

        for c in s:
            if c not in close:
                stack.append(c)
                continue

            if len(stack)==0:
                return False
            
            if hmap[stack[-1]] == c:
                stack.pop()
            else:
                return False
        
        return len(stack)==0
                

        

