class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasDuplicates = False
        seen = set()
        for index, value in enumerate(nums):
            if value in seen:
                hasDuplicates = True
                break
            seen.add(value)
        return hasDuplicates
