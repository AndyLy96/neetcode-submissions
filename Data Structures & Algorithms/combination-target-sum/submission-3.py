class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, currsum):
            if currsum == target:
                return res.append(subset.copy())

            if currsum > target or i >= len(nums):
                return
            
            subset.append(nums[i])
            dfs(i, currsum + nums[i])
            subset.pop()
            dfs(i+1, currsum)

        dfs(0, 0)
        return res