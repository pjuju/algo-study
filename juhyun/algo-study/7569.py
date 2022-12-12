M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

day = 0
untomatoes = []

for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 0:
                untomatoes.append((i,j,k))



dx, dy, dz = [1,-1,0,0,0,0], [0,0,1,-1,0,0], [0,0,0,0,1,-1]



while untomatoes:
    new_tomatoes = []

    for untomato in untomatoes:
        cx, cy, cz = untomato

        for i in range(6):
            nx,ny,nz = cx+dx[i], cy+dy[i], cz+dz[i]
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
                if arr[nx][ny][nz] == 1:
                    new_tomatoes.append(untomato)
    
    if not new_tomatoes:
        day = -1
        break

    for new_tomato in new_tomatoes:
        x,y,z = new_tomato
        arr[x][y][z] = 1
        if new_tomato in untomatoes:
            untomatoes.remove(new_tomato)

    day += 1

print(day)


