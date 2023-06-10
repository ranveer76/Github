def sequence_sort(x,z):
    n=len(x)
    for i in range(n-1):
        _min=i
        for j in range(i+1,n):
            if z=="ascending" and x[j]<x[_min]:
                    _min=j
            elif z=="descending" and x[j]>x[_min]:
                    _min=j
        x[i],x[_min]=x[_min],x[i]
    return x
