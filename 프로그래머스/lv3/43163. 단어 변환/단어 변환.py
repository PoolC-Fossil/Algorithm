from collections import deque

def solution(begin, target, words):
    def check(a, b):
        limit = 1
        for i in range(len(a)):
            if a[i] != b[i]:
                if limit:
                    limit -= 1
                    continue
                return False
        return True

    queue = deque([begin])
    visited = {w: 0 for w in words}
    visited[begin] = 1

    while queue:
        cur = queue.popleft()
        if cur == target:
            break

        for nxt in words:
            if visited[nxt]:
                continue

            if check(cur, nxt):
                visited[nxt] = visited[cur] + 1
                queue.append(nxt)

    return result - 1 if (result := visited.get(target)) else 0