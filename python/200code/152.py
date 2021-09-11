import os 
path='C:\\Users\\s_andycho1120\\code\\python\\200code'

os.chdir(path)
newfolder='test_new_folder'
try:
    os.makedirs(newfolder)
    print('made new folder %s'%(path+'\\'+newfolder))
except Exception as e:
    print(e)
    
