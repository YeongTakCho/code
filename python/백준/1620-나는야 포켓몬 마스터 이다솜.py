import sys
p_num,s_num=map(int,sys.stdin.readline().strip().split())
poketmons=dict()
poketmonsReverse=dict()
searches=[]
for i in range(p_num):
    poketmons[(sys.stdin.readline().strip())]=i+1
poketmonsReverse={v:k for k,v in poketmons.items()}

for i in range(s_num):
    searches.append(sys.stdin.readline().strip())

for search in searches:
    try:
        search=int(search)
        print(poketmonsReverse[search])
    except:
        print(poketmons[search])
