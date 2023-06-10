import tkinter as tk
from PIL import Image, ImageTk

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
    elif value == '<-':
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

def calculator():
    w = tk.Tk()
    w.geometry("740x500+600+300")
    w.title("Calculator")
    background_image = Image.open("img/back.jpeg")
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(w, image=background_photo)
    background_label.pack()
    background_label.image = background_photo
    global x1, x2, txt
    x1 = tk.StringVar()
    x2 = tk.StringVar()

    entry_frame = tk.Frame(w)
    entry_frame.pack(pady=10)

    x = tk.Entry(entry_frame, textvariable=x2, justify="right", bd=3, bg="white", fg="black",
                 font=("Arial", 20), relief="sunken", highlightcolor="red",
                 highlightthickness=1, highlightbackground="red",
                 state="normal", cursor="arrow", takefocus=False)
    x.pack(expand=True, fill='both')

    txt = tk.Label(w, text="", width=20, justify="right", anchor="e",
                   bg="white", fg="black", font=("Arial", 20), relief="sunken", bd=3,
                   highlightcolor="red", highlightthickness=1, highlightbackground="red",
                   padx=5, pady=5, state="normal", cursor="arrow",
                   wraplength=1000, takefocus=False, activebackground="white")
    txt.pack(pady=10)

    buttons_frame = tk.Frame(w)
    buttons_frame.pack()

    buttons = [
        ('1', 2, 10), ('2', 2, 110), ('3', 2, 210), ('+', 2, 310),
        ('4', 3, 10), ('5', 3, 110), ('6', 3, 210), ('-', 3, 310),
        ('7', 4, 10), ('8', 4, 110), ('9', 4, 210), ('*', 4, 310),
        ('0', 5, 10), ('.', 5, 110), ('=', 5, 210), ('/', 5, 310),
        ('C', 6, 10), ('(', 6, 110), (')', 6, 210), ('<-', 6, 310)
    ]

    for button_row in buttons:
        value, row, col = button_row
        button = tk.Button(buttons_frame, text=value, command=lambda v=value: handle_button_click(v), width=10,
                           bg="white", fg="black", bd=3, font=("Arial", 20),
                           relief="raised", highlightcolor="red",
                           highlightthickness=1, highlightbackground="red",
                           padx=2, pady=2, state="normal", cursor="arrow",
                           takefocus=False,
                           activebackground="white")
        button.grid(row=row, column=col, padx=5, pady=5)

    
    w.bind('<Key>', handle_key_press)
    w.mainloop()

calculator()
