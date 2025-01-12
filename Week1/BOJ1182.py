from itertools import combinations

# 입력
N, S = map(int, input().split())
numbers = list(map(int, input().split()))

# 부분수열의 합이 S인 경우의 수를 저장하는 변수
answer = 0

# 모든 부분수열의 조합 탐색
for r in range(1, N + 1):  # 부분수열의 길이를 1부터 N까지 탐색
    for subset in combinations(numbers, r):  # r개의 원소를 가지는 부분수열 생성
        if sum(subset) == S:  # 부분수열의 합이 S인지 확인
            answer += 1

# 출력
print(answer)