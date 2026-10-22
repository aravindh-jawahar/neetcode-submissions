class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        duplicates = set()
        for item in nums:
            if item not in seen:
                seen.add(item)
            else:
                duplicates.add(item)
        return len(duplicates) > 0