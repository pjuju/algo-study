N = int(input())
numbers = list(map(int, input().split()))
counts = [1] * N

for i in range(1, N):
    for j in range(i):
        if numbers[i] > numbers[j] and counts[i] < counts[j]+1:
            counts[i] = counts[j]+1

print(max(counts))

[10 20 10 30 20 50]
[1 2 1 3 2 4]