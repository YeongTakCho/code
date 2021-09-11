
n = int(input())

array = set(input().split())

m = int(input())

find = list(input().split())

for num in find:
    if num in array:
        print(1)
    else:
        print(0)