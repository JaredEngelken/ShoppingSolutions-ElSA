### A place for some tkinter widgets ###
from Tkinter import*
import tkFont

### GUI definitions ###
win = Tk()
win.title("My Simple GUI")
myFont = tkFont.Font(family = 'Helvetica', size = 12, weight = "bold")

leftFrame = Frame(win)
leftFrame.pack(side = LEFT)
rightFrame = Frame(win)
rightFrame.pack(side = RIGHT)
midFrame = Frame(win)
midFrame.pack(side = RIGHT)

### Variable definitions for widgts ###
checkVal1 = IntVar()
checkVal2 = IntVar()
sliderVal = DoubleVar()
rad = IntVar()

### Event Functions ###
def buttonPress():
    print('Slider value is {}' .format(sliderVal.get()))
def checkToggle():
    print('\nCheckbox #1  #2\n        {}  {}' .format(checkVal1.get(), checkVal2.get()))
def checkRadio():
    select = "Radio button " + str(rad.get()) + " selected"
    label.config(text = select)
def close():
    win.destroy() #close GUI

### Widgets ###
# Button - triggers a command when it is pressed
myButton = Button(midFrame, text = 'load', font = myFont, command = buttonPress, bg = 'bisque2', height = 1)
    #widgetName = widgetType(frame, text, font, what it does, base color, size)
myButton.pack(side = BOTTOM)
    #packs the given widget into the specified frame with all the other widgets in that frame with a certain location if given eg. BOTTOM

# 2 checkboxes - update attached variables and call command when toggled
check1 = Checkbutton(leftFrame, text = 'Lights ', variable = checkVal1, command = checkToggle)
check1.pack() 
check2 = Checkbutton(leftFrame, text = 'Sprinkler ', variable = checkVal2, command = checkToggle)
check2.pack()

# Radio buttons - good for mutually exclusive options
label = Label(leftFrame)
label.pack()
label.config(text = "No option selected")
R1 = Radiobutton(leftFrame, text = 'Option 1', variable = rad, value = 1, command = checkRadio)
R1.pack() 
R2 = Radiobutton(leftFrame, text = 'Option 2', variable = rad, value = 2, command = checkRadio)
R2.pack()

# Slider Bar - good for continuous parameter adjustment
slider = Scale(midFrame, variable = sliderVal, from_=100.0, to=0.0) #from is the top of the scale!
slider.pack()

# Spinbox - selectfrom a range of predetermined values
numOption = Spinbox(rightFrame, from_=1, to=10, width = 5)
numOption.pack(side = TOP)

# Exit button - closes the GUI
exitButton = Button(rightFrame, text = 'Exit', font = myFont, command = close, bg = 'red', width = 6)
exitButton.pack(side = BOTTOM)

win.mainloop() #loops forever
