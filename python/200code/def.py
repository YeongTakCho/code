strs=['str1','str2','str3','str4','str5']
global_dict={}
def mdict(*nums):
    global global_dict
    if len(strs)>len(nums):
        lens=len(nums)
    else:
        lens=len(strs)
    for i in range(lens):
        global_dict[strs[i]]=nums[i]
mdict(1,2,3,4)
print(global_dict)

