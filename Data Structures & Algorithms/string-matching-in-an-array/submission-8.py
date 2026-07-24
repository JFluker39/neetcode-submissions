class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        out = []
        my_set = set()
        for w in words:
            for j in words:
                if w in j and w != j and w not in my_set:
                    out.append(w)
                    my_set.add(w)
        return out
