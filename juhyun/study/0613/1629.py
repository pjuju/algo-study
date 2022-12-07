a,b,c = map(int, input().split())
val = a

while b != 1:
    temp = 1
    while temp*2 < b:
        val **= 2
        temp *= 2
        b -= temp

print(val%c)




print((a**b)%c)