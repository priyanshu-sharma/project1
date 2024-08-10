class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        output = [i for i in range(0, len(nums) + 1)]
        return list(set(output).difference(nums))[0]