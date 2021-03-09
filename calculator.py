#            Scientific Calculator           #

from tkinter import *
import os
import webbrowser
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator made by Kaushal")
root.configure(bg='black')
root.resizable(width=False, height=False)
root.geometry("480x568+450+90")
calc = Frame(root,bg='black')


calc.grid()

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
                fo = open("History.txt", "a")
                fo.write(screen.get()+" = "+str(value)+"\r\n")
                fo.close()


            except Exception as e:
                print(e)
                value = "Error"
                fo = open("History.txt", "a")
                fo.write(screen.get()+" = "+str(value)+"\r\n")
                fo.close()

        scvalue.set(value)
        screen.update()

    elif text == "AC":
        scvalue.set("")
        screen.update()

    elif text == "Del" :
        tempv=scvalue.get()
        tempv=tempv[0:-1]
        scvalue.set(tempv)
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

# Here are the Classes for all the Buttons in the Scientific Calculator.

def fact(self):
    n=float(scvalue.get())
    temp=float(n)
    i=1
    while i<n:
        temp=temp*i
        i=i+1
    fo = open("History.txt", "a")
    fo.write(screen.get() + "! = " + str(temp) + "\r\n")
    fo.close()
    scvalue.set(str(temp))


def asin(self):
    fo = open("History.txt", "a")
    fo.write("sin-1(" + screen.get() + ") = ")
    scvalue.set(str(math.asin(float(scvalue.get()))))
    screen.update()
    fo.write(screen.get()+"(radian)\r\n")
    fo.close()

def acos(self):
    fo = open("History.txt", "a")
    fo.write("cos-1(" + screen.get() + ") = ")
    scvalue.set(str(math.acos(float(scvalue.get()))))
    screen.update()
    fo.write(screen.get()+"(radian)\r\n")
    fo.close()

def squre(self):
    fo = open("History.txt", "a")
    fo.write("(" + screen.get() +")^2 = ")
    scvalue.set(str(float(scvalue.get())*float(scvalue.get())))
    screen.update()
    fo.write(screen.get() + "\r\n")
    fo.close()

def cube(self):
    fo = open("History.txt", "a")
    fo.write("(" + screen.get() +")^3 = ")
    scvalue.set(str(float(scvalue.get())*float(scvalue.get())*float(scvalue.get())))
    screen.update()
    fo.write(screen.get() + "\r\n")
    fo.close()

def cuberoot(self):
    fo = open("History.txt", "a")
    fo.write("cubrt(" + screen.get() + ") = ")
    scvalue.set(str(math.pow(float(scvalue.get()),1/3)))
    screen.update()
    fo.write(screen.get() + "\r\n")
    fo.close()

def pi(self):
        scvalue.set(scvalue.get()+str(math.pi))
        screen.update()

def exp(self) :
      fo = open("History.txt", "a")
      fo.write("Exp(" + screen.get() + ") = ")
      scvalue.set(math.exp(int(scvalue.get())))
      screen.update()
      fo.write(screen.get() + "\r\n")
      fo.close()

def squared(self):
        fo = open("History.txt", "a")
        fo.write("sqrt("+screen.get() + ") = ")
        scvalue.set(math.sqrt(float(scvalue.get())))
        screen.update()
        fo.write(screen.get()+"\r\n")
        fo.close()

def cos(self):
        fo = open("History.txt", "a")
        fo.write("cos("+screen.get() + ") = ")
        scvalue.set(math.cos(math.radians(float(scvalue.get()))))
        screen.update()
        fo.write(screen.get()+"\r\n")
        fo.close()

def cosh(self):
        fo = open("History.txt", "a")
        fo.write("cosh("+screen.get() + ") = ")
        scvalue.set(math.cosh(math.radians(float(scvalue.get()))))
        screen.update()
        fo.write(screen.get()+"\r\n")
        fo.close()

def tan(self):
        fo = open("History.txt", "a")
        fo.write("tan("+screen.get() + ") = ")
        scvalue.set(math.tan(math.radians(float(scvalue.get()))))
        screen.update()
        fo.write(screen.get()+"\r\n")
        fo.close()

def sin(self):
        fo = open("History.txt", "a")
        fo.write("sin("+screen.get() + ") = ")
        scvalue.set(math.sin(math.radians(float(scvalue.get()))))
        screen.update()
        fo.write(screen.get()+"\r\n")
        fo.close()

def sinh(self):
        fo = open("History.txt", "a")
        fo.write("sinh("+screen.get() + ") = ")
        scvalue.set(math.sinh(math.radians(float(scvalue.get()))))
        screen.update()
        fo.write(screen.get()+"\r\n")
        fo.close()

def log(self):
        fo = open("History.txt", "a")
        fo.write("log("+screen.get() + ") = ")
        scvalue.set(math.log(float(scvalue.get())))
        screen.update()
        fo.write(screen.get()+"\r\n")
        fo.close()

