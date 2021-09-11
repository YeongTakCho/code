# strdata=input('정렬할 문자열을 입력하세요')
strdata='가라마바사타사타카파타자까짜?'
str1=sorted(strdata)
str2=sorted(strdata,reverse=True)

print(str1)
print(str2)

str11=''.join(str1)
str22=''.join(str2)

print(str11)
print(str22)

listdata=['s','werwesdfwe','g','sdf','gw','acf','adfsrq','asfd4gwefre']
len_sorted=sorted(listdata,key=len)
print(len_sorted)

