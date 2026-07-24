class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        x = len(tasks)
        if n == 0:
            return x
        min_cpu = x
        freq = [0] * 26
        for t in tasks:
            freq[ord(t) - ord("A")] += 1
        max_num = 0
        n_max = 0
        for f in freq:
            if f > max_num:
                max_num = f
                n_max = 1
            elif f == max_num:
                n_max += 1
        return max(x, ((n + 1) * (max_num - 1)) + n_max)
