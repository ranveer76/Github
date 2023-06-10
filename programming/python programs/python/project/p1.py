from p import *
import pyautogui as pg
from time import sleep
def pr(inp1):
    global x2,ro,co,oup
    for co in range(inp1):
        if (d[x2](ro,co,inp1)):
            pg.typewrite('*')
        else:
            pg.typewrite(' ')
def sp(inp1):
    for co in range(inp1//2):
        pg.typewrite(' ')



while True:
    tinp=int(input('Enter: 1 for horizontal pattern.\n2 for vertical.\nEnter Any No. to exit:\n'))
    if tinp<1 or tinp>2:
        print('Thanks for using this program')
        break
    inp=input('\nEnter input: ')
    inp1=int(input('\nEnter size: '))
    le=len(inp)
    x9=int(input('\nEnter: 1 For Lower case.\n2 For Upper case.\n'))
    ti=int(input('\nEnter: 1 For Desired no.\n2 For Vowels.\n3 For all.\n'))
    d={'A':A,'B':B,'C':C,'D':D,'E':E,'F':F,'G':G,'H':H,'I':I,'J':J,'K':K,'L':L,'M':M,'N':N,'O':O,'P':P,'Q':Q,'R':R,'S':S,'T':T,'U':U,'V':V,'W':W,'X':X,'Y':Y,'Z':Z,'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'p':p,'q':q,'r':r,'s':s,'t':t,'u':u,'v':v,'w':w,'x':x,'y':y,'z':z}

    if x9==1:
        inp=inp.lower()
    elif x9==2:
        inp=inp.upper()
    if ti==1:
        x3==input('\nEnter desired alphabet: ')[0]
    elif ti==2:
        d={'A':A,'E':E,'I':I,'O':O,'U':U,'a':a,'e':e,'i':i,'o':o,'u':u}
    sleep(3)

    if tinp==1:
        inp=inp.split()
        for oupx in inp:
            for ro in range(inp1):
                for oup in oupx:
                    if ti!=4:
                        x3=oup
                    if oup in d and x3==oup:
                        x2=oup
                        sp(inp1)
                        pr(inp1)
                pg.press('enter')
            pg.press('enter')
    elif tinp==2:
        for oup in range(le):
            pg.press('enter')
            for ro in range(inp1):
                if ti!=4:
                    x3=inp[oup]
                if inp[oup] in d and x3==inp[oup]:
                    x2=inp[oup]
                    pr(inp1)
                pg.press('enter')

