from tkinter import Tk, Entry, Text

def key_pressed(event):
    key = event.keysym
    message = ""

    if len(key) > 1:
        message = 'It is a non-alphanumeric key'
    elif 'a' <= key <= 'z':
        message = 'It is a lowercase letter.'
    elif 'A' <= key <= 'Z':
        message = 'It is an uppercase letter.'
    elif '0' <= key <= '9':
        message = 'It is a number.'

    text_widget.insert('end', message + '\n')

root = Tk()
root.title("tk")

entry_widget = Entry(root)
entry_widget.pack()

text_widget = Text(root)
text_widget.pack()

entry_widget.bind("<KeyPress>", key_pressed)

root.mainloop()
