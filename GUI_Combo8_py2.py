#import tkinter in a universal way that would work for both python2 and python3
try:
    #Python 2
    import Tkinter as tk
except ImportError:
    #Python 3
    import tkinter as tk
#from Tkinter import *
import tkFont
import pandas as pd
import openpyxl
from openpyxl import load_workbook
import numpy as np
import os
import time



#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
### GUI definitions ###
root = tk.Tk()
root.title("ElSA")
myFont = tkFont.Font(family = 'Helvetica', size = 12, weight = "bold")

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

class Boom(tk.Frame):
    #global listbox
    global test_list3
    global listbox_update
    global sheet_1
    global itemlist
    global pricelist
    global on_keyrelease
    global on_select
    global topFrame1
    global leftFrame1
    global rightFrame1
    global searchButton
    global change
    global screenWidth
    global screenHeight

    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    x = (screenWidth/2) - (screenWidth/2)
    y = (screenHeight/2) - (screenHeight/2)
        
    root.geometry('%dx%d+%d+%d' % (screenWidth, screenHeight, x, y))
    root.resizable(width = False, height = False)

    print screenWidth
    print screenHeight
    
    # create all of the main containers
    topFrame1 = tk.Frame(root, bg='lightskyblue', width = 1920, height = 200, padx = 5, pady = 5)
    leftFrame1 = tk.Frame(root, bg='blue', width = 640, height = 800, padx = 5, pady = 5)
    centerFrame1 = tk.Frame(root, bg='deepskyblue', width = 640, height = 800, padx = 5, pady = 5)
    rightFrame1 = tk.Frame(root, bg='darkblue', width = 640, height = 800, padx = 5, pady = 5)
    bottomFrame1 = tk.Frame(root, bg='magenta', width = 1920, height = 200, padx = 5, pady = 5)

    # layout all of the main containers
    root.grid_rowconfigure(0, weight=1)


    topFrame1.grid(row=0, columnspan = 3, sticky="nsew")
    leftFrame1.grid(row=1, column = 0, sticky="nsew")
    centerFrame1.grid(row=1, column = 1, sticky="nsew")
    rightFrame1.grid(row=1, column = 2, sticky="nsew")
    bottomFrame1.grid(row=2, columnspan = 3, sticky="nsew")
    
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
### Event Functions ###
    def close():
        root.destroy() #close GUI
    def listbox_update(data):
        # delete previous data
        listbox.delete(0, 'end')
        # sorting data 
        data = sorted(data, key=str.lower)
        # put new data
        for item in data:
            listbox.insert('end', item)
    def on_keyrelease(event):
        # get text from entry
        value = event.widget.get()
        value = value.strip().lower()
        # get data from test_list
        if value == '':
            data = []
        else:
            data = []
            for item in test_list3:
                if value in item.lower():
                    data.append(item)                
        # update data in listbox
        listbox_update(data)
    def listbox_update(data):
        # delete previous data
        listbox.delete(0, 'end')
        # sorting data 
        data = sorted(data, key=str.lower)
        # put new data
        for item in data:
            listbox.insert('end', item)
    def gsearch():
        searchButton.destroy()
        # Search Entry
        entry = tk.Entry(topFrame1)
        entry.grid()
        entry.bind('<KeyRelease>', on_keyrelease)

        global listbox
        listbox = tk.Listbox(topFrame1)
        listbox.grid()
        listbox.bind('<<ListboxSelect>>', on_select)
        listbox_update([])
