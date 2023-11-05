from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root = Tk()
root.config(bg="#CDE990")
root.title("Library Management")
root.geometry("800x800")
root.minsize(900,550)
root.maxsize(900,550)


Label(root, text="Welcome to AITM Library", font="CASTELLAR 32 bold",bg="#CDE990",padx=0, pady=15).grid(row=0, column=3)


name = Label(root, text="Name",font=('calibre',18,'normal'),bg="#CDE990")
roll = Label(root, text="Roll no",font=('calibre',18,'normal'),bg="#CDE990")
phone = Label(root, text="Phone",font=('calibre',18,'normal'),bg="#CDE990")
course=Label(root, text= "Course",font=('calibre',18,'normal'),bg="#CDE990")
branch=Label(root,text="Branch",font=('calibre',18,'normal'),bg="#CDE990")
semester=Label(root,text="Semester",font=('calibre',18,'normal'),bg="#CDE990")
working=Label(root,text="Work",font=('calibre',18,'normal'),bg="#CDE990")


name.grid(row=1, column=2)
roll.grid(row=2, column=2)
phone.grid(row=3, column=2)
course.grid(row=4,column=2)
branch.grid(row=5,column=2)
semester.grid(row=6,column=2)
working.grid(row=7,column=2)


namevalue = StringVar()
rollvalue = StringVar()
phonevalue = StringVar()
num=["Btech", "Barch","Bfad"]
variable=StringVar(root)
variable.set("Select an Option")
branch=["CSE","IT","CIVIL","AIML","CSDS"]
br=StringVar(root)
br.set("Select an Option")
sem=[1,2,3,4,5,6,7,8,9,10]

var=StringVar(root)
var.set("Select an Option")
w0=["ISSUE BOOK","RETURN BOOK", "DONATE BOOK"]
work=StringVar(root)
work.set("Select an Option")





nameentry = Entry(root, textvariable=namevalue , font=('calibre',18,'normal'))
rollentry = Entry(root, textvariable=rollvalue, font=('calibre',18,'normal'))
phoneentry = Entry(root, textvariable=phonevalue, font=('calibre',18,'normal'))
courseentry=OptionMenu(root, variable , *num)
branchentry=OptionMenu(root,br,*branch)
sementry=OptionMenu(root,var,*sem)
workingg=OptionMenu(root,work,*w0)


# Packing the Entries
nameentry.grid(row=1, column=3)
rollentry.grid(row=2, column=3)
phoneentry.grid(row=3, column=3)
courseentry.grid(row=4 , column=3)
branchentry.grid(row=5 , column=3)
sementry.grid(row=6,column=3)
workingg.grid(row=7,column=3)

books=["DATA STRUCTURE", " CO&A ","DISCRETE " , " HISTORY ", " CIVICS "]

def submit():
    
   if work.get()== "ISSUE BOOK":
    top=Toplevel()
    top.title("ISSUE BOOKS ")
    top.geometry("400x200")
    top.minsize(600,200)
    top.maxsize(600,200)
    Label(top, text="ISSUE BOOKS ", font="CASTELLAR 32 bold",padx=10, pady=15).grid(row=1 , column=2)
    ab=Label(top,text="Available books",font=('calibre',18,'normal'),padx=0 , pady=20)
    ab.grid(row=2 , column=1)

    n=StringVar(top)
    aval=ttk.Combobox(top,width=30,textvariable=n)
    aval['values']=books
    aval.grid(row=2 , column=2)
    aval.current()
    def ISSUE():
        messagebox.showinfo(title="return " , message="Thank you for visiting AITM libray \n keep the book safe and return it on time")
        books.remove(n.get())
    Button(top,text="    ISSUE     ",command= ISSUE).grid(row=3, column=2)

    





   if work.get()=="RETURN BOOK":
        toPP=Toplevel()
        toPP.title("Return book")
        toPP.geometry("400x200")
        
        toPP.minsize(600,200)
        toPP.maxsize(600,200)
        
        Label(toPP, text="RETURN BOOK", font="CASTELLAR 32 bold",padx=10, pady=15).grid(row=1 , column=2)
        ab=Label(toPP,text="Select book:",font=('calibre',18,'normal'),padx=0 , pady=20)
        ab.grid(row=2 , column=1)

        n=StringVar(toPP)
        aval=ttk.Combobox(toPP,width=30,textvariable=n)
        aval['values']=("DATA STRUCTURE", " CO&A ","DISCRETE " , " HISTORY ", " CIVICS ")
        aval.grid(row=2 , column=2)
        aval.current()
        def returnn():
            messagebox.showinfo(title="return " , message="Thank you for Returning the book!")
            books.append(namevalues.get())
        Button(toPP,text="  RETURN   ",command= returnn).grid(row=4, column=2)

        
        






   if work.get()=="DONATE BOOK":
        to=Toplevel()
        to.title("Donate book")
        to.geometry("400x200")
        to.minsize(800,300)
        to.maxsize(800,300)
        Label(to, text="DONATE BOOK", font="CASTELLAR 32 bold").grid(row=1 , column=2)
        ab=Label(to,text="BOOK NAME",font=('calibre',18,'normal'),padx=0 , pady=20)
        ab.grid(row=2 , column=1)
        namevalues=StringVar()
        a=Entry(to, textvariable=namevalues , font=('calibre',18,'normal')).grid(row=2 , column=2)

        abc=Label(to,text="AUTHOR ",font=('calibre',18,'normal'),padx=0 , pady=20)
        abc.grid(row=3 , column=1)
        authorvalues=StringVar()
        Entry(to, textvariable=authorvalues , font=('calibre',18,'normal')).grid(row=3 , column=2)
        def donate():
            messagebox.showinfo(title="Doante" , message="Thank you for donating the book!")
            books.append(namevalues.get())

        Button(to,text="  DONATE  ",command= donate).grid(row=4, column=2)
  
        









Button(text="       SUBMIT       ",command=submit).grid(row=8, column=3)
Button(text="       CANCEL       ", command=quit).grid(row=8,column=2)




root.mainloop()
