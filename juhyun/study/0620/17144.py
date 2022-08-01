import heapq

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
dr, dc = [0,0,1,-1], [1,-1,0,0]
queue = []

while queue:
    check, r, c = heapq.heappop(queue)
    for x in range(4):
        nr, nc = r+dr[x], c+dc[x]
        if 0 <= nr < R and 0 <= nc < C:
            
