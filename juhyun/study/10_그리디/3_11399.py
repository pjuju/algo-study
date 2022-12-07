N = int(input())
lst = list(map(int, input().split()))

# lst.sort()
# result = t = 0
#
# for i in range(N):
#     result += (t+lst[i])
#     t += lst[i]
# print(result)


used = [0] * N
def func(i, v, time):
    if i == N:
        print(result)
        return
    print(v)
    for j in range(N):
        if not used[j]:
            used[j] = 1
            func(i+1, time, time+lst[j])
            used[j] = 0


func(0,0,0)