def degrees(self):
        fo = open("History.txt", "a")
        fo.write("Radian("+screen.get() + ") = ")
        scvalue.set(math.degrees(float(scvalue.get())))
        screen.update()
        fo.write(screen.get()+" (degree)\r\n")
        fo.close()

def log10(self):
        fo = open("History.txt", "a")
        fo.write("log10("+screen.get() + ") = ")
        scvalue.set(math.log10(float(scvalue.get())))
        screen.update()
        fo.write(screen.get()+"\r\n")
        fo.close()

scvalue = StringVar()
scvalue.set("0")
# Here is the code for Display of Calculator.

screen = Entry(calc,  textvar=scvalue,font=('Helvetica', 20, 'bold'), bg='black', fg='white', bd=30,
                   width=28, justify=RIGHT)
screen.grid(row=0, column=0, columnspan=4, pady=1)

# Here is the code for NUMBER PAD in Calculator.

numberpad = "789456123"
i = 0
btn = []
for j in range(2, 5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, bg='blue', fg='white', font=('Helvetica', 20, 'bold'),
                          bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i].bind("<Button-1>", click)
        i += 1

# ====================================================================================================== #

# Here is the code for Button of Standard Calulator.

b = Button(calc, text="AC", width=6, height=2, bg='red', fg='white', font=('Helvetica', 20, 'bold')
                  , bd=4,)
b.bind("<Button-1>", click)
b.grid(row=1, column=0, pady=1)

btnAllClear = Button(calc, text="Del", width=6, height=2, bg='red', fg='white', font=('Helvetica', 20, 'bold'),
                     bd=4)
btnAllClear.bind("<Button-1>", click)
btnAllClear.grid(row=1, column=1, pady=1)

btnsq = Button(calc, text="\u221A", width=6, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'),
               bd=4)
btnsq.bind("<Button-1>", click)
btnsq.grid(row=1, column=2, pady=1)

btnAdd = Button(calc, text="+", width=6, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'),
                bd=4)
btnAdd.bind("<Button-1>", click)
btnAdd.grid(row=1, column=3, pady=1)

btnSub = Button(calc, text="-", width=6, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'),
                bd=4)
btnSub.bind("<Button-1>", click)
btnSub.grid(row=2, column=3, pady=1)

btnMul = Button(calc, text="*", width=6, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'),
                bd=4)
btnMul.bind("<Button-1>", click)
btnMul.grid(row=3, column=3, pady=1)

btnDiv = Button(calc, text="/", width=6, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'),
                bd=4)
btnDiv.bind("<Button-1>", click)
btnDiv.grid(row=4, column=3, pady=1)

btnZero = Button(calc, text="0", width=6, height=2, bg='blue', fg='white', font=('Helvetica', 20, 'bold'),
                 bd=4)
btnZero.bind("<Button-1>", click)
btnZero.grid(row=5, column=1, pady=1)

btnDot = Button(calc, text=".", width=6, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'),
                bd=4)
btnDot.bind("<Button-1>", click)
btnDot.grid(row=5, column=0, pady=1)

btnPM = Button(calc, text='%', width=6, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'),
               bd=4)
btnPM.bind("<Button-1>", click)
btnPM.grid(row=1, column=2, pady=1)

btndeg = Button(calc, text="**", width=6, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'),
                bd=4)
btndeg.bind("<Button-1>", click)
btndeg.grid(row=5, column=2, pady=1)

btnEquals = Button(calc, text="=", width=6, height=2, bg='red', fg='white', font=('Helvetica', 20, 'bold'),
                   bd=4)
btnEquals.bind("<Button-1>", click)
btnEquals.grid(row=5, column=3, pady=1)
# ===================================================================================================== #

# Here is the code for Buttons of Scientific Calulator.
# Here i make the rows for the Button of Scientific Calulator.
# ROW 1 :

btndeg = Button(calc, text="(", width=6, height=2, bg='blue', fg='white', font=('Helvetica', 20, 'bold'),
                bd=4,)
btndeg.bind("<Button-1>", click)
btndeg.grid(row=1, column=4, pady=1)

btndeg = Button(calc, text=")", width=6, height=2, bg='blue', fg='white', font=('Helvetica', 20, 'bold'),
                bd=4)
btndeg.bind("<Button-1>", click)
btndeg.grid(row=1, column=5, pady=1)

btnPM = Button(calc, text="exp",width=6, height=2,bg='blue',fg='white', font=('Helvetica',20,'bold'),
                  bd=4)
btnPM.bind("<Button-1>", exp)
btnPM.grid(row=1, column=6, pady = 1)

btndeg = Button(calc, text="deg", width=6, height=2, bg='blue', fg='white', font=('Helvetica', 20, 'bold'),
                bd=4)
btndeg.bind("<Button-1>", degrees)
btndeg.grid(row=1, column=7, pady=1)

# **************************************************************************************************** #

# ROW 2 :

btnPi = Button(calc, text="π", width=6, height=2, bg='blue', fg='white', font=('Helvetica', 20, 'bold'),
               bd=4)
