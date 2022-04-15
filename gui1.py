from tkinter import *

from tkinter.messagebox import *



def BMI():

   

    height=float(heightTxt.get())

    

    weight=float(weightTxt.get())

    
    bmi = (weight *0.45)/((height *0.02)**2)

   

    showinfo('BMI','BMI is {:2f}'.format(bmi))

    

    heightTxt.set('')

    weightTxt.set('')


root=Tk()



heightTxt = StringVar()

weightTxt = StringVar()

nameTxt= StringVar()

ageTxt = StringVar()




Label(root,text='Enter your Name : ').grid(row=0,column=0)

Entry(root,textvariable=nameTxt).grid(row=0, column=1)



Label(root,text='Enter your Age: ').grid(row=1,column=0)

Entry(root,textvariable=ageTxt).grid(row=1, column=1)




Label(root,text='Enter your height: ').grid(row=2,column=0)

Entry(root,textvariable=heightTxt).grid(row=2, column=1)



Label(root,text='Enter your weight: ').grid(row=3,column=0)

Entry(root,textvariable=weightTxt).grid(row=3, column=1)




Button(root,text='Compute BMI', command=BMI, ).grid(row=4,column=0,columnspan=2)


root.mainloop()