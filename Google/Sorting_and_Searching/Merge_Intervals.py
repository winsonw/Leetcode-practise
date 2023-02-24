class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l = len(intervals)
        new_intervals = []
        i = 0
        
        while i < l:
            left = intervals[i][0]
            right = intervals[i][1]
            i += 1
            while i < l and (left <= intervals[i][0] <= right or left <= intervals[i][1] <= right):
                if intervals[i][0] < left:
                    left = intervals[i][0]
                if intervals[i][1] > right:
                    right = intervals[i][1]
                i += 1
            new_intervals.append([left, right])
            
        return new_intervals
            