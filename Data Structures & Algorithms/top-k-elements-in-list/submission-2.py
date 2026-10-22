from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = Counter(nums)
        sort_freq = sorted(groups.items(), key = lambda x: x[1], reverse = True)
        return [x[0] for x in sort_freq[:k]]