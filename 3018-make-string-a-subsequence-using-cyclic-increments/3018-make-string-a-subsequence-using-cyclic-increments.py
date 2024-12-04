class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        m, n = len(str1), len(str2)
        i,j = 0, 0
        while (i<m and j<n):
            if (str1[i] == str2[j] or chr(ord(str1[i]) + 1) == str2[j] or 
            (ord(str1[i]) - ord('a') + 1) % 26 + ord('a') == ord(str2[j])):
                j+=1
            i+=1

        return j == n