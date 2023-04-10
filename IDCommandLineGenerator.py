'''
Comma separate ID and Name in txt file


Use Tkinter to create text boxes which user-enters for
ID
user
IG Y/N

'''

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

# On line 59, enter in the path of your file

myFile = "C:\\directory\file.txt”

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