#___________________________________________________________________________GROSS STUFF BELOW___________________________________#
        tree = tk.Tk()

        ws = tree.winfo_screenwidth()
        print ws# width of the screen
        hs = tree.winfo_screenheight() # height of the screen
        w = ws

        butheight = w/250
        butwidth = w/200
        h = 80*butheight
        # calculate x and y coordinates for the Tk tree window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        # set the dimensions of the screen 
        # and where it is placed
        tree.geometry('%dx%d+%d+%d' % (w, h, x, y))
        tree.resizable(width=False, height=False)

        ##def updateSearch(searchstring):
        ##    search = Button(text = ''.join(searchstring))
        ##    search.grid(row = 0, column = 0)
            

        def AllCaps():

            #______All Caps_______________________________#
            #First Row#
            Qbut = tk.Button(cntr.row1, text = 'Q', bg = 'white', command = lambda j='Q': Caps2Lower(j))
            Qbut.grid(column = 1, row = 1)
            Qbut.config(height = butheight, width = butwidth)

            Wbut = tk.Button(cntr.row1, text = 'W', bg = 'white', command = lambda j='W': Caps2Lower(j))
            Wbut.grid(column = 2, row = 1)
            Wbut.config(height = butheight, width = butwidth)

            Ebut = tk.Button(cntr.row1, text = 'E', bg = 'white', command = lambda j='E': Caps2Lower(j))
            Ebut.grid(column = 3, row = 1)
            Ebut.config(height = butheight, width = butwidth)

            Rbut = tk.Button(cntr.row1, text = 'R', bg = 'white', command = lambda j='R': Caps2Lower(j))
            Rbut.grid(column = 4, row = 1)
            Rbut.config(height = butheight, width = butwidth)

            Tbut = tk.Button(cntr.row1, text = 'T', bg = 'white', command = lambda j='T': Caps2Lower(j))
            Tbut.grid(column = 5, row = 1)
            Tbut.config(height = butheight, width = butwidth)

            Ybut = tk.Button(cntr.row1, text = 'Y', bg = 'white', command = lambda j='Y': Caps2Lower(j))
            Ybut.grid(column = 6, row = 1)
            Ybut.config(height = butheight, width = butwidth)

            Ubut = tk.Button(cntr.row1, text = 'U', bg = 'white', command = lambda j='U': Caps2Lower(j))
            Ubut.grid(column = 7, row = 1)
            Ubut.config(height = butheight, width = butwidth)

            Ibut = tk.Button(cntr.row1, text = 'I', bg = 'white', command = lambda j='I': Caps2Lower(j))
            Ibut.grid(column = 8, row = 1)
            Ibut.config(height = butheight, width = butwidth)

            Obut = tk.Button(cntr.row1, text = 'O', bg = 'white', command = lambda j='O': Caps2Lower(j))
            Obut.grid(column = 9, row = 1)
            Obut.config(height = butheight, width = butwidth)

            Pbut = tk.Button(cntr.row1, text = 'P', bg = 'white', command = lambda j='P': Caps2Lower(j))
            Pbut.grid(column = 10, row = 1)
            Pbut.config(height = butheight, width = butwidth)

            #IF PADDING NEEDED --> Obut.grid(column = 9, row = 1, padx = w/40, pady = h/40)

            #Second Row#
            Abut = tk.Button(cntr.row2, text = 'A', bg = 'white', command = lambda j='A': Caps2Lower(j))
            Abut.grid(column = 1, row = 1)
            Abut.config(height = butheight, width = butwidth)

            Sbut = tk.Button(cntr.row2, text = 'S', bg = 'white', command = lambda j='S': Caps2Lower(j))
            Sbut.grid(column = 2, row = 1)
            Sbut.config(height = butheight, width = butwidth)

            Dbut = tk.Button(cntr.row2, text = 'D', bg = 'white', command = lambda j='D': Caps2Lower(j))
            Dbut.grid(column = 3, row = 1)
            Dbut.config(height = butheight, width = butwidth)

            Fbut = tk.Button(cntr.row2, text = 'F', bg = 'white', command = lambda j='F': Caps2Lower(j))
            Fbut.grid(column = 4, row = 1)
            Fbut.config(height = butheight, width = butwidth)

            Gbut = tk.Button(cntr.row2, text = 'G', bg = 'white', command = lambda j='G': Caps2Lower(j))
            Gbut.grid(column = 5, row = 1)
            Gbut.config(height = butheight, width = butwidth)

            Hbut = tk.Button(cntr.row2, text = 'H', bg = 'white', command = lambda j='H': Caps2Lower(j))
            Hbut.grid(column = 6, row = 1)
            Hbut.config(height = butheight, width = butwidth)

            Jbut = tk.Button(cntr.row2, text = 'J', bg = 'white', command = lambda j='J': Caps2Lower(j))
            Jbut.grid(column = 7, row = 1)
            Jbut.config(height = butheight, width = butwidth)

            Kbut = tk.Button(cntr.row2, text = 'K', bg = 'white', command = lambda j='K': Caps2Lower(j))
            Kbut.grid(column = 8, row = 1)
            Kbut.config(height = butheight, width = butwidth)

            Lbut = tk.Button(cntr.row2, text = 'L', bg = 'white', command = lambda j='L': Caps2Lower(j))
            Lbut.grid(column = 9, row = 1)
            Lbut.config(height = butheight, width = butwidth)

            #Third Row#
            ShiftBut = tk.Button(cntr.row3, text = 'Shift', bg = 'white', command = LowerCase)
            ShiftBut.grid(column = 1, row = 1)
            ShiftBut.config(height = butheight, width = butwidth*2)

            Zbut = tk.Button(cntr.row3, text = 'Z', bg = 'white', command = lambda j='Z': Caps2Lower(j))
            Zbut.grid(column = 3, row = 1)
            Zbut.config(height = butheight, width = butwidth)

            Xbut = tk.Button(cntr.row3, text = 'X', bg = 'white', command = lambda j='X': Caps2Lower(j))
            Xbut.grid(column = 4, row = 1)
            Xbut.config(height = butheight, width = butwidth)

            Cbut = tk.Button(cntr.row3, text = 'C', bg = 'white', command = lambda j='C': Caps2Lower(j))
            Cbut.grid(column = 5, row = 1)
            Cbut.config(height = butheight, width = butwidth)

            Vbut = tk.Button(cntr.row3, text = 'V', bg = 'white', command = lambda j='V': Caps2Lower(j))
            Vbut.grid(column = 6, row = 1)
            Vbut.config(height = butheight, width = butwidth)

            Bbut = tk.Button(cntr.row3, text = 'B', bg = 'white', command = lambda j='B': Caps2Lower(j))
            Bbut.grid(column = 7, row = 1)
            Bbut.config(height = butheight, width = butwidth)

            Nbut = tk.Button(cntr.row3, text = 'N', bg = 'white', command = lambda j='N': Caps2Lower(j))
            Nbut.grid(column = 8, row = 1)
            Nbut.config(height = butheight, width = butwidth)

            Mbut = tk.Button(cntr.row3, text = 'M', bg = 'white', command = lambda j='M': Caps2Lower(j))
            Mbut.grid(column = 9, row = 1)
            Mbut.config(height = butheight, width = butwidth)

            DelBut = tk.Button(cntr.row3, text = 'Delete', bg = 'white', command = delete)
            DelBut.grid(column = 10, row = 1)
            DelBut.config(height = butheight, width = butwidth*2)


            #Fourth Row#
            NumBut = tk.Button(cntr.row4, text = '123', bg = 'white')
            NumBut.grid(column = 1, row = 1)
            NumBut.config(height = butheight, width = butwidth*2)

            Spacebut = tk.Button(cntr.row4, text = 'Space', bg = 'white',command=lambda:action(' '))
            Spacebut.grid(column = 3, row = 1)
            Spacebut.config(height = butheight, width = butwidth*8)

            Clearbut = tk.Button(cntr.row4, text = 'Clear Search', bg = 'white',command = clearsearch)
            Clearbut.grid(column = 4, row = 1)
            Clearbut.config(height = butheight, width = butwidth*2)

        def LowerCase():
            #cntr = Frame(tree)

            #______All Caps_______________________________#
            #First Row#
            Qbut = tk.Button(cntr.row1, text = 'q', bg = 'white',command=lambda:action('q'))
            Qbut.grid(column = 1, row = 1)
            Qbut.config(height = butheight, width = butwidth)

            Wbut = tk.Button(cntr.row1, text = 'w', bg = 'white',command=lambda:action('w'))
            Wbut.grid(column = 2, row = 1)
            Wbut.config(height = butheight, width = butwidth)

            Ebut = tk.Button(cntr.row1, text = 'e', bg = 'white',command=lambda:action('e'))
            Ebut.grid(column = 3, row = 1)
            Ebut.config(height = butheight, width = butwidth)

            Rbut = tk.Button(cntr.row1, text = 'r', bg = 'white',command=lambda:action('r'))
            Rbut.grid(column = 4, row = 1)
            Rbut.config(height = butheight, width = butwidth)

            Tbut = tk.Button(cntr.row1, text = 't', bg = 'white',command=lambda:action('t'))
            Tbut.grid(column = 5, row = 1)
            Tbut.config(height = butheight, width = butwidth)

            Ybut = tk.Button(cntr.row1, text = 'y', bg = 'white',command=lambda:action('y'))
            Ybut.grid(column = 6, row = 1)
            Ybut.config(height = butheight, width = butwidth)

            Ubut = tk.Button(cntr.row1, text = 'u', bg = 'white',command=lambda:action('u'))
            Ubut.grid(column = 7, row = 1)
            Ubut.config(height = butheight, width = butwidth)

            Ibut = tk.Button(cntr.row1, text = 'i', bg = 'white',command=lambda:action('i'))
            Ibut.grid(column = 8, row = 1)
            Ibut.config(height = butheight, width = butwidth)

            Obut = tk.Button(cntr.row1, text = 'o', bg = 'white',command=lambda:action('o'))
            Obut.grid(column = 9, row = 1)
            Obut.config(height = butheight, width = butwidth)

            Pbut = tk.Button(cntr.row1, text = 'p', bg = 'white',command=lambda:action('p'))
            Pbut.grid(column = 10, row = 1)
            Pbut.config(height = butheight, width = butwidth)


            #Second Row#
            Abut = tk.Button(cntr.row2, text = 'a', bg = 'white',command=lambda:action('a'))
            Abut.grid(column = 1, row = 1)
            Abut.config(height = butheight, width = butwidth)

            Sbut = tk.Button(cntr.row2, text = 's', bg = 'white',command=lambda:action('s'))
            Sbut.grid(column = 2, row = 1)
            Sbut.config(height = butheight, width = butwidth)

            Dbut = tk.Button(cntr.row2, text = 'd', bg = 'white',command=lambda:action('d'))
            Dbut.grid(column = 3, row = 1)
            Dbut.config(height = butheight, width = butwidth)

            Fbut = tk.Button(cntr.row2, text = 'f', bg = 'white',command=lambda:action('f'))
            Fbut.grid(column = 4, row = 1)
            Fbut.config(height = butheight, width = butwidth)

            Gbut = tk.Button(cntr.row2, text = 'g', bg = 'white',command=lambda:action('g'))
            Gbut.grid(column = 5, row = 1)
            Gbut.config(height = butheight, width = butwidth)

            Hbut = tk.Button(cntr.row2, text = 'h', bg = 'white',command=lambda:action('h'))
            Hbut.grid(column = 6, row = 1)
            Hbut.config(height = butheight, width = butwidth)

            Jbut = tk.Button(cntr.row2, text = 'j', bg = 'white',command=lambda:action('j'))
            Jbut.grid(column = 7, row = 1)
            Jbut.config(height = butheight, width = butwidth)

            Kbut = tk.Button(cntr.row2, text = 'k', bg = 'white',command=lambda:action('k'))
            Kbut.grid(column = 8, row = 1)
            Kbut.config(height = butheight, width = butwidth)

            Lbut = tk.Button(cntr.row2, text = 'l', bg = 'white',command=lambda:action('l'))
            Lbut.grid(column = 9, row = 1)
            Lbut.config(height = butheight, width = butwidth)

            #Third Row#
            ShiftBut = tk.Button(cntr.row3, text = 'Shift', bg = 'white', command = AllCaps)
            ShiftBut.grid(column = 1, row = 1)
            ShiftBut.config(height = butheight, width = butwidth*2)

            Zbut = tk.Button(cntr.row3, text = 'z', bg = 'white',command=lambda:action('z'))
            Zbut.grid(column = 3, row = 1)
            Zbut.config(height = butheight, width = butwidth)

            Xbut = tk.Button(cntr.row3, text = 'x', bg = 'white',command=lambda:action('x'))
            Xbut.grid(column = 4, row = 1)
            Xbut.config(height = butheight, width = butwidth)

            Cbut = tk.Button(cntr.row3, text = 'c', bg = 'white',command=lambda:action('c'))
            Cbut.grid(column = 5, row = 1)
            Cbut.config(height = butheight, width = butwidth)

            Vbut = tk.Button(cntr.row3, text = 'v', bg = 'white',command=lambda:action('v'))
            Vbut.grid(column = 6, row = 1)
            Vbut.config(height = butheight, width = butwidth)

            Bbut = tk.Button(cntr.row3, text = 'b', bg = 'white',command=lambda:action('b'))
            Bbut.grid(column = 7, row = 1)
            Bbut.config(height = butheight, width = butwidth)

            Nbut = tk.Button(cntr.row3, text = 'n', bg = 'white',command=lambda:action('n'))
            Nbut.grid(column = 8, row = 1)
            Nbut.config(height = butheight, width = butwidth)

            Mbut = tk.Button(cntr.row3, text = 'm', bg = 'white',command=lambda:action('m'))
            Mbut.grid(column = 9, row = 1)
            Mbut.config(height = butheight, width = butwidth)

            DelBut = tk.Button(cntr.row3, text = 'Delete', bg = 'white', command = delete)
            DelBut.grid(column = 10, row = 1)
            DelBut.config(height = butheight, width = butwidth*2)


            #Fourth Row#
            NumBut = tk.Button(cntr.row4, text = '123', bg = 'white')
            NumBut.grid(column = 1, row = 1)
            NumBut.config(height = butheight, width = butwidth*2)

            Spacebut = tk.Button(cntr.row4, text = 'Space', bg = 'white',command=lambda:action(' '))
            Spacebut.grid(column = 3, row = 1)
            Spacebut.config(height = butheight, width = butwidth*8)

            Clearbut = tk.Button(cntr.row4, text = 'Clear Search', bg = 'white', command = clearsearch)
            Clearbut.grid(column = 4, row = 1)
            Clearbut.config(height = butheight, width = butwidth*2)

        #All Called Functions
        def Caps2Lower(WhichBut):
            action(WhichBut)
            LowerCase()
            
        def delete():
            cntr.txt = cntr.entry.get()[:-1]
            cntr.entry.delete(0,END)
            cntr.entry.insert(0,cntr.txt)
            if len(cntr.txt) == 0:
                AllCaps()
        def clearsearch():
            cntr.entry.delete(0,END)
            AllCaps()

        def action(argi): 
            """pressed button's value is inserted into the end of the text area"""
            cntr.entry.insert(END,argi)
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#


        #_______________________________Main_Loop_________________________________#
        #Frame SetUp#
        cntr = tk.Frame(tree)

        cntr.row0 = tk.Frame(tree)
        cntr.row1 = tk.Frame(tree)
        cntr.row2 = tk.Frame(tree)
        cntr.row3 = tk.Frame(tree)
        cntr.row4 = tk.Frame(tree)

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
        Percentbut = tk.Button(cntr.row0, text = '%', bg = 'white',command=lambda:action('%'))
        Percentbut.grid(column = 1, row = 1)
        Percentbut.config(height = butheight/2, width = butwidth)

        Onebut = tk.Button(cntr.row0, text = '1', bg = 'white',command=lambda:action('1'))
        Onebut.grid(column = 2, row = 1)
        Onebut.config(height = butheight/2, width = butwidth)

        Twobut = tk.Button(cntr.row0, text = '2', bg = 'white',command=lambda:action('2'))
        Twobut.grid(column = 3, row = 1)
        Twobut.config(height = butheight/2, width = butwidth)

        Threebut = tk.Button(cntr.row0, text = '3', bg = 'white',command=lambda:action('3'))
        Threebut.grid(column = 4, row = 1)
        Threebut.config(height = butheight/2, width = butwidth)

        Fourbut = tk.Button(cntr.row0, text = '4', bg = 'white',command=lambda:action('4'))
        Fourbut.grid(column = 5, row = 1)
        Fourbut.config(height = butheight/2, width = butwidth)

        Fivebut = tk.Button(cntr.row0, text = '5', bg = 'white',command=lambda:action('5'))
        Fivebut.grid(column = 6, row = 1)
        Fivebut.config(height = butheight/2, width = butwidth)

        Sixbut = tk.Button(cntr.row0, text = '6', bg = 'white',command=lambda:action('6'))
        Sixbut.grid(column = 7, row = 1)
        Sixbut.config(height = butheight/2, width = butwidth)

        Sevenbut = tk.Button(cntr.row0, text = '7', bg = 'white',command=lambda:action('7'))
        Sevenbut.grid(column = 8, row = 1)
        Sevenbut.config(height = butheight/2, width = butwidth)

        Eightbut = tk.Button(cntr.row0, text = '8', bg = 'white',command=lambda:action('8'))
        Eightbut.grid(column = 9, row = 1)
        Eightbut.config(height = butheight/2, width = butwidth)

        Ninebut = tk.Button(cntr.row0, text = '9', bg = 'white',command=lambda:action('9'))
        Ninebut.grid(column = 10, row = 1)
        Ninebut.config(height = butheight/2, width = butwidth)

        Zerobut = tk.Button(cntr.row0, text = '0', bg = 'white',command=lambda:action('0'))
        Zerobut.grid(column = 11, row = 1)
        Zerobut.config(height = butheight/2, width = butwidth)



        #Start Program in AllCaps#
        AllCaps()
        tree.mainloop()
