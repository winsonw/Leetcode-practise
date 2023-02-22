class Solution(object):
    def oddEvenJumps(self, arr):
        self.l = len(arr)
        s_l = sorted(range(self.l), key = lambda i:arr[i])
        odd_jump = self.stack_idea(s_l)


        s_l_r = sorted(range(self.l), key = lambda i:arr[i], reverse=True)
        even_jump = self.stack_idea(s_l_r)

        track = [[-1, -1] for i in range(self.l)]
        track[-1] = [1,1]
        count = 1

        for i in range(self.l-1):
            index = -i-2
            if odd_jump[index]:
                track[index][1] = track[odd_jump[index]][0]

            if even_jump[index]:
                track[index][0] = track[even_jump[index]][1]

            if track[index][1] == 1:
                count += 1
        return count



    def stack_idea(self, s_l):
        jump = [None] * self.l
        stack = []
        for i in s_l:
            while stack and i > stack[-1]:
                jump[stack.pop()] = i
            stack.append(i)
        return jump