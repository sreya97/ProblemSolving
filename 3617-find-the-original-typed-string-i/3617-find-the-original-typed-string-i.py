class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        count = 1
        i=0
        while i < n:
            j = 0
            while j < n:
                if j+1 < n and word[j]==word[j+1]:
                    count+=1
                j+=1
            i=j
                
        return count