#_______________________________________________________________________________________________________________________________#

        
    def on_select(event):
    # Takes user selection and removes price information in order to use selected item to search for other info
    #______________________________________________________________________________________________________________#
        grabitem = event.widget.get(event.widget.curselection()) #the initial selection of the user
        for t in range(0, sheet_1.max_row):
            itemlist[t] = sheet_1.cell(row = t+1, column = 1).value #Pulls all strings from column 1 describing item
            itemlist2 = ['{} '.format(elem) for elem in itemlist] #Formats to remove 'u' type from string

            pricelist[t] = ('   |${}|'.format(sheet_1.cell(row = t+1, column = 3).value)) #Pulls all strings from column 3 describing price
            pricelist2 = ['{} '.format(elem) for elem in pricelist] #Formats to remove 'u' type from string
        
        test_list = map(str.__add__, itemlist2, pricelist2) #combines lists into one in order to find index within list of selected item
        test_list3 = filter(lambda a: a != 'Item    |$Cost| ', test_list) #clean up list
        print test_list3

        grabitemindex = test_list3.index(grabitem)+1 #finds index of selected item
        pricelength = len(pricelist2[grabitemindex]) #finds length of displayed price info in order to determine how long of a string to delete

        item = grabitem[:-pricelength] #deletes price info leaving only item title
    #______________________________________________________________________________________________________________#

    #Below runs item through Pandas
        file = 'Grocery.xlsx'
        xl = pd.ExcelFile(file)
        
        # Generate DataFrame from imported spreadsheet and print
        df1 = xl.parse('Page 1')
        print (df1)

        #regenerate list of items in inventory
        list1 = [""]*(sheet_1.max_row)
        for t in range(0, sheet_1.max_row):
            list1[t] = sheet_1.cell(row = t+1, column = 1).value
            list2 = filter(lambda a: a != "Item", list1)
            list3 = ['{} '.format(elem) for elem in list2]
        print list3
        
        rowselect = list3.index(item)
        row4search = rowselect+2 #find in which row item exists
        print row4search


        code=sheet_1.cell(row=row4search, column=2).value #Fill in data to blank arrays from spreadsheet
        cost=sheet_1.cell(row=row4search, column=3).value
        aisle=sheet_1.cell(row=row4search, column=4).value
        bay=sheet_1.cell(row=row4search, column=5).value

        # Full info display
        print (sheet_1.cell(row=row4search, column=1).value)
        print ('Barcode {}'.format(code)) #Display desired item barcode
        print ('Price ${}'.format(cost)) #Display desired item cost
        print ('Aisle {}'.format(aisle)) #Display desired item isle
        print ('Bay {}'.format(bay)) #Display desired item bay

        # CART LIST
        def addCartList():
            shoppingCartButton = tk.Button(rightFrame1, text = item, bg = 'thistle')
            #shoppingCartButton.grid(column = 1)
            shoppingCartButton.pack()
        
        # SHOPPING LIST
        addCartButton = tk.Button(leftFrame1, text = 'ADD '+item+' $'+str(cost)+' Aisle '+str(aisle), command = addCartList, bg = 'plum')
        #addCartButton.grid(column = 1)
        addCartButton.pack()
        
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
# --- Main --- #

    #Loads workbook to look for items in inventory 
    wb = load_workbook('Grocery.xlsx')
    sheet_1 = wb['Page 1']
    itemlist = [""]*(sheet_1.max_row)
    pricelist = [""]*(sheet_1.max_row)
    for t in range(0, sheet_1.max_row):
        itemlist[t] = sheet_1.cell(row = t+1, column = 1).value #Pulls all strings from column 1
        itemlist2 = ['{} '.format(elem) for elem in itemlist] #Formats to remove 'u' type from string

        pricelist[t] = ('   |${}|'.format(sheet_1.cell(row = t+1, column = 3).value)) #Pulls all strings from column 3
        pricelist2 = ['{} '.format(elem) for elem in pricelist] #Formats to remove 'u' type from string
    
    test_list = map(str.__add__, itemlist2, pricelist2)
    
    test_list3 = filter(lambda a: a != 'Item    |$Cost| ', test_list) #Combines item with price info for user
    print test_list3

    # Shopping Cart Label
    shoppingCartLabel = tk.Label(rightFrame1, text = "Your Shopping Cart:", bg = 'orchid', fg = 'floralwhite', font = myFont)
    #shoppingCartLabel.grid(column = 1, row = 1, rowspan = 2, padx = 10)
    shoppingCartLabel.pack()
    
    # Shopping List Label
    addCartLabel = tk.Label(leftFrame1, text = "Shopping List\nClick to add items to cart: ", bg = 'cornflowerblue', fg = 'lavenderblush', font = myFont)
    #addCartLabel.grid(column = 1, row = 1, padx = 10)
    addCartLabel.pack()
    
    # Search label
    searchButton = tk.Button(topFrame1, text = 'Search', bg = 'mediumslateblue', fg = 'snow', font = myFont, command = gsearch)
    #searchButton = tk.Button(topFrame1, text = 'Search', bg = 'mediumslateblue', fg = 'snow', font = myFont, command = change)
    searchButton.grid(column = 1, row = 1, rowspan = 2)    

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#


#Display the menu
frame01 = Boom()
frame01.mainloop()
