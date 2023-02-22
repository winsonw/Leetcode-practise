class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        missing = []
        i = 0
        while i < len(nums) and lower > nums[i]:
            i += 1
        num = lower -1
        
        while i < len(nums):
            if num >= (lower-1) and num <= upper:
                if nums[i] <= upper:
                    s_up = nums[i]
                else:
                    s_up = upper+1
                    
                if num + 1 < s_up:
                    missing.append(str(num+1))
                    if num + 1 < s_up - 1:
                        missing[-1]+= "->" + str(s_up-1)
                num = s_up  
            i+= 1
            # lower = min(lower, nums[i])
            # if i < len(nums):
            #     num = nums[i]
            
        if num + 1 <= upper:
            missing.append(str(num+1))
            if num + 1 <= upper - 1:
                missing[-1]+= "->" + str(upper)
        
        return missing
                    