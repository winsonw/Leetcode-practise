class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        current = ['',s[0]]
        l = len(s)
        i = 1
        j = -1
        
        ma = 1
        while i < l:
            while i < l and s[i] in current:
                if s[i] == current[0]:
                    current[0], current[1] = current[1], current[0]
                i += 1
            length = i - j - 1
            if length > ma:
                ma = length
            j = i -1
            while j >= 0 and s[j] == current[1]:
                j -= 1
            if i < l:
                current[0], current[1] = current[1], s[i]
        return ma
                