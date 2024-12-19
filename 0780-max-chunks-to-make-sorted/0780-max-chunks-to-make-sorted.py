class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        sumofval, sumofindices, chunks = 0, 0, 0
        for i in range(len(arr)):
            sumofval += arr[i]
            sumofindices += i
            if sumofval == sumofindices:
                chunks += 1
        return chunks