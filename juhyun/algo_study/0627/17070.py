N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
result = 0

def func(r2,c2,d):
    global result
    if r2 == N-1 and c2 == N-1 :
        result += 1

    else:
        if d != 2:  #세로가 아니면 (1, 3)
            if c2+1 < N and not arr[r2][c2+1]:
                func(r2,c2+1,1)
        if d != 1: # 가로가 아니면 (2, 3)
            if r2+1 < N and not arr[r2+1][c2]:
                func(r2+1,c2,2)

        # 전부(1,2,3)
        if r2 + 1 < N and c2 + 1 < N:
            if not arr[r2 + 1][c2 + 1] and not arr[r2][c2 + 1] and not arr[r2 + 1][c2]:
                func(r2+1, c2+1, 3)


func(0,1,1) #가로로 시작
print(result)




# bfs
# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N)]
# result = 0
# from collections import deque
# queue = deque([])
# queue.append((0,1,1))
#
# while queue:
#     r2,c2,d = queue.popleft()
#     if r2 == N-1 and c2 == N-1 :
#         result += 1
#
#     else:
#         if d == 1:
#             if c2+1 < N and not arr[r2][c2+1]:
#                 queue.append((r2,c2+1,1))
#             if r2+1 < N and c2+1 < N and not arr[r2+1][c2+1] and not arr[r2][c2+1] and not arr[r2+1][c2]:
#                 queue.append((r2+1, c2 + 1, 3))
#
#         if d == 2:
#             if r2+1 < N and not arr[r2+1][c2]:
#                 queue.append((r2+1,c2,2))
#             if r2+1 < N and c2+1 < N and not arr[r2+1][c2+1] and not arr[r2][c2+1] and not arr[r2+1][c2]:
#                 queue.append((r2+1, c2+1, 3))
#
#         if d == 3:
#             if c2+1 < N and not arr[r2][c2+1]:
#                 queue.append((r2,c2+1,1))
#             if r2 + 1 < N and not arr[r2 + 1][c2]:
#                 queue.append((r2 + 1, c2, 2))
#             if r2+1 < N and c2+1 < N and not arr[r2+1][c2+1] and not arr[r2][c2+1] and not arr[r2+1][c2]:
#                 queue.append((r2 + 1, c2 + 1, 3))
#
#
# print(result)
