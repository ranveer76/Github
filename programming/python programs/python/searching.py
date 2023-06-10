from sorting import *

def lin(a,x):#linear search
    t=1
    upp=len(a)

    if x not in a:
        t=(' is not in')
        return False,a,t
    else:
        for i in range(upp):
            if a[i]==x:
                return(True,i,t)#return index no. and no. of time loop run
                break
            t+=1

def bn(a,x):#binary search
    print('for bubble sort enter: 1\n'+'for insertion enter: 2\n'+'for selection enter: 3\n'+'for merge sort enter: 4')
    x1=int(input())#select sorting method
    print()
    
    t=1
    l1=[bubblesort,insertionsort,selectionsort,m]
    l2=['Bubble','Insertion','Selection','Merge']
    
    a,f=l1[x1-1](a,t)
    
    print(l2[x1-1],'Sorted list:\n',a,'\n')
    low=0
    upp=len(a)
    
    print()
    if x in a:
        while low<upp:
            mid=(low+upp)//2
            if a[mid]==x:
                return(True,mid,t)#return index no. and no. of time loop run
                break
            elif a[mid]>x:
                upp=mid
            elif a[mid]<x:
                low=mid
            t+=1
    else:
        t=(' is not in')
        return False,a,t
