class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if sum(subset) == target:
                return res.append(subset.copy())

            if sum(subset) > target:
                return
            
            if i >= len(nums):
                return

            subset.append(nums[i])
            dfs(i)
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res