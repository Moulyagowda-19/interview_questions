def rch(arr,rat,units): #arr = 2,3,1,4,5,6
    if len(arr)==0:
        return -1
    foodreq = rat*units
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum>=foodreq:
            return i+1
    return 0
