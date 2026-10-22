class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        result = []
        for index, item in enumerate(nums):
            compliment = target - item
            if compliment in seen:
                result = [seen[compliment], index ]
                break
            seen[item] = index
        return result