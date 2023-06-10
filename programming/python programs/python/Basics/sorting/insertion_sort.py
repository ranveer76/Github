def insertion_sort(x,z):
    for i in range(1,len(x)):
        for j in range(i-1,-1,-1):
            if z=="ascending" and x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
            elif z=="descending" and x[j]<x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
    return x