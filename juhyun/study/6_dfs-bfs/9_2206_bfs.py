from collections import deque
dr, dc = [0,0,1,-1], [1,-1,0,0]

def bfs():
    queue = deque()
    queue.append((0, 0, 0))

    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1

    while queue:
        r, c, cnt = queue.popleft()
        if r == N-1 and c == M-1:
            return visited[r][c]

        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if arr[nr][nc] == 0:
                    queue.append((nr,nc,cnt))
                    visited[nr][nc] = visited[r][c] + 1
                else:
                    if cnt == 0:
                        queue.append((nr,nc,cnt+1))
                        visited[nr][nc] = visited[r][c] + 1
    else:
        return -1

N, M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
result = bfs()
print(result)

