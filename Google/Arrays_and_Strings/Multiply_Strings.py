class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num3 = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                num3[i + j] += int(num1[len(num1)-i-1]) * int(num2[len(num2)-j-1])
                # print(i,j, num3)
                
        for i in range(len(num3)-1):
            num3[i+1] += num3[i] // 10
            num3[i] = str(num3[i] % 10)
            
        num3[-1] = str(num3[-1])
        while num3[-1] == '0' and len(num3) > 1:
            num3.pop(-1)
        
        return ''.join(reversed(num3))
                