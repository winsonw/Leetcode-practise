class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ma = nums[0]
        for i in range(len(nums)-1):
            index = i + 1
            if index > ma:
                return False
            current = index + nums[index]
            if current > ma:
                ma = current
        return True