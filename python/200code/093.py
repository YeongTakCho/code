log='name:조:1 sex:male:2 country:korea:3'
ret1=log.split()
for data in ret1:
    r1, r2,r3=data.split(':')
    print("%s -> %s->%s"%(r1,r2,r3))

bond='!'
log=['name:조', 'sex:male','country:korea:3']
b_log= bond.join(log)
print(b_log)
bond=''
b_log=bond.join(log)
print(b_log)

txt='오늘은 내일 내일은 오늘 모래 그믐은'
r_txt=txt.replace('오늘','매일')
print(r_txt)

r_txt=txt.replace('매일','내일') #no error (텍스트에 바꾸려는 글자가 없어도 오류가 생기지 않음)
print(r_txt)

