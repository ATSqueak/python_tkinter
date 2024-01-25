'''
Comma separate tradeID and TraderName in txt file
 

Use TKinter to create text boxes which user-enters for
MW trade ID
user
IG Y/N
 

myFile = "C:\\Users\\text.txt"
 
tradeList = []
commandList = []
with open(myFile) as file:
    count = 0
    for line in file:
        if count >= 1:
            tradeList.append(line.strip().split(','))
        count += 1
 
# print(tradeList)
 
for item in tradeList:
    commandList.append("commandCaller.exe Transfer \"ID=" + item[0] + "|USER=" + item[1] + "|IG=Y\"")
    commandList.append(("sleep 2"))
 
for item in commandList:
    print(item)
 
   
from tkinter import *
 
def UpdateOutput():
    Output.delete(1.0, END)
    textOutput = "command.exe host port transfer \"ID=" + ID.get() + "|USER=" + User.get() + "|IG=" + IG.get() + "\""
    Output.insert(END, textOutput)
 
# Create object
root = Tk()
 
# Adjust size
root.geometry("1000x500")
root.title("Support Transfer ID")
# root.resizable(width=True, height=True)
root.resizable(width=False, height=False)
 
# Set variables
ID = StringVar()
IG = StringVar()
User = StringVar()
 
# set option lists
IGoptions = ["Y", "N"]
UserOptions = ["Team", "Name1", "Name2", "Name3", "Name4", "Name5"]
 
# initial dropdown menu text
IG.set("IG")
User.set("User Name")
 
# Entry for user to set variables
IDLbl = Label(root, text="ID: ")
ID = Entry(root, width=15, font=("Comic Sans", 14, ""), textvariable=ID)
IDLbl.place(x=20, y=20)
ID.place(x=80, y=20)
 
IGLbl = Label(root, text="IG: ")
IGdropdown = OptionMenu(root, IG, *IGoptions)
IGLbl.place(x=20, y=60)
IGdropdown.place(x=80, y=60)
 
UserLbl = Label(root, text="User: ")
Userdropdown = OptionMenu(root, User, *UserOptions)
UserLbl.place(x=20, y=100)
Userdropdown.place(x=80, y=100)
 
myFile = "D:\\Test\\transfer_trade.txt"
 
list = []
commandList = []
with open(myFile) as file:
    count = 0
    for line in file:
        if count >= 1:
            list.append(line.strip().split(','))
        count += 1
 
for item in list:
    commandList.append("command.exe host port transfer \"ID=" + item[0] + "|USER=" + item[1] + "|IG=Y\"")
    commandList.append(("sleep 2"))
 
for item in commandList:
    print(item)
 
frm_buttons = Frame(root)
bUpdate = Button(frm_buttons, text="Update", command=UpdateOutput)
bExit = Button(frm_buttons, text="Exit", command=root.destroy)
 
bUpdate.grid(row=0, column=0, sticky="ew", pady=5)
bExit.grid(row=0, column=1, sticky="ew", padx=5)
 
frm_buttons.place(x=80, y=150)
 
Output = Text(root, height=10, width=100)
Output.place(x=80, y=200)
 
root.mainloop()
 

'''
 
from tkinter import *
from tkinter import messagebox
import os
import subprocess
 
def UpdateOutput():
    Output.delete(1.0, END)
    textOutput = "commandCaller.exe server port Transfer \"ID=" + MWID.get() + "|USER=" + User.get() + "|IG=" + IG.get() + "\""
    Output.insert(END, textOutput)
 
def help_text():
    messagebox.showinfo("Help","Please enter the details as requested in the fields.\nSubmit will create the text that will be passed to the CommandCaller executable.")
 
def Execute():
    textOutput = "commandCaller.exe server port Transfer \"ID=" + MWID.get() + "|USER=" + User.get() + "|IG=" + IG.get() + "\""
    textOutput2 = "commandCaller.exe server port Transfer \"ID=" + MWID.get() + "|USER=" + User.get() + "|IG=" + IG.get() + "\""
    os.chdir('C:\\Users\\')
    subprocess.call(textOutput)
    subprocess.call(textOutput2)
    print("Sucessful...")
 

# Create object
root = Tk()
 
# Adjust size
root.geometry("1000x500")
root.title("Support Transfer Trade")
# root.resizable(width=True, height=True)
root.resizable(width=False, height=False)
 
# Set variables
MWID = StringVar()
IG = StringVar()
User = StringVar()
 
# set option lists
IGoptions = ["Y", "N"]
UserOptions = ["Team ONLY", "Name1", "Name2", "Name3", "Name4", "Name5"]
 
# initial dropdown menu text
IG.set("Interest Group")
User.set("User Name")
 
# Entry for user to set variables
MWIDLbl = Label(root, text="MWID: ")
MWID = Entry(root, width=15, font=("Comic Sans", 14, ""), textvariable=MWID)
MWIDLbl.place(x=20, y=20)
MWID.place(x=80, y=20)
 
IGLbl = Label(root, text="IG: ")
IGdropdown = OptionMenu(root, IG, *IGoptions)
IGLbl.place(x=20, y=60)
IGdropdown.place(x=80, y=60)
 
UserLbl = Label(root, text="User: ")
Userdropdown = OptionMenu(root, User, *UserOptions)
UserLbl.place(x=20, y=100)
Userdropdown.place(x=80, y=100)
 
frm_buttons = Frame(root)
bUpdate = Button(frm_buttons, text="Update", command=UpdateOutput)
bHelp = Button(frm_buttons, text="Help",command=help_text)
bExecute = Button(frm_buttons, text="Execute?", command=Execute)
bExit = Button(frm_buttons, text="Exit", command=root.destroy)
 
bUpdate.grid(row=0, column=0, sticky="ew", pady=5)
bHelp.grid(row=0, column=1, sticky="ew", padx=5)
bExecute.grid(row=0, column=2, sticky="ew", padx=5)
bExit.grid(row=0, column=3, sticky="ew", padx=5)
 
frm_buttons.place(x=80, y=150)
 
Output = Text(root, height=10, width=100)
Output.place(x=80, y=200)
 
root.mainloop()
 
