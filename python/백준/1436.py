#3자리 ->4자리 ->5자리 ... 순으로 탐색
#4자리 이상일 경우 666의 위치를 옮겨가며 구함, 중복제거 후 순서대로 나열
'''
3자리 ->1번 ->1번 sum 1 total 1
4자리 ->2번 ->9번, 10번 sum 19 total 20 (- 1) = 19
5자리 ->3번 ->90번, 90번, 100번 sum 280 total 300 (-19) =280
6자리 ->4번 ->900번, 900번, 900번, 1000번 sum 3700 total 4000  = 3700
7자리 -> 46000
'''
search_num=int(input())
start_num=0 #찾은 갯수
num_len=3 #찾을 숫자의 길이
nums_List=[] #숫자의 보관
while True:
    for i in range(10**(num_len-3)):#len=6일때 가정, i=0~999
        for j in range(num_len-2): #j=0~3 
            if j==num_len-3:
                append_num=666*10**(num_len-3)+ i
            else:
                append_num=666*10**(j)+(i//(10**(j)))*10**(j+3)+i%(10**(j))   #len=5 j=0 ->--666 + (i//1 * 1000) // j=1 ->-666- (i//10 * 10000 + i%10) // i=2 -> 666-- + (i//100)
            nums_List.append(append_num)  #len=6 j=0 ->---666 + (i//1 * 1000) // j=1 ->--666- (i//10 * 10000 + i%10) // i=2 -> -666-- + (i//100 *100000+ i%100) //j=3 -> 666--- + (i//1000)
    nums_List.sort()

    result=[nums_List[0]]; i=0
    for value in nums_List: #중복제거
        if value != result[i]:
            result.append(value)
            i+=1

    start_num=len(result)
    if start_num>=search_num:
        print(result[search_num-1])
        break
    num_len+=1

