def counting(a):    #aabc
    r={}
    for ch in a:                    
        if ch in r:                 
            r[ch]=r.get(ch,0)+1
        else:
            r[ch]=1
    for ch in r:
        if r[ch] == 1:
            return ch
    return 0
