def sosu(n):
    for i in range(2, int(n**(0.5))+1):
        if n%i == 0:
            return False
    return True

nums = []
while True:
    n = int(input())
    if n == 0:
        break
    nums.append(n)

sosus = []
for i in range(2, 2*max(nums)+1):
    if sosu(i):
        sosus.append(i)


for num in nums:
    cnt = 0
    for x in range(num+1, 2*num+1):
        if x in sosus:
            cnt += 1
    print(cnt)




