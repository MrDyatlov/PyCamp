from tkinter import *

# FONTs
FONT = ("Bahnschrift", 11, "normal")
FONT2 = ("Arial", 9, "normal")



# window
window = Tk()
window.title("BMI Calculater")
window.minsize(width=200, height=200)
#window.attributes("-fullscreen", True)


# open int the middle | open little above-average
#window.eval('tk::PlaceWindow . center')
window.update()
width_s = window.winfo_screenwidth()
height_s = window.winfo_screenheight()
width_w = window.winfo_width()
height_w = window.winfo_height()
x = (width_s / 2) - (width_w / 2)
y = (height_s / 2) - (height_w)
window.geometry('%dx%d+%d+%d' % (width_w, height_w, x, y))


# only number entry func
def only_numbers(value):
    return value.isdigit()

validation = window.register(only_numbers)

# weight label
w_label = Label(text="Weight(kg)", font=FONT)
window.config(pady=10)
w_label.pack()

# weight entry
w_entry = Entry(window, validate="key", validatecommand=(validation, '%S'), width=20)
w_entry.focus()
w_entry.pack()


# height label
h_label = Label(text="Height(cm)", font=FONT)
h_label.config(pady=10)
h_label.pack()

# height entry
h_entry = Entry(window, validate="key", validatecommand=(validation, '%S'), width=20)
h_entry.pack()


bmi_label = None
# calculate func
def calculate():
    h = h_entry.get()
    w = w_entry.get()
    bmi = float(w) / ((float(h) / 100)**2)

    global bmi_label

    if bmi_label is not None:
        bmi_label.destroy()
        if bmi <= 18.4:
            bmi_label = Label(text="Your BMI {}.Skinny boy-h.".format(format(bmi, '.1f')), font=FONT2)
            bmi_label.pack()
        elif bmi >= 18.5 and bmi <= 24.9:
            bmi_label = Label(text=f"Your BMI {format(bmi, '.1f')}. Normal.", font=FONT2)
            bmi_label.pack()
        elif bmi >= 25.0 and bmi <= 39.9:
            bmi_label = Label(text="Your BMI {}. Overweight.".format(format(bmi, '.1f')), font=FONT2)
            bmi_label.pack()
        else:
            bmi_label = Label(text="Your BMI ?. Sorry we can't calculate. Lose some weight and try again.", font=FONT2, wraplength=200)
            bmi_label.pack()
    else:
        if bmi <= 18.4:
            bmi_label = Label(text="Your BMI {}.Skinny boy-h.".format(format(bmi, '.1f')), font=FONT2)
            bmi_label.pack()
        elif bmi >= 18.5 and bmi <= 24.9:
            bmi_label = Label(text=f"Your BMI {format(bmi, '.1f')}. Normal.", font=FONT2)
            bmi_label.pack()
        elif bmi >= 25.0 and bmi <= 39.9:
            bmi_label = Label(text="Your BMI {}. Overweight.".format(format(bmi, '.1f')), font=FONT2)
            bmi_label.pack()
        else:
            bmi_label = Label(text="Your BMI ?. Sorry we can't calculate. Lose some weight and try again.", font=FONT2, wraplength=200)
            bmi_label.pack()

# calculate button
calculate_button = Button(text="Calculate", command=calculate, borderwidth=0)
calculate_button.config(pady=10)
calculate_button.pack()

window.mainloop()
