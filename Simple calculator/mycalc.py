#  from tkinter import *
#  screen= Tk()

#  screen.mainloop()
from tkinter import *
import math
# from tkinter import messagebox
screen = Tk()

screen.title("bikal calculator")
screen.configure(bg='blue')
screen.maxsize(width=453,height=490)
screen.minsize(width=362,height=490)
screen.geometry=("362*488")
# def equal():
#     global operator
#     result=eval(operator)
# 	operator=str(result)
# 	tex.set(result)
	
def equal():
	global operator
	result=eval(operator)
	operator=str(result)
	tex.set(result)
    
	    # messagebox.showinfo('Notification','syntaxError')

def clear():
    global operator
    operator=''
    tex.set(operator )
def cmsin():
	global operator
	result=math.sin(eval(tex.get()))
	operator=str(result)
	tex.set(operator)

def cmcos():
	global operator
	result=math.cos(eval(tex.get()))
	operator=str(result)
	tex.set(operator)

def cmtan():
	global operator
	result=math.tan(eval(tex.get()))
	operator=str(result)
	tex.set(operator)

def cmlog():
	global operator
	result=math.log(eval(tex.get()))
	operator=str(result)
	tex.set(operator)

def cmsqrt():
	global operator
	result=math.sqrt (eval(tex.get()))
	operator=str(result)
	tex.set(operator)
def click(number):
    global operator
    operator+=str(number)
    tex.set(operator)
tex=StringVar()
operator=''
entry1=Entry(screen,bg="brown",font=('arial',20,"italic bold"),bd="30",justify='right',textvariable=tex)
entry1.grid(row=0,columnspan=4)
btn7=Button(screen,text='7',font=("arial",20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(7),activebackground='green')
btn7.grid(row=1,column=0)

btn8=Button(screen,text='8',font=("arial",20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(8),activebackground='green')
btn8.grid(row=1,column=1 )

btn9=Button(screen,text='9',font=("arial",20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(9),activebackground='green')
btn9.grid(row=1,column=2)

btnadd=Button(screen,text='+',font=("arial",20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click('+' ),activebackground='green')
btnadd.grid(row=1,column=3 )

btn4=Button(screen,text='4',font=("arial",20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(4),activebackground='green')
btn4.grid(row=2,column=0)

btn5=Button(screen,text='5',font=("arial",20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(5),activebackground='green')
btn5.grid(row=2,column=1 )

btn6=Button(screen,text='6',font=("arial",20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(6),activebackground='green')
btn6.grid(row=2,column=2)

btnsub=Button(screen,text='-',font=("arial",20,'italic bold'),bd=8,padx=18,pady=16,command=lambda:click('-'),activebackground='green')
btnsub.grid(row=2,column=3 )

btn1=Button(screen,text='1',font=("arial",20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(1),activebackground='green')
btn1.grid(row=3,column=0)

btn2=Button(screen,text='2',font=("arial",20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(2),activebackground='green')
btn2.grid(row=3,column=1 )

btn3=Button(screen,text='3',font=("arial",20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(3),activebackground='green')
btn3.grid(row=3,column=2)

btnmul=Button(screen,text='*',font=("arial",20,'italic bold'),bd=8,padx=18,pady=16,command=lambda:click('*'),activebackground='green')
btnmul.grid(row=3,column=3 )

btn0=Button(screen,text='0',font=("arial",20,'italic bold'),bd=8,padx=16,pady=16,command=lambda:click(0),activebackground='green')
btn0.grid(row=4,column=0)

btnclear=Button(screen,text='C',font=("arial",20,'italic bold'),bd=8,padx=16,pady=16,command=clear,activebackground='green')
btnclear.grid(row=4,column=1 )

btnequal=Button(screen,text='=',font=("arial",20,'italic bold'),bd=8,padx=16,pady=16,command=equal,activebackground='green')
btnequal.grid(row=4,column=2)

btndiv=Button(screen,text='/',font=("arial",20,'italic bold'),bd=8,padx=18,pady=16,command=lambda:click('/'),activebackground='green')
btndiv.grid(row=4,column=3 )

###advance
btnsin=Button(screen,text='sin',font=("arial",15,'italic bold'),bd=8,padx=14,pady=19,command=cmsin,activebackground='green')
btnsin.grid(row=0,column=4 )

btncos=Button(screen,text='cos',font=("arial",15,'italic bold'),bd=8,padx=14,pady=19,command=cmcos,activebackground='green')
btncos.grid(row=1,column=4 )

btntan=Button(screen,text='tan',font=("arial",15,'italic bold'),bd=8,padx=14,pady=19,command=cmtan,activebackground='green')
btntan.grid(row=2,column=4 )

btnsqrt=Button(screen,text='sqrt',font=("arial",15,'italic bold'),bd=8,padx=14,pady=19,command=cmsqrt,activebackground='green')
btnsqrt.grid(row=3,column=4 )

btnlog=Button(screen,text='log',font=("arial",15,'italic bold'),bd=8,padx=14,pady=19,command=cmlog,activebackground='green')
btnlog.grid(row=4,column=4 )

screen.mainloop()