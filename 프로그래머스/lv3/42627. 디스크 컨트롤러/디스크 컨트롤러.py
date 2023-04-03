from heapq import heappop, heappush

def solution(jobs: list):
    N = len(jobs)
    result = 0
    handling = []
    ready_queue = []

    jobs.sort(key=lambda x: -x[0])

    t = jobs[-1][0]
    while jobs and t == jobs[-1][0]:
        t = jobs[-1][0]
        heappush(ready_queue, jobs.pop()[::-1])

    while ready_queue:
        if not handling:
            handling.append(heappop(ready_queue))
        
        for _ in range(handling[0][0]):
            t += 1
            while jobs and t == jobs[-1][0]:
                heappush(ready_queue, jobs.pop()[::-1])
        
        result += t - handling[0][1]
        handling = []

        while jobs and not ready_queue:
            t += 1
            while jobs and t == jobs[-1][0]:
                heappush(ready_queue, jobs.pop()[::-1])
    
    return result // N