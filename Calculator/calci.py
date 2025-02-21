from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("644x900")
root.title("Calculator By Priyanshu Rai")
root.configure(bg='black')

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue ,borderwidth=5, relief=RIDGE, bg="lightyellow", font="lucida 50 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)



f = Frame(root, bg="cyan" ,borderwidth=3)
b = Button(f, text="9", padx=25, pady=10, font="lucida 28 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=25, pady=10, font="lucida 28 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)


b = Button(f, text="7", padx=25, pady=10, font="lucida 28 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
f.pack()






f = Frame(root, bg="cyan" ,borderwidth=3)
b = Button(f, text="6", padx=25, pady=10, font="lucida 28 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=25, pady=10, font="lucida 28 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)


b = Button(f, text="4", padx=25, pady=10, font="lucida 28 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
f.pack()





f = Frame(root, bg="cyan" ,borderwidth=3)
b = Button(f, text="3", padx=25, pady=10, font="lucida 28 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=25, pady=10, font="lucida 28 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)


b = Button(f, text="1", padx=25, pady=10, font="lucida 28 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
f.pack()




f = Frame(root, bg="cyan" ,borderwidth=3)
b = Button(f, text="0", padx=25, pady=10, font="lucida 28 bold")
b.pack(side=LEFT, padx=13, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="00", padx=15, pady=10, font="lucida 28 bold")
b.pack(side=LEFT, padx=20, pady=5)
b.bind("<Button-1>", click)


b = Button(f, text="C", padx=22, pady=10, bg="orange",font="lucida 28 bold")
b.pack(side=LEFT, padx=12, pady=5)
b.bind("<Button-1>", click)
f.pack()





f = Frame(root, bg="cyan" ,borderwidth=3)
b = Button(f, text="+", padx=25, pady=10, bg="orange",font="lucida 28 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=30, pady=5, bg="orange",font="lucida 32 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)


b = Button(f, text="*", padx=25, pady=10, bg="orange",font="lucida 28 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
f.pack()





f = Frame(root, bg="cyan" ,borderwidth=3)
b = Button(f, text="/", padx=25, pady=10, bg="orange",font="lucida 28 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=25, pady=10, bg="orange",font="lucida 28 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=25, pady=10, bg="orange",font="lucida 28 bold")
b.pack(side=LEFT, padx=15, pady=5)
b.bind("<Button-1>", click)
f.pack()

root.mainloop()
