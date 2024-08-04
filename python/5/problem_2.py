class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = max(nums)
        max_ending_here, min_ending_here = 1, 1
        for i in range(0, len(nums)):
            if nums[i] == 0:
                max_ending_here, min_ending_here = 1, 1
            temp = max_ending_here * nums[i]
            max_ending_here = max(temp, min_ending_here * nums[i], nums[i])
            min_ending_here = min(temp, min_ending_here * nums[i], nums[i])
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far