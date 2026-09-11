class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = [[] for _ in range(len(nums) + 1)]

        for i in nums:
            freq[i] = 1 + freq.get(i,0)

        for i,j in freq.items():
            res[j].append(i)           

        ans = []
        for i in range(len(res)-1, 0, -1):
            for num in res[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans