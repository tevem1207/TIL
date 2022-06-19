import sys 
sys.stdin = open('input1.txt')


import sys
input = sys.stdin.readline


N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + matrix[i-1][j-1]


for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    total = dp[y2][x2] - dp[y2][x1-1] - dp[y1-1][x2] + dp[y1-1][x1-1]
    print(total)
