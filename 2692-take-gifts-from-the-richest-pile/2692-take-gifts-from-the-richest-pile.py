class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        while k:
            gifts.sort(reverse=True)
            pile = gifts[0]
            gifts.pop(0)
            gifts.append(int(sqrt(pile)))
            k -= 1
        return sum(gifts)