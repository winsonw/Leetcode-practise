class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x<0 else 1
        x_s = str(abs(x))
        r = [x_s[len(x_s)- i- 1] for i in range(len(x_s))]
        out = sign * int(''.join(r))
        if out < - (2**31) or out > (2**31 - 1):
            out = 0
        return out