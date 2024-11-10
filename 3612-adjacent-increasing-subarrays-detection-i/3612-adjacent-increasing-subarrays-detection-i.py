class Solution(object):
    

    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def isStrictlyIncreasing(nums, start, k):
            for i in range(start, start+k-1):
                if nums[i]>=nums[i+1]:
                    return False
            return True

        n = len(nums)
        if n < 2*k:
            return False

        for i in range(n-2*k+1):
            if isStrictlyIncreasing(nums, i, k) and isStrictlyIncreasing(nums, i+k, k):
                return True

        return False