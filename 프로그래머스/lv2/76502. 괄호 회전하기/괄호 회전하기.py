from collections import deque

def solution(s):
    p_map = {
        "{": "}",
        "(": ")",
        "[": "]",
    }
    def check(s: deque):
        stack = []
        for p in s:
            if p in p_map.keys():
                stack.append(p)
                continue
            if stack and p_map.get(stack[-1]) == p:
                stack.pop()
            else:
                return False
        return False if stack else True

    count = 0
    s = deque(s)
    for _ in range(len(s)):
        if check(s):
            count += 1
        s.append(s.popleft())
    return count