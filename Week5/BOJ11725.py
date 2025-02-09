import sys

# 1. 문제 input 입력받기 & 그래프 저장
from collections import deque
N = int(sys.stdin.readline())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y = map(int, sys.stdin.readline().split())
    arr[x].append(y)
    arr[y].append(x)

now = 1
que = deque()
que.append(1)

parent = [0 for _ in range(N+1)]
parent[1] = 1

# 2. BFS 탐색을 진행
while que:
    now = que.popleft()
    for x in arr[now]:
        if parent[x] == 0:
            parent[x] = now
            que.append(x)

for i in range(2, N+1):
    print(parent[i])
