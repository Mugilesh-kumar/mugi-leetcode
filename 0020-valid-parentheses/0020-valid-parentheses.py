class Solution:
    def isValid(self, s):
        arr=[]
        pair={')':'(',']':'[','}':'{'}
        if len(s)<=2 and s[0]==s[-1]:
            return False
        for i in s:
            if i in '({[':
                arr.append(i)
            else:
                if not arr or arr.pop()!=pair[i]:
                    return False
                    
        return len(arr)==0
        

        
                


                

            

        