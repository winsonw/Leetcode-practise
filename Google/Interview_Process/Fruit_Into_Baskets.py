class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        ma = -1
        last_type = -1
        ts = set()
        last_long = 0
        current = 0
        
        for f in fruits:
            if len(ts)<2 or f in ts:
                ts.add(f)
                current += 1
            else:
                if current > ma:
                    ma = current
                current = last_long + 1
                ts = {f, last_type}
                
            if f == last_type:
                last_long += 1
            else:
                last_long = 1
                last_type = f
        
        if current > ma:
            ma = current
                
        return ma