btnPi.bind("<Button-1>", pi)
btnPi.grid(row=2, column=4, pady=1)

btnsin = Button(calc, text="sin", width=6, height=2, bg='blue', fg='white', font=('Helvetica', 20, 'bold'),
                bd=4)
btnsin.bind("<Button-1>", sin)
btnsin.grid(row=2, column=5, pady=1)

btnCos = Button(calc, text="cos", width=6, height=2, bg='blue', fg='white', font=('Helvetica', 20, 'bold'),
                bd=4)
btnCos.bind("<Button-1>", cos)
btnCos.grid(row=2, column=6, pady=1)

btntan = Button(calc, text="tan", width=6, height=2, fg='white', bg='blue', font=('Helvetica', 20, 'bold'),
                bd=4)
btntan.bind("<Button-1>", tan)
btntan.grid(row=2, column=7, pady=1)
# ******************************************************************************************************#

# ROW 3 :

btnE = Button(calc, text="!", width=6, height=2, fg='white', bg='blue', font=('Helvetica', 20, 'bold'),
              bd=4)
btnE.bind("<Button-1>", fact)
btnE.grid(row=3, column=4, pady=1)

btnE = Button(calc, text="e", width=6, height=2, fg='white', bg='blue', font=('Helvetica', 20, 'bold'),
              bd=4)
btnE.bind("<Button-1>", click)
btnE.grid(row=3, column=5, pady=1)

btnE = Button(calc, text="asin", width=6, height=2, bg='blue', fg='white', font=('Helvetica', 20, 'bold'),
              bd=4)
btnE.bind("<Button-1>", asin)
btnE.grid(row=3, column=6, pady=1)

btnE = Button(calc, text="acos", width=6, height=2, bg='blue', fg='white', font=('Helvetica', 20, 'bold'),
              bd=4)
btnE.bind("<Button-1>", acos)
btnE.grid(row=3, column=7, pady=1)

# ******************************************************************************************************#

# ROW 4 :

btnsq = Button(calc, text="\u221A", width=6, height=2, bg='blue', fg='white', font=('Helvetica', 20, 'bold'),
               bd=4)
btnsq.bind("<Button-1>", squared)
btnsq.grid(row=4, column=4, pady=1)

btnsinh = Button(calc, text="x2", width=6, height=2, bg='blue', fg='white', font=('Helvetica', 20, 'bold'),
                 bd=4)
btnsinh.bind("<Button-1>", squre)
btnsinh.grid(row=4, column=5, pady=1)

btnsinh = Button(calc, text="sinh", width=6, height=2, bg='blue', fg='white', font=('Helvetica', 20, 'bold'),
                 bd=4)
btnsinh.bind("<Button-1>", sinh)
btnsinh.grid(row=4, column=6, pady=1)

btnCosh = Button(calc, text="cosh", width=6, height=2, bg='blue', fg='white', font=('Helvetica', 20, 'bold'),
                 bd=4)
btnCosh.bind("<Button-1>", cosh)
btnCosh.grid(row=4, column=7, pady=1)

# ******************************************************************************************************#

# ROW 5 :

btnlog = Button(calc, text="∛", width=6, height=2, bg='blue', fg='white', font=('Helvetica', 20, 'bold'),
                bd=4)
btnlog.bind("<Button-1>", cuberoot)
btnlog.grid(row=5, column=4, pady=1)

btnlog = Button(calc, text="x3", width=6, height=2, bg='blue', fg='white', font=('Helvetica', 20, 'bold'),
                bd=4)
btnlog.bind("<Button-1>", cube)
btnlog.grid(row=5, column=5, pady=1)

btnlog = Button(calc, text="log", width=6, height=2, bg='blue', fg='white', font=('Helvetica', 20, 'bold'),
                bd=4)
btnlog.bind("<Button-1>", log)
btnlog.grid(row=5, column=6, pady=1)

btnlog10 = Button(calc, text="log10", width=6, height=2, bg='blue', fg='white', font=('Helvetica', 20, 'bold')
                  , bd=4)
btnlog10.bind("<Button-1>", log10)
btnlog10.grid(row=5, column=7, pady=1)

lblDisplay = Label(calc, text="Scientific Calculator", font=('Helvetica', 30, 'bold'),
                   bg='yellow', fg='red', justify=CENTER)
lblDisplay.grid(row=0, column=4, columnspan=4,)

# ====================================================================================================== #
# Here are the fucntions for ManuBar.

def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Do you want to exit ?")
    if iExit > 0:
        root.destroy()
        return

def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("944x568")

def Standard():
    root.resizable(width=False, height=False)
    root.geometry("480x568")

def History():
    webbrowser.open("History.txt")

menubar = Menu(calc)

# ManuBar 1 :
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Standard", command=Standard)
# ManuBar 2 :
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Scientific", command=Scientific)
# ManuBar 3 :
historymenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="History",command=History)
# MenuBar 4:
exitmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Exit", command=iExit)

root.config(menu=menubar)

root.mainloop()