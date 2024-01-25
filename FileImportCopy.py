'''In the case of the automated process failing these are the steps to manually copy the required MDB files from the SFTP server to the local SHR folders.
 
1/ Go to SFTP directory \\server\Data\
2/ Looks for files with today's date
3/ Copy all MDB files to a local temporary directory
4/ Go to the local directory
5/ Rename files that are required - these show the R12 runs and the required RSA files.
6/ Copy renamed files to shr directories:
 
7/ On LONSHR folders check presence of empty dlcomplete.txt file if not present then create this
 
8/ Delete files from local temporary directory - ready for next period copy
'''
 
import os
import fnmatch
from os import listdir
from os.path import isfile, join
from datetime import datetime
import time
import tkinter as tk
from typing import Final
import shutil
from datetime import date
from pathlib import Path
 
# Constants
remote_host: Final = \\\\LONS00118177\\Data\\Triparty\\EOCL\\
BANKSHR: Final = \\\\lonshr-stardata\\StarData\\EuroClear\\Triparty\\
FBANKSHR: Final = \\\\lonshr-stardata\\StarData\\EuroClear_F\\Triparty\\
FOSHR: Final = \\\\lonshr-stardata\\StarReports\\TriWeb\\LON_PAR_IBV\\
local_folder: Final = "C:\\TEMP\\Triparty\\"
local_folder_bank: Final = "C:\\TEMP\\Triparty\\Bank\\"
local_folder_bank_rename: Final = "C:\\TEMP\\Triparty\\Bank\\rename\\"
local_folder_fbank: Final = "C:\\TEMP\\Triparty\\FBANK\\"
local_folder_fbank_rename: Final = "C:\\TEMP\\Triparty\\FBANK\\rename\\"
 
#copy all MDB files from remote_host to local_folder
 
def copy_files_within_date_range(source_folder, target_folder, days, extension):
    cutoff_time = time.time() - days * 86400
    for filename in os.listdir(source_folder):
        source_file = os.path.join(source_folder, filename)
        if os.path.isfile(source_file) and os.path.getmtime(source_file) > cutoff_time and filename.endswith(extension):
            shutil.copy(source_file, target_folder)
    print("Today's files copied")
 
def copy_files_with_extension_and_date_label(source_folder, target_folder):
    for filename in os.listdir(source_folder):
        source_file = os.path.join(source_folder, filename)
        if os.path.isfile(source_file) and (filename[-12:] == date.today().strftime('%Y%m%d') + '.mdb') :
            shutil.copy(source_file, target_folder)
    print("Today's files copied")
 

def delete_files_in_directory(directory_path):
   try:
     files = os.listdir(directory_path)
     for file in files:
       file_path = os.path.join(directory_path, file)
       if os.path.isfile(file_path):
         os.remove(file_path)
     print("All files deleted successfully.")
   except OSError:
     print("Error occurred while deleting files.")
 

# Delete all files from local_host including sub-directories
delete_files_in_directory(local_folder)
delete_files_in_directory(local_folder_bank)
delete_files_in_directory(local_folder_fbank)
delete_files_in_directory(local_folder_bank_rename)
delete_files_in_directory(local_folder_fbank_rename)
 
# Example usage to copy files modified within the last 1 day
#copy_files_within_date_range(remote_host, local_folder, 1, '.mdb')
 
#Now copy files based on the string date stamp and include the .mdb
#copy_files_with_extension_and_date_label(remote_host, local_folder)
 
#Go to local directory and get the latest run then copy to a sub-directory and rename files there ready to copy to LON SHR directory
 
#account_list = ['999999',955555']
bank_pattern = '*999999'
fbank_pattern = '*955555*'
 
for filename in os.listdir(local_folder):
   #print(filename)
   #print ('Filename: %-25s %s' % (filename, fnmatch.fnmatch(filename, pattern)))
   if (fnmatch.fnmatch(filename, bank_pattern)):
 
      shutil.copy2(os.path.join(local_folder,filename), local_folder_bank)
   if (fnmatch.fnmatch(filename, fbank_pattern)):
      shutil.copy2(os.path.join(local_folder,filename), local_folder_fbank)
 

runNum = []
maxRun = 0
date = ''
triprev = ''
tripprv = ''
tradprv = ''
 
for filename in os.listdir(local_folder_bnp):
   date = filename[-12:]
   if(filename[0:9] == 'TRIPREV3R') and (filename[10:11] == "_"):
      runNum.append(int(filename[9:10]))
   if(filename[0:9] == 'TRIPREV3R') and (filename[11:12] == "_"):
      runNum.append(int(filename[9:11]))
 
#copy single file to sub-directory
maxRun = max(runNum)
triprev = 'TRIPREV3R' + str(maxRun) + '_' + '99809' + '_' + date
shutil.copy2(os.path.join(local_folder_bank,triprev), local_folder_bank_rename)
 
runNum = []
maxRun = 0
 
