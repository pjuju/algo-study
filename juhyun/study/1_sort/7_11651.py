def Sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if i == j:
                continue
            elif arr[i][1] > arr[j][1]:
                arr[i],arr[j] = arr[j],arr[i]

            elif arr[i][1] == arr[j][1]:
                if arr[i][0] > arr[j][0]:
                    arr[i],arr[j] = arr[j],arr[i]

    for i in range(len(arr)):
        print(*arr[i])

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

Sort(arr)







