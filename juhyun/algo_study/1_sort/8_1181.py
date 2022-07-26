def DictSort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if len(arr[i]) > len(arr[j]):
                arr[i],arr[j] = arr[j],arr[i]

            elif len(arr[i]) == len(arr[j]):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]

    return arr


N = int(input())
arr = []
for _ in range(N):
    arr.append(input())

arr = list(set(arr))
print('\n'.join(DictSort(arr)))



#2
# import sys
# N = int(sys.stdin.readline())
# arr_set = set()
# for _ in range(N):
#     arr_set.add(sys.stdin.readline().rstrip()) # 줄바꿈 요소를 제거해줘야 함
#
# arr=list(arr_set)
# arr.sort(key=lambda x: (len(x), x))
#
# for x in arr:
#     print(x)

    
# 13
# but
# i
# wont
# hesitate
# no
# more
# no
# more
# it
# cannot
# wait
# im
# yours