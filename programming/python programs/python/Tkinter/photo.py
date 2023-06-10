from tkinter import *
from PIL import Image, ImageTk

def resize(event):
    w, h = event.width, event.height
    image = Image.open('img/back.jpeg')
    image = image.resize((w, h), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, image=photo, anchor=NW)
    canvas.image = photo
    
def update_display():
    try:
        x2.set(eval(x1.get()))
    except:
        pass
    txt['text'] = x1.get()

def handle_button_click(value):
    if value == '=':
        handle_equal_click()
    elif value == 'C':
        handle_clear_click()
    elif value == '←':
        handle_backspace_click()
    else:
        x1.set(x1.get() + str(value))
        update_display()

def handle_equal_click():
    try:
        result = eval(x1.get())
        x1.set(str(result))
        txt['text'] = x1.get()
    except:
        x1.set('Error')
        txt['text'] = 'Error'

def handle_clear_click():
    x1.set('')
    x2.set('')
    txt['text'] = ''

def handle_backspace_click():
    i = x1.get()
    x1.set(i[:-1])
    update_display()

def handle_key_press(event):
    key = event.char
    if key.isdigit():
        handle_button_click(key)
    elif key == '+':
        handle_button_click('+')
    elif key == '-':
        handle_button_click('-')
    elif key == '*':
        handle_button_click('*')
    elif key == '/':
        handle_button_click('/')
    elif key == '.':
        handle_button_click('.')
    elif key == '(':
        handle_button_click('(')
    elif key == ')':
        handle_button_click(')')
    elif key == '\r':
        handle_equal_click()
    elif key == '\x08':
        handle_backspace_click()
    elif key == '\x1b':
        handle_clear_click()

def handle_button_hover(event):
    event.widget['bg'] = 'red'
def handle_button_hover_leave(event):
    event.widget['bg'] = 'white'

def calculator():
    w = app
    global x1, x2, txt, x
    x1 = StringVar()
    x2 = StringVar()

    entry_frame = Frame(w)
    entry_frame.grid(row=0, column=0, sticky='nsew'
                     )

    x = Entry(entry_frame, textvariable=x2, justify="right", bd=3, bg="white", fg="black",
                 font=("Arial", 20), relief="sunken", highlightcolor="red",
                 highlightthickness=1, highlightbackground="red",
                 state="normal", cursor="arrow", takefocus=False)
    x.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

    txt = Label(w, text="", width=20, justify="right", anchor="e",
                   bg="white", fg="black", font=("Arial", 20), relief="sunken", bd=3,
                   highlightcolor="red", highlightthickness=1, highlightbackground="red",
                   padx=5, pady=5, state="normal", cursor="arrow",
                   wraplength=1000, takefocus=False, activebackground="white")
    txt.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

    buttons_frame = Frame(w)
    buttons_frame.grid(row=1, column=0
                       )
    # buttons_frame.configure(bg='black')

    buttons = [
        ('1', 2, 10), ('2', 2, 110), ('3', 2, 210), ('+', 2, 310),
        ('4', 3, 10), ('5', 3, 110), ('6', 3, 210), ('-', 3, 310),
        ('7', 4, 10), ('8', 4, 110), ('9', 4, 210), ('*', 4, 310),
        ('0', 5, 10), ('.', 5, 110), ('=', 5, 210), ('/', 5, 310),
        ('C', 6, 10), ('(', 6, 110), (')', 6, 210), ('←', 6, 310)    ]

    for button_row in buttons:
        value, row, col = button_row
        button = Button(buttons_frame, text=value, command=lambda v=value: handle_button_click(v), width=10,
                           bg="white", fg="black", bd=3, font=("Arial", 20),
                           relief="raised", highlightcolor="red",
                           highlightthickness=1, highlightbackground="red",
                           padx=2, pady=2, state="normal", cursor="hand2",
                           takefocus=False,
                           activebackground="red", activeforeground="white")
        button.grid(row=row, column=col, padx=5, pady=5)
        button.bind('<Enter>', handle_button_hover)
        button.bind('<Leave>', handle_button_hover_leave)
    w.bind('<Key>', handle_key_press)


app=Tk()
app.title('Image Resizer')

canvas=Canvas(app)
image=ImageTk.PhotoImage(Image.open('img/back.jpeg'))
canvas.create_image(0,0, anchor=NW, image=image)
canvas.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10, ipadx=10, ipady=10,
            )
calculator()
app.bind('<Configure>', resize)
app.mainloop()