ch=input('문자 1개를 입력하세요')
ch=ch[0]
print('입력한 문자: %s 코드값: %d [16진수:%s]'%(ch,ord(ch),hex(ord(ch))))

# val=int(input('코드값을 입력하세요'))
i=0
while True:
    try:
        ch=i
        print('%d -> %s'%(i,chr(i)))
    except:
        print('%d -> no ch'%(i))
        break
    finally:
        i+=1

