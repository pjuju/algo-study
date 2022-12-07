import sys
read = sys.stdin.readline
dr = [0,0,-1,1]
dc = [1,-1,0,0]

def func(arr):
    possible = 0
    lst = []
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1:
                visited[i][j] = 1
                for x in range(4):
                    nr = i + dr[x]
                    nc = j + dc[x]
                    if 0 <= nr < M and 0 <= nc < N:
                        if not visited[nr][nc] and arr[nr][nc] == 0:
                            lst.append([nr,nc])
                            possible = 1
    if possible:
        for a in lst:
            arr[a[0]][a[1]] = 1
        global count
        count += 1
        func(arr)

N,M = map(int, read().split())
arr = [list(map(int, read().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
count = 0
func(arr)

result = count
for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            result = -1
            break
print(result)






