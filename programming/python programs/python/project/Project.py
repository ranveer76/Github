from tkinter import *
import tkinter.font as font
from subproject import *
def program():

    rt = Tk()
    rt.title("tkinter")
    myFont = font.Font(family="arial", size = 20, weight = "bold")

    rt.columnconfigure(0,weight=1)
    rt.columnconfigure(1,weight=1)


    l1=Label(rt,text='Input:')
    l1.grid(column=0,row=1)

    l2=Entry()
    l2.grid(column=1,row=1)


    l3=Label(rt,text='Size:')
    l3.grid(column=0,row=2)

    size=IntVar()
    l4=Entry(rt,textvariable=size)
    l4.grid(column=1,row=2)



    OPT_label=Label(rt,text='Options 1:')
    OPT_label.grid(column=0,row=3)
    OPT=IntVar()

    radm=Radiobutton(rt,text='Horizontal',padx=20,variable=OPT,value=0)
    radf=Radiobutton(rt,text='Vertical',padx=20,variable=OPT,value=1)

    radm.grid(column=0,row=4)
    radf.grid(column=1,row=4)

    OPT_1=Label(rt,text='Options 2:')
    OPT_1.grid(column=0,row=5)
    OPT1=IntVar()

    ra1=Radiobutton(rt,text='Uppercase',padx=20,variable=OPT1,value=0)
    ra2=Radiobutton(rt,text='Lowercase',padx=20,variable=OPT1,value=1)
    ra3=Radiobutton(rt,text='Same',padx=20,variable=OPT1,value=2)
    
    ra1.grid(column=0,row=6)
    ra2.grid(column=1,row=6)
    ra3.grid(column=2,row=6)

    OPT_2=Label(rt,text='Options 2:')
    OPT_2.grid(column=0,row=7)
    OPT2=IntVar()

    rd1=Radiobutton(rt,text='Desired Alphabet',padx=20,variable=OPT2,value=0)
    rd2=Radiobutton(rt,text='Vowels',padx=20,variable=OPT2,value=1)
    rd3=Radiobutton(rt,text='Print all',padx=20,variable=OPT2,value=2)

    rd1.grid(column=0,row=8)
    rd2.grid(column=1,row=8)
    rd3.grid(column=2,row=8)


    def get_1():
        x1=l2.get()
        x2=OPT.get()
        x3=OPT1.get()
        x4=OPT2.get()
        x5=size.get()
        x6=l6.get()

        return (x1),(x2),(x3),(x4),(x5),(x6)
    def get_2():
        a1=list(get_1())
        run(a1)
        return
    l5=Label(rt,text='enter desired alphabet:')
    l5.grid(column=0,row=9)
     
    l6=Entry()
    l6.grid(column=1,row=9)

    
    submit=Button(rt,text='Submit',command=get_2)
    submit.grid(column=0,row=10,columnspan=2)

    rt.mainloop()
program()
