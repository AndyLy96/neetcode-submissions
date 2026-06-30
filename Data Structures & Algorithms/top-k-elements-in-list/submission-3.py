class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            table[num]= 1+ table.get(num,0)
        for num, cnt in table.items():
            freq[cnt].append(num)
        print(freq)
        res = []
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

            