class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        output = []
        n=len(words)
        for i in range(n):
            for j in range(n):
                if i!=j and words[i] in words[j]:
                    output.append(words[i])
                    break
        return output 