class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        n = len(s)
        zero = 0

        for i in range(n-1):
            if s[i] == '0':
                zero += 1
            one = 0
            for j in range(i+1, n):
                if s[j] == '1':
                    one += 1
            ans = max(ans, one+zero)

        return ans