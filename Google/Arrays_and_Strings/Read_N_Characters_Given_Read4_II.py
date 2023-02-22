# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.pointer = 0
        self.remain = []
        
    def read(self, buf: List[str], n: int) -> int:
        index = 0
        con = True
        while con and index < n :
            if self.pointer < len(self.remain) and self.remain[self.pointer]:
                buf[index]=self.remain[self.pointer]
                self.pointer+= 1
                index += 1
            else:
                buf4 = ['']*4
                con = read4(buf4)
                self.pointer = 0
                self.remain = buf4
        return index
            
            
        