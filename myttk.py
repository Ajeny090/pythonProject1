import tkinter
from tkinter import ttk

def option_selected():
    print(combo.get())
    print(combo1.get())
w = tkinter.Tk()
label = tkinter.Label(w,text="Options")
label.grid(row=0,column=0)
combo = ttk.Combobox(w,values=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"])
combo.grid(row=0,column=1)
label4 = tkinter.Label(w,text="Courses")
label4.grid(row=1, column=0)
combo1 = ttk.Combobox(w,values=["Management","Communication","Project Management"])
combo1.grid(row=1,column=1)

label3 = tkinter.Button(w,text="Enter", command=option_selected)
label3.grid(row = 2,column=1)

w.mainloop()