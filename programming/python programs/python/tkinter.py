from tkinter import *
import tkinter.font as font
r = Tk()
r.title("tkinter")
myFont = font.Font(family="arial", size = 20, weight = "bold")
def clickYes():
    myLabel1 = Label(r,text = "thanks for using python")
    myLabel1.pack()
def clickNo():
    myLabel2 = Label(r,text = "D:\Free Fire_2020-09-28-09-36-46.mp4")
    myLabel2.pack()
myButton1 = Button(r,text = "Yes",padx=30, pady=15, bg = "red", fg ="white", command = clickYes)
myButton1["font"] = myFont
myButton1.pack()
myButton2 = Button(r,text ="No",padx=35, pady=15, bg = "blue", fg ="white", command = clickNo)
myButton2["font"] = myFont
myButton2.pack()
r.mainloop()
