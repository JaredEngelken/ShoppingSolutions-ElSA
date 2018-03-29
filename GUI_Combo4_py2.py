from Tkinter import *
import tkFont
import pandas as pd
import openpyxl
from openpyxl import load_workbook
import numpy as np
import os

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

### Event Functions ###
def close():
    root.destroy() #close GUI
def itemButton():
    Label(root, text = item).pack()
def pandas():
    ### PANDAS
    # Import desired inventory file and save as a variable
    file = 'Grocery.xlsx'
    xl = pd.ExcelFile(file)

    # Display all sheets that exist in spreadsheet file
    print(xl.sheet_names)

    # Generate DataFrame from imported spreadsheet and print
    df1 = xl.parse('Page 1')
    print (df1)
    shoplist = ["" for x in range(1)]

    item = ment.get()
    itemButton = Button(root, text = item).pack()

    if item != "Done":
        if df1['Item'].str.match(item).any():
            for j in range(len(shoplist)):
                if shoplist[j] == "":
                    shoplist[j] = item
                    shoplist.append("")
                    print (shoplist)
                            # Use to test location of specific item-->> print(df1.loc[df1['Item'] == 'Nuts'])

                        # Find row in which desired item exists
                    for p in range(len(shoplist)-1):
                         #  rowselect = (df1.index[df1['Item'] == shoplist[p]])
                        row4search = ((df1.index[df1['Item'].str.contains(shoplist[p])])+1)

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
                    break
        else:
            print("Item not found. Please add a new Item.")

#Entry Box
ment = StringVar()
mbutton = Button(root, text = 'Search', command = pandas, fg = 'red', bg = 'blue').pack()
mEntry = Entry(root, textvariable = ment).pack()

# Exit button - closes the GUI
exitButton = Button(rightFrame, text = 'Exit', font = myFont, command = close, bg = 'red', width = 6)
exitButton.pack(side = BOTTOM)

#Display the menu
root.mainloop() #loops forever
