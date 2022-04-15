from tkinter import Tk,Button
from time import strftime,localtime
from tkinter.messagebox import showinfo
def clicked():
    time=strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n',localtime())

    print(time)
    showinfo(message=time)

root=Tk()
button=Button(root,text='Click Me',command=clicked)
button.pack()
root.mainloop()
