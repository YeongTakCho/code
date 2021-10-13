N, M = map(int,input().split())
nums = list(set(map(int,input().split()))); nums.sort()

arr= [0] * M
data = list()
Zero= 0

def recurse(hight: int, repeat_list : list , arr : list, MAX : int , result : list) -> None:
    for i in range(len(repeat_list)):
        arr[hight] = repeat_list[i]

        if hight < MAX - 1:
            recurse(hight +1, repeat_list[i:], arr, MAX, result)
        else:
            result.append(arr.copy())

recurse(Zero, nums, arr, M, data)

for each_list in data:
    for value in each_list:
        print(value, end= ' ')
    print()
