class Solution(object):
    def lengthOfLastWord(self, s):
      if s:
        arr=s.split()
        return len(arr[-1])

