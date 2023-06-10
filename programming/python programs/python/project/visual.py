from tkinter import *
from tkcalendar import DateEntry
import tkinter.font as font

r = Tk()
r.title("tkinter")
myFont = font.Font(family="arial", size = 20, weight = "bold")

r.columnconfigure(0,weight=1)
r.columnconfigure(1,weight=1)

label1=Label(r,text='Input:')
label1.grid(column=0,row=1)

label2=Entry()
label2.grid(column=1,row=1)

glabel=Label(r,text='Gender:')
glabel.grid(column=0,row=2)

gender=IntVar()

radm=Radiobutton(r,text='male',padx=20,variable=gender,value=0)
radf=Radiobutton(r,text='female',padx=20,variable=gender,value=1)

radm.grid(column=0,row=3)
radf.grid(column=1,row=3)

flight=Label(r,text='Options:')
flight.grid(column=0,row=4)

first=IntVar()
first_c=Checkbutton(r,text='First Class',variable=first)
first_c.grid(column=1,row=5)

firstm=IntVar()
first_m=Checkbutton(r,text='Meal',variable=firstm)
first_m.grid(column=1,row=6)

llabel=Label(r,text='lugagge:')
llabel.grid(column=0,row=7)

l_weigh=Scale(r,from_=0,to=200,orient=HORIZONTAL)
l_weigh.grid(column=0,row=8,columnspan=2,sticky=W+E)

dest=Label(r,text='Destination')
dest.grid(column=0,row=9)

destl=['moscow','india','australia','canada']
destv=StringVar(r)
destv.set('Select a Destination')

destm=OptionMenu(r,destv,*destl)
destm.grid(column=0,row=10,columnspan=2,sticky=W+E)

dep=Label(r,text='Departure Date')
dep.grid(column=0,row=11)

depD=DateEntry(r,selectmode='day',date_pattern='yyyy-mm-dd',width=10)
depD.grid(column=0,row=12)
depD._top_cal.overrideredirect(False)

def get_flight():
    if label2.get()!='' and l_weigh.get()>0:
        print('Name: ',label2.get())
        print('Gender: ',end='')
        if (gender.get())==0:
            print('Male')
        elif (gender.get())==1:
            print('Female')
        print('Class:',end=' ')
        if first.get()==1:
            print('First Class')
        else:
            print('No First Class')
        print('Additonal:',end=' ')
        if firstm.get()==1:
            print('Meal')
        else:
            print('No Meal')
        print('Luggage Weight',l_weigh.get())
        print('Destination:',destv.get())
        print('Destination Date:',depD.get())
    return

submit=Button(r,text='Submit',command=get_flight)
submit.grid(column=0,row=21,columnspan=2)

r.mainloop()
