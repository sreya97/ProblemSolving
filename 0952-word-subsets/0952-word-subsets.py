class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq = Counter()
        for word2 in words2:
            w2 = Counter(word2)
            for char, count in w2.items():
                max_freq[char] = max(max_freq[char], count)

        result = []
        for word1 in words1:
            w1 = Counter(word1)
            if all(w1[char] >= max_freq[char] for char in max_freq):
                result.append(word1)

        return result