import os
from datetime import datetime
import time
import tkinter as tk
from typing import Final
from os import listdir
from os.path import isfile, join

# Constants
c_path: Final = "c:\\"
c_temp_path: Final = "c:\\Temp\\"
c_prog_files: Final = "c:\\Program Files\\"
c_windows_path: Final = "c:\\Windows\\"


# define a func to take in directory path and return list of files in an array variable
def find_files_in_path(directory_name):
    todays_date = datetime.now()
    today = todays_date.date()

    path_text = []

    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(directory_name)

    for root, dirs, files in os.walk(directory_name):
        for filename in files:
            fullfilename = ''
            file_time = os.path.getmtime(directory_name+filename)
            file_date = datetime.fromtimestamp(file_time)
            file_day = file_date.date()
            if file_day == today:
                #print(f'Files are {directory_name + filename}' + '  ' + (time.ctime(mtime)))
                fullfilename = str(filename + ' ' + (time.ctime(mtime)))
                path_text.append(fullfilename)
        return path_text

def populateWindow():
    #C Path
    pathText = find_files_in_path(c_path)
    #print(pathText)
    for files in pathText:
        c_window.insert(tk.END, files + '\n')

    #C Temp Path
    pathText = find_files_in_path(c_temp_path)
    #print(pathText)
    for files in pathText:
        c_temp_window.insert(tk.END, files + '\n')

    #C Prog Path
    pathText = find_files_in_path(c_prog_files)
    #print(pathText)
    for files in pathText:
        c_prog_files_window.insert(tk.END, files + '\n')

    #C Windows Path
    pathText = find_files_in_path(c_windows_path)
    #print(pathText)
    for files in pathText:
        c_windows_window.insert(tk.END, files + '\n')


def update():
    c_window.delete(1.0, tk.END)
    c_temp_window.delete(1.0, tk.END)
    c_prog_files_window.delete(1.0, tk.END)
    c_windows_window.delete(1.0, tk.END)

    #window.after(5000)
    populateWindow()


window = tk.Tk()
window.title('Simple Explorer')
window.geometry("1000x750")
window.resizable(width=True, height=True)

c_window = tk.Text(window, height=10, width=100)
c_temp_window = tk.Text(window, height=10, width=100)
c_prog_files_window = tk.Text(window, height=10, width=100)
c_windows_window = tk.Text(window, height=10, width=100)
csScrollbar = tk.Scrollbar(window)
csScrollbar.config(command=c_prog_files_window.yview)

cpathlbl = tk.Label(window, text="C Path:")
cpathlbl.config(font=("Comic Sans Serif", 10))
ctemplbl = tk.Label(window, text="C Temp Files:")
ctemplbl.config(font=("Comic Sans Serif", 10))

cproglbl = tk.Label(window, text="C Prog Files Path:")
cproglbl.config(font=("Comic Sans Serif", 10))
cwinlbl = tk.Label(window, text="C Windows Files:")
cwinlbl.config(font=("Comic Sans Serif", 10))

frm_buttons = tk.Frame(window)
bUpdate = tk.Button(frm_buttons, text="Update", command=update)
bExit = tk.Button(frm_buttons, text="Exit", command=window.destroy)

#Put it on the Grid
cpathlbl.grid(row=0, column=0, sticky="ew", pady=5)
c_window.grid(row=0, column=1, sticky="ew", pady=5)
ctemplbl.grid(row=1, column=0, sticky="ew", pady=5)
c_temp_window.grid(row=1, column=1, sticky="ew", pady=5)
csScrollbar.grid(row=1, column=2, sticky='ns')

cproglbl.grid(row=2, column=0, sticky="ew", pady=5)
c_prog_files_window.grid(row=2, column=1, sticky="ew", pady=5)

cwinlbl.grid(row=3, column=0, sticky="ew", pady=5)
c_windows_window.grid(row=3, column=1, sticky="ew", pady=5)


bUpdate.grid(row=0, column=0, sticky="ew" ,pady=5)
bExit.grid(row=0, column=1, sticky="ew", padx=5)

frm_buttons.grid(row=4,column=1, sticky="ns")

window.mainloop()
