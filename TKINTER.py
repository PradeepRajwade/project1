from tkinter import *
def btnclick(number):
    global val
    val=val+str(number)
   
    scvalue.set(val)

def btnc():
    global val 
    val= ""
    scvalue.set("")

def btneq():
    try:
        global val
        result=str(eval(val))
        scvalue.set(result)
    except:
        scvalue.set("Error")  


    
root=Tk()
root.geometry("361x381")
root.title("Manual calculator")
val=""
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,bg="light blue",font="lucida 40 bold",bd=12,justify="right")
screen.grid(row=0,columnspan=4)

btn9=Button(root,text='9',font=("Ariel",12,"bold"),bg="grey",bd=12,height=3,width=8,command=lambda:btnclick(9))
btn9.grid(row=1,column=2)

bt8=Button(root,text='8',font=("Ariel",12,"bold"),bg="grey",bd=12,height=3,width=8,command=lambda:btnclick(8))
bt8.grid(row=1,column=1)

btn7=Button(root,text='7',font=("Ariel",12,"bold"),bg="grey",bd=12,height=3,width=8,command=lambda:btnclick(7))
btn7.grid(row=1,column=0)

btnadd=Button(root,text='+',font=("Ariel",12,"bold"),bg="orange",bd=12,height=3,width=8,command=lambda:btnclick("+"))
btnadd.grid(row=1,column=3)

btn6=Button(root,text='6',font=("Ariel",12,"bold"),bg="grey",bd=12,height=3,width=8,command=lambda:btnclick(6))
btn6.grid(row=2,column=2)

btn5=Button(root,text='5',font=("Ariel",12,"bold"),bg="grey",bd=12,height=3,width=8,command=lambda:btnclick(5))
btn5.grid(row=2,column=1)

btn4=Button(root,text='4',font=("Ariel",12,"bold"),bg="grey",bd=12,height=3,width=8,command=lambda:btnclick(4))
btn4.grid(row=2,column=0)

btnsub=Button(root,text='-',font=("Ariel",12,"bold"),bg="orange",bd=12,height=3,width=8,command=lambda:btnclick("-"))
btnsub.grid(row=2,column=3)

btn3=Button(root,text='3',font=("Ariel",12,"bold"),bg="grey",bd=12,height=3,width=8,command=lambda:btnclick(3))
btn3.grid(row=3,column=2)

btn2=Button(root,text='2',font=("Ariel",12,"bold"),bg="grey",bd=12,height=3,width=8,command=lambda:btnclick(2))
btn2.grid(row=3,column=1)

btn1=Button(root,text='1',font=("Ariel",12,"bold"),bg="grey",bd=12,height=3,width=8,command=lambda:btnclick(1))
btn1.grid(row=3,column=0)

btnmul=Button(root,text='x',font=("Ariel",12,"bold"),bg="orange",bd=12,height=3,width=8,command=lambda:btnclick("*"))
btnmul.grid(row=3,column=3)

btndiv=Button(root,text='/',font=("Ariel",12,"bold"),bg="orange",bd=12,height=3,width=8,command=lambda:btnclick("/"))
btndiv.grid(row=5,column=3)

btnc=Button(root,text='c',font=("Ariel",12,"bold"),bg="green",bd=12,height=3,width=8,command=btnc)
btnc.grid(row=4,column=2)

btneq=Button(root,text='=',font=("Ariel",12,"bold"),bg="orange",bd=12,height=3,width=8,command=btneq)
btneq.grid(row=4,column=3)

btnze=Button(root,text='0',font=("Ariel",12,"bold"),bg="grey",bd=12,height=3,width=8,command=lambda:btnclick(0))
btnze.grid(row=4,column=1)

btnDOT=Button(root,text='.',font=("Ariel",12,"bold"),bg="grey",bd=12,height=3,width=8,command=lambda:btnclick("."))
btnDOT.grid(row=5,column=0)

btnDZ=Button(root,text='00',font=("Ariel",12,"bold"),bg="grey",bd=12,height=3,width=8,command=lambda:btnclick("00"))
btnDZ.grid(row=5,column=1)

btnPER=Button(root,text='%',font=("Ariel",12,"bold"),bg="grey",bd=12,height=3,width=8,command=lambda:btnclick("%"))
btnPER.grid(row=4,column=0)
root.mainloop()