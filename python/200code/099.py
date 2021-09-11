range1=range(10) #range자료형 ->리스트가 아니라 객체임!
print(type(range1))
print(list(range1))

solarsys=['태양','수소','금성','지구','화성','목성','토성','천왕성','지구']
planted='지구'
state=solarsys.index(planted)
print(state)
state=solarsys.index(planted,state+1)
print(state)
solarsys[state]='end'
print(solarsys )
