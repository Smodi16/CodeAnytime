from Tkinter import*


def btnclick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_Input.set("")

def btnEqualsInput():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=""

cal=Tk()
cal.title("Calculator")
operator=""
text_Input=StringVar()

txtDisplay=Entry(cal,font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,
                 bg="#F0E68C",justify='right').grid(columnspan=4)

btn7=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="7",
            bg="#F0E68C",command=lambda:btnclick(7)).grid(row=1,column=0)
btn8=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="8",
            bg="#F0E68C",command=lambda:btnclick(8)).grid(row=1,column=1)
btn9=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="9",
            bg="#F0E68C",command=lambda:btnclick(9)).grid(row=1,column=2)
Addition=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="+",
            bg="#F0E68C",command=lambda:btnclick("+")).grid(row=1,column=3)
#================================================================================
btn4=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="4",
            bg="#F0E68C",command=lambda:btnclick(4)).grid(row=2,column=0)
btn5=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="5",
            bg="#F0E68C",command=lambda:btnclick(5)).grid(row=2,column=1)
btn6=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="6",
            bg="#F0E68C",command=lambda:btnclick(6)).grid(row=2,column=2)
Subtraction=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="-",
            bg="#F0E68C",command=lambda:btnclick("-")).grid(row=2,column=3)
#=================================================================================
btn1=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="1",
            bg="#F0E68C",command=lambda:btnclick(1)).grid(row=3,column=0)
btn2=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="2",
            bg="#F0E68C",command=lambda:btnclick(2)).grid(row=3,column=1)
btn3=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="3",
            bg="#F0E68C",command=lambda:btnclick(3)).grid(row=3,column=2)
Multiply=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="*",
            bg="#F0E68C",command=lambda:btnclick("*")).grid(row=3,column=3)
#=================================================================================
btn0=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="0",
            bg="#F0E68C",command=lambda:btnclick(0)).grid(row=4,column=0)
btnClear=Button(cal,padx=16,pady=16,bd=8,fg="#8B8682",font=('arial',20,'bold'),text="C",
            bg="#F0E68C",command=btnClearDisplay).grid(row=4,column=1)
btnEquals=Button(cal,padx=16,pady=16,bd=8,fg="#8B8682",font=('arial',20,'bold'),text="=",
            bg="#F0E68C",command=btnEqualsInput).grid(row=4,column=2)
Division=Button(cal,padx=16,pady=16,bd=8,fg="black",font=('arial',20,'bold'),text="/",
            bg="#F0E68C",command=lambda:btnclick("/")).grid(row=4,column=3)
#=================================================================================



cal.mainloop()












