def shell_sort(items):
    h=len(items)//2
    while h>=1:
        for i in range(h,len(items)):
            j=i
            while j>=h and items[j]<items[j-h]:
                items[j],items[j-h]=items[j-h],items[j]
                j-=h
        print("{}-정렬 결과 : ".format(h), items)
        h//=2

items=[39,23,15,47,11,56,61,16,12,19,21,41]
print("정렬 전 :",end="")
print(items)
shell_sort(items)
print("정렬 후 :",end="")
print(items)


