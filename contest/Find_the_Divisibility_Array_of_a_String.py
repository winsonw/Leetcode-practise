class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        d = [0 for i in range(n)]
        current = m
        # d[0] = 1 if int(word[0]) % m == 0 else 0
        
        last_digit = []
        while not current % 10 in last_digit:
            last_digit.append(current % 10)
            current += m
        
        current = 0
        
        for i in range(n):
            current = current*10 + int(word[i])
            if int(word[i]) in last_digit:
                if current % m == 0:
                    d[i] = 1
            current = current % m
        
        return d