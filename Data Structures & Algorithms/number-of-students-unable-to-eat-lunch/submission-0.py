class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        counter = Counter(students)

        for s in sandwiches:
            if counter[s] > 0:
                res -= 1
                counter[s] -= 1
            else:
                break

        return res