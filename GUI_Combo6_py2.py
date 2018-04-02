from Tkinter import *
import tkFont
import pandas as pd
import openpyxl
from openpyxl import load_workbook
import numpy as np
import os
import time



### GUI definitions ###
root = Tk()
root.title("ElSA")
myFont = tkFont.Font(family = 'Helvetica', size = 12, weight = "bold")

class Boom(Frame):
    global clear
    global listbox_update
    global test_list
    wb = load_workbook('Grocery.xlsx') #Loads spreadsheet
    sheet_1 = wb['Page 1'] #Extracts desired sheet
    for t in range(1,sheet_1.max_row):
        test_list[t]=sheet_1.cell(row=t+1, column=1).value
    
    global listbox
    ### Event Functions ###
    def on_keyrelease(event):
        # get text from entry
        value = event.widget.get()
        value = value.strip().lower()
        # get data from test_list
        if value == '':
            data = []
        else:
            data = []
            for item in test_list:
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
    def close():
        root.destroy() #close GUI
    def pandas():
        file = 'Grocery.xlsx'
        xl = pd.ExcelFile(file)

        # Display all sheets that exist in spreadsheet file
        print(xl.sheet_names)

        # Generate DataFrame from imported spreadsheet and print
        df1 = xl.parse('Page 1')
        print (df1)
        shoplist = ["" for x in range(1)]

        # Get the item from the search box and make a button with searched item if found
        item = ment.get()
  
        wb = load_workbook('Grocery.xlsx') #Loads spreadsheet
        sheet_1 = wb['Page 1'] #Extracts desired sheet
        for totMatch in range(len(row4search)):
            code = np.zeros(sheet_1.max_row) #Create blank array based on size of inventory list
            cost = np.zeros(sheet_1.max_row)
            aisle = np.zeros(sheet_1.max_row)
            bay = np.zeros(sheet_1.max_row)
         
            for i in range(1,sheet_1.max_row):
                code[i]=sheet_1.cell(row=i+1, column=2).value #Fill in data to blank arrays from spreadsheet
                cost[i]=sheet_1.cell(row=i+1, column=3).value
                aisle[i]=sheet_1.cell(row=i+1, column=4).value
                bay[i]=sheet_1.cell(row=i+1, column=5).value                                
                    
        # Full info display
            print (sheet_1.cell(row=row4search[totMatch]+1, column=1).value)
            print ('Barcode', code[row4search[totMatch]]) #Display desired item barcode
            print ('Price', cost[row4search[totMatch]]) #Display desired item cost
            print ('Aisle', aisle[row4search[totMatch]]) #Display desired item isle
            print ('Bay', bay[row4search[totMatch]]) #Display desired item bay

        # CART LIST
            def addCartList():
                shoppingCartButton = Button(root, text = item)
                shoppingCartButton.grid(column = 4)
            
        # SHOPPING LIST
            def addShopList():
                addCartButton = Button(root, text = item, command = addCartList)
                addCartButton.grid(column = 3) 
            
            #Add item to shoplist button with info (!!!ONLY DISPLAYS SEARCH NOT ACTUAL NAME OF ITEM!!!)
            itemButton = Button(root, text = 'ADD '+item+' $'+str(cost[row4search[totMatch]])+' Aisle '+str(aisle[row4search[totMatch]]), command = addShopList)
            itemButton.grid(column = 1, columnspan = 2)
            # MAKE THIS THING DISAPEAR ON NEXT SEARCH!!!

    def on_select(event):
        # display element selected on list
        print('(event) previous:', event.widget.get('active'))
        print('(event)  current:', event.widget.get(event.widget.curselection()))
        print('---')


    # Shopping Cart Label
    shoppingCartLabel = Label(root, text = "Your Shopping Cart:", bg = 'green', fg = 'black', font = myFont)
    shoppingCartLabel.grid(column = 4, row = 1)

    # Shopping List Label
    addCartLabel = Label(root, text = "Shopping List\nClick to add items to cart: ", bg = 'white', fg = 'black', font = myFont)
    addCartLabel.grid(column = 3, row = 1)

    # Search label
    searchLabel = Label(root, text = 'Search:', bg = 'blue', fg = 'white', font = myFont)
    searchLabel.grid(column = 1, row = 1)

    # Search Entry
    entry = Entry(root)
    entry.grid(column = 1, row = 2)
    entry.bind('<KeyRelease>', on_keyrelease)

    listbox = Listbox(root)
    listbox.grid(column = 1, row = 3)
    listbox.bind('<<ListboxSelect>>', on_select)
    listbox_update([])

#Display the menu
frame01 = Boom()
frame01.mainloop()
