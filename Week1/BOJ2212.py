import sys

board = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 1. 입력값 받기
for _ in range(5):
    arr = sys.stdin.readline().split()
    board.append(arr)
    
answer = set()

# 2. 재귀 함수: 다섯 번 이동하는 탐색 구현하기
def dfs(x, y, now):
    now += str(board[x][y])
    if len(now) == 6: # answer 의 길이가 6이 되면 탐색 중단
        answer.add(now)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue
        dfs(nx,ny,now)
    

# 3. 탐색 진행하기
for i in range(5):
    for j in range(5):
        dfs(i,j,"")


# 4. 정답 출력하기
print(len(answer))