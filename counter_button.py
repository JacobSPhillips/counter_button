from tkinter import *

count = 0


def click():
    global count
    count += 1
    print(count)


window = Tk()

button = Button(window,
                text="Click me!",
                command=click,
                font=("Comic Sans", 30),
                fg='#00ff00',
                bg='black',
                activebackground='black',
                activeforeground="#00ff00",
                state=ACTIVE,
                )
button.pack()

window.mainloop()
