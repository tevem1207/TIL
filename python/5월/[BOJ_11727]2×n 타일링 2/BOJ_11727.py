import sys 
sys.stdin = open('input3.txt')

n = int(input())

dp = [0 for _ in range(1001)]
dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2] * 2) % 10007

print(dp[n])
