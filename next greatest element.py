def next_grt(arr):
    n=len(arr)
    stck=[]
    res=[-1]*n
    for i in range(n-1,-1,-1):             #8          1(4)         7(3)             6(2)
        
        while stck and stck[-1]<=arr[i]:  #false     8<=1 false     1<=7  8<=7        7<=6
            stck.pop()                                              #8
        if stck:                          #false       res[4]=8      res[3]=8        res[2]=8
            res[i]=stck[-1]
            
        stck.append(arr[i])               # stck[8]    stck[8,1]    stck=[8,7]       stck=[8,6]
    return res
