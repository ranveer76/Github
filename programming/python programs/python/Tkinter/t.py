from tkinter import *
from PIL import Image, ImageTk

def resize_image(event):
    global resized_image, resized_photo
    w, h = event.width, event.height
    resized_image = original_image.resize((w, h), Image.ANTIALIAS)
    resized_photo = ImageTk.PhotoImage(resized_image)
    background_label.config(image=resized_photo)

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
    global original_image,background_label,app
    app = Tk()
    app.title('Image Resizer')
    original_image = Image.open('img/back.jpeg')
    resized_image = original_image.copy()
    resized_photo = ImageTk.PhotoImage(resized_image)

    background_label = Label(app, image=resized_photo)
    background_label.place(relx=0, rely=0, relwidth=1, relheight=1)
    global x1, x2, txt, x
    x1 = StringVar()
    x2 = StringVar()
    w = app
    w.rowconfigure(0, weight=1)
    w.rowconfigure(1, weight=1)
    w.rowconfigure(2, weight=1)
    w.columnconfigure(0, weight=1)

    # entry_frame = Frame(w)
    # entry_frame.grid(row=0, column=0, sticky='nsew')

    x = Entry(w, textvariable=x2, justify="right", bg="white", fg="black",
                 font=("Arial", 20), relief="sunken", highlightcolor="red",
                 highlightthickness=1, highlightbackground="red",
                 state="normal", cursor="arrow", takefocus=False)
    x.grid(row=0, column=0, pady=10)

    txt = Label(w, text="", width=20, justify="right", anchor="e",
                   bg="white", fg="black", font=("Arial", 20), relief="sunken", bd=3,
                   highlightcolor="red", highlightthickness=1, highlightbackground="red",
                   padx=5, pady=5, state="normal", cursor="arrow",
                   wraplength=1000, takefocus=False, activebackground="white")
    txt.grid(row=1, column=0, pady=10)

    buttons_frame = Frame(w, bg="black")
    buttons_frame.grid(row=2, column=0)
    buttons_frame.rowconfigure(0, weight=1)
    buttons_frame.rowconfigure(1, weight=1)
    buttons_frame.rowconfigure(2, weight=1)
    buttons_frame.rowconfigure(3, weight=1)
    buttons_frame.rowconfigure(4, weight=1)
    buttons_frame.columnconfigure(0, weight=1)
    buttons_frame.columnconfigure(1, weight=1)
    buttons_frame.columnconfigure(2, weight=1)
    buttons_frame.columnconfigure(3, weight=1)
    buttons = [
        ('1', 0, 0), ('2', 0, 1), ('3', 0, 2), ('+', 0, 3),
        ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('-', 1, 3),
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
        ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('/', 3, 3),
        ('C', 4, 0), ('(', 4, 1), (')', 4, 2), ('←', 4, 3)
    ]

    for button_row in buttons:
        value, row, col = button_row
        button = Button(buttons_frame, text=value, command=lambda v=value: handle_button_click(v), width=10,
                           bg="white", fg="black", bd=0, font=("Arial", 14),
                           relief="raised", highlightcolor="red",
                           highlightthickness=1, highlightbackground="red",
                            state="normal", cursor="hand2",
                           takefocus=False,
                           activebackground="red", activeforeground="white")
        button.grid(row=row, column=col, padx=5, pady=5)
        button.bind('<Enter>', handle_button_hover)
        button.bind('<Leave>', handle_button_hover_leave)
    w.bind('<Key>', handle_key_press)
    
    app.bind('<Configure>', resize_image)
    app.mainloop()

calculator()

