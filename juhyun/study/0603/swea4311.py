def func(number):
    global result

    stack = []
    for num in touch:
        stack.append((num, 2))

    while stack:
        n,c = stack.pop(0)

        if M - result < c:
            result = -1
            return
        if n == number:
            result += c
            break

        for nn in touch:
            if nn != 0:
                if 1 in cal:
                    stack.append((n + nn, c + 2))
                if 2 in cal:
                    stack.append((n - nn, c + 2))
                if 3 in cal:
                    stack.append((n * nn, c + 2))
                if 4 in cal:
                    stack.append((n // nn, c + 2))


T = int(input())
for tc in range(1, 1+T):
    N, O, M = map(int, input().split())
    touch = list(map(int, input().split()))
    cal = list(map(int,input().split()))
    W = input()
    result = 0
    for num in W:
        if result != -1:
            if int(num) in touch:
                result += 1
            else:
                func(int(num))

    print(result)



