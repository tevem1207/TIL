import sys
sys.stdin = open('input.txt', encoding='UTF-8')


def get_rotation(strings, N):
    result = ['' for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result[j] += strings[-(i+1)][j]
    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [''.join(input().split()) for _ in range(N)]
    m_90 = get_rotation(matrix, N)
    m_180 = get_rotation(m_90, N)
    m_270 = get_rotation(m_180, N)

    print(f'#{tc}')
    for i in range(N):
        print(m_90[i], m_180[i], m_270[i])
