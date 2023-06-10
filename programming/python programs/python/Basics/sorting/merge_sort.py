def merge_sort(x,z):
    if len(x)>1:
        mid=len(x)//2
        left=x[:mid]
        right=x[mid:]
        merge_sort(left,z)
        merge_sort(right,z)
        i=j=k=0
        while i<len(left) and j<len(right):
            if z=="ascending":
                if left[i]<right[j]:
                    x[k]=left[i]
                    i+=1
                else:
                    x[k]=right[j]
                    j+=1
            elif z=="descending":
                if left[i]>right[j]:
                    x[k]=left[i]
                    i+=1
                else:
                    x[k]=right[j]
                    j+=1
            k+=1
        while i<len(left):
            x[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            x[k]=right[j]
            j+=1
            k+=1
    return x
