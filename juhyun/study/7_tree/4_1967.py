import sys
input = sys.stdin.readline
N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, c = map(int,input().split())
    tree[a].append((b,c))

def func():
    result = 0 # 전체 결과
    for x in range(1,N+1): # 루트 지점 : x
        v_l = [] # x의 자식 노드들에서 출발해 가장 멀리 간 거리들
        v = 0
        for i,c in tree[x]:
            cnt = c
            queue = [(i,c)]
            while queue:
                i,c = queue.pop(0)
                if c > cnt:
                    cnt = c
                for ni,nc in tree[i]:
                        queue.append((ni,c+nc))

            v_l.append(cnt)

        v_1 = sorted(v_l, reverse=True)

        for i in range(len(v_l)):
            if i < 2: # 가장 먼거 두개만 더해줌
                v += v_1[i]
        if v > result:
            result = v

    print(result)





func()





