class Solution:
    def candy(self, ratings: List[int]) -> int:
        l = len(ratings)
        candies = [1] * l
        def match(index):
            if index != 0:
                if ratings[index] > ratings[index - 1] and candies[index] <= candies[index - 1]:
                    candies[index] = candies[index - 1] +1
            if index != (l - 1):
                if ratings[index] > ratings[index + 1] and candies[index] <= candies[index + 1]:
                    candies[index] = candies[index + 1] +1
        
        for i in range(l):
            match(i)
            
        for i in range(l):
            match(l-i-1)

        return sum(candies)