from tkinter import *
import time
import random

root = Tk()
root.geometry("1600x800")
root.title("Calculator")
#======================Variables=============================
text_input = StringVar()
operator = ""


top = Frame(root, width=1600, height=50, bg='powder blue', relief=SUNKEN)
top.pack(side=TOP)
f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)
f2 = Frame(root, width=300, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)
#============================time================================
localtime = time.asctime(time.localtime(time.time()))
#====================================info====================================
lblinfo = Label(top, font=('arial', 50, 'bold'), text="Restraunt Management System", fg='Steel Blue', bd=10, anchor='w')
lblinfo.grid(row=0, column=0)
lblinfo = Label(top, font=('arial', 20, 'bold'), text=localtime, fg='Steel Blue', bd=10, anchor='w')
lblinfo.grid(row=1, column=0)
#=============================Calculator=====================================


def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def btncleardisplay():
    global operator
    operator = ''
    text_input.set("")


def btnequalinput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ''


def Ref():
    x = random.randint(12908, 50876)
    randomref = str(x)
    rand.set(randomref)
    cof = float(Fries.get())
    cod = float(Drinks.get())
    cofillet = float(Fillet.get())
    cofburger = float(Burger.get())
    cofchicken = float(Chicken.get())
    cocheese = float(Cheese.get())

    CostofFries = cof * 0.99
    CostofDrinks = cod * 1
    CostofFillet = cofillet * 2.99
    CostofBurger = cofburger * 2.87
    CostofChicken = cofchicken * 2.89
    CostofCheese = cocheese * 2.69

    CostofMeal = '$', str('%2f' % (CostofFries + CostofFillet + CostofDrinks + CostofCheese + CostofBurger + CostofChicken))
    PayTax = ((CostofFries + CostofFillet + CostofDrinks + CostofCheese + CostofBurger + CostofChicken) * 0.2)
    TotalCost = (CostofFries + CostofFillet + CostofDrinks + CostofCheese + CostofBurger + CostofChicken)
    ServiceCharge = ((CostofFries + CostofFillet + CostofDrinks + CostofCheese + CostofBurger + CostofChicken) / 99)
    Service = '$', str('%2f' % ServiceCharge)
    PaidTax = '$', str('%2f' % PayTax)
    Overallcost = '$', str('%2f' % (PayTax + TotalCost + ServiceCharge))

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    Subtotal.set(CostofMeal)
    Total.set(Overallcost)


def qexit():
    root.destroy()


def Reset():
    rand.set('')
    Fries.set('')
    Burger.set('')
    Fillet.set('')
    Subtotal.set('')
    Total.set('')
    Service_Charge.set('')
    Drinks.set('')
    Tax.set('')
    Cost.set('')
    Chicken.set('')
    Cheese.set('')


txtdisplay = Entry(f2, font=('arial', 20, 'bold'), textvariable=text_input, bd=30, insertwidth=4, bg='powder blue', justify='right')
txtdisplay.grid(columnspan=4)
btn7 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='7', bg='powder blue', command=lambda: btnclick(7)).grid(row=2, column=0)
btn8 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='8', bg='powder blue', command=lambda: btnclick(8)).grid(row=2, column=1)
btn9 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='9', bg='powder blue', command=lambda: btnclick(9)).grid(row=2, column=2)
Addition = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='+', bg='powder blue', command=lambda: btnclick('+')).grid(row=2, column=3)
#=============================================================================================
btn4 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='4', bg='powder blue', command=lambda: btnclick(4)).grid(row=3, column=0)
btn5 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='5', bg='powder blue', command=lambda: btnclick(5)).grid(row=3, column=1)
btn6 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='6', bg='powder blue', command=lambda: btnclick(6)).grid(row=3, column=2)
Subtraction = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='-', bg='powder blue', command=lambda: btnclick('-')).grid(row=3, column=3)
#================================================================================================
btn1 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='1', bg='powder blue', command=lambda: btnclick(1)).grid(row=4, column=0)
btn2 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='2', bg='powder blue', command=lambda: btnclick(2)).grid(row=4, column=1)
btn3 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='3', bg='powder blue', command=lambda: btnclick(3)).grid(row=4, column=2)
Multiplication = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='*', bg='powder blue', command=lambda: btnclick('*')).grid(row=4, column=3)
#====================================================================================================
btn0 = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='0', bg='powder blue', command=lambda: btnclick(0)).grid(row=5, column=0)
btnclear = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='C', bg='powder blue', command=btncleardisplay).grid(row=5, column=1)
btnequal = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='=', bg='powder blue', command=btnequalinput).grid(row=5, column=2)
Division = Button(f2, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='/', bg='powder blue', command=lambda: btnclick('/')).grid(row=5, column=3)
#===========================================Variables===================================================================
rand = StringVar()
Fries = StringVar()
Burger = StringVar()
Fillet = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Chicken = StringVar()
Cheese = StringVar()
#========================================================Label1==========================================================
lblreference = Label(f1, font=('arial', 16, 'bold'), text='Reference', bd=16, anchor='w').grid(row=0, column=0)
txtreference = Entry(f1, font=('arial', 16, 'bold'), textvariable=rand, bd=10, insertwidth=4, bg='powder blue', justify=RIGHT).grid(row=0, column=1)

