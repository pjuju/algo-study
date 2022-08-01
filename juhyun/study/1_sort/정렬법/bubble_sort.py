def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1,-1,-1):
        change=False
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                change=True
        if change==False:
            break
    return arr

items=[40,70,60,30,10,50]
print("정렬 전 :",end="")
print(items)
bubble_sort(items)
print("정렬 후 :",end="")
print(items)
