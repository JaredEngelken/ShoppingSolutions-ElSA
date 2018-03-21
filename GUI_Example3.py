#Coded for Python 2.7#

### A place for some tkinter widgets ###
from Tkinter import*
from tkFileDialog import askopenfilename
import tkFont
import tkMessageBox
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

### GUI definitions ###
root = Tk()
root.geometry('400x200')
root.title("My Simple GUI")
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
led = LED(14)

### Event Functions ###
def buttonPress():
    print('Slider value is {}' .format(sliderVal.get()))
def checkToggle():
    print('\nCheckbox #1  #2\n        {}  {}' .format(checkVal1.get(), checkVal2.get()))
def checkRadio():
    select = "Radio button " + str(rad.get()) + " selected"
    label.config(text = select)
def close():
    RPi.GPIO.cleanup() #switch off GPIO pins
    root.destroy() #close GUI
def NewFile():
    print ("New File")
def OpenFile():
    name = askopenfilename()
def About():
    print ("This is a compiled GUI example.")
def placeholder():
    popup = Toplevel() #TopLevel means New Window
    popup.title("Example Window") #name of the new window
    #Fill the popup window with the Canvas() example image
    C = Canvas(popup, bg = "blue", height = 250, width = 300)
    coord = 10, 50, 240, 210
    arc = C.create_arc(coord, start = 0, extent = 150, fill = "red")
    C.pack()
    popup.mainloop()
def error():
    tkMessageBox.showerror("Error","You messed up!")
def warning():
    tkMessageBox.showwarning("Warning","Don't mess up!")
def info():
    tkMessageBox.showinfo("Information","You've been informed!")
def ledToggle():
    if led.is_lit:
        led.off()
        ledButton['text'] = "Turn LED on!"
        print ('LED OFF')
    else:
        led.on()
        ledButton['text'] = "Turn LED off!"
        print ('LED ON')

### Widgets ###
# Button - triggers a command when it is pressed
myButton = Button(midFrame, text = 'load', font = myFont, command = buttonPress, bg = 'bisque2', height = 1)
    #widgetName = widgetType(frame, text, font, what it does, base color, size)
myButton.pack(side = BOTTOM)
    #packs the given widget into the specified frame with all the other widgets in that frame with a certain location if given eg. BOTTOM
ledButton = Button(rightFrame, text = 'Turn LED on!', font = ('Times New Roman', 15), command = ledToggle, bg = 'blue', fg = 'white', height = 1, width =12)
    #fg changes the text color while bg changes the widget color
    #You can also set the widget text font within the widget itself
ledButton.pack()

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

### Menu Bars ###
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "New", command = NewFile)
filemenu.add_command(label = "Open...", command = OpenFile)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = root.quit)

GEENmenu = Menu(menu)
menu.add_cascade(label = "GEEN 3400", menu = GEENmenu)
GEENmenu.add_command(label = "Amelia is cool", command = placeholder)
GEENmenu.add_command(label = "Christian is cool", command = placeholder)
GEENmenu.add_command(label = "Haley is cool", command = placeholder)
GEENmenu.add_command(label = "Jared is cool", command = placeholder)

helpmenu = Menu(menu, tearoff = 0)
helpmenu.add_command(label = "Info", command = info)
helpmenu.add_separator()
helpmenu.add_command(label = "Warning", command = warning)
helpmenu.add_command(label = "Error", command = error)
menu.add_cascade(label = "Help", menu = helpmenu)

### Message Box ###
tkMessageBox.showinfo("Greetings", "Welcome to this GUI example!")



mainloop() #loops forever
