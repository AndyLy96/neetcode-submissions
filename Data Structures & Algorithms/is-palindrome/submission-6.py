class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = "".join([char for char in s if char.isalnum()]).lower()
        
        tableS, tableT = [0] * len(result), [0] * len(result)

        for i, c in enumerate(result):
            if c.isalnum():
                tableS[i] = c
                tableT[i] = c
                
        print(tableS)
        print(tableT[::-1])

        return tableS == tableT[::-1]