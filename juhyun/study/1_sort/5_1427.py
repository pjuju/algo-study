num = input()
num_li = []

# 리스트에 담기
for i in num:
    num_li.append(int(i))

# 내림차순으로 정렬
num_li.sort(reverse=True)

# 하나씩 출력 (end=''로)
for v in num_li:
    print(v, end='')

