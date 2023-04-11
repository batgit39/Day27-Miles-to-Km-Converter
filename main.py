from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_ans.config(text = f"{km}")

window = Tk()
window.title("Miles to Km")

miles_input = Entry()
miles_input.grid(column = 1, row = 0)

miles_label = Label(text = "Miles")
miles_label.grid(column = 2, row = 0)

equal_to = Label(text = "is equal to ")
equal_to.grid(column = 0, row = 1)

km_ans = Label(text = "0")
km_ans.grid(column = 1, row = 1)

km_label = Label(text = "Kilometers")
km_label.grid(column = 2, row = 1)

calc_button = Button(text = "Calculate", command = miles_to_km)
calc_button.grid(column = 1, row = 2)
window.mainloop()


