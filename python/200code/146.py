from os.path import getsize
from os import remove
file1= 'C:\\Users\\s_andycho1120\\code\\python\\200code\\img_sample.jpg'
file2= 'C:\\Users\\s_andycho1120\\code\\python\\200code\\fighter.png'
file_size1=getsize(file1)
file_size2=getsize(file2)
print('file name: %s\t filesize:%d'%(file1,file_size1))
print('file name: %s\t filesize:%d'%(file2,file_size2))

file3='C:\\Users\\s_andycho1120\\code\\python\\200code\\img_copy.jpg'
k=input('[%s]를 정말 삭제하시겠습니까? (Y/N)'%file3)
if k=='Y':
    remove(file3)
    print('deleted')