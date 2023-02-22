class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        l = len(words[0])
        sol = []
        def form_dics(l):
            d = [{i:[] for i in 'abcdefghijklmnopqrstuvwxyz'} for j in range(l)]
            for i in range(len(words)):
                for j in range(l):
                    d[j][words[i][j]].append(i)
            return d
        disc = form_dics(l)
            
        
#         def match(selected, new):
#             le = len(selected)
#             for i in range(le):
#                 if words[selected[i]][le] != words[new][i]:
#                     return False
#             return True
        
#         def find(selected):
#             for i in range(len(words)):
#                 if match(selected, i):
#                     selected.append(i)
#                     if len(selected) == l:
#                         sol.append(selected[:])
#                     else:
#                         find(selected)
#                     selected.pop()

        def form_new_range(selected):
            c = len(selected)
            new_range = disc[0][words[selected[0]][c]][:]
            for i in range(c - 1):
                j = 0
                while j < len(new_range):
                    if new_range[j] in disc[i+1][words[selected[i+1]][c]]:
                        j+= 1
                    else:
                        new_range.pop(j)
            return new_range

        def find(selected, rang):
            for i in rang:
                if len(selected) == l - 1:
                    sol.append(selected + [i])
                else:
                    new_range = form_new_range(selected + [i])
                    if len(new_range) != 0:
                        find(selected + [i], new_range)
            
                  
        find([], [i for i in range(len(words))])
        
        def translate(s):
            return [words[i] for i in s]
        return [translate(i) for i in sol]