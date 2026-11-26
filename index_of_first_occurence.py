class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            matched = 0

            for j in range(len(needle)):
                if needle[j] == haystack[i + j]:
                    matched += 1
                else:
                    break

            if matched == len(needle):
                return i

        return -1