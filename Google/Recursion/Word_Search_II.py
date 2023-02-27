class TreeNode:
    def __init__(self):
        self.next = dict()
        self.word = None

        
class Trie:
    def __init__(self):
        self.root = TreeNode()
        
    def insert(self, word):
        current = self.root
        for letter in word:
            if not letter in current.next:
                current.next[letter] = TreeNode()
            current = current.next[letter]
        current.word = word
    
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        t = Trie()
        found = set()
        visited = [[0 for j in range(n)] for i in range(m)]
        for word in words:
            t.insert(word)
            
            
#         def print_trie(current):
#             print(current.letter, current.word, current.next)
#             for key in current.next:
#                 print_trie(current.next[key])
                
#         print_trie(t.root)
            
        def dfs(x, y, current):
            if not (0 <= x < m and 0 <= y < n) or visited[x][y] or not board[x][y] in current.next:
                return
            parent, current = current, current.next[board[x][y]]
            if current.word:
                found.add(current.word)
            visited[x][y] = 1
            # map(dfs, [x+1, x-1, x , x], [y, y, y+1, y-1], [current]*4)
            dfs(x+1, y, current)
            dfs(x-1, y, current)
            dfs(x, y+1, current)
            dfs(x, y-1, current)
            visited[x][y] = 0
            
            if len(current.next) == 0:
                parent.next.pop(board[x][y])
            return 
            
        
        for i in range(m):
            for j in range(n):
                dfs(i ,j, t.root)
                
                
        return found
                    
                    