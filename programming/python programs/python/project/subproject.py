from A_to_Z import *
import pyautogui as pg
from time import sleep


def pr(inp1,x2,ro,d1):
    global oup
    
    for co in range(inp1):
        if (d1[x2](ro,co,inp1)):
            pg.typewrite('*')
        else:
            pg.typewrite(' ')
    return

def sp(inp1):
    for co in range(inp1//2):
        pg.typewrite(' ')
    return

def hori(inp,ti,le,inp1,x3):
    d1={'A':A,'B':B,'C':C,'D':D,'E':E,'F':F,'G':G,'H':H,'I':I,'J':J,'K':K,'L':L,'M':M,'N':N,'O':O,'P':P,'Q':Q,'R':R,'S':S,'T':T,'U':U,'V':V,'W':W,'X':X,'Y':Y,'Z':Z,'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'p':p,'q':q,'r':r,'s':s,'t':t,'u':u,'v':v,'w':w,'x':x,'y':y,'z':z}

    if ti==1:
        d1={'A':A,'E':E,'I':I,'O':O,'U':U,'a':a,'e':e,'i':i,'o':o,'u':u}
    inp=inp.split()
    for oupx in inp:
        for ro in range(inp1):
            for oup in oupx:
                if ti!=0:
                    x3=oup
                if oup in d1 and x3==oup:
                    x2=oup
                    sp(inp1)
                    pr(inp1,x2,ro,d1)
            pg.press('enter')
        pg.press('enter')
    return

def ver(inp,ti,le,inp1,x3):
    d1={'A':A,'B':B,'C':C,'D':D,'E':E,'F':F,'G':G,'H':H,'I':I,'J':J,'K':K,'L':L,'M':M,'N':N,'O':O,'P':P,'Q':Q,'R':R,'S':S,'T':T,'U':U,'V':V,'W':W,'X':X,'Y':Y,'Z':Z,'a':a,'b':b,'c':c,'d':d,'e':e,'f':f,'g':g,'h':h,'i':i,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'p':p,'q':q,'r':r,'s':s,'t':t,'u':u,'v':v,'w':w,'x':x,'y':y,'z':z}

    if ti==1:
        d1={'A':A,'E':E,'I':I,'O':O,'U':U,'a':a,'e':e,'i':i,'o':o,'u':u}
    for oup in range(le):
        pg.press('enter')
    for ro in range(inp1):
        if ti!=0:
            x3=inp[oup]
        if inp[oup] in d1 and x3==inp[oup]:
            x2=inp[oup]
            pr(inp1,x2,ro,d1)
        pg.press('enter')
    return

def run(a1):
    global d1
    inp=str(a1[0])
    tinp=int(a1[1])
    x9=int(a1[2])
    ti=int(a1[3])
    le=len(inp)
    inp1=int(a1[4])
    de=[hori,ver]
    
    if x9==1:
        inp=inp.lower()
    elif x9==0:
        inp=inp.upper()
    x3=inp
    if ti==0:
        x3=str(a1[5])[0]
    sleep(3)
    de[tinp](inp,ti,le,inp1,x3)

