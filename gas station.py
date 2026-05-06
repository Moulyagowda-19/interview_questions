def gas_st(gas,cost):
    if sum(gas)<sum(cost): #15<16 True
        return -1
    g = startidx = 0
    for i in range(len(gas)):       # i=0         1              2           3
        g = g +gas[i]-cost[i]       # 0+1-3=2     0+2-4=-2      0+3-5=-2     3+4-1=6
        if g<0:                     # true        #true         true          false
            g=0                     # g=0         #g=0          g=0           
            startidx =i+1           # 1           2             3            
    return startidx
