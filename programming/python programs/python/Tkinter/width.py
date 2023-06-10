import tkinter as tk

def get_screen_width(event):
    screen_width = event.width
    w=screen_width
    label['text'] = str(w)
    get_screen_height(event)
    
def get_screen_height(event):
    screen_height = event.height
    h=screen_height
    label1['text'] = str(h)



root = tk.Tk()
root.title("Get Screen Width and Height")
root.geometry("1920x1080+0+0")
w= root.winfo_screenwidth()
h= root.winfo_screenheight()
frame=root
# frame=tk.Frame(root, width=w, height=h)
# frame.pack()
tk.Label(frame, text="Resize the window", bg="yellow",
            fg="red", font="Arial 20").grid(row=0, column=0,columnspan=2,
                                            padx=10, pady=10, ipadx=10, ipady=10)
tk.Label(frame, text="Screen Width:", bg="yellow",
         fg="red", font="Arial 20").grid(row=1, column=0, sticky="nsew",
                                         padx=10, pady=10, ipadx=10, ipady=10)

tk.Label(frame, text="Screen Height:", bg="yellow",
         fg="red", font="Arial 20").grid(row=1, column=1, sticky="nsew",
                                         padx=10, pady=10, ipadx=10, ipady=10)

label = tk.Label(frame, text="Screen Width: ", bg="white",
                 fg="black", font="Arial 16")
label.grid(row=2, column=0, sticky="nsew", padx=10, pady=10, ipadx=10, ipady=10)

label1 = tk.Label(frame, text="Screen Height: ", bg="white",
                    fg="black", font="Arial 16")
label1.grid(row=2, column=1, sticky="nsew", padx=10, pady=10, ipadx=10, ipady=10)

# Bind the <Configure> event to the get_screen_width function
root.bind("<Configure>", get_screen_width)

root.mainloop()



