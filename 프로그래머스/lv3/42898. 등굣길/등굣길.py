def solution(m, n, puddles):
    grid = [[0]*(m+1) for _ in range(n+1)]
             
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == j == 1:
                grid[1][1] = 1
                continue
            if [j, i] not in puddles:
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
                
    return grid[n][m] % 1000000007