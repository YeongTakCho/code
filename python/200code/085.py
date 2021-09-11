print('문자들만있는지알아보는메소드'.isalpha())
print('문자들만 있는지 알아보는 메소드'.isalpha())

print('01012345678'.isdigit())
print('010-1234-5678'.isdigit())
print('0x23'.isdigit()) #False

print('01234한글English'.isalnum())

print('abcdEFG 한글 123'.upper())
print('abcdEFG 한글 123'.lower())

txt='    양쪽에 공백이 있는 문자입니다           '
txt_strip=[txt,txt.lstrip(),txt.rstrip(),txt.strip()]
for txts in txt_strip:
    print('<'+txts+'>')

numStrs=['123','123.4','-123','-123.4','한글','english']
for numStr in numStrs:
    try:
        num=int(numStr)
        print('정수 숫자는 %d입니다'%num)
    except:
        try:
            num=float(numStr)
            print('실수 숫자는 %.1f입니다'%num)
        except:
            print('---숫자를 입력하세요---')