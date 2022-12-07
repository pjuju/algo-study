# import sys
# N = int(sys.stdin.readline())
# arr = []
# for _ in range(N):
#     val = list(map(int,sys.stdin.readline().split()))
#     arr.append(val)
#
# new_arr = arr.sort(key=lambda x: (x[0], x[1]))
#
#
# for val in arr:
#     print(val[0],val[1])


def BubbleSort(arr):
    for i in range(len(arr)-1,-1,-1):
        for j in range(i):
            if arr[j][0] > arr[i][0]:
                arr[j],arr[i] = arr[i],arr[j]
            elif arr[j][0] == arr[i][0]:
                if arr[j][1] > arr[i][1]:
                    arr[j], arr[i] = arr[i], arr[j]


    for i in range(len(arr)):
        print(*arr[i])

import sys
N = int(sys.stdin.readline())
arr = [list(map(int,input().split())) for _ in range(N)]

BubbleSort(arr)








