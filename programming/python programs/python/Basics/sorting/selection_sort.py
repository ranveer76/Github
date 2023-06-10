def selection_sort(x,z):
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if z=="ascending" and x[i]>x[j]:
                x[i],x[j]=x[j],x[i]
            elif z=="descending" and x[i]<x[j]:
                x[i],x[j]=x[j],x[i]
    return x