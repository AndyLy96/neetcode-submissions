class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            table[n] = 1 + table.get(n, 0)
        for n, count in table.items():
            freq[count].append(n)

        res = []
        for n in range(len(freq) -1, 0, -1):
            for num in freq[n]:
                res.append(num)

            if len(res) == k:
                return res