lblfries = Label(f1, font=('arial', 16, 'bold'), text='Large Fries', bd=16, anchor='w').grid(row=1, column=0)
txtreference = Entry(f1, font=('arial', 16, 'bold'), textvariable=Fries, bd=10, insertwidth=4, bg='powder blue', justify=RIGHT).grid(row=1, column=1)

lblburger = Label(f1, font=('arial', 16, 'bold'), text='Burger Meal', bd=16, anchor='w').grid(row=2, column=0)
txtburger = Entry(f1, font=('arial', 16, 'bold'), textvariable=Burger, bd=10, insertwidth=4, bg='powder blue', justify=RIGHT).grid(row=2, column=1)

lblfillet = Label(f1, font=('arial', 16, 'bold'), text='Fillet_o_meal', bd=16, anchor='w').grid(row=3, column=0)
txtFillet = Entry(f1, font=('arial', 16, 'bold'), textvariable=Fillet, bd=10, insertwidth=4, bg='powder blue', justify=RIGHT).grid(row=3, column=1)

lblchicken = Label(f1, font=('arial', 16, 'bold'), text='Chicken Meal', bd=16, anchor='w').grid(row=4, column=0)
txtchicken = Entry(f1, font=('arial', 16, 'bold'), textvariable=Chicken, bd=10, insertwidth=4, bg='powder blue', justify=RIGHT).grid(row=4, column=1)

lblcheese = Label(f1, font=('arial', 16, 'bold'), text='Cheese Meal', bd=16, anchor='w').grid(row=5, column=0)
txtcheese = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cheese, bd=10, insertwidth=4, bg='powder blue', justify=RIGHT).grid(row=5, column=1)
#===================================================Label2==========================================================
lbldrinks = Label(f1, font=('arial', 16, 'bold'), text='Drinks', bd=16, anchor='w').grid(row=0, column=2)
txtdrinks = Entry(f1, font=('arial', 16, 'bold'), textvariable=Drinks, bd=10, insertwidth=4, bg='#ffffff', justify=RIGHT).grid(row=0, column=3)

lblCost = Label(f1, font=('arial', 16, 'bold'), text='Cost of Meal', bd=16, anchor='w').grid(row=1, column=2)
txtcost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cost, bd=10, insertwidth=4, bg='#ffffff', justify=RIGHT).grid(row=1, column=3)

lblservice = Label(f1, font=('arial', 16, 'bold'), text='Service Charge', bd=16, anchor='w').grid(row=2, column=2)
txtservice = Entry(f1, font=('arial', 16, 'bold'), textvariable=Service_Charge, bd=10, insertwidth=4, bg='#ffffff', justify=RIGHT).grid(row=2, column=3)

lbltax = Label(f1, font=('arial', 16, 'bold'), text='Tax', bd=16, anchor='w').grid(row=3, column=2)
txttax = Entry(f1, font=('arial', 16, 'bold'), textvariable=Tax, bd=10, insertwidth=4, bg='#ffffff', justify=RIGHT).grid(row=3, column=3)

lblsubtotal = Label(f1, font=('arial', 16, 'bold'), text='Sub Total', bd=16, anchor='w').grid(row=4, column=2)
txtsubtotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=Subtotal, bd=10, insertwidth=4, bg='#ffffff', justify=RIGHT).grid(row=4, column=3)

lbltotal = Label(f1, font=('arial', 16, 'bold'), text='Total', bd=16, anchor='w').grid(row=5, column=2)
txttotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4, bg='#ffffff', justify=RIGHT).grid(row=5, column=3)
#======================================================Button==================================================
btntotal = Button(f1, padx=16, pady=16, bd=16, fg='black', font=('arial', 16, 'bold'), width=10, text='Total', bg='powder blue', command=Ref).grid(row=7, column=1)
btnreset = Button(f1, padx=16, pady=16, bd=16, fg='black', font=('arial', 16, 'bold'), width=10, text='Reset', bg='powder blue', command=Reset).grid(row=7, column=2)
btnexit = Button(f1, padx=16, pady=16, bd=16, fg='black', font=('arial', 16, 'bold'), width=10, text='Exit', bg='powder blue', command=qexit).grid(row=7, column=3)


root.mainloop()
