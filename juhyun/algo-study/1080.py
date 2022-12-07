N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]
ans = [list(map(int, input())) for _ in range(N)]
result = 0


def check():
    for i in range(N):
        for j in range(M):
            if arr[i][j] != ans[i][j]:
                return False

    return True


for i in range(N-2):
  for j in range(M-2):
      if arr[i][j] != ans[i][j]:
          for rr in range(i, i + 3):
              for cc in range(j, j + 3):
                arr[rr][cc] = (arr[rr][cc] + 1) / 2
          result += 1
      if arr == ans:
          break
  if arr == ans:
      break

if arr != ans and N>=2 and M>=2:
    print(result)
else:
    print(-1)
