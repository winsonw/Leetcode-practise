class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        hash_table = [0] * 10001
        for left, right in intervals:
            while left < right:
                hash_table[left] = 1
                left += 1
            if hash_table[right] == 0:
                hash_table[right] = 2
                
                
        
        index = 0
        new_intervals = []
        while index < 10001:
            left = index
            while hash_table[index] == 1:
                index += 1
            
            if hash_table[index] == 2:
                index += 1
            if index != left:
                new_intervals.append([left, index-1])
            else:
                index += 1
        
        print(hash_table)
        
        return new_intervals
            