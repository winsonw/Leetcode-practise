class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.d = dict()
        for i in nums:
            if i in self.d:
                self.d[i] += 1
            else:
                self.d[i] = 1
        o = sorted(set(nums))
        i = 0
        accept = []
        l = len(o)
        
        def check(index):
            if self.d[index] > 0:
                self.d[index] -= 1
                return True
            return False
        
        def uncheck(index):
            self.d[index] += 1
            
        
        while i < l and o[i]<=0:
            check(o[i])
            
            j = l - 1
            mid = (-o[i])/ 2.0
            while j >= 0 and check(o[j]) and o[j] >= mid:
                k = -(o[i] + o[j])
                if k >= o[i] and k in self.d and check(k):
                    accept.append([o[i], o[j], k])
                    uncheck(k)
                uncheck(o[j])
                j -= 1
            if o[j] < mid: uncheck(o[j])
            
            uncheck(o[i])
            i += 1
        return accept
            