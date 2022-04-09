data = input()
result= []
cnt_get =[0]

def get_c():
    if cnt_get[0] == len(data):
        return ' '
    cnt_get[0]+=1
    return data[cnt_get[0] -1]

def pmmd(c):
    sol()
    result.append(c)

def f_brachet():
    sol()

def b_brachet():
    pass    

cmd = '+-*/()'

def sol():
    c= get_c()
    if c in cmd:
        if c in cmd[0:4]:
            pmmd(c)
        if c == '(':
            f_brachet()
        if c == ')':
            b_brachet()
    elif c == ' ':
        return
    else:
        result.append(c)
        sol()

sol()
print(str(result))

