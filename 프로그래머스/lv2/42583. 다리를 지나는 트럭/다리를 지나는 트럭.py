from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer, bsum = 0, 0
    bridge = deque([0] * (bridge_length))
    tq = deque(truck_weights)
    while tq:
        tpop, bpop = tq.popleft(), bridge.pop()
        bsum -= bpop
        if bsum + tpop <= weight:
            bridge.appendleft(tpop)
            bsum += tpop
        else:
            bridge.appendleft(0)
            tq.appendleft(tpop)
        answer += 1  
    for i in range(bridge_length):
        if bridge[i] != 0:
            answer += (bridge_length-i)
            break
    return answer