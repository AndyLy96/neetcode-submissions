class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        self = set()
        for i in range(len(nums)):
            if nums[i] in self:
                return True
            self.add(nums[i])
        return False