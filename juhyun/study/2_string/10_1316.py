N = int(input())
cnt = 0
for _ in range(N):
    text = input()
    now = text[0] #현재 글자
    arr = [text[0]] #이미 나왔던 알파벳들
    for i in range(len(text)): #텍스트 순회
        if text[i] != now: #현재 알파벳랑 다르면
            if text[i] in arr: # +이미 나왔던 글자들에도 있으면 반복문 종료
                break 
            arr.append(text[i]) # 알파벳 리스트에 추가
            now = text[i] # 현재 알파벳 변경
        else: # 현재 알파벳이랑 같으면 pass
            pass 
    else: # 반복문 다 순회하면
        cnt += 1

print(cnt)

