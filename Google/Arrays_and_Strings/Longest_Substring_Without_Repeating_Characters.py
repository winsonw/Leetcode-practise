class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ma = 0
        l = 0
        last = ''
        for c in s:
            if c in last:
                if l > ma:
                    ma = l
                last = last.split(c)[1]
                l = len(last)
            last += c
            l += 1
        if l > ma:
            ma = l
        return ma
        