class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_nums = sorted(nums1+nums2)
        l = len(new_nums)
        i = l // 2
        if l % 2 ==0:
            return (new_nums[i] + new_nums[i-1])/2
        return new_nums[i]
    
#         l1 = [-1000001] + l1 + [1000001]
#         l2 = [-1000002] + l2 + [1000002]
#         l1 = len(nums1)
#         l2 = len(nums2)
#         l = l1 + l2
        
        
#         i1 = l1 // 2
#         i2 = l2 // 2
        
#         m1 = nums1[i1]
#         move = 0
            
#         if m1 > nums2[i2]:
#             while m1 >= nums2[i2 + move]:
#                 move += 1
            
            
#             index = i2 - + 1
#             while move_left
#         else:
#             while m1 <= nums2[i2 - move]:
#                 move -= 1
#             i2 -= 1    
            
#             move_right = l2 - i2 + 1