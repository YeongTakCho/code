import os
path='C:\\Users\\s_andycho1120\\code\\python\\200code'
os.chdir(path)

target_folder='test_new_folder'
k=input('do you want to delete dir-[%s] (y/n)'%target_folder)
if k=='y':
    try:
        os.rmdir(target_folder)
        print('%s is deleted'%target_folder)
    except Exception as e:
        print(e)