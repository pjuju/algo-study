from collections import deque # 이거 안쓰면 시간초과
import sys
read = sys.stdin.readline

def func():
    while queue:
        h,r,c = queue.popleft()
        for x in range(6):
            nh = h + dh[x]
            nr = r + dr[x]
            nc = c + dc[x]
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M:
                if arr[nh][nr][nc] == 0:
                    queue.append((nh,nr,nc))
                    arr[nh][nr][nc] = arr[h][r][c] + 1


M, N, H = map(int, read().split())
arr = [[list(map(int, read().split())) for _ in range(N)] for _ in range(H)]
# [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]]
queue = deque()
dr = [1,-1,0,0,0,0]
dc = [0,0,-1,1,0,0]
dh = [0,0,0,0,1,-1]
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                queue.append((h,i,j))

func()

result = 0
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] > result:
                result = arr[h][i][j] - 1
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 0:
                result = -1
                break

print(result)





