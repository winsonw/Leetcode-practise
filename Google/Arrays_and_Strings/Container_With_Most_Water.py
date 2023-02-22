class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        trigger = True
        self.ma = 0
                
        def check(left, right):
            volumne = (right - left) * min(height[left], height[right])
            if volumne > self.ma:
                self.ma = volumne
        
        while left < right and trigger:
            trigger = False
            while left < right and height[left] < height[right]:
                trigger = True
                check(left, right)
                left += 1
            while left < right and height[left] >= height[right]:
                trigger = True
                check(left, right)
                right -= 1
        return self.ma
        