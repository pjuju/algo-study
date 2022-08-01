K,N = map(int,input().split())
lan = [int(input()) for _ in range(K)]
cnt = [0]*K

low = 1
high = max(lan)

while low<=high:
    mid = (low+high)//2
    for i in range(K):
        cnt[i]=lan[i]//mid

    if sum(cnt)<N:
        # 자르는 크기 줄여야됨
        high=mid-1
    else:
        low=mid+1

print(high)