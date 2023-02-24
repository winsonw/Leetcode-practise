class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        follow_up = [[] for i in range(numCourses)]
        required = [0 for i in range(numCourses)]
        open_list = []
        order = []
        
        for a,b in prerequisites:
            required[a] += 1
            follow_up[b].append(a)
            
        for i in range(numCourses):
            if required[i] == 0:
                open_list.append(i)
        
        while open_list:
            current = open_list.pop(0)
            order.append(current)
            for unlock in follow_up[current]:
                required[unlock] -= 1
                if required[unlock] == 0:
                    open_list.append(unlock)
        
        return order if len(order) == numCourses else []
                