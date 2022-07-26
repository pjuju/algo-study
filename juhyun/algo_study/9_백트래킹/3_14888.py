def dfs(idx, val, a, b, c, d):
    global min_v, max_v
    if idx == N-1:
        if val < min_v:
            min_v = val
        if val > max_v:
            max_v = val
        return
    if a:
        dfs(idx + 1, val + nums[idx + 1], a-1 , b, c, d)
    if b:
        dfs(idx + 1, val - nums[idx + 1], a, b-1, c, d)
    if c:
        dfs(idx + 1, val * nums[idx + 1], a, b, c-1, d)
    if d:
        dfs(idx + 1, int(val / nums[idx + 1]), a, b, c, d-1)

N = int(input())
nums = list(map(int, input().split()))
a,b,c,d = map(int, input().split()) #덧 뺄 곱 몫

max_v = -1000000000
min_v = 1000000000
dfs(0,nums[0],a,b,c,d)
print(max_v)
print(min_v)

# 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다.
print(-9//2) : -5 1
print(int(-9//2)) : int(-4.5)
print(int(-9/2)) : int(-4.5)
