import tkinter as tk
import random as rd
from array_importer import importer,print_list

def import_list():
    t=print_list()
    return t
def sort(x,y,z):
    x1=importer(x)
    n=[]
    for i in range(len(y)):
        n.append(int(y[i]))
    x=x1(n,z)
    list_sort=[]
    for i in x:
        list_sort.append(str(mylist[int(i)]))
    
    listbox.delete(0,tk.END)
    for item in list_sort:
        listbox.insert("end",item)
    label['text']="Sorted list is: "
    for i in range(len(list_sort)):
        label['text']+=list_sort[int(i)]+" "

def random():
    rd.shuffle(listx)
    myl=[]
    for i in listx:
        myl.append(str(mylist[int(i)]))
    listbox.delete(0,tk.END)
    for item in myl:
       listbox.insert("end",item) 
    label['text']="Random list is: "
    for i in myl:
        label['text']+=i+" "

def reset():
    listbox.delete(0,tk.END)
    for item in original_mylist:
        listbox.insert("end",mylist[int(item)])
    label['text']="Original list is: "
    for i in original_mylist:
        label['text']+=mylist[int(i)]+" "
    
root = tk.Tk()

# Create a list of 5 items
mylist={
    1:"one", 2:"two", 3:"three", 4:"four", 5:"five"
}
listx=list(mylist.keys())
rd.shuffle(listx)

original_mylist=tuple(listx)
# Create a constant variable as a list




mylist1=["ascending","descending"]
mylist2=import_list()
x1=tk.StringVar(root)
x1.set(mylist1[0])
x2=tk.OptionMenu(root,x1,*mylist1)
x2.pack(side=tk.TOP)

y1=tk.StringVar(root)
y1.set(mylist2[0])
y2=tk.OptionMenu(root,y1,*mylist2)
y2.pack(side=tk.TOP)
# Create a listbox widget
listbox = tk.Listbox(root, width=50, height=6,
                     selectmode=tk.SINGLE, bg='yellow', fg='red',
                     font=('times', 15, 'bold'), activestyle='dotbox',
                      justify=tk.CENTER,cursor='heart', 
                     relief=tk.RAISED, bd=5, highlightcolor='red',
                     highlightthickness=5, highlightbackground='yellow',
                     takefocus=True, selectbackground='violet',
                     selectforeground='white')
tk.Button(root, text='Sort',command=lambda:sort(y1.get(),listx,x1.get()),
          bg='green', fg='white', font=('times', 15, 'bold')).pack(side=tk.TOP)
tk.Button(root, text='Random',command=random, bg='orange',
            fg='white', font=('times', 15, 'bold')).pack(side=tk.TOP)
tk.Button(root, text='Reset',command=reset,
            bg='blue', fg='white', font=('times', 15, 'bold')).pack(side=tk.TOP)           
tk.Button(root, text='Exit Application',
          command=root.destroy, bg='red',
            fg='white', font=('times', 15, 'bold')).pack(side=tk.BOTTOM)
# Add the list items to the listbox
for item in listx:
   listbox.insert("end", mylist[item])
#checking changes
label = tk.Label(root, text='Listbox with scrollbar and items',
                    font=('times', 20, 'bold'))
label.pack(side=tk.TOP)
label = tk.Label(root, text="",
                    font=('times', 20, 'bold'))
for i in listx:
    label["text"]+=str(mylist[i])+" "

label.pack(side=tk.TOP)


# Create a vertical scrollbar to the right of the listbox
yscroll = tk.Scrollbar(command=listbox.yview, orient=tk.VERTICAL)
listbox.configure(yscrollcommand=yscroll.set)

# Pack everything into the root
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, padx=10, pady=10)
yscroll.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()

# Path: array_3.py
# Compare this snippet from array_importer.py:

# def importer(x):
#     if x=="bubble_sort":
#         from sorting.bubble_sort import sort
#     elif x=="insertion_sort":
#         from sorting.insertion_sort import insertion_sort as sort
#     elif x=="selection_sort":
#         from sorting.selection_sort import selection_sort as sort
#     elif x=="sequence_sort":
#         from sorting.sequence_sort import sequence_sort as sort
#     elif x=="merge_sort":
#         from sorting.merge_sort import merge_sort as sort
#     elif x=="quick_sort":
#         from sorting.quick_sort import quick_sort as sort
#     elif x=="heap_sort":
#         from sorting.heap_sort import heap_sort as sort
#     elif x=="counting_sort":
#         from sorting.counting_sort import counting_sort as sort
#     elif x=="radix_sort":
#         from sorting.radix_sort import radix_sort as sort
#     elif x=="bucket_sort":
#         from sorting.bucket_sort import bucket_sort as sort
#     else:
#         from sorting.shell_sort import shell_sort as sort
#     return sort
# def print_list():
#     t=[
#     "bubble_sort","selection_sort","insertion_sort",
#    "merge_sort","quick_sort","heap_sort",
#    "counting_sort","radix_sort","bucket_sort",
#    "shell_sort","sequence_sort"
#    ]
#     return t
#