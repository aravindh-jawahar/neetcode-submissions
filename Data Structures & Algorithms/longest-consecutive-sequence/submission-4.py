class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums_set = set(nums)
        max_length = 0

        for index, item in enumerate(nums_set):
            if item - 1 not in nums_set:
                current_item = item
                current_streak = 1

                while current_item + 1 in nums_set:
                    current_item += 1
                    current_streak += 1
                
                if current_streak > max_length:
                    max_length = current_streak

        return max_length