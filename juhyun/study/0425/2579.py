N = int(input())
# lst = [0] + [int(input()) for _ in range(N)]
# result = 0
#
# def func(n, suc, val):
#     global result
#     if n <= 0:
#         if val > result:
#             result = val
#         return
#
#     val += lst[n]
#     if not suc:
#         func(n-1, suc+1, val)
#         func(n-2, 0, val)
#
#     else:
#         func(n-2, 0, val)
#
# func(N,0,0)
# print(result)



lst = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N+1)

for i in range(N):

