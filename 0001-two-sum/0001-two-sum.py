class Solution:
    def twoSum(self,arr, target):
        sum=0
        for i in range(len(arr)):
            for j in range(len(arr)):
                sum=arr[i]+arr[j]
                #j+=1
                if sum==target and i!=j:
                    return [i,j]
                j+=1    
            i+=1
        