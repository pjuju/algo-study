X = int(input())

def orm(n):
    str_num = str(n)
    length = len(str_num)

    for i in range(1, length):
        if int(str_num[i]) < int(str_num[i-1]):
            return False

    return True

def solve(N):
    if N == 1:
        return 10

    cnt = 0
    for n in range(10**(N-1), 10**N):
        if orm(n):
            cnt += 1

    return cnt + solve(N-1)


print(solve(X))