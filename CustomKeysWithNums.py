import Tkinter as tk
from Tkinter import *

root = Tk()


ws = root.winfo_screenwidth()
print ws# width of the screen
hs = root.winfo_screenheight() # height of the screen
w = ws

butheight = w/250
butwidth = w/200
h = 80*butheight
# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(width=False, height=False)

##def updateSearch(searchstring):
##    search = Button(text = ''.join(searchstring))
##    search.grid(row = 0, column = 0)
    

def AllCaps():

    #______All Caps_______________________________#
    #First Row#
    Qbut = Button(cntr.row1, text = 'Q', bg = 'white', command = lambda j='Q': Caps2Lower(j))
    Qbut.grid(column = 1, row = 1)
    Qbut.config(height = butheight, width = butwidth)

    Wbut = Button(cntr.row1, text = 'W', bg = 'white', command = lambda j='W': Caps2Lower(j))
    Wbut.grid(column = 2, row = 1)
    Wbut.config(height = butheight, width = butwidth)

    Ebut = Button(cntr.row1, text = 'E', bg = 'white', command = lambda j='E': Caps2Lower(j))
    Ebut.grid(column = 3, row = 1)
    Ebut.config(height = butheight, width = butwidth)

    Rbut = Button(cntr.row1, text = 'R', bg = 'white', command = lambda j='R': Caps2Lower(j))
    Rbut.grid(column = 4, row = 1)
    Rbut.config(height = butheight, width = butwidth)

    Tbut = Button(cntr.row1, text = 'T', bg = 'white', command = lambda j='T': Caps2Lower(j))
    Tbut.grid(column = 5, row = 1)
    Tbut.config(height = butheight, width = butwidth)

    Ybut = Button(cntr.row1, text = 'Y', bg = 'white', command = lambda j='Y': Caps2Lower(j))
    Ybut.grid(column = 6, row = 1)
    Ybut.config(height = butheight, width = butwidth)

    Ubut = Button(cntr.row1, text = 'U', bg = 'white', command = lambda j='U': Caps2Lower(j))
    Ubut.grid(column = 7, row = 1)
    Ubut.config(height = butheight, width = butwidth)

    Ibut = Button(cntr.row1, text = 'I', bg = 'white', command = lambda j='I': Caps2Lower(j))
    Ibut.grid(column = 8, row = 1)
    Ibut.config(height = butheight, width = butwidth)

    Obut = Button(cntr.row1, text = 'O', bg = 'white', command = lambda j='O': Caps2Lower(j))
    Obut.grid(column = 9, row = 1)
    Obut.config(height = butheight, width = butwidth)

    Pbut = Button(cntr.row1, text = 'P', bg = 'white', command = lambda j='P': Caps2Lower(j))
    Pbut.grid(column = 10, row = 1)
    Pbut.config(height = butheight, width = butwidth)

    #IF PADDING NEEDED --> Obut.grid(column = 9, row = 1, padx = w/40, pady = h/40)

    #Second Row#
    Abut = Button(cntr.row2, text = 'A', bg = 'white', command = lambda j='A': Caps2Lower(j))
    Abut.grid(column = 1, row = 1)
    Abut.config(height = butheight, width = butwidth)

    Sbut = Button(cntr.row2, text = 'S', bg = 'white', command = lambda j='S': Caps2Lower(j))
    Sbut.grid(column = 2, row = 1)
    Sbut.config(height = butheight, width = butwidth)

    Dbut = Button(cntr.row2, text = 'D', bg = 'white', command = lambda j='D': Caps2Lower(j))
    Dbut.grid(column = 3, row = 1)
    Dbut.config(height = butheight, width = butwidth)

    Fbut = Button(cntr.row2, text = 'F', bg = 'white', command = lambda j='F': Caps2Lower(j))
    Fbut.grid(column = 4, row = 1)
    Fbut.config(height = butheight, width = butwidth)

    Gbut = Button(cntr.row2, text = 'G', bg = 'white', command = lambda j='G': Caps2Lower(j))
    Gbut.grid(column = 5, row = 1)
    Gbut.config(height = butheight, width = butwidth)

    Hbut = Button(cntr.row2, text = 'H', bg = 'white', command = lambda j='H': Caps2Lower(j))
    Hbut.grid(column = 6, row = 1)
    Hbut.config(height = butheight, width = butwidth)

    Jbut = Button(cntr.row2, text = 'J', bg = 'white', command = lambda j='J': Caps2Lower(j))
    Jbut.grid(column = 7, row = 1)
    Jbut.config(height = butheight, width = butwidth)

    Kbut = Button(cntr.row2, text = 'K', bg = 'white', command = lambda j='K': Caps2Lower(j))
    Kbut.grid(column = 8, row = 1)
    Kbut.config(height = butheight, width = butwidth)

    Lbut = Button(cntr.row2, text = 'L', bg = 'white', command = lambda j='L': Caps2Lower(j))
    Lbut.grid(column = 9, row = 1)
    Lbut.config(height = butheight, width = butwidth)

    #Third Row#
    ShiftBut = Button(cntr.row3, text = 'Shift', bg = 'white', command = LowerCase)
    ShiftBut.grid(column = 1, row = 1)
    ShiftBut.config(height = butheight, width = butwidth*2)

    Zbut = Button(cntr.row3, text = 'Z', bg = 'white', command = lambda j='Z': Caps2Lower(j))
    Zbut.grid(column = 3, row = 1)
    Zbut.config(height = butheight, width = butwidth)

    Xbut = Button(cntr.row3, text = 'X', bg = 'white', command = lambda j='X': Caps2Lower(j))
    Xbut.grid(column = 4, row = 1)
    Xbut.config(height = butheight, width = butwidth)

    Cbut = Button(cntr.row3, text = 'C', bg = 'white', command = lambda j='C': Caps2Lower(j))
    Cbut.grid(column = 5, row = 1)
    Cbut.config(height = butheight, width = butwidth)

    Vbut = Button(cntr.row3, text = 'V', bg = 'white', command = lambda j='V': Caps2Lower(j))
    Vbut.grid(column = 6, row = 1)
    Vbut.config(height = butheight, width = butwidth)

    Bbut = Button(cntr.row3, text = 'B', bg = 'white', command = lambda j='B': Caps2Lower(j))
    Bbut.grid(column = 7, row = 1)
    Bbut.config(height = butheight, width = butwidth)

    Nbut = Button(cntr.row3, text = 'N', bg = 'white', command = lambda j='N': Caps2Lower(j))
    Nbut.grid(column = 8, row = 1)
    Nbut.config(height = butheight, width = butwidth)

    Mbut = Button(cntr.row3, text = 'M', bg = 'white', command = lambda j='M': Caps2Lower(j))
    Mbut.grid(column = 9, row = 1)
    Mbut.config(height = butheight, width = butwidth)

    DelBut = Button(cntr.row3, text = 'Delete', bg = 'white', command = delete)
    DelBut.grid(column = 10, row = 1)
    DelBut.config(height = butheight, width = butwidth*2)


    #Fourth Row#
    NumBut = Button(cntr.row4, text = '123', bg = 'white')
    NumBut.grid(column = 1, row = 1)
    NumBut.config(height = butheight, width = butwidth*2)

    Spacebut = Button(cntr.row4, text = 'Space', bg = 'white',command=lambda:action(' '))
    Spacebut.grid(column = 3, row = 1)
    Spacebut.config(height = butheight, width = butwidth*8)

    Clearbut = Button(cntr.row4, text = 'Clear Search', bg = 'white',command = clearsearch)
    Clearbut.grid(column = 4, row = 1)
    Clearbut.config(height = butheight, width = butwidth*2)

