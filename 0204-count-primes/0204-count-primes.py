class Solution:
    def countPrimes(self, n: int) -> int:
        arr = [0]*n
        c=0
        
        for i in range(2,int(n**0.5)+1):
            for j in range(i*i,n,i):
                arr[j]=1
        
        for k in range(2,len(arr)):
            if arr[k]==0:
                c+=1
        return (c)