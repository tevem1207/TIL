import sys
sys.stdin = open('input.txt', encoding='UTF-8')

for _ in range(10):
    tc = input()
    strs = [input() for _ in range(100)]
    max_cnt = 0

    for i in range(100):
        for M in range(2, 101):
            if M > max_cnt + 2:
                break
            for j in range(100 - M + 1):
                for k in range(M // 2):
                    if strs[i][j + k] != strs[i][j + M - 1 - k]:
                        break
                else:
                    if M > max_cnt:
                        max_cnt = M
                    break

    T_strs = ['' for _ in range(100)]
    for i in range(100):
        for j in range(100):
            T_strs[j] += strs[i][j]

    for i in range(100):
        for M in range(2, 101):
            if M > max_cnt + 2:
                break
            for j in range(100 - M + 1):
                for k in range(M // 2):
                    if T_strs[i][j + k] != T_strs[i][j + M - 1 - k]:
                        break
                else:
                    if M > max_cnt:
                        max_cnt = M
                    break

    print(f"#{tc} {max_cnt}")
