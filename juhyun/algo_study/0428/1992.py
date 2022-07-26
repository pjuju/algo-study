N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
r = c = 0
stack = [(r,c)]
while stack:
    nr, nc = stack.pop(0)
    for x in range(N-nr-1):
        for r in range(nr+1, x):
            for c in range(nc+1 x):
                arr[r][c]

