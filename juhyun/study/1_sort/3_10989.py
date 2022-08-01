# N = int(input())
# nums = [0] * 10001
#
# for _ in range(N):
#     nums[int(input())] += 1
#
# for i in range(1, 10001):
#     if nums[i] != 0:
#         for j in range((nums[i])):
#             print(i)

import sys
inputs = sys.stdin.readline

n = int(inputs().rstrip())
num = [0] * 10001 #카운팅 정렬

for _ in range(n):
    a = int(inputs().rstrip())
    num[a] += 1

for i in range(1, 10001): # 인덱스 = 숫자
    if num[i] != 0: # 카운트가 0이 아니면
        for j in range((num[i])): #카운트 수만큼
            print(i) # 프린트