def LowerCase():
    #cntr = Frame(root)

    #______All Caps_______________________________#
    #First Row#
    Qbut = Button(cntr.row1, text = 'q', bg = 'white',command=lambda:action('q'))
    Qbut.grid(column = 1, row = 1)
    Qbut.config(height = butheight, width = butwidth)

    Wbut = Button(cntr.row1, text = 'w', bg = 'white',command=lambda:action('w'))
    Wbut.grid(column = 2, row = 1)
    Wbut.config(height = butheight, width = butwidth)

    Ebut = Button(cntr.row1, text = 'e', bg = 'white',command=lambda:action('e'))
    Ebut.grid(column = 3, row = 1)
    Ebut.config(height = butheight, width = butwidth)

    Rbut = Button(cntr.row1, text = 'r', bg = 'white',command=lambda:action('r'))
    Rbut.grid(column = 4, row = 1)
    Rbut.config(height = butheight, width = butwidth)

    Tbut = Button(cntr.row1, text = 't', bg = 'white',command=lambda:action('t'))
    Tbut.grid(column = 5, row = 1)
    Tbut.config(height = butheight, width = butwidth)

    Ybut = Button(cntr.row1, text = 'y', bg = 'white',command=lambda:action('y'))
    Ybut.grid(column = 6, row = 1)
    Ybut.config(height = butheight, width = butwidth)

    Ubut = Button(cntr.row1, text = 'u', bg = 'white',command=lambda:action('u'))
    Ubut.grid(column = 7, row = 1)
    Ubut.config(height = butheight, width = butwidth)

    Ibut = Button(cntr.row1, text = 'i', bg = 'white',command=lambda:action('i'))
    Ibut.grid(column = 8, row = 1)
    Ibut.config(height = butheight, width = butwidth)

    Obut = Button(cntr.row1, text = 'o', bg = 'white',command=lambda:action('o'))
    Obut.grid(column = 9, row = 1)
    Obut.config(height = butheight, width = butwidth)

    Pbut = Button(cntr.row1, text = 'p', bg = 'white',command=lambda:action('p'))
    Pbut.grid(column = 10, row = 1)
    Pbut.config(height = butheight, width = butwidth)


    #Second Row#
    Abut = Button(cntr.row2, text = 'a', bg = 'white',command=lambda:action('a'))
    Abut.grid(column = 1, row = 1)
    Abut.config(height = butheight, width = butwidth)

    Sbut = Button(cntr.row2, text = 's', bg = 'white',command=lambda:action('s'))
    Sbut.grid(column = 2, row = 1)
    Sbut.config(height = butheight, width = butwidth)

    Dbut = Button(cntr.row2, text = 'd', bg = 'white',command=lambda:action('d'))
    Dbut.grid(column = 3, row = 1)
    Dbut.config(height = butheight, width = butwidth)

    Fbut = Button(cntr.row2, text = 'f', bg = 'white',command=lambda:action('f'))
    Fbut.grid(column = 4, row = 1)
    Fbut.config(height = butheight, width = butwidth)

    Gbut = Button(cntr.row2, text = 'g', bg = 'white',command=lambda:action('g'))
    Gbut.grid(column = 5, row = 1)
    Gbut.config(height = butheight, width = butwidth)

    Hbut = Button(cntr.row2, text = 'h', bg = 'white',command=lambda:action('h'))
    Hbut.grid(column = 6, row = 1)
    Hbut.config(height = butheight, width = butwidth)

    Jbut = Button(cntr.row2, text = 'j', bg = 'white',command=lambda:action('j'))
    Jbut.grid(column = 7, row = 1)
    Jbut.config(height = butheight, width = butwidth)

    Kbut = Button(cntr.row2, text = 'k', bg = 'white',command=lambda:action('k'))
    Kbut.grid(column = 8, row = 1)
    Kbut.config(height = butheight, width = butwidth)

    Lbut = Button(cntr.row2, text = 'l', bg = 'white',command=lambda:action('l'))
    Lbut.grid(column = 9, row = 1)
    Lbut.config(height = butheight, width = butwidth)

    #Third Row#
    ShiftBut = Button(cntr.row3, text = 'Shift', bg = 'white', command = AllCaps)
    ShiftBut.grid(column = 1, row = 1)
    ShiftBut.config(height = butheight, width = butwidth*2)

    Zbut = Button(cntr.row3, text = 'z', bg = 'white',command=lambda:action('z'))
    Zbut.grid(column = 3, row = 1)
    Zbut.config(height = butheight, width = butwidth)

    Xbut = Button(cntr.row3, text = 'x', bg = 'white',command=lambda:action('x'))
    Xbut.grid(column = 4, row = 1)
    Xbut.config(height = butheight, width = butwidth)

    Cbut = Button(cntr.row3, text = 'c', bg = 'white',command=lambda:action('c'))
    Cbut.grid(column = 5, row = 1)
    Cbut.config(height = butheight, width = butwidth)

    Vbut = Button(cntr.row3, text = 'v', bg = 'white',command=lambda:action('v'))
    Vbut.grid(column = 6, row = 1)
    Vbut.config(height = butheight, width = butwidth)

    Bbut = Button(cntr.row3, text = 'b', bg = 'white',command=lambda:action('b'))
    Bbut.grid(column = 7, row = 1)
    Bbut.config(height = butheight, width = butwidth)

    Nbut = Button(cntr.row3, text = 'n', bg = 'white',command=lambda:action('n'))
    Nbut.grid(column = 8, row = 1)
    Nbut.config(height = butheight, width = butwidth)

    Mbut = Button(cntr.row3, text = 'm', bg = 'white',command=lambda:action('m'))
    Mbut.grid(column = 9, row = 1)
    Mbut.config(height = butheight, width = butwidth)

    DelBut = Button(cntr.row3, text = 'Delete', bg = 'white', command = delete)
    DelBut.grid(column = 10, row = 1)
    DelBut.config(height = butheight, width = butwidth*2)


    #Fourth Row#
    NumBut = Button(cntr.row4, text = '123', bg = 'white')
    NumBut.grid(column = 1, row = 1)
    NumBut.config(height = butheight, width = butwidth*2)

    Spacebut = Button(cntr.row4, text = 'Space', bg = 'white',command=lambda:action(' '))
    Spacebut.grid(column = 3, row = 1)
    Spacebut.config(height = butheight, width = butwidth*8)

    Clearbut = Button(cntr.row4, text = 'Clear Search', bg = 'white', command = clearsearch)
    Clearbut.grid(column = 4, row = 1)
    Clearbut.config(height = butheight, width = butwidth*2)

