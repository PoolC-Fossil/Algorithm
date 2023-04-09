from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    result = 1
    total_weight = truck_weights[0]
    passing = deque([(truck_weights.popleft(), result + bridge_length)])

    while passing:
        result += 1

        if passing[0][1] == result:
            total_weight -= passing.popleft()[0]

        if truck_weights and total_weight + truck_weights[0] <= weight:
            total_weight += truck_weights[0]
            passing.append((truck_weights.popleft(), result + bridge_length))
        
    return result