def insertion_sort(items):
    for i in range(1,len(items)):
        for j in range(i,0,-1):
            if items[j-1]>items[j]:
                items[j],items[j-1]=items[j-1],items[j]
            else:
                break

items=[40,70,60,30,10,50]
print("정렬 전 :",end="")
print(items)
insertion_sort(items)
print("정렬 후 :",end="")
print(items)
