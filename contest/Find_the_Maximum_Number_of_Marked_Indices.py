class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        mid = l // 2
        left, right = 0, l - l // 2
        maxNum = 0
        
        print(nums)
        
        while right < l and left < mid:
            if left < mid and nums[right] / 2 >= nums[left]:
                maxNum += 2
                left += 1
            right += 1
        
            
        
        return maxNum