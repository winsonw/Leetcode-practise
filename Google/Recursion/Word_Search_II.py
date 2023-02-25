class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        char_dict = dict()
        for i in range(m):
            for j in range(n):
                letter = board[i][j]
                if letter not in char_dict:
                    char_dict[letter] = []
                char_dict[letter].append([i,j])
        # substrings = [[dict() for j in range(n)] for i in range(m)]
                
        def find_word(position, remain, sequence):
            if len(remain) == 0:
                return 1
            x, y = position
            if not (0 <= x < m and 0 <= y < n) or position in sequence or board[x][y] != remain[0]:
                return 0
            # if remain in substrings[x][y]:
            #     return 1
            if find_word([x+1, y], remain[1:], sequence + [position]) or find_word([x-1, y], remain[1:], sequence + [position]) or find_word([x, y+1], remain[1:], sequence + [position]) or find_word([x, y-1], remain[1:], sequence + [position]):
                return 1
            
            # is_found = max(map(find_word, [[x+1, y], [x-1, y], [x, y+1], [x, y-1]], 
            #                [remain[1:]]*4, 
            #                [sequence + [position]] * 4))
            
            # if is_found:
            #     substrings[x][y].add(remain)
            
            return 0
            
            
            
        found = []
        
        for word in words:
            cond = True
            for letter in word:
                if not letter in char_dict:
                    cond = False
                    continue
                    
            if cond:
                for coord in char_dict[word[0]]:
                    if find_word(coord, word, []):
                        found.append(word)
                        break
                # if max([find_word(coord, word, []) for coord in char_dict[word[0]]]):
                #     found.append(word)
                    
        return found
                    
                    