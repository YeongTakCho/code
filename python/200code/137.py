f = open('C:\\Users\\s_andycho1120\\code\\python\\200code\\stockcode.txt', 'r')
data = f.read()
print(data)
f.close()

f = open('C:\\Users\\s_andycho1120\\code\\python\\200code\\stockcode.txt', 'r')
line_num=0
line=f.readline()
while line:
    print("%d %s"%(line_num,line),end='')
    line=f.readline()
    line_num+=1
f.close

f = open('C:\\Users\\s_andycho1120\\code\\python\\200code\\stockcode.txt', 'r')
lines=f.readlines()
print('\n')
print(lines)
f.close

f = open('C:\\Users\\s_andycho1120\\code\\python\\200code\\stockcode.txt', 'w')
text=input('텍스트에 저장할 내용을 입력하세요')
f.write(text)
f.close

f = open('C:\\Users\\s_andycho1120\\code\\python\\200code\\stockcode.txt', 'w')
count=1
data=[]
print('데이터 입력을 완료하면 [Enter]을 입력하시오')
while True:
    text=input('%d번째 줄에 저장할 데이터를 입력하세요'%count)
    if text=='':
        break
    data.append(text)
    count+=1
f.writelines(data)
f.close    
