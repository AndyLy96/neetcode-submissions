class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        print(intervals)
        remove = 0
        prev_end = intervals[0][1]

        for start,end in intervals[1::]:
            if start >= prev_end:
                prev_end = end
                continue
            else:
                remove += 1
                if end < prev_end:
                    prev_end = end  
        
        return remove 