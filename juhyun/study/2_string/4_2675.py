N = int(input()) #tc 개수

for tc in range(1,1+N):
    S, R = input().split() #반복 수, 문자
    S = int(S) #숫자로 변환

    result = '' # 빈 문자
    for a in R:
        result += a*S # 각 문자열 S번 반복한 것 더해줌

    print(result)
