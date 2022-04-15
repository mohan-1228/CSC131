from tkinter import *

master  = Tk()
master.title("GUIs drawing goemetric shapes")

#creating a simple canvas.
canvas = Canvas(master,height = "300",width = "300")

canvas.grid(row =1 , columnspan = 10)
v = IntVar()
var1 = IntVar()

#this function will call on change of radio button


# draw rectangle function
def change():
    
    if v.get() ==1 :
        if(var1.get()==0):
            canvas.create_rectangle(50,50,250,250)
        else:
            canvas.create_rectangle(50,50,250,250,fill="red")
    elif v.get() ==2 :
        if(var1.get()==0):
            canvas.create_oval(100,100,50,50)
        else:
            canvas.create_oval(50,100,250,200,fill="yellow")
def clearAll():
    canvas.delete("all")
    v.set(False)  # deselect check radio button
    var1.set(False)  # deselect check radio button
    
  
Radiobutton(master,text="Rectangle",padx = 20,variable=v,command=change,value=1).grid(row=2, column=1, sticky=W, pady=4)
Radiobutton(master,text="Oval",padx = 20,variable=v, command=change,value=2).grid(row=2, column=2, sticky=W, pady=4)

Checkbutton(master, text="Filled", variable=var1,command=change).grid(row=2, column=3, sticky=W, pady=4)

Button(master, text='Clear',command=clearAll).grid(row=2, column=4, sticky=W, pady=4)

mainloop()
