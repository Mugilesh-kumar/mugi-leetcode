class Solution(object):
    def majorityElement(self, nums):
        max_count=0
        arr={}
        count=[]
        for i in nums:
            if i not in arr:
                arr[i]=1
            elif i in arr:
                arr[i]+=1
        ele=max(arr,key=arr.get)    
        return ele
            
        