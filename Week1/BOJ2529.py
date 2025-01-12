import sys
from itertools import permutations

# 1. 문제의 입력값 받기
K = int(sys.stdin.readline())
arr = list(sys.stdin.readline().split())
numbers = [0,1,2,3,4,5,6,7,8,9]

# 2. K+1개의 숫자를 선택하는 모든 순열 구하기
per_list = list(permutations(numbers,K+1))

# 3. 순열의 부등호 만족 여부 확인 함수 구현하기
def check_ok(numbers):
    flag = True
    for i in range(0,K):
        if arr[i] == '<':
            if not numbers[i] < numbers[i+1]:
                flag = False
                break
        if arr[i] == '>':
            if not numbers[i] > numbers[i+1]:
                flag = False
                break
    return flag

# 4. 최댓값 찾기: 내림차순으로 정렬하여 탐색하기
for x in reversed(per_list):
    if check_ok(x):
        for i in x:
            print(i, end='')
        break
print()

# 5. 최솟값 찾기: 오름차순으로 정렬하여 탐색하기
for x in per_list:
    if check_ok(x):
        for i in x:
            print(i, end='')
        break