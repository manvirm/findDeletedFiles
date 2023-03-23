import os
import optparse
from winreg import *

# Convert user ID to username
def sid2user(sid):
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE,
                      "SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList"
                      + '\\' + sid)
        (value, type) = QueryValueEx(key, 'PorfileImagePath')
        user = value.split('\\')[-1]
        return user
    except:
        return sid

# Find path to deleted files
def returnDir():
    dirs = ['C:\\Recycler\\', 'C:\\Recycled\\', 'C:\\$Recycle.Bin\\']
    for recycleDir in dirs:
        if os.path.isdir(recycleDir):
            return recycleDir
    return None
    
# Find recycled files
def findRecycled(recycleDir):
    dirList = os.listdir(recycleDir)
    for sid in dirList:
        files = os.listdir(recycleDir + sid)
        user = sid2user(sid)
        print('\n[*] Listing Files for User: ' + str(user))
        for file in files:
            print('[+] Found File: ' + str(file))

def main():
    # Find path to deleted files
    recycledDir = returnDir()
    # Find recycled files
    findRecycled(recycledDir)

if __name__ == '__main__':
    main()