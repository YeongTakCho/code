arr=input().split('-',1)
plus= sum(map(int,arr[0].split('+')))
if len(arr)==2:
    minus=sum([sum(map(int,tmpstr.split('+'))) for tmpstr in arr[1].split('-')])
else:
    minus=0
print(plus-minus)