def sort(x,z):
    for i in range(len(x)):
        for j in range(len(x)-i-1):
            if z=="ascending" and x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
            elif z=="descending" and x[j]<x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
    return x