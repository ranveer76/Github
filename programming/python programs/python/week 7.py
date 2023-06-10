from searching import *
from sorting import *

def search(List):
    
    search=int(input('no. you want to search: '))
    l1=[bn,lin]
    print('\nfor binary search enter: 1\nfor sequential search enter: 2\n')
    x1=int(input())
    a1=True
    a1,a,t=l1[x1-1](List,search)
    if a1 == True:
        print(search,'is on index no.',a)
        print('loop runned',t,'times.')
    else:
        print(str(search)+t,a)

def sort(a):
    l1=[bubblesort,insertionsort,selectionsort,m]
    l2=['Bubble','Insertion','Selection','Merge']
    t=1
    
    print('for bubble sort enter: 1\n'+'for insertion enter: 2\n'+'for selection enter: 3\n'+'for merge sort enter: 4')
    x1=int(input())#select sorting method
    print()
    a,t=l1[x1-1](a,t)
    print(l2[x1-1],'Sorted list:\n',a,'\n')
    print('loop runs',t,'times.')


List=[int(x) for x in input('list: ').split()]
pro=[search,sort]
pr=['Searching from','Sorting']
xc=int(input('for search enter: 1\nfor sort enter: 2\n'))
print('you are',pr[xc-1],'List.')
pro[xc-1](List)
