class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         wordList.append(beginWord)
#         self.h = dict()
#         self.n = {word:[] for word in wordList}
        
#         def find_difference(a, b):
#             count = 0
#             for i in range(len(a)):
#                 if a[i] != b[i]:
#                     count += 1
#             return count
        
#         def find_neigh(a, current_h):
#             for i in range(3):
#                 near_h = current_h + i -1
#                 if near_h in self.h:
#                     for word in self.h[near_h]:
#                         if not word in self.n[a] and find_difference(word, a) == 1:
#                             self.n[a].append(word)
#                             self.n[word].append(a)
            
                          
#         for word in wordList:
#             current_h = find_difference(endWord, word)
#             if current_h in self.h:
#                 self.h[current_h].append(word)
#             else:
#                 self.h[current_h] = [word]
#             find_neigh(word, current_h)

        wordList.append(beginWord)
        l = len(beginWord)
        self.n = {word:[] for word in wordList}
        
        d = dict()
        for word in wordList:
            for i in range(l):
                part = word[0:i] + '*' + word[i+1:]
                if not part in d:
                    d[part] = []
                    
                if d[part]:
                    for neigh in d[part]:
                        self.n[neigh].append(word)
                        self.n[word].append(neigh)
                d[part].append(word)
        
                    
        
            
        open_list = [beginWord]
        current = beginWord
        g = {word:100000 for word in wordList}
        g[current] = 0
        cameFrom = dict()
        
        def find_route(cameFrom, a):
            if not a in cameFrom:
                return 1
            return find_route(cameFrom, cameFrom[a]) + 1
        
        while open_list:
            current = open_list.pop(0)
            if current == endWord:
                return find_route(cameFrom, endWord)
            for word in self.n[current]:
                new_g = g[current] + 1
                if new_g < g[word]:
                    g[word] = new_g
                    cameFrom[word] = current
                    if word not in open_list:
                        open_list.append(word)
        return 0

    
        