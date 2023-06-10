def o0():
    if (x==0 or j==0 or x==K-1 or j==K-3)and(not(((x==0 or x==K-1)and(j==0 or j==K-3))or j>K-3)):
        print('*',end='')
    else:
        print(' ',end='')
        
def o1():
    global to
    if (j==to or j==K//2 or x==K-1):
        print('*',end='')
        to-=1
    else:
        print(' ',end='')
def o2():
    global xo
    if ((x==0 or x==K-1 or j==xo or(x==1 and j==1))and(not((x==0 and j==1)or((x==0)and(j==0 or j==K-1))or(x==K-1 and j==0)))):
        print('*',end='')
        if j==xo:
            xo-=1
    else:
        print(' ',end='')
def o3():
    if (x==0 or x==K-1 or x==K//2 or j==K-1)and(not((x==0 or x==K-1 or x==K//2)and(j==0 or j==K-1))):
        print('*',end='')
    else:
        print(' ',end='')
def o4():
    global ox
    if (j==K-2 or (j==K-ox and x<=K//2)or x==K//2)and(not(j<1)):
        print('*',end='')
        ox+=1
    else:
        print(' ',end='')
def o5():
    if (x==0 or x==K-1 or x== K//2 or j==0 or(j==K-1 and x>K//2))and(not(((x==K//2 or x==K-1)and(j==K-1))or((x in range(((K//2)+1),K-1)) and(j==0)))):
        print('*',end='')
    else:
        print(' ',end='')
def o6():
    if (x==0 or x==K-1 or x== K//2 or j==0 or(j==K-1 and x>K//2))and(not((x==K//2 and j==K-1)or((x==0 or x==K-1)and(j==0 or j==K-1)))):
        print('*',end='')
    else:
        print(' ',end='')
def o7():
    global xo
    if (x==0 or j==xo):
        print('*',end='')
        if j==xo:
            xo-=1
    else:
        print(' ',end='')
def o8():
    if (x==0 or j==0 or x==K//2 or j==K-1 or x==K-1)and(not((x==0 or x==K//2 or x==K-1)and(j==0 or j==K-1))):
        print('*',end='')
    else:
        print(' ',end='')
def o9():
    if (x==0 or (j==0 and (x<=K//2 or x==K-2)) or x==K//2 or j==K-1 or x==K-1)and(not(((x==0 or x==K//2 or x==K-1)and(j==0))or((x==0 or x==K-1)and(j==K-1)))):
        print('*',end='')
    else:
        print(' ',end='')

n=input()
D=int(input())

K=int(input())
for i in str(n):
    if D==1:
        if int(i)%2==0:
            continue
    elif D==2:
        if((int(i)%2)==0):
            continue
    elif D==3:
        Ap=1
        for x in range(1,(int(i))):
            if int(i)%x==0:
                Ap+=1
        if Ap!=2:
            continue
    elif D==4:
        pass
    else:
        break
    to=(K//2)-1
    xo=K-1
    ox=2
    for x in range(K):
        for j in range(K):
            i=int(i)
            if i==1:
                o1()
            elif i==0:
                o0()
            elif i==2:
                o2()
            elif i==3:
                o3()
            elif i==4:
                o4()
            elif i==5:
                o5()
            elif i==6:
                o6()
            elif i==7:
                o7()
            elif i==8:
                o8()
            else:
                o9()
        print()
input('any key to exit')

