class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        w = s.split()
        count = 0
        for char in w[-1]:
            count += 1
        

        return count
        