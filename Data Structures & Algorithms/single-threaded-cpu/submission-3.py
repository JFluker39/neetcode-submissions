class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        out = []
        waiting = []
        for i in range(len(tasks)):
            heapq.heappush(waiting, (tasks[i][0], tasks[i][1], i))
        queued = []
        time = 1
        while waiting: 
            while waiting and waiting[0][0] <= time:
                task = heapq.heappop(waiting)
                heapq.heappush(queued, (task[1], task[2]))
            if queued:
                pop = heapq.heappop(queued)
                out.append(pop[1])
                time += pop[0]
            else:
                time = waiting[0][0]
        while queued:
            pop = heapq.heappop(queued)
            out.append(pop[1])
        return out