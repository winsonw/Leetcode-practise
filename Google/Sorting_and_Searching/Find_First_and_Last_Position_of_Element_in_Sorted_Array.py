class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not target in nums:
            return [-1,-1]
        left = nums.index(target)
        nums.reverse()
        right = nums.index(target)
        return [left, len(nums) - right -1]