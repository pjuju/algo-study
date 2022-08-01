def func(x):
    queue = [x]
    istree = 1
    visitied[x] = 1
    while queue:
        a = queue.pop(0)
        visitied[a] = 1
        for b in forest[a]:
            if visitied[b]:
                istree = 0
            else:
                queue.append(b)
    return istree


tc = 1
while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    forest = [[] for _ in range(N+1)]
    for _ in range(M):
        a,b = map(int,input().split())
        forest[a].append(b)
        forest[b].append(a)

    result = 0
    visitied = [0] * (N+1)

    for x in range(1,N+1):
        if not visitied[x]:
            result += func(x)

    if result == 0:
        print(f"Case {tc}: No trees.")
    elif result == 1:
        print(f"Case {tc}: There is one tree.")
    else:
        print(f"Case {tc}: A forest of {result} trees.")

    tc += 1


