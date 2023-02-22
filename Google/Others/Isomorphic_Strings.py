class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        l = len(s)
        if l != len(t):
            return False
        
        index1 = 0
        index2 = 0
        d1 = dict()
        d2 = dict()
        
        for i in range(l):
            if not s[i] in d1:
                d1[s[i]] = index1
                index1 += 1
                
            if not t[i] in d2:
                d2[t[i]] = index2
                index2 += 1
                
            if d1[s[i]] != d2[t[i]]:
                return False
            
        return True
            
            