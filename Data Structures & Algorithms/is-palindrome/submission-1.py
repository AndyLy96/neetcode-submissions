class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(char for char in s if char.isalnum()).lower()
        cleannew = clean
        if len(cleannew) % 2 != 0:
            middle = len(clean) // 2
            cleannew = cleannew[:middle] + cleannew[middle+1:]

        print(cleannew)
        firsthalf = cleannew[0:int(len(cleannew)/2)]
        secondhalf = cleannew[(int((len(cleannew))/2)):len(cleannew)]

        firsthalfSorted = "".join(sorted(firsthalf))
        secondhalfSorted = "".join(sorted(secondhalf))
        
        if firsthalfSorted == secondhalfSorted:
            return True
        return False