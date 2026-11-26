class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        w = s.split()
        reverse = " ".join(w[::-1])
        return reverse