class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        clopen = {")" : "(", "]" : "[", "}" : "{"}

        for c in s:
            if c in clopen:
                if stack and stack[-1] == clopen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False