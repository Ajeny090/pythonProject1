import tkinter


def enter():
    name = entry.get()
    pa = entry1.get()
    print(f"The UserName: {name}")
    print(f"The password: {pa}")
    print("*******************")

w = tkinter.Tk()
w.title("Registration")
fr = tkinter.Frame(w)
fr.grid()
label1 = tkinter.Label(fr,text="User Name")
label1.grid(row=0,column=0)
entry = tkinter.Entry(fr)
entry.grid(row=0,column=1)
label2 = tkinter.Label(fr,text="Password")
label2.grid(row=1,column=0)
entry1 = tkinter.Entry(fr,show="*")
entry1.grid(row=1,column=1)

#Create a button
button = tkinter.Button(fr,text="Sign Up", command=enter)
button.grid(row=2,column=1)

tkinter.mainloop()
