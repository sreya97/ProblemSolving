class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        shuffledstr = ""
        for i in range(len(indices)):
            shuffledstr += s[indices.index(i)]

        return shuffledstr