#int(): 인자로 정수형식의 문자열을 받으면 정수로 변환

print(int('123'))
print(int(' 123'))
print(int('123 '))
# errorcode: print(int('1 23'))
# errorcode: print(int('123.0'))
# errorcode: print(int('123.4'))
print(int(23))

#float(): 인자로 실수형식의 문자열을 받으면 실수로 변환

print(float('123'))

if float('123')==123: #True
    print("float('123')=123")
if float('123')==123.0: #True
    print("float('123')=123.0")