#All Called Functions
def Caps2Lower(WhichBut):
    action(WhichBut)
    LowerCase()
    
def delete():
    cntr.txt = cntr.e.get()[:-1]
    cntr.e.delete(0,END)
    cntr.e.insert(0,cntr.txt)
    if len(cntr.txt) == 0:
        AllCaps()
def clearsearch():
    cntr.e.delete(0,END)
    AllCaps()

def action(argi): 
    """pressed button's value is inserted into the end of the text area"""
    cntr.e.insert(END,argi)
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#


#_______________________________Main_Loop_________________________________#
#Frame SetUp#
cntr = Frame(root)
cntr.e = Entry(root)
cntr.e.grid(row=1,column=2,columnspan = 2, pady=3)
cntr.e.focus_set()

cntr.row0 = Frame(root)
cntr.row1 = Frame(root)
cntr.row2 = Frame(root)
cntr.row3 = Frame(root)
cntr.row4 = Frame(root)

cntr.row0.grid(row=0, padx = w/64)
cntr.row0.rowconfigure(0, weight = 1)
cntr.row1.grid(row=1, padx = w/64)
cntr.row1.rowconfigure(1, weight = 1)
cntr.row2.grid(row=2, padx = w/64)
cntr.row2.rowconfigure(2, weight = 1)
cntr.row3.grid(row=3, padx = w/64)
cntr.row3.rowconfigure(3, weight = 1)
cntr.row4.grid(row=4, padx = w/64)
cntr.row4.rowconfigure(4, weight = 1)


