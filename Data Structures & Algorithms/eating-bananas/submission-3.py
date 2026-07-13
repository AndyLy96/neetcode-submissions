class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r

        while l < r:
            k = (l+r)//2
            time = h
            for p in piles:
                if time < 0:
                    break
                else:
                    timeeat = math.ceil(p/k)
                    time -= timeeat
            if time < 0:
                l = k + 1
            else:
                r = k
        return l
