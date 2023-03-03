class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        l = len(nums)
        left = [0 for i in range(l)]
        right = [0 for i in range(l)]
        answer = [0 for i in range(l)]
        
        for i in range(l-1):
            left[i+1] = left[i] + nums[i]
            right[l-(i+2)] = right[l-(i+1)] + nums[l-(i+1)]
            
        return [abs(left[i] - right[i]) for i in range(l)]