def counting_sort(x,z):
    n=len(x)
    output=[0]*n
    count=[0]*(max(x)+1)
    if z=="ascending":
        for i in range(n):
            count[x[i]]+=1
        for i in range(1,len(count)):
            count[i]+=count[i-1]
        for i in range(n-1,-1,-1):
            output[count[x[i]]-1]=x[i]
            count[x[i]]-=1
        for i in range(n):
            x[i]=output[i]
    elif z=="descending":
        for i in range(n):
            count[x[i]]+=1
        for i in range(len(count)-2,-1,-1):
            count[i]+=count[i+1]
        for i in range(n):
            output[count[x[i]]-1]=x[i]
            count[x[i]]-=1
        for i in range(n):
            x[i]=output[i]
    return x