from tkinter import *
from tkinter import messagebox

money = 10
currentfruit = "Apple"
numOfApples = 0

def buyapple():
    global money
    global numOfApples
    if money < 1:
        messagebox.showinfo("Error", "You do not have enough money!")
    else:
        money = money - 1
        numOfApples = numOfApples + 1
        currentfruitstringvar.set("Apple x" + str(numOfApples))
        if numOfApples < 10:
            currentfruitlabel.place(x="180", y="290")
        if numOfApples < 100 and numOfApples > 9:
            currentfruitlabel.place(x="175", y="290")
        if numOfApples < 1000 and numOfApples > 99:
            currentfruitlabel.place(x="170", y="290")
        moneystringvar.set("You have $" + str(money))
        if money < 10:
            moneylabel.place(x="327", y="0")
        if money < 100 and money > 9:
            moneylabel.place(x="320", y="0")
        if money < 1000 and money > 99:
            moneylabel.place(x="315", y="0")

def buyapplepack():
    global money
    global numOfApples
    if money < 6:
        messagebox.showinfo("Error", "You do not have enough money!")
    else:
        money = money - 6
        numOfApples = numOfApples + 6
        currentfruitstringvar.set("Apple x" + str(numOfApples))
        if numOfApples < 10:
            currentfruitlabel.place(x="180", y="290")
        if numOfApples < 100 and numOfApples > 9:
            currentfruitlabel.place(x="175", y="290")
        if numOfApples < 1000 and numOfApples > 99:
            currentfruitlabel.place(x="170", y="290")
        moneystringvar.set("You have $" + str(money))
        if money < 10:
            moneylabel.place(x="327", y="0")
        if money < 100 and money > 9:
            moneylabel.place(x="320", y="0")
        if money < 1000 and money > 99:
            moneylabel.place(x="315", y="0")

def buyapplecrate():
    global money
    global numOfApples
    if money < 36:
        messagebox.showinfo("Error", "You do not have enough money!")
    else:
        money = money - 36
        numOfApples = numOfApples + 36
        currentfruitstringvar.set("Apple x" + str(numOfApples))
        if numOfApples < 10:
            currentfruitlabel.place(x="180", y="290")
        if numOfApples < 100 and numOfApples > 9:
            currentfruitlabel.place(x="175", y="290")
        if numOfApples < 1000 and numOfApples > 99:
            currentfruitlabel.place(x="170", y="290")
        moneystringvar.set("You have $" + str(money))
        if money < 10:
            moneylabel.place(x="327", y="0")
        if money < 100 and money > 9:
            moneylabel.place(x="320", y="0")
        if money < 1000 and money > 99:
            moneylabel.place(x="315", y="0")

def clicked():
    global money
    global currentfruit
    global numOfApples
    if currentfruit == "Apple":
        if numOfApples == 0:
            messagebox.showinfo("Error", "You do not have any Apples!")
        else:
            numOfApples = numOfApples - 1
            currentfruitstringvar.set("Apple x" + str(numOfApples))
            if numOfApples < 10:
                currentfruitlabel.place(x="180", y="290")
            if numOfApples < 100 and numOfApples > 9:
                currentfruitlabel.place(x="175", y="290")
            if numOfApples < 1000 and numOfApples > 99:
                currentfruitlabel.place(x="170", y="290")
            money = money + 2
            moneystringvar.set("You have $" + str(money))
            if money < 10:
                moneylabel.place(x="327", y="0")
            if money < 100 and money > 9:
                moneylabel.place(x="320", y="0")
            if money < 1000 and money > 99:
                moneylabel.place(x="315", y="0")

def inventoryOnClose():
    root.deiconify()
    inventorywindow.destroy()

def marketOnClose():
    root.deiconify()
    marketwindow.destroy()
    
def upgradesOnClose():
    root.deiconify()
    upgradeswindow.destroy()

def inventory():
    global inventorywindow
    global numOfApples
    root.withdraw()
    inventorywindow = Toplevel()
    inventorywindow.title("Fruit Clicker - Inventory")
    inventorywindow.geometry("400x350+300+100")
    inventorywindow.protocol("WM_DELETE_WINDOW", inventoryOnClose)
    applesinventory = StringVar()
    applesinventory.set("Apples: " + str(numOfApples))
    applesinvlabel = Label(inventorywindow, textvariable=applesinventory)
    applesinvlabel.grid(row="0", column="0")
    inventorywindow.mainloop()

def market():
    global marketwindow
    root.withdraw()
    marketwindow = Toplevel()
    marketwindow.title("Fruit Clicker - Market")
    marketwindow.geometry("400x350+300+100")
    marketwindow.protocol("WM_DELETE_WINDOW", marketOnClose)
    Label(marketwindow, text="Buy\nApple").grid(row="0", column="0")
    Button(marketwindow, text="Buy Apple\n$1", command=buyapple).grid(row="0", column="1")
    Button(marketwindow, text="Buy Pack (6)\n$6", command=buyapplepack).grid(row="0", column="2")
    Button(marketwindow, text="Buy Crate (36)\n$36", command=buyapplecrate).grid(row="0", column="3")
    marketwindow.mainloop()

def upgrades():
    global upgradeswindow
    root.withdraw()
    upgradeswindow = Toplevel()
    upgradeswindow.title("Fruit Clicker - Upgrades")
    upgradeswindow.geometry("400x350+300+100")
    upgradeswindow.protocol("WM_DELETE_WINDOW", upgradesOnClose)
    upgradeswindow.mainloop()

root = Tk()
root.title("Fruit Clicker")
root.geometry("400x350+300+100")

inventorybutton = Button(root, text="Inventory", fg="White", bg="Black", width="6", command=inventory)
inventorybutton.grid(column="0", row="0")

marketbutton = Button(root, text="Market", fg="White", bg="Black", width="6", command=market)
marketbutton.grid(column="0", row="1")

upgradesbutton = Button(root, text="Upgrades", fg="White", bg="Black", width="6", command=upgrades)
upgradesbutton.grid(column="0", row="2")

leftfruitbutton = Button(root, text="<")
leftfruitbutton.place(x="100", y="285")

currentfruitstringvar = StringVar()
if currentfruit == "Apple":  
    currentfruitstringvar.set("Apple x" + str(numOfApples))
    currentfruitlabel = Label(root, textvariable=currentfruitstringvar, fg="Black")
    if numOfApples < 10:
        currentfruitlabel.place(x="180", y="290")
    if numOfApples < 100 and numOfApples > 9:
        currentfruitlabel.place(x="175", y="290")
    if numOfApples < 1000 and numOfApples > 99:
        currentfruitlabel.place(x="170", y="290")

rightfruitbutton = Button(root, text=">")
rightfruitbutton.place(x="287", y="285")

moneystringvar = StringVar()
moneystringvar.set("You have $" + str(money))
moneylabel = Label(root, textvariable=moneystringvar)
if money < 10:
    moneylabel.place(x="327", y="0")
if money < 100 and money > 9:
    moneylabel.place(x="320", y="0")
if money < 1000 and money > 99:
    moneylabel.place(x="315", y="0")

clickerphoto = PhotoImage(file = "apple.png")
clickerbutton = Button(root, text="Clicker Button", image=clickerphoto, fg="Black", command=clicked)
clickerbutton.place(x="100", y="75")

root.mainloop()