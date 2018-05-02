from Tkinter import *
root = Tk()
root.title("Menu Bar Example")

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

#create menu entry and sub-options
filemenu = Menu(menubar, tearoff  = 0) #tearoff determines whether the drop down menu can be pulled away
filemenu.add_command(label = "Open", command = placeholder) #opens a new window called placeholder
filemenu.add_command(label = "Save", command = placeholder)
filemenu.add_command(label = "Save as...", command = placeholder)
filemenu.add_separator() #adds a separating line between the command above and the command below
filemenu.add_command(label = "Quit", command = root.quit)
menubar.add_cascade(label = "File", menu = filemenu)
    # The order of the add_cascade functions determines tehe order of the menu options

#Create more menus
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
root.mainloop()
