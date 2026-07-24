class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        my_order = {}
        for i in range(len(order)):
            my_order[order[i]] = i
        
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                if my_order[words[i][j]] == my_order[words[i + 1][j]]:
                    continue
                elif my_order[words[i][j]] < my_order[words[i + 1][j]]:
                    break
                else:
                    return False
        return True
                