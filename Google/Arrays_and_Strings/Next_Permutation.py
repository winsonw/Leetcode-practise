class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        stack = [nums.pop()]
        print(stack)
        
        while nums and nums[-1] >= stack[-1]:
            stack.append(nums.pop())
            
        if nums:
            i = 0
            while stack[i] <= nums[-1]:
                i += 1
                
            t = stack[i]
            stack[i] = nums[-1]
            nums[-1] = t
        
        while stack:
            nums.append(stack.pop(0))
        return nums