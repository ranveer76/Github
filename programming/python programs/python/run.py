from searching import *
from sorting import *
import random

a=range(random.randint(20,150))

c=random.randint(5,20)#no.of elements in list
n=random.sample(a,c)#list

print('no.of elements in list:',c)
print('\nlist:\n',n)

x=random.choice(n)#element you want to search
print('\ninteger you want to search:\n',x)

print('\nfor Binary search enter: 1\n'+'for Linear search enter: 2')
x1=int(input())#select searching method

l1=[bn,lin]
l2=['Binary search','Linear search']

print('\nyou selected '+l2[x1-1]+':\n')

k,t=l1[x1-1](n,x)#get index no. of searched element and no. times loop run to search
print('index no. of integer you searched: ',k)
print()
print('no. of times searched: ',t)
input()
