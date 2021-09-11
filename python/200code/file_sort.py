import os

def getfiles(dirpath):
    filelist = [s for s in os.listdir(dirpath)
        if os.path.isfile(os.path.join(dirpath, s))]
    filelist.sort(key=lambda s: os.path.getmtime(os.path.join(dirpath, s)))
    return filelist

file1= getfiles('C:\Users\s_andycho1120\code\python')