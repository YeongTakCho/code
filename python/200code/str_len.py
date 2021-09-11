txt='python'
for i in range(len(txt)+1):
    print("%s"%txt[:i])
txt='abcdefghijk'
txt2=txt[2:5:2]
print(txt2)
txt3=txt[::-1]
print(txt3)
txt4=txt[5:2:-1]
print(txt4)