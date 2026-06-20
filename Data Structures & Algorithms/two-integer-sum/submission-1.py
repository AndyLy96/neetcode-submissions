class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        value = 0
        for i in range(len(nums)):
            value = target - nums[i]
            list = []            
            if value in map:
                list.append(map[value])
                list.append(i)
                print(list)
                return list
            map[nums[i]] = i
        return list

