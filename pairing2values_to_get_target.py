def pairs(a,b,x):
    res=[]
    b_set=set(b) #to shrink repeating pairs if there are repating val in list ex:a[1,1,2] b[2,3,3,] x=4 so we get two pairs of(1,3) so we use set  
    for u in a:
        comp = x-u
        if comp in b:
            res.append((u,comp))
    result.sort()
    return res
