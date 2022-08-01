# import sys
# N = int(sys.stdin.readline().rstrip())
# arr = list(map(int,sys.stdin.readline().split()))
#
# result = [0]*N
#
# for i in range(N):
#     for j in range(N):
#         if arr[i] > arr[j]:
#             result[i] += 1
#
# print(*result)





import sys
N = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().split()))

arr_2 = list(set(arr)) # 중복값 제거한 리스트
for i in range(len(arr_2)):
    for j in range(i+1,len(arr_2)):
        if arr_2[i] > arr_2[j]:
            arr_2[i],arr_2[j] = arr_2[j],arr_2[i]

result_dict = {arr_2[i] : i for i in range(len(arr_2))} # 새 딕셔너리

for x in arr:
    print(result_dict[x], end=' ')

# 5
# 2 4 -10 4 -9