for filename in os.listdir(local_folder_bank):
   date = filename[-12:]
   if(filename[0:9] == 'TRIPPRV3R') and (filename[10:11] == "_"):
      runNum.append(int(filename[9:10]))
   if(filename[0:9] == 'TRIPPRV3R') and (filename[11:12] == "_"):
      runNum.append(int(filename[9:11]))
 
#copy single file to sub-directory
maxRun = max(runNum)
tripprv = 'TRIPPRV3R' + str(maxRun) + '_' + '99809' + '_' + date
#print(tripprv)
shutil.copy2(os.path.join(local_folder_bank,tripprv), local_folder_bank_rename)
 
runNum = []
maxRun = 0
 
for filename in os.listdir(local_folder_bank):
   date = filename[-12:]
   if(filename[0:9] == 'TRADPRV3R') and (filename[10:11] == "_"):
      runNum.append(int(filename[9:10]))
   if(filename[0:9] == 'TRADPRV3R') and (filename[11:12] == "_"):
      runNum.append(int(filename[9:11]))
 
#copy single file to sub-directory
maxRun = max(runNum)
tradprv = 'TRADPRV3R' + str(maxRun) + '_' + '99809' + '_' + date
#print(tradprv)
shutil.copy2(os.path.join(local_folder_bank,tradprv), local_folder_bank_rename)
 
#Copy RSA files
for filename in os.listdir(local_folder_bank):
   if(filename[0:3] == 'RSA'):
      shutil.copy2(os.path.join(local_folder_bank,filename), local_folder_bank_rename)
 

#FBANK files - Finding the max current-run TRIPREV / RSA
runNum = []
maxRun = 0
date = ''
triprev = ''
 
for filename in os.listdir(local_folder_fbank):
   date = filename[-12:]
   if(filename[0:9] == 'TRIPREV3R') and (filename[10:11] == "_"):
      runNum.append(int(filename[9:10]))
   if(filename[0:9] == 'TRIPREV3R') and (filename[11:12] == "_"):
      runNum.append(int(filename[9:11]))
 
#copy single file to sub-directory
maxRun = max(runNum)
triprev = 'TRIPREV3R' + str(maxRun) + '_' + '94783' + '_' + date
#print(triprev)
shutil.copy2(os.path.join(local_folder_fbank,triprev), local_folder_fbank_rename)
 
#Copy RSA files
for filename in os.listdir(local_folder_fbank):
   if(filename[0:3] == 'RSA'):
      shutil.copy2(os.path.join(local_folder_fbank,filename), local_folder_fbank_rename)
 
#Renaming files - BANK
for filename in os.listdir(local_folder_bank_rename):
   if(filename[0:3] == "RSA"):
      os.rename(os.path.join(local_folder_bank_rename,filename),os.path.join(local_folder_bank_rename,filename[0:9] + '_169.mdb'))
 
for filename in os.listdir(local_folder_bank_rename):
   if(filename[0:4] == "TRAD" or filename[0:4] == "TRIP") and (filename[10:11] == "_"):
      os.rename(os.path.join(local_folder_bank_rename,filename),os.path.join(local_folder_bank_rename,filename[0:10] + '_169.mdb'))
   if(filename[0:4] == "TRAD" or filename[0:4] == "TRIP") and (filename[11:12] == "_"):
      os.rename(os.path.join(local_folder_bank_rename,filename),os.path.join(local_folder_bank_rename,filename[0:11] + '_169.mdb'))
 
print("BANK FIles:")
for filename in os.listdir(local_folder_bank_rename):
   print(filename)
   shutil.copy2(os.path.join(local_folder_bank_rename,filename), BANKSHR)
 
#check if dlcomplete.txt file exists on shr else create it
'''
filepath = BANKSHR/'dlcomplete.txt'
# Check if the file already exists
if not filepath.exists():
    # Create a new file
    filepath.touch()
    print("File created successfully.")
else:
    print("File already exists.")
'''
 
#Renaming files - FBANK
for filename in os.listdir(local_folder_fbank_rename):
   if(filename[0:3] == "RSA"):
      os.rename(os.path.join(local_folder_fbank_rename,filename),os.path.join(local_folder_fbank_rename,filename[0:9] + '_016.mdb'))
 
for filename in os.listdir(local_folder_fbank_rename):
   if(filename[0:4] == "TRIP") and (filename[10:11] == "_"):
      os.rename(os.path.join(local_folder_fbank_rename,filename),os.path.join(local_folder_fbank_rename,filename[0:10] + '_016.mdb'))
   if(filename[0:4] == "TRIP") and (filename[11:12] == "_"):
      os.rename(os.path.join(local_folder_fbank_rename,filename),os.path.join(local_folder_fbank_rename,filename[0:11] + '_016.mdb'))
 
print("FBank Files:")
for filename in os.listdir(local_folder_fbank_rename):
   print(filename)
   shutil.copy2(os.path.join(local_folder_fbank_rename,filename),FBANKSHR)


