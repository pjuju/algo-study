def dfs(r,c,cnt,move):
    global result
    if move > result:
        return
    if r == N-1 and c == M-1:
        if move < result:
            result = move
            return

    for k in range(4):
        nr, nc = r+dr[k], c+dc[k]
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            if arr[nr][nc] == 0:
                visited[nr][nc] = 1
                dfs(nr,nc,cnt,move+1)
                visited[nr][nc] = 0

            else:
                if cnt == 0:
                    visited[nr][nc] = 1
                    dfs(nr, nc, cnt+1, move + 1)
                    visited[nr][nc] = 0

dr, dc = [0,0,1,-1], [1,-1,0,0]
N, M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
result = 11111111111111
dfs(0,0,0,1)
if result == 11111111111111:
    print(-1)
else:
    print(result)


