class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        n=len(pref)
        c=0
        for i in range(len(words)):
            s1 = words[i]
            if pref == s1[:n]:
                c += 1
        return c