class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        index = -1
        l = len(digits)
        while digits[index] >= 10:
            if index == -l:
                digits = [0] + digits
            digits[index] -= 10
            index -= 1
            digits[index] += 1
        return digits