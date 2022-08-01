def merge(items,temp,low,mid,high):
    i=low
    j=mid+1
    for k in range(low,high+1):
        if i > mid:
            temp[k]=items[j]
            j+=1
        elif j>high:
            temp[k]=items[i]
            i+=1
        elif items[j]<items[i]:
            temp[k]=items[j]
            j+=1
        else:
            temp[k]=items[i]
            i+=1
    for k in range(low,high+1):
        items[k]=temp[k]

def merge_sort(items,temp,low,high):
    if high<=low:
        return None
    mid =low+(high-low)//2
    merge_sort(items,temp,low,mid)
    merge_sort(items,temp,mid+1,high)
    merge(items,temp,low,mid,high)
    
items=[54,88,77,26,93,17,49,10,17,77,11,31,22,44,17,20]
temp=[None]*len(items)

print("정렬 전 :",end="")
print(items)

merge_sort(items,temp,0,len(items)-1)
print("정렬 후 :",end="")
print(items)
