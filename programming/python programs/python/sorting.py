def bubblesort(arr,t=1):#bubble sort
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                t+=1
    return arr,t#return sorted list

def insertionsort(arr,t=1):#insertion sort
    n=len(arr)
    for i in range(1,n):
        c=arr[i]
        po=i
        while c<arr[po-1] and po>0:
            arr[i]=arr[po-1]
            po-=1
            t+=1
        arr[po]=c
    return arr,t#return sorted list

def selectionsort(arr,t=1):#selection sort
    n=len(arr)
    for i in range(n-1):
        c=i
        for j in range(i+1,n):
            if arr[j]<arr[c]:
                c=j
        arr[i],arr[c]=arr[c],arr[i]
        t+=1
    return arr,t#return sorted list

def m(lis,k=1):
    if len(lis)>1:
        mid=len(lis)//2
        l=lis[:mid]
        r=lis[mid:]
        m(l)
        m(r)
        k=i=j=0
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                lis[k]=l[i]
                i+=1
            else:
                lis[k]=r[j]
                j+=1
            k+=1
            
        while i<len(l):
            lis[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            lis[k]=r[j]
            j+=1
            k+=1
        return lis,k
