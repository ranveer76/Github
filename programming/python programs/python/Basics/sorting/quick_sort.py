def quick_sort(x,z):
    if len(x)>1:
        pivot=x[0]
        i=0
        for j in range(len(x)-1):
            if z=="ascending":
                if x[j+1]<pivot:
                    x[j+1],x[i+1]=x[i+1],x[j+1]
                    i+=1
            elif z=="descending":
                if x[j+1]>pivot:
                    x[j+1],x[i+1]=x[i+1],x[j+1]
                    i+=1
        x[0],x[i]=x[i],x[0]
        left=x[:i]
        right=x[i+1:]
        quick_sort(left,z)
        quick_sort(right,z)
        x=left+[x[i]]+right
    return x
