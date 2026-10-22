class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        result = []

        for index, num in enumerate(nums):
            # result[index] = prefix
            result.append(prefix)
            prefix *= num
        
        suffix = 1

        for indx in range(len(nums) - 1, -1, -1):
            result[indx] *= suffix
            suffix *= nums[indx]
        return result
        