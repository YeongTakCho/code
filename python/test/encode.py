#bytes
print(bytes(5))
print(bytes([10,20,30]))
print(bytes(b'test'))

print('테스트'.encode()) #공백 =utf-8
print('테스트'.encode('utf-8')) #9바이트 -> 한글 1글자당 3바이트
print('테스트'.encode('euc-kr')) #6바이트 -> 한글 1글자당 2파이트 
#케릭터 셋에 따라 저장되는 값이 다르다.

print('test'.encode('utf-8'))
print('test'.encode('euc-kr'))

testStr=b'test'
print(testStr)
print('decode utf-8 '+ testStr.decode('utf-8'))
print('decode euc-kr ' +testStr.decode('euc-kr'))
#둘다 디코딩되는 이유: 인코딩된 문자(영어)의 바이트값이 utf-8과 euc-kr이 같음

if b'test'=='test'.encode('utf-8'):
    print("b'test'와 'test'.encode는 같다") #같다
else:
    print("b'test'와 'test'.encode는 다르다")
#그러나 b'oo'과 .encode('utf-8')이 같지 않음을 주의해야함
#b'oo'은 ascii코드에 존재하는 문자만 인코딩 가능하나 utf-8은 ascii외의 문자도 인코딩이 가능하다
#b'oo'은 .encode('utf-8') 보다 확장성이 떨어지므로 ascii문자만 사용하는 프로그램을 만들게 아니라면 .encode를 사용하는 것이 바람직하다고 생각한다.

#b'한글'은 에러코드 ->b'oo'는 ascii코드에 존재하는 문자만 가능
 
testStr='한글'.encode('euc-kr')
print(testStr)
print(testStr.decode('euc-kr'))
#print(testStr.decode('utf-8')): errorcode 
# errormsg: 0xc7 는 utf-8에 존재하지 않는 문자이다
testStr='한글'.encode('utf-8')
print(testStr)
#print(testStr.decode('euc-kr')) :errorcode
#UnicodeDecodeError: 'euc_kr' codec can't decode 
#byte 0xed in position 0: illegal multibyte sequence
print(testStr.decode('utf-8'))



"""
정리
영어(및 숫자와 일부 특수문자)는 어떤 케릭터셋으로 인코딩하든 바이트값(16진수로 표현했을때의 숫자)이 같기 때문에 모든 케릭터셋으로 디코딩이 가능하다
이외의 문자는 인코딩한 케릭터셋으로 디코딩해야하며 그 외에는 에러이다
이유: 케릭터셋별로 문자를 인코딩하는 방식이 다르기 때문에

참고자료
https://200301.tistory.com/9
https://sagittariusof85s.tistory.com/267
"""