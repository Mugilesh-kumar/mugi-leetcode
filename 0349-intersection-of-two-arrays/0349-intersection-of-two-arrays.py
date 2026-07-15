class Solution(object):
    def intersection(self, nums1, nums2):
        opt=[]
        arr1=set(nums1)
        arr2=set(nums2)
        result=list(arr1&arr2)
        return result