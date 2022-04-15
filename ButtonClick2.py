from tkinter import Tk,Button
from time import strftime,localtime,gmtime
from tkinter.messagebox import showinfo
def clicked():
    time=strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n',localtime())
    time2=strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n',gmtime())
    print(time)
    print(time2)
    showinfo(message=time)
    showinfo(message=time2)

root=Tk()
button=Button(root,text='Click Me',command=clicked)
button.pack()
root.mainloop()
