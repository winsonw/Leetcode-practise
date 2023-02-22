class Solution(object):
    def licenseKeyFormatting(self, s, k):
        s = s.replace('-', '')
        
        l = len(s)
        t = l // k
        remain = l % k
        if remain == 0:
            remain = k
            t -= 1
            
        words = [s[0:remain]] + [s[(remain+i*k):(remain+(i+1)*k)] for i in range(t)]
        
        return '-'.join(words).upper()
        