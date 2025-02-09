import sys
import heapq

# 1. 문제 input 입력받기
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 2. 사진틀 관리 딕셔너리 생성하기
candidate_heap = {}

for x in arr:
    # 후보가 사진틀 안에 존재하는 경우
    if x in candidate_heap:
        candidate_heap[x] += 1
    else:
        # 사진틀 개수가 N개 이상일 경우
        if len(candidate_heap) >= N:
            del_key = heapq.nsmallest(1, candidate_heap, key=candidate_heap.get)
            candidate_heap.pop(del_key[0])
        candidate_heap[x] = 1

# 3. 오름차순 정렬하기
res = sorted(candidate_heap.keys())
for i in res:
    print(i, end=' ')