class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # has_duplicates = False
        # seen = set()
        # for index, value in enumerate(nums):
        #     if value in seen:
        #         has_duplicates = True
        #         break
        #     seen.add(value)

        # return has_duplicates
        return len(nums) != len(set(nums))