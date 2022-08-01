def selection_sort(items):
    for i in range(0,len(items)-1):
        minimum=i
        for j in range(i,len(items)):
            if items[minimum]>items[j]:
                minimum=j
        items[i],items[minimum]=items[minimum],items[i]


items=[40,70,60,30,10,50]
print("정렬 전 :",end="")
print(items)
selection_sort(items)
print("정렬 후 :",end="")
print(items)
