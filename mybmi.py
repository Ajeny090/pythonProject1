import tkinter

def bmi():
    try:
        weight = int(entry1.get())
        height = float(entry2.get())
        bmi2 = int(weight/height**2)
        result_label.config(text=f"Your BMI is {bmi2}")
        if bmi2 < 18.5:
            opinion_label.config(text=f"Your BMI is less than 18.5, which is considered underweight.")
        elif 18.5 < bmi2 < 24.5:
            opinion_label.config(text=f"Your BMI is between 18.5 to 24.5, which is considered normal.")
        elif 24.5 < bmi2 < 29.9:
            opinion_label.config(text=f"Your BMI is between 24.5 to 29.9, which is considered overweight.")
        elif bmi2 > 29.9:
            opinion_label.config(text=f"Your BMI is above 29.9, which is considered obesity.")
    except ValueError:
        result_label.config(text="Please enter valid numbers")
    except ZeroDivisionError:
        result_label.config(text="Height cannot be zero")


windows = tkinter.Tk()
windows.title("Get Your BMI")
frame = tkinter.Frame(windows)
frame.grid(padx=10,pady=10)

label1 = tkinter.Label(frame,text="Enter your weight in kg")
label1.grid(row=0,column=0,padx=5,pady=5)

entry1 = tkinter.Entry(frame)
entry1.grid(row=0,column=1,padx=5,pady=5)

label2 = tkinter.Label(frame,text="Enter height in meters")
label2.grid(row=1,column=0,padx=5,pady=5)

entry2 = tkinter.Entry(frame)
entry2.grid(row=1,column=1,padx=5,pady=5)

button1 = tkinter.Button(frame,text="Enter", command=bmi)
button1.grid(row=2,column=1,padx=5,pady=5)

result_label = tkinter.Label(frame, text="")
result_label.grid(row=3,column=0,columnspan=2,padx=5,pady=5)

opinion_label = tkinter.Label(frame, text="")
opinion_label.grid(row=4, column=0, padx=5,pady=5)


windows.mainloop()
