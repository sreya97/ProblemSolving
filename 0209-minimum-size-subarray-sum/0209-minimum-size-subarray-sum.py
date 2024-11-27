class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l, total = 0,0
        res = float("inf")
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r-l+1, res)
                total -= nums[l]
                l+=1

        if res == float("inf"):
            return 0
        else:
            return res
        # return 0 if res==float("inf") else return res