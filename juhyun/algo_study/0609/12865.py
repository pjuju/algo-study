# N, K = map(int, input().split())
# values = [0]*N
# weights = [0]*N
# result = 0
#
# for i in range(N):
#     W, V = map(int, input().split())
#     weights[i] = W
#     values[i] = V
#
# def func(idx, val, wei):
#     global result
#
#     if idx == N:
#         if val > result :
#             result = val
#         return
#     if wei + weights[idx] <= K:
#         func(idx+1, val+values[idx], wei+weights[idx])
#     func(idx+1, val, wei)
#
# func(0,0,0)
# print(result)



N,K = map(int,input().split())

dp = [0] * (K+1)
for _ in range(N): # 무게 별 최대 가치
    w,v = map(int,input().split())
    for i in range(K, w-1, -1): # 왜 range(w, K+1)은 안되는가? 중복?
        dp[i] = max(dp[i], dp[i-w] + v)

print(dp[-1])