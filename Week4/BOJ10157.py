import sys

# 1. 문제의 input 입력받기
C, R = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

# 2. 방향 전환 순서
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 3. 초기값 설정하기
visited = [[False for _ in range(R+1)] for _ in range(C+1)]
x = 1
y = 1
dir = 0
visited[1][1] = True

# 4. 예외 처리: 좌석 배정이 불가능한 경우
if K > R * C:
    print('0')
else: # 5. 자리 배치 시뮬레이션
    for i in range(1, K):
        # 5-1. 현재 방향에서 다음 자리 확인하기
        nx = x + dx[dir]
        ny = y + dy[dir]
        # 5-2. 배치 가능 여부 확인
        if nx <= 0 or nx > C or ny <= 0 or ny > R or visited[nx][ny]:
            # 5-3. 배치 불가능 불가능 시: 다음 방향으로 전환 & 다시 다음 자리 구하기
            dir = (dir+1) % 4
            nx = x + dx[dir]
            ny = y + dy[dir]
        # 5-4. 자리 업데이트 및 방문 체크
        x = nx
        y = ny
        visited[x][y] = True
    print(x, end = ' ')
    print(y)

