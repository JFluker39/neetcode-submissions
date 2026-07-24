class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        max_num = 0
        for num in people:
            if num > max_num:
                max_num = num
        count_arr = [0] * (max_num + 1)
        for num in people:
            count_arr[num] += 1
        x = 0
        i = 0
        while i < n:
            while x < len(count_arr) and count_arr[x] != 0:
                people[i] = x
                i += 1
                count_arr[x] -= 1
            x += 1
        amount = 0
        l = 0
        r = n - 1
        while l <= r:
            if people[l] + people[r] <= limit:
                amount += 1
                l += 1
                r -= 1
            else:
                amount += 1
                r -= 1
        return amount