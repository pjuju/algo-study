def partition(items,pivot,high):
    i=pivot+1
    j=high
    while True:
        while i <high and items[i]<items[pivot]:
            i+=1
        while j>pivot and items[j]>items[pivot]:
            j-=1
        if j<=i:
            break
        items[i],items[j]=items[j],items[i]
        i+=1
        j-=1
    items[pivot],items[j]=items[j],items[pivot]
    return j

def quick_sort(items,low,high):
    if low<high:
        pivot = partition(items,low,high)
        quick_sort(items,low,pivot-1)
        quick_sort(items,pivot+1,high)
        
items=[54,88,77,26,93,17,49,10,17,77,11,31,22,44,17,20]
print("정렬 전 :",end="")
print(items)
quick_sort(items,0,len(items)-1)
print("정렬 후 :",end="")
print(items)
