from Tkinter import *
import tkFont

### GUI definitions ###
root = Tk()
root.title("ElSA")
myFont = tkFont.Font(family = 'Helvetica', size = 12, weight = "bold")

leftFrame = Frame(root)
leftFrame.pack(side = LEFT)
rightFrame = Frame(root)
rightFrame.pack(side = RIGHT)
midFrame = Frame(root)
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
    #win.destroy() #close GUI
    root.destroy()
def placeholder():
    top = Toplevel() #TopLevel means New Window
    top.title("Example Window") #name of the new window
    #Fill the popup window with the Canvas() example image
    C = Canvas(popup, bg = "blue", height = 250, width = 300)
    coord = 10, 50, 240, 210
    arc = C.create_arc(coord, start = 0, extent = 150, fill = "red")
    C.pack()
    top.mainloop()

menubar = Menu(root)

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

# Create 'File', 'GEEN3400', and 'Help' menubars and submenus
filemenu = Menu(menubar, tearoff  = 0) #tearoff determines whether the drop down menu can be pulled away
filemenu.add_command(label = "Open", command = placeholder) #opens a new window called placeholder
filemenu.add_command(label = "Save", command = placeholder)
filemenu.add_command(label = "Save as...", command = placeholder)
filemenu.add_separator() #adds a separating line between the command above and the command below
filemenu.add_command(label = "Quit", command = close)
menubar.add_cascade(label = "File", menu = filemenu)
    # The order of the add_cascade functions determines tehe order of the menu options
    
GEENmenu = Menu(menubar, tearoff = 0)
GEENmenu.add_command(label = "Amelia is cool", command = placeholder)
GEENmenu.add_command(label = "Christian is cool", command = placeholder)
GEENmenu.add_command(label = "Haley is cool", command = placeholder)
GEENmenu.add_command(label = "Jared is cool", command = placeholder)
menubar.add_cascade(label = "GEEN 3400", menu = GEENmenu)

helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "How To", command = placeholder)
helpmenu.add_separator()
helpmenu.add_command(label = "About", command = placeholder)
menubar.add_cascade(label = "Help", menu = helpmenu)

#Display the menu
root.config(menu = menubar)
root.mainloop() #loops forever
