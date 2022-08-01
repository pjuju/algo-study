def sums(n):
    if 1<= n <= 2:
        return n
    if n==3:
        return n+1
    else:
        return sums(n - 1) + sums(n - 2) + sums(n - 3)  # 규칙을 찾아내는게 중요!


def dfs(n):
    global result

    if n == 0 :
        result += 1
        return
    else:
        if n - 1 >= 0:
            dfs(n-1)
        if n - 2 >= 0:
            dfs(n-2)
        if n - 3 >= 0:
            dfs(n-3)


T = int(input())
for tc in range(T):
    n = int(input())
    result = 0
    ans1 = sums(n)
    dfs(n)
    ans2 = result
    print(ans1, ans2)
