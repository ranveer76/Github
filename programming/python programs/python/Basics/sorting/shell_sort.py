def shell_sort(x,z):
    n=len(x)
    gap=n//2
    while gap>0:
        for i in range(gap,n):
            temp=x[i]
            j=i
            if z=="ascending":
                while j>=gap and x[j-gap]>temp:
                    x[j]=x[j-gap]
                    j-=gap
            elif z=="descending":
                while j>=gap and x[j-gap]<temp:
                    x[j]=x[j-gap]
                    j-=gap
            x[j]=temp
        gap//=2
    return x
