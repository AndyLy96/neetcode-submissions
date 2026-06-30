class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for n in nums:
            table[n] = 1 + table.get(n, 0)
        final = sorted(table, key=table.get, reverse=True)[:k]
        return final

            