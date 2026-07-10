class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        maxWater = (r-l) * min(heights[l],heights[r])

        while l < r:
            temp = (r-l) * min(heights[l],heights[r])
            maxWater = max(maxWater, temp)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxWater


