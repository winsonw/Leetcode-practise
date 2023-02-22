class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        self.max_digit = 0
        self.max_s = ''
        
        def expand(left,right):
            if not (left < 0 or right >= l):
                if s[left] == s[right]:
                    if right - left + 1 > self.max_digit:
                        self.max_digit = right - left + 1
                        self.max_s = s[left:right+1]
                    expand(left-1, right+1)
            
        for i in range(l):
            expand(i,i)
            expand(i,i+1)
        return self.max_s