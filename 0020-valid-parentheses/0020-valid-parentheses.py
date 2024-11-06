class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        closetoOpen = {")":"(", "}":"{", "]":"["}

        for b in s:
            if b in closetoOpen:
                if stack and stack[-1]==closetoOpen[b]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(b)
        return True if not stack else False