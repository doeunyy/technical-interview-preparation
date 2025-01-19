import sys

# 1. 문제의 입력값 받기
N, K = map(int, sys.stdin.readline().split())
str1 = list(sys.stdin.readline().strip())

ans = 0
for i in range(0, N):
    # 2. 사람 발견 -> 인접한 K개의 원소 탐색
    if str1[i] == 'P':
        for j in range(i-K, i+K+1):
            # 3. 햄버거가 발견되면 탐색 종료
            if 0 <= j < N and str1[j] == 'H':
                str1[j] = 'X'
                ans += 1
                break
print(ans)