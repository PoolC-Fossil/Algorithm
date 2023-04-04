def solution(numbers):
    N = len(numbers)
    answer = [-1] * N
    stack = []

    for i in range(N):
        if not stack:
            stack.append(i)
            continue

        while stack and numbers[i] > numbers[stack[-1]]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    
    return answer