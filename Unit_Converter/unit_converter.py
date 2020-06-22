from tkinter import *
from tkinter.ttk import Combobox
import decimal

# create window class
window = Tk()

# constants
WIDTH = 450 #window.winfo_screenwidth()
HEIGHT = 300
XPOS = 50
YPOS = 100
screen_size = str(WIDTH) + 'x' + str(HEIGHT)# + ' + ' + str(XPOS) + ' + ' + str(YPOS)

units = {
    "length": {
        "meters": {
            "meters": lambda x: x,
            "yards": lambda x: 1.0936 * x,
            "feet": lambda x: 3.28084 * x,
            "centimeters": lambda x: 100 * x,
            "kilometers": lambda x: x / 1000.0,
            "miles": lambda x: x / 1000.0 / 1.60934
        },
        "yards": {
            "yards": lambda x: x,
            "meters": lambda x: x / 1.0936,
            "centimeters": lambda x: x / 1.0936 * 100,
            "feet": lambda x: 3 * x,
            "kilometers": lambda x: 0.0009144 * x,
            "miles": lambda x: 0.0009144 * x / 1.60934
        },
        "centimeters": {
            "centimeters": lambda x: x,
            "meters": lambda x: x / 100.0,
            "yards": lambda x: x * 1.0936 / 100,
            "feet": lambda x: x * 3.28084 / 100,
            "miles": lambda x: x * 100 * 1000 / 1.60934
        },
        "feet": {
            "feet": lambda x: x,
            "meters": lambda x: x / 3.28084,
            "yards": lambda x: x / 3.0,
            "centimeters": lambda x: x * 100 / 3.28084,
            "kilometers": lambda x: x * 3.28084 / 1000,
            "miles": lambda x: x * 3.28084 / 1000 / 1.60934
        },
        "miles": {
            "miles": lambda x: x,
            "kilometers": lambda x: 1.60934 * x,
            "meters": lambda x: 1.60934 * x * 1000,
            "centimeters": lambda x: 1.60934 * x * 1000 * 100,
            "feet": lambda x: 5280 * x,
            "yards": lambda x: 5280 * x / 3.0
        },
        "kilometers": {
            "kilometers": lambda x: x,
            "meters": lambda x: x * 1000,
            "centimeters": lambda x: x * 1000 * 100,
            "miles": lambda x: x / 1.60934,
            "yards": lambda x: x * 1093.61,
            "feet": lambda x: x * 1093.61 * 3
        }
    },
    "temperature": {
        "celsius": {
            "celsius": lambda x: x,
            "fahrenheit": lambda x: 1.8 * x + 32,
            "kelvin": lambda x: x + 273,
        },
        "fahrenheit": {
            "fahrenheit": lambda x: x,
            "celsius": lambda x: (x - 32) * 5.0 / 9.0,
            "kelvin": lambda x: (x - 32) * 5.0 / 9.0 + 273,
        },
        "kelvin": {
            "kelvin": lambda x: x,
            "celsius": lambda x: x - 273,
            "fahrenheit": lambda x: 1.8 * (x - 273) + 32,
        }
    }
}

def updateSelection(event):
    cb1['values'] = tuple(units[Categorycb.get().lower()].keys())
    cb2['values'] = tuple(units[Categorycb.get().lower()].keys())

def convert():
    # gets units slected
    units1 = cb1.get()
    units2 = cb2.get()

    # gets number entered on left
    entry = txtfld1.get()

    # converts to new units
    newValue = calculate(entry, units1, units2)

    # displays new value
    txtfld2.delete(0, END)
    txtfld2.insert(0, newValue)

def calculate(entry, units1, units2):
    
    # Area, length, etc
    unitType = Categorycb.get().lower()

    # check if same units then switch
    if units1 == units2:
        newValue = entry

    # checks if entry is a letter
    elif entry.isdigit() == False:
        newValue = 420

    else:
        entry = float(entry)
        # get formula to covert from dict 'units' above
        for unit_types in units:
            if unit_types == unitType:
                # loops through unit categories (feet, inches, etc) for units1
                for unit_names_1 in units[unit_types]:
                    if unit_names_1 == units1:
                        # loops through unit categories (feet, inches, etc) for units2 inside of unit1
                        for unit_names_2 in units[unit_types][unit_names_1]:
                            if unit_names_2 == units2:
                                # using function, find new value
                                newValue = (units[unit_types][unit_names_1][unit_names_2](entry))

                                # gets length of number
                                newValueLength = len(str(abs(newValue)))

                                # scientific notation if num is too big to fit FIXME
                                if newValueLength >= 8:
                                    newValue = "{:.4e}".format(newValue)

                                return newValue


# widgets-------------------------------------------

# Length, area, etc
Categorycb = Combobox(window, values=tuple([x.capitalize() for x in units.keys()]), width = 20) #list(units.keys())
Categorycb.place(x=WIDTH/2-70, y=38)
Categorycb.bind('<<ComboboxSelected>>', updateSelection)

# Labels
lbl1 = Label(window, text = 'Convert this', font = ('Helvetica, 12'))
lbl1.place(x=10, y=100)

lbl2 = Label(window, text = 'to this', font = ('Helvetica, 12'))
lbl2.place(x=255, y=100)

arrowlbl = Label(window, text = '-->')
arrowlbl.place(x=WIDTH/2 - 10, y=HEIGHT/2)

# Text fields
txtfld1 = Entry(window, text="entry1", width = 10, bd = 2)
txtfld1.place(x=13, y=HEIGHT/2)
txtfld1.bind("<KeyRelease>", lambda value : convert()) # auto converts as user types

txtfld2 = Entry(window, text="entry2", width = 10, bd = 2)
txtfld2.place(x=258, y=HEIGHT/2)

# Dropdown boxes
cb1 = Combobox(window, width = 15)
cb1.place(x=80, y=HEIGHT/2)

cb2 = Combobox(window, width = 15)
cb2.place(x=325, y=HEIGHT/2)

# btn = Button(window, text = "Calculate", fg = 'black', command = button_convert)
# btn.place(x=WIDTH/2 - 35, y=HEIGHT/2 + 45)

window.title('Unit Converter')
window.geometry(screen_size) # width x height + xpos + ypos
window.mainloop()
