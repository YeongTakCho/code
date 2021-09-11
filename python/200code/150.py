import os,glob
folder='C:\\Users\\s_andycho1120\\code\\python\\200code'
file_list=os.listdir(folder)
print(file_list)

os.chdir('C:\\Users\\s_andycho1120\\code\\python\\200code')
files='*.py'
file_list=glob.glob(files)
print(file_list)

pdir=os.getcwd();print(pdir)
os.chdir('..');print(os.getcwd())
os.chdir(pdir);print(os.getcwd())