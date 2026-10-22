class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       seen = {}
       result = []

       for index, value in enumerate(nums):
            compliment = target - value
            if compliment in seen:
                result = [seen[compliment], index]
                break
            seen[value] = index

       return result