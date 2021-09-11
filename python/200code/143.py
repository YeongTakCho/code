buffsize=1024
img_path=open('C:\\Users\\s_andycho1120\\code\\python\\200code\\img_sample.jpg', 'rb')
img_copy=open('C:\\Users\\s_andycho1120\\code\\python\\200code\\img_copy.jpg', 'wb')
data=img_path.read(buffsize)
while data:
    img_copy.write(data)
    data=img_path.read(buffsize)
img_copy.close()
img_path.close()
