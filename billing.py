from tkinter import*

root = Tk()
root.geometry("900x500")
root.title("Brain power super market bill management")
root.resizable(0, 0)

def Reset():
    entry_rice.delete (0, END)
    entry_beans.delete (0, END)
    entry_spaghetti.delete (0, END)
    entry_indomine.delete (0, END)
    entry_bread.delete (0, END)
    entry_semo.delete (0, END)
    entry_wheat.delete (0, END)
    entry_yam.delete (0, END)

def Total():
    try:a1=int(rice.get())
    except: a1=0
    

    try:a2=int(beans.get())
    except: a2=0

    try:a3=int(spaghetti.get())
    except: a3=0

    try:a4=int(indomine.get())
    except: a4=0


    try:a5=int(bread.get())
    except: a5=0

    try:a6=int(semo.get())
    except: a6=0

    try:a7=int(wheat.get())
    except: a7=0

    try:a8=int(yam.get())
    except: a8=0


#define cost of each item per quantity
    c1= 200*a1
    c2= 200*a2
    c3= 450*a3
    c4= 700*a4
    c5= 500*a5
    c6= 500*a6
    c7= 800*a7
    c8= 900*a8

    lbl_total = Label(f2, font=("arial", 20, "bold"), text="Total", width=14, fg="brown", bg="black")
    lbl_total.place(x=0, y=50)

    entry_total=Entry(f2, font=("arial", 20, "bold"), textvariable=Total_bill, bd=6, width=15, bg="green")
    entry_total.place(x=20, y=100)

    totalcost= c1+c2+c3+c4+c5+c6+c7+c8
    string_bill="NGN.",str("%.2f" %totalcost)
    Total_bill.set(string_bill)



Label(text= "BILL  MANAGEMENT", bg= "gray", fg="white", font=("calibre, 25"), width="200", height="2").pack()

#MENU CARD
f=Frame(root, bg="yellow", highlightbackground="black", highlightthickness=1, width=250, height= 370)
f.place(x=12, y=85)

Label(f, text="MENU", font=("Gabriola", 20, "bold"), fg="black", bg="yellow").place(x=50, y=0)

Label(f, font=("lucida calligraphy", 12, "bold"), text= "rice ...NGN.200", fg="black", bg="yellow").place(x=20, y=40)
Label(f, font=("lucida calligraphy", 12, "bold"), text= "beans ....NGN.200", fg="black", bg="yellow").place(x=20, y=70)
Label(f, font=("lucida calligraphy", 12, "bold"), text= "spaghetti ..NGN.450", fg="black", bg="yellow").place(x=20, y=100)
Label(f, font=("lucida calligraphy", 12, "bold"), text= "indomine ....NGN.700", fg="black", bg="yellow").place(x=20, y=130)
Label(f, font=("lucida calligraphy", 12, "bold"), text= "bread ....NGN.500", fg="black", bg="yellow").place(x=20, y=160)
Label(f, font=("lucida calligraphy", 12, "bold"), text= "semo ...NGN.500", fg="black", bg="yellow").place(x=20, y=190)
Label(f, font=("lucida calligraphy", 12, "bold"), text= "wheat ....NGN.800", fg="black", bg="yellow").place(x=20, y=220)
Label(f, font=("lucida calligraphy", 12, "bold"), text= "yam....NGN.900", fg="black", bg="yellow").place(x=20, y=250)

#BILL
f2= Frame(root, bg="brown",highlightbackground="black", highlightthickness=1, width=250, height= 370)
f2.place(x=600, y=85)

bill = Label(f2, text="Bill", font=("calibre", 14), bg="brown")
bill.place(x=100, y=10)


#ENTRY WORK
f1=Frame(root, bd=5, height=370, width=250, relief= RAISED)
f1.pack()


rice=StringVar()
beans=StringVar()
spaghetti= StringVar()
indomine = StringVar()
bread = StringVar()
semo = StringVar()
wheat = StringVar()
yam = StringVar()
Total_bill= StringVar()

#Label 
lbl_rice= Label(f1, font=("aria", 15, "bold"), text="rice", width=7, fg="blue")
lbl_beans= Label(f1, font=("aria", 15, "bold"), text="beans", width=7, fg="blue")
lbl_spaghetti= Label(f1, font=("aria", 15, "bold"), text="spaghetti", width=7, fg="blue")
lbl_indomine= Label(f1, font=("aria", 15, "bold"), text="indomine", width=7, fg="blue")
lbl_bread= Label(f1, font=("aria", 15, "bold"), text="bread", width=7, fg="blue")
lbl_semo= Label(f1, font=("aria", 15, "bold"), text="semo", width=7, fg="blue")
lbl_wheat= Label(f1, font=("aria", 15, "bold"), text="wheat", width=7, fg="blue")
lbl_yam= Label(f1, font=("aria", 15, "bold"), text="yam", width=7, fg="blue")

lbl_rice.grid(row=1, column=0)
lbl_beans.grid(row=2, column=0)
lbl_spaghetti.grid(row=3, column=0)
lbl_indomine.grid(row=4, column=0)
lbl_bread.grid(row=5, column=0)
lbl_semo.grid(row=6, column=0)
lbl_wheat.grid(row=7, column=0)
lbl_yam.grid(row=8, column=0)


#Entry
entry_rice=Entry(f1,font=("arial", 20, "bold"), textvariable=rice, bd=6,width=8, bg="white")
entry_beans=Entry(f1,font=("arial", 20, "bold"), textvariable=beans, bd=6,width=8, bg="white")
entry_spaghetti=Entry(f1,font=("arial", 20, "bold"), textvariable=spaghetti, bd=6,width=8, bg="white")
entry_indomine=Entry(f1,font=("arial", 20, "bold"), textvariable=indomine, bd=6,width=8, bg="white")
entry_bread=Entry(f1,font=("arial", 20, "bold"), textvariable=bread, bd=6,width=8, bg="white")
entry_semo=Entry(f1,font=("arial", 20, "bold"), textvariable=semo, bd=6,width=8, bg="white")
entry_wheat=Entry(f1,font=("arial", 20, "bold"), textvariable=wheat, bd=6,width=8, bg="white")
entry_yam=Entry(f1,font=("arial", 20, "bold"), textvariable=yam, bd=6,width=8, bg="white")

entry_rice.grid(row=1, column=1)
entry_beans.grid(row=2, column=1)
entry_spaghetti.grid(row=3, column=1)
entry_indomine.grid(row=4, column=1)
entry_bread.grid(row=5, column=1)
entry_semo.grid(row=6, column=1)
entry_wheat.grid(row=7, column=1)
entry_yam.grid(row=8,column=1)


#buttons
btn_resest = Button(f1, bd=5, bg="blue", font=("arial", 12, "bold"), width=10, text="Reset", command=Reset)
btn_resest.grid(row=9, column=0)


btn_total = Button(f1, bd=5, fg="blue", font=("arial", 12,"bold"), width=10, text="Total", command=Total)
btn_total.grid(row=9, column=1)



root.mainloop()