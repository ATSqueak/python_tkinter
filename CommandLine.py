'''
Comma separate ID in txt file
 
    count = 0
    for line in file:
        if count >= 1:
            #print("Record{}: {}".format(count, line.strip()))
            list.append(line.strip().split(','))
        count += 1
 
       
myFile = "C:\\Users\\text.txt"
count = 0
 
list = []
commandList = []
with open(myFile) as fp:
    for line in fp:
        count += 1
        list.append(line.strip())
 
for item in list:
    commandList.append("Command.exe " + item)
    commandList.append(("sleep 2"))
 
os.chdir('C:\\Users')
for item in commandList:
    #subprocess.call(item)
    print(item)
'''
 

from tkinter import *
import os
import subprocess
 
def UpdateOutput():
    Output.delete(1.0, END)
    contracts = ContractID.get()
 
    tradeList = []
    commandList = []
    for item in contracts.split(','):
        tradeList.append(item)
 
    commandList.clear()
    for item in tradeList:
        commandList.append("Command.exe " + str(item))
       
    for item in commandList:
        Output.insert(INSERT,"\n")
        Output.insert(END, item)
 

def Execute():
 
    contracts = ContractID.get()
    tradeList = []
    commandList = []
    for item in contracts.split(','):
        tradeList.append(item)
 
    commandList.clear()
    for item in tradeList:
        commandList.append("Command.exe " + str(item))
 
    os.chdir('C:\\Users\\ ')
    for item in commandList:
        subprocess.call(item)
        print(item)
 
# Create object
root = Tk()
 
# Adjust size
root.geometry("1000x500")
root.title("Support Command")
# root.resizable(width=True, height=True)
root.resizable(width=False, height=False)
 
# Set variables
ContractID = StringVar()
 
# Entry for user to set variables
IDLbl = Label(root, text="Contract ID: ")
ID = Entry(root, width=15, font=("Comic Sans", 14, ""), textvariable=ContractID)
IDLbl.place(x=20, y=20)
ID.place(x=100, y=20)
 
frm_buttons = Frame(root)
bUpdate = Button(frm_buttons, text="Update", command=UpdateOutput)
bExit = Button(frm_buttons, text="Exit", command=root.destroy)
bExecute = Button(frm_buttons, text="Execute?", command=Execute)
 
bUpdate.grid(row=0, column=0, sticky="ew", pady=5)
bExit.grid(row=0, column=1, sticky="ew", padx=5)
bExecute.grid(row=0, column=2, sticky="ew", padx=5)
 
frm_buttons.place(x=80, y=150)
 
Output = Text(root, height=10, width=100)
Output.place(x=80, y=200)
 
root.mainloop()