#Numbers#
Percentbut = Button(cntr.row0, text = '%', bg = 'white',command=lambda:action('%'))
Percentbut.grid(column = 1, row = 1)
Percentbut.config(height = butheight/2, width = butwidth)

Onebut = Button(cntr.row0, text = '1', bg = 'white',command=lambda:action('1'))
Onebut.grid(column = 2, row = 1)
Onebut.config(height = butheight/2, width = butwidth)

Twobut = Button(cntr.row0, text = '2', bg = 'white',command=lambda:action('2'))
Twobut.grid(column = 3, row = 1)
Twobut.config(height = butheight/2, width = butwidth)

Threebut = Button(cntr.row0, text = '3', bg = 'white',command=lambda:action('3'))
Threebut.grid(column = 4, row = 1)
Threebut.config(height = butheight/2, width = butwidth)

Fourbut = Button(cntr.row0, text = '4', bg = 'white',command=lambda:action('4'))
Fourbut.grid(column = 5, row = 1)
Fourbut.config(height = butheight/2, width = butwidth)

Fivebut = Button(cntr.row0, text = '5', bg = 'white',command=lambda:action('5'))
Fivebut.grid(column = 6, row = 1)
Fivebut.config(height = butheight/2, width = butwidth)

Sixbut = Button(cntr.row0, text = '6', bg = 'white',command=lambda:action('6'))
Sixbut.grid(column = 7, row = 1)
Sixbut.config(height = butheight/2, width = butwidth)

Sevenbut = Button(cntr.row0, text = '7', bg = 'white',command=lambda:action('7'))
Sevenbut.grid(column = 8, row = 1)
Sevenbut.config(height = butheight/2, width = butwidth)

Eightbut = Button(cntr.row0, text = '8', bg = 'white',command=lambda:action('8'))
Eightbut.grid(column = 9, row = 1)
Eightbut.config(height = butheight/2, width = butwidth)

Ninebut = Button(cntr.row0, text = '9', bg = 'white',command=lambda:action('9'))
Ninebut.grid(column = 10, row = 1)
Ninebut.config(height = butheight/2, width = butwidth)

Zerobut = Button(cntr.row0, text = '0', bg = 'white',command=lambda:action('0'))
Zerobut.grid(column = 11, row = 1)
Zerobut.config(height = butheight/2, width = butwidth)



#Start Program in AllCaps#
AllCaps()


root.mainloop()


