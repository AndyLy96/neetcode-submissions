class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) -1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > nums[left] and nums[left] > nums[right]:
                left = middle
            elif nums[middle] < nums[right] and nums[left]> nums[right]:
                right = middle
            else:
                if nums[left] < nums[right]:
                    return nums[left]
                return nums[right]

        return -1