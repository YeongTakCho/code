def ftxt(txt, find_txt):
    state=list()
    start=0
    range_num=len(txt)-len(find_txt)
    append_num=len(find_txt)
    recent=int()
    while start <= range_num:
        try:
            state.append(recent=(txt.find(find_txt,start)))
            start=recent+append_num
        except:
            break
    return state
print(ftxt('abcdefgabceabc','abc'))