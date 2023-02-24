class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0 or newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        l = len(intervals)
        i = 0
        
        while i < l and intervals[i][1] < newInterval[0]:
            i += 1
            
        if i == l:
            return intervals + [newInterval]
        
        left_index = i
        left = intervals[i][0] if intervals[i][0] < newInterval[0] else newInterval[0]
        
        while i < l and intervals[i][0] <= newInterval[1]:
            i += 1
        
        print(i)
        right = newInterval[1] if intervals[i-1][1] < newInterval[1] else intervals[i-1][1]
        
        
            
        return intervals[:left_index] + [[left, right]] + intervals[i:]