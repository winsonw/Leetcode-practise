class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = []
        s_t = set([i for i in t])
        d_t = {c_t:i for i,c_t in enumerate(s_t)}
        count = [0] * len(s_t)
        for c in t:
            count[d_t[c]] += 1
        # print(d_t, count)
        # print('-------------------------')
            
        left = 0
        right = 0
        min_l = 0
        min_r = 0
        min_len = 999999
        for c in s:
            right += 1
            if c in d_t: count[d_t[c]] -= 1
            # print(c)
            while max(count)<= 0 and left < right:
                # print(count)
                if (right - left) < min_len:
                    min_l = left
                    min_r = right
                    min_len = right - left
                if s[left] in d_t: count[d_t[s[left]]] += 1
                left += 1
        return s[min_l:min_r]