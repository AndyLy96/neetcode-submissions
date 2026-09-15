class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cons = set()

        for n in nums:
            if n in cons:
                return True
            cons.add(n)

        return False