text = input().upper() # 텍스트 입력받아서 바로 대문자화

alpha_list=list(set(text)) # 알파벳 리스트
alpha_cnt = [0] * len(alpha_list) # 횟수 세는 리스트

for i in range(len(alpha_list)):
    for j in range(len(text)):
        if alpha_list[i] == text[j]: # 알파벳이 텍스트에 있으면
            alpha_cnt[i] += 1 # 횟수 리스트의 같은 인덱스 값에 1 더해줌

for i in range(len(alpha_cnt)): # 횟수 리스트 내림차순 정렬
    for j in range(i+1,len(alpha_cnt)):
        if alpha_cnt[i] < alpha_cnt[j]:
            alpha_cnt[i],alpha_cnt[j] = alpha_cnt[j], alpha_cnt[i]
            alpha_list[i],alpha_list[j] = alpha_list[j], alpha_list[i] # 알파벳 리스트도 같이 정렬해줌

if alpha_cnt[0] == alpha_cnt[1]: # 제일 높은 횟수와 다음으로 높은 횟수가 같으면
    print('?')
else:
    print(alpha_list[0])





# # 백준
# text = input().upper() # 텍스트 입력받아서 바로 대문자화
# alpha_list = list(set(text))
#
# max_cnt = 0
# max_cnt_idx = 0
# max_cnt_num = 0
# for i in range(len(alpha_list)):
#     alpha_cnt = text.count(alpha_list[i])
#     if alpha_cnt > max_cnt:
#         max_cnt = alpha_cnt
#         max_cnt_idx = i
#         max_cnt_num = 1
#     elif alpha_cnt == max_cnt:
#         max_cnt_num += 1
#
# if max_cnt_num > 1:
#     print('?')
# else:
#     print(alpha_list[max_cnt_idx])

