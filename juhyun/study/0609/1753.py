INF = 0xfffff
V,E = map(int, input().split())
K = int(input())
adj = [[INF]*(V+1) for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,input().split())
    adj[u][v] = w

dp = adj[K][:]
dp[K] = 0
U = [K]

while len(U) <= V-1:
    min_v = 0xffffff
    min_idx = K
    for i in range(1, V):
        if i not in U and dp[i] < min_v:
            min_v = dp[i]
            min_idx = i

    U.append(min_idx)

    for i in range(1, V+1):
        val = dp[min_idx] + adj[min_idx][i]
        if val <= dp[i]:
            dp[i] = val

for i in range(1, V+1):
    if dp[i] == INF:
        print("INF")
    else:
        print(dp[i])


