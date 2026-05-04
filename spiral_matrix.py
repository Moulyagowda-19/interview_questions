class Solution(object):
    def spiralOrder(self,arr) :
        res=[]
        top = left = 0
        right = len(arr[0])-1 #last column
        bottom = len(arr)-1 #last row
        while left<=right and top<=bottom:
            for j in range(left,right+1):
                res.append(arr[top][j])  #j will move left to right and top is fixed
                # [0][0]==>2, [0][1]==>4, [0][2]==>6
            top += 1
            for i in range(top,bottom+1):
                res.append(arr[i][right]) #right is fixed i moves from top to bottom
                # [1][2]==> 3 ,[2][2]==>10  
            right -=1
            if top<=bottom:
                for j in range(right,left-1,-1):
                    res.append(arr[bottom][j]) #bottom is fixed and it moves right to left
                    #[2][1]=9, [2][0]=>8
                bottom -=1
            if left<=right:
                for i in range(bottom, top-1,-1):
                    res.append(arr[i][left]) #left is fixed moves from bottom to top
                    #[2][0]==>8 , [1][0]==>-1
                
                left +=1
        return res